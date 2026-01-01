from typing import List

from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram_mailing.database.models import MailingModel


class MailingRepository:

    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def get_by_id(self, mailing_id: int) -> MailingModel | None:
        stmt = Select(MailingModel).where(MailingModel.id == mailing_id)
        result = await self._session.execute(stmt)
        mailing: MailingModel = result.scalar_one_or_none()
        if mailing:
            await mailing.awaitable_attrs.media
            await mailing.awaitable_attrs.buttons
        return mailing

    async def get_all(self) -> list[MailingModel]:
        stmt = Select(MailingModel)
        result = await self._session.execute(stmt)
        mailings = result.scalars().all()
        return mailings # type: ignore

    async def save(self, mailing: MailingModel) -> MailingModel:
        merged_data = await self._session.merge(mailing)
        await self._session.flush()
        await self._session.commit()
        return merged_data
