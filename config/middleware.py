from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject, Update, Message

class DbMiddleware(BaseMiddleware):
    def __init__(self, pool) -> None:
        self.pool = pool

    async def __call__(self, 
                        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
                        event: Message, data: Dict[str, Any]) -> Any:
        async with self.pool.acquire() as conn:
            data['conn'] = conn
            return await handler(event, data)