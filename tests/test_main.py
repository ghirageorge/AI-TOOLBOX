import pytest
from click.testing import CliRunner
from ai_toolbox.main import cli

@pytest.fixture
def runner():
    """Fixture providing a Click CLI runner."""
    return CliRunner()

class TestCLI:
    """Tests for the AI Toolbox CLI."""

    def test_cli_group_exists(self, runner):
        """Test that the CLI group is callable."""
        result = runner.invoke(cli, ['--help'])
        assert result.exit_code == 0
        assert 'AI Toolbox Command Line Interface' in result.output

    def test_hello_command(self, runner):
        """Test the hello command outputs the correct message."""
        result = runner.invoke(cli, ['hello'])
        assert result.exit_code == 0
        assert 'hello from AI toolbox!' in result.output

    def test_hello_command_help(self, runner):
        """Test the hello command help message."""
        result = runner.invoke(cli, ['hello', '--help'])
        assert result.exit_code == 0
        assert 'Prints a greeting message.' in result.output

    def test_invalid_command(self, runner):
        """Test that an invalid command returns an error."""
        result = runner.invoke(cli, ['invalid'])
        assert result.exit_code != 0