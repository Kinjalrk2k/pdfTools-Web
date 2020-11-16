from app import CurrentConfig
from config import ProdConfig


def test_ProdConfig():
    assert CurrentConfig == ProdConfig


def test_time_limit():
    assert CurrentConfig.TIME_LIMIT <= 600
