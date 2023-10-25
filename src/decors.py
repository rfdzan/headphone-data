from collections.abc import Callable
from typing import Any

from constants import JSON_FILES
from src.data.sql_query import insert_into_headphones


def write_result(filename: str):
    def decorator(func):
        def wrapper(*args):
            try:
                result = func(args)
            except TypeError:
                result = func()
            with open(JSON_FILES.joinpath(filename), "w") as file:
                file.write(result)

        return wrapper

    return decorator


def insert_to_headphone_db(func: Callable):
    def wrapper(*args):
        # try:
        result: list[dict[str, Any]] = func(args)
        # except TypeError:
        #     result: list[dict[str, Any]] = func()
        insert_into_headphones(result)

    return wrapper