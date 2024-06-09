from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware, Dispatcher
from aiogram.types import TelegramObject, Update, Message
from config.database.database import create_pool
from peewee import Database

class DbMiddleware(BaseMiddleware):
    def __init__(self, db: Database) -> None:
        self.db = db

    async def __call__(self, 
                        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
                        event: Message, data: Dict[str, Any]) -> Any:
        with self.db.connection_context():
            data['db'] = self.db
            return await handler(event, data)