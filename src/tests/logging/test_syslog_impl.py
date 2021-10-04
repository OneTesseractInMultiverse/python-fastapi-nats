from app.logging.interfaces import AbstractLogger
from app.logging.syslog_impl import StandardOutputLogger
from mock import patch


def get_logger() -> AbstractLogger:
    return StandardOutputLogger()


@patch('app.logging.syslog_impl.logging')
def test_standard_output_logger_when_info_logging_info_is_called(mock_logging):
    # Prepare
    logger = get_logger()

    # Act
    logger.info('info message')

    assert mock_logging.info.called


@patch('app.logging.syslog_impl.logging')
def test_standard_output_logger_when_error_logging_error_is_called(mock_logging):
    # Prepare
    logger = get_logger()

    # Act
    logger.error('error message')

    assert mock_logging.error.called


@patch('app.logging.syslog_impl.logging')
def test_standard_output_logger_when_warning_logging_warning_is_called(mock_logging):
    # Prepare
    logger = get_logger()

    # Act
    logger.warning('info message')

    assert mock_logging.warning.called


@patch('app.logging.syslog_impl.logging')
def test_standard_output_logger_when_debug_logging_debug_is_called(mock_logging):
    # Prepare
    logger = get_logger()

    # Act
    logger.debug('info message')

    assert mock_logging.debug.called


@patch('app.logging.syslog_impl.datetime')
def test_standard_output_logger_when_error_correct_error_dict_is_produced(mock_datetime):
    # Prepare
    expected = {
        'utc_datetime': 'date',
        'message': 'error message',
        'level': 'ERROR'
    }
    logger = get_logger()
    mock_datetime.datetime.utcnow.return_value = 'date'

    # Act
    actual = logger.error('error message')

    assert expected == actual


@patch('app.logging.syslog_impl.datetime')
def test_standard_output_logger_when_info_correct_info_dict_is_produced(mock_datetime):
    # Prepare
    expected = {
        'utc_datetime': 'date',
        'message': 'info message',
        'level': 'INFO'
    }
    logger = get_logger()
    mock_datetime.datetime.utcnow.return_value = 'date'

    # Act
    actual = logger.info('info message')

    assert expected == actual


@patch('app.logging.syslog_impl.datetime')
def test_standard_output_logger_when_warning_correct_warning_dict_is_produced(mock_datetime):
    # Prepare
    expected = {
        'utc_datetime': 'date',
        'message': 'warning message',
        'level': 'WARNING'
    }
    logger = get_logger()
    mock_datetime.datetime.utcnow.return_value = 'date'

    # Act
    actual = logger.warning('warning message')

    assert expected == actual


@patch('app.logging.syslog_impl.datetime')
def test_standard_output_logger_when_debug_correct_debug_dict_is_produced(mock_datetime):
    # Prepare
    expected = {
        'utc_datetime': 'date',
        'message': 'debug message',
        'level': 'DEBUG'
    }
    logger = get_logger()
    mock_datetime.datetime.utcnow.return_value = 'date'

    # Act
    actual = logger.debug('debug message')

    assert expected == actual
