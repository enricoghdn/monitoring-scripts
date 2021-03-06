"""Test suite for monitoring_scripts.nagios_common"""

import pytest

from monitoring_scripts import nagios_common as unit


def test_plugin_exit_error():
    """Assert ValueError is raised if passed code is not an instance of
    nagios_common.Codes"""

    plain_int_code = 0

    with pytest.raises(ValueError):
        unit.plugin_exit(plain_int_code)


def test_plugin_exit_message_print(capfd):
    """Assert the specified message is printed to stdout"""

    message = 'test message'

    with pytest.raises(SystemExit):
        unit.plugin_exit(unit.Codes.OK, message=message)
    stdout = capfd.readouterr()[0]

    assert message in stdout


def test_plugin_exit_status_print(capfd):
    """Assert that the exit code name is printed to stdout"""

    exit_code = unit.Codes.CRITICAL
    message = 'message'

    with pytest.raises(SystemExit):
        unit.plugin_exit(exit_code, message=message)
    stdout = capfd.readouterr()[0]

    assert exit_code.name in stdout


def test_plugin_exit_quiet(capfd):
    """Assert nothing is printed to stdout if message is None"""

    exit_code = unit.Codes.CRITICAL

    with pytest.raises(SystemExit):
        unit.plugin_exit(exit_code)
    stdout = capfd.readouterr()[0]

    assert not stdout


def test_plugin_exit_code():
    """Assert program exit code is correct"""

    exit_code = unit.Codes.UNKNOWN
    expected_exit_value = exit_code.value

    with pytest.raises(SystemExit) as exit_info:
        unit.plugin_exit(exit_code)

    assert exit_info.value.code == expected_exit_value
