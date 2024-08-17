import pytest
from prolog.core import trace
from loguru import logger


@pytest.fixture
def caplog(caplog: pytest.LogCaptureFixture) -> pytest.LogCaptureFixture:
    logger.add(caplog.handler, format="{message}")
    yield caplog
    logger.remove()


def test_trace(caplog) -> None:
    @trace
    def dummy_function() -> None:
        pass

    with caplog.at_level("INFO"):
        dummy_function()

    assert "Calling function dummy_function" in caplog.text
    assert "Finished calling function dummy_function" in caplog.text
