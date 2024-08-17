from prolog.core import trace

@trace
def dummy_function() -> None:
    print("Hello, World!")

dummy_function()