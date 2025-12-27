from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
)

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from aiogram_mailing import MailingUsersSource
from aiogram_mailing.database.helper import SQLAlchemyDatabaseHelper
from aiogram_mailing.database.repository import MailingRepository


class DBMiddleware(BaseMiddleware):

    def __init__(
            self,
            database_helper: SQLAlchemyDatabaseHelper,
            data_source: MailingUsersSource
    ) -> None:
        super().__init__()
        self._database_helper = database_helper
        self._data_source = data_source

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data['am_users_source'] = self._data_source

        async with self._database_helper.get_session() as session:
            data['am_db_session'] = session
            data['am_mailing_repo'] = MailingRepository(session=session)
            return await handler(event, data)
