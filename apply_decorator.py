from typing import Callable


def apply_decorator(func: Callable[[], None]) -> Callable[[], None]:
    def wrapper():
        print("Decorator applied")
        return func()

    return wrapper


@apply_decorator
def decorator_func() -> None:
    print("abigail")


decorator_func()
