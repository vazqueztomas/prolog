from typing import Callable
from functools import wraps
from .log import log


def trace(func: Callable[None, None]) -> Callable[None, None]:
    @wraps(func)
    def wrapper():
        log(f"Calling function {func.__name__}")
        func()
        log(f"Finished calling function {func.__name__}")

    return wrapper
