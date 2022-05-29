# McRcon
Python package for authenticating and communicating with a Minecraft server using the Minecraft RCON protocol

# Sample Usage
```python
import asyncio

import mc_rcon


async def test_auth() -> None:
    async with mc_rcon.RconClient("123.2.3.4", 25575, "AVeryRealPassword") as client:
        print(await client.send("list"))


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(test_auth())

```
