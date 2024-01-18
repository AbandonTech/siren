from models import Command

Advancement = Command(
    command="advancement",
    multiplayer_only=False,
    op_level=2,
    block_command=False,
    mob_command=False,
    player_command=True,
    world_command=False
)

Attribute = Command(
    command="attribute",
    op_level=2,
    mob_command=True,
    player_command=True
)

Ban = Command(
    command="ban",
    multiplayer_only=True,
    op_level=3,
    player_command=True
)

BanIp = Command(
    command="ban-ip",
    multiplayer_only=True,
    op_level=3,
    player_command=True
)

Banlist = Command(
    command="banlist",
    multiplayer_only=True,
    op_level=3,
    player_command=True
)

Bossbar = Command(
    command="bossbar",
    op_level=2,
    player_command=True,
    world_command=True
)

Clear = Command(
    command="clear",
    op_level=2,
    player_command=True
)

Clone = Command(
    command="clone",
    op_level=2,
    block_command=True,
)

Damage = Command(
    command="damage",
    op_level=1,
    mob_command=True,
    player_command=True
)

Data = Command(
    command="data",
    op_level=2,
    mob_command=True,
    player_command=True,
    block_command=True
)

Datapack = Command(
    command="datapack",
    op_level=2,
    world_command=True
)

Debug = Command(
    command="debug",
    op_level=3
)

DefaultGameMode = Command(
    command="defaultgamemode",
    op_level=2,
    world_command=True
)

Deop = Command(
    command="deop",
    multiplayer_only=True,
    op_level=3,
    player_command=True
)

Difficulty = Command(
    command="difficulty",
    op_level=2,
    world_command=True
)

Effect = Command(
    command="effect",
    op_level=2,
    mob_command=True,
    player_command=True
)
