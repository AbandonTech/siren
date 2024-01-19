from models import Command

commands = {
    "advancement": Command(
        command="advancement",
        multiplayer_only=False,
        op_level=2,
        block_command=False,
        mob_command=False,
        player_command=True,
        world_command=False
    ),
    "attribute": Command(
        command="attribute",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "ban": Command(
        command="ban",
        multiplayer_only=True,
        op_level=3,
        player_command=True
    ),
    "ban-ip": Command(
        command="ban-ip",
        multiplayer_only=True,
        op_level=3,
        player_command=True
    ),
    "banlist": Command(
        command="banlist",
        multiplayer_only=True,
        op_level=3,
        player_command=True
    ),
    "bossbar": Command(
        command="bossbar",
        op_level=2,
        player_command=True,
        world_command=True
    ),
    "clear": Command(
        command="clear",
        op_level=2,
        player_command=True
    ),
    "clone": Command(
        command="clone",
        op_level=2,
        block_command=True,
    ),
    "damage": Command(
        command="damage",
        op_level=1,
        mob_command=True,
        player_command=True
    ),
    "data": Command(
        command="data",
        op_level=2,
        mob_command=True,
        player_command=True,
        block_command=True
    ),
    "datapack": Command(
        command="datapack",
        op_level=2,
        world_command=True
    ),
    "debug": Command(
        command="debug",
        op_level=3
    ),
    "defaultgamemode": Command(
        command="defaultgamemode",
        op_level=2,
        world_command=True
    ),
    "deop": Command(
        command="deop",
        multiplayer_only=True,
        op_level=3,
        player_command=True
    ),
    "difficulty": Command(
        command="difficulty",
        op_level=2,
        world_command=True
    ),
    "effect": Command(
        command="effect",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "enchant": Command(
        command="enchant",
        op_level=2,
        player_command=True
    ),
    "execute": Command(
        command="execute",
        op_level=2,
        block_command=True,
        mob_command=True,
        player_command=True,
        world_command=True
    ),
    "experience": Command(
        command="experience",
        op_level=2,
        player_command=True
    ),
    "fill": Command(
        command="fill",
        op_level=2,
        block_command=True,
    ),
    "fillbiome": Command(
        command="fillbiome",
        op_level=2,
        world_command=True
    ),
    "forceload": Command(
        command="forceload",
        op_level=2,
        world_command=True
    ),
    "function": Command(
        command="function",
        op_level=2,
        world_command=True
    ),
    "gamemode": Command(
        command="gamemode",
        op_level=2,
        player_command=True
    ),
    "gamerule": Command(
        command="gamerule",
        op_level=2,
        world_command=True
    ),
    "give": Command(
        command="give",
        op_level=2,
        player_command=True
    ),
    "help": Command(
        command="help",
        op_level=0
    ),
    "item": Command(
        command="item",
        op_level=2,
        block_command=True,
        mob_command=True,
        player_command=True
    ),
    "jfr": Command(
        command="jfr",
        op_level=4
    ),
    "kick": Command(
        command="kick",
        op_level=3,
        player_command=True
    ),
    "kill": Command(
        command="kill",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "list": Command(
        command="list",
        op_level=0,
        player_command=True
    ),
    "locate": Command(
        command="locate",
        op_level=2,
        block_command=True,
        mob_command=True,
        world_command=True
    ),
    "loot": Command(
        command="loot",
        op_level=2,
        block_command=True,
        mob_command=True,
        player_command=True
    ),
    "me": Command(
        command="me",
        op_level=0,
        player_command=True
    ),
    "msg": Command(
        command="msg",
        op_level=0,
        player_command=True
    ),
    "op": Command(
        command="op",
        op_level=3,
        multiplayer_only=True,
        player_command=True
    ),
    "pardon": Command(
        command="pardon",
        op_level=3,
        multiplayer_only=True,
        player_command=True
    ),
    "pardon-ip": Command(
        command="pardon-ip",
        op_level=3,
        multiplayer_only=True,
        player_command=True
    ),
    "particle": Command(
        command="particle",
        op_level=2,
        player_command=True
    ),
    "perf": Command(
        command="perf",
        op_level=4,
        multiplayer_only=True,
        world_command=True
    ),
    "place": Command(
        command="place",
        op_level=2,
        block_command=True,
        world_command=True
    ),
    "playsound": Command(
        command="playsound",
        op_level=2,
        player_command=True
    ),
    "publish": Command(
        command="publish",
        op_level=4,
        singleplayer_only=True,
        world_command=True
    ),
    "random": Command(
        command="random",
        op_level=2
    ),
    "recipe": Command(
        command="recipe",
        op_level=2,
        player_command=True
    ),
    "reload": Command(
        command="reload",
        op_level=2,
        world_command=True
    ),
    "return": Command(
        command="return",
        op_level=2
    ),
    "ride": Command(
        command="ride",
        op_level=0,
        mob_command=True,
        player_command=True
    ),
    "save-all": Command(
        command="save-all",
        op_level=4,
        multiplayer_only=True,
        world_command=True
    ),
    "save-off": Command(
        command="save-off",
        op_level=4,
        multiplayer_only=True,
        world_command=True
    ),
    "save-on": Command(
        command="save-on",
        op_level=4,
        multiplayer_only=True,
        world_command=True
    ),
    "say": Command(
        command="say",
        op_level=2,
        player_command=True
    ),
    "schedule": Command(
        command="schedule",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "scoreboard": Command(
        command="scoreboard",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "seed": Command(
        command="seed",
        op_level=2,
        world_command=True
    ),
    "setblock": Command(
        command="setblock",
        op_level=2,
        block_command=True,
    ),
    "setidletimeout": Command(
        command="setidletimeout",
        op_level=3,
        multiplayer_only=True,
        player_command=True
    ),
    "setworldspawn": Command(
        command="setworldspawn",
        op_level=2,
        world_command=True
    ),
    "spawnpoint": Command(
        command="spawnpoint",
        op_level=2,
        player_command=True
    ),
    "spectate": Command(
        command="spectate",
        op_level=2,
        player_command=True
    ),
    "spreadplayers": Command(
        command="spreadplayers",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "stop": Command(
        command="stop",
        op_level=4,
        multiplayer_only=True,
        world_command=True
    ),
    "stopsound": Command(
        command="stopsound",
        op_level=2,
        player_command=True
    ),
    "summon": Command(
        command="summon",
        op_level=2,
        mob_command=True
    ),
    "tag": Command(
        command="tag",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "team": Command(
        command="team",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "teammsg": Command(
        command="teammsg",
        op_level=0,
        player_command=True
    ),
    "teleport": Command(
        command="teleport",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "tell": Command(
        command="tell",
        op_level=0,
        player_command=True
    ),
    "tellraw": Command(
        command="tellraw",
        op_level=2,
        player_command=True
    ),
    "time": Command(
        command="time",
        op_level=2,
        world_command=True
    ),
    "title": Command(
        command="title",
        op_level=2,
        player_command=True
    ),
    "tm": Command(
        command="tm",
        op_level=0,
        player_command=True
    ),
    "tp": Command(
        command="tp",
        op_level=2,
        mob_command=True,
        player_command=True
    ),
    "trigger": Command(
        command="trigger",
        op_level=0,
        player_command=True
    ),
    "w": Command(
        command="w",
        op_level=0,
        player_command=True
    ),
    "weather": Command(
        command="weather",
        op_level=2,
        world_command=True
    ),
    "whitelist": Command(
        command="whitelist",
        op_level=3,
        multiplayer_only=True,
        player_command=True
    ),
    "worldborder": Command(
        command="worldborder",
        op_level=2,
        world_command=True
    ),
    "xp": Command(
        command="xp",
        op_level=2,
        player_command=True
    ),
}
