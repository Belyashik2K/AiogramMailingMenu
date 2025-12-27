from typing import (
    Any,
    Awaitable,
    Callable,
    Dict,
)
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from aiogram_mailing.core.services.mailing import MailingService


class MailingServiceMiddleware(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        data_source = data.get('am_users_source')
        if data_source is None:
            raise RuntimeError("MailingUsersSource is not provided in data")

        repository = data.get('am_mailing_repo')
        if repository is None:
            raise RuntimeError("MailingRepository is not provided in data")

        service = MailingService(
            data_source=data_source,
            repository=repository
        )
        data['am_mailing_service'] = service

        return await handler(event, data)
