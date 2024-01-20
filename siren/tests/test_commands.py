from siren.commands import commands


def test_commands_have_correct_names():
    for command_name, command in commands.items():
        assert command_name == command.command
