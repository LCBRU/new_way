import os
from lbrc_flask.config import BaseConfig, BaseTestConfig
from lbrc_flask.validators import parse_date


class Config(BaseConfig):
    pass


class TestConfig(BaseTestConfig):
    pass
