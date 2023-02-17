import dataclasses
import os
from pathlib import Path


@dataclasses.dataclass
class DefaultSettings:
    """
    Default configs for application.
    """

    TMP_PATH: Path = Path(os.getenv('TMP_PATH'))
    TENSORBOARD_LOGS_PATH: Path = TMP_PATH / 'tensorboard'
    WEIGHTS_PATH: Path = TMP_PATH / 'weights'
    CACHE_PATH: Path = TMP_PATH / 'cache'
    LOGFILE_PATH: Path = TMP_PATH / 'logfile.log'
    LOGGER_NAME: str = 'autodl'
    CONSOLE_LOG_NAME: str = 'console-log'
