import asyncio
import struct

PADDING = b"\x00\x00"


class RconClient:
    """Manages minecraft RCON authentication and message sending."""

    def __init__(self, host: str, port: int, password: str):
        self.host = host
        self.port = port
        self.password = password

        self.is_authenticated = False

        self._reader: asyncio.StreamReader | None = None
        self._writer: asyncio.StreamWriter | None = None

    async def __aenter__(self) -> "RconClient":
        if not self._writer:
            self._reader, self._writer = await asyncio.open_connection(self.host, self.port)
            await self.authenticate()

        return self
    
    async def __aexit__(self, *_) -> None:
        if self._writer:
            self._writer.close()
    
    async def authenticate(self) -> None:
        if not self.is_authenticated:
            await self._send(3, self.password)
            self.is_authenticated = True
    
    async def _read_data(self, data_len: int) -> bytes:
        data = b""
        
        while len(data) < data_len:
            data += await self._reader.read(data_len - len(data))
        
        return data
    
    async def _send(self, packet_type: int, message: str) -> str:
        if not self._writer:
            raise ConnectionError("Client is not connected. Ensure you are using an async context manager.")

        out_packet = struct.pack("<li", 0, packet_type) + message.encode("utf8") + PADDING
        out_packet_len = struct.pack("<i", len(out_packet))
        self._writer.write(out_packet_len + out_packet)

        in_packet_len = struct.unpack("<i", await self._read_data(4))
        in_packet = await self._read_data(in_packet_len[0])

        in_packet_id = struct.unpack("<ii", in_packet[:8])[0]
        in_data, in_padding = in_packet[8:-2], in_packet[-2:]

        if in_padding != PADDING:
            raise ValueError("Received packet was not well formed.")
        if in_packet_id == -1:
            raise ConnectionRefusedError("Invalid password")
        
        data = in_data.decode("utf8")

        return data

    async def send(self, command: str) -> str:
        result = await self._send(2, command)
        await asyncio.sleep(0.5)
        return result
