from typing import (
    TYPE_CHECKING,
    Optional,
)

from aiogram_mailing import MailingUsersSource
from aiogram_mailing.core.errors import MailingMenuError
from aiogram_mailing.database.models import MailingModel

if TYPE_CHECKING:
    # It should be an interface, but I want keep it simple for now
    from aiogram_mailing.database.repository import MailingRepository


class MailingService:
    def __init__(
            self,
            data_source: MailingUsersSource,
            repository: 'MailingRepository'
    ) -> None:
        self._data_source = data_source
        self._repository = repository

    async def get_mailing(self, mailing_id: int) -> "MailingModel":
        info = await self._repository.get_by_id(mailing_id)
        if not info:
            raise MailingMenuError(f"Mailing with id {mailing_id} not found")
        return info

    async def get_all_mailings(self) -> list["MailingModel"]:
        mailings = await self._repository.get_all()
        if not mailings:
            raise MailingMenuError("No mailings found")
        return mailings

    async def create_mailing(self) -> "MailingModel":
        mailing_model = MailingModel()
        return await self._repository.save(mailing_model)

    async def set_new_text(self, mailing_id: int, new_text: str | None) -> None:
        mailing = await self.get_mailing(mailing_id)
        mailing.text = new_text
        await self._repository.save(mailing)
