import inspect
from typing import Callable

from core.helpers.cache.base import BaseKeyMaker


class CustomKeyMaker(BaseKeyMaker):
    async def make(self, function: Callable, prefix: str, *args, **kwargs) -> str:
        path = f"{prefix}::{inspect.getmodule(function).__name__}.{function.__name__}"

        params = kwargs['request'].__dict__
        headers = dict(params['scope']['headers'])
        accept_language = headers.get(b'accept-language', b'').decode('utf-8')

        # args = ""

        # for arg in inspect.signature(function).parameters.values():
        #     args += arg.name

        # if args:
        #     return f"{path}.{args}"

        return path
