from aiogram.filters import BaseFilter
from aiogram.types import Update

from . import UserDataSource

class IsAdmin(BaseFilter):
    def __init__(
            self,
            data_source: UserDataSource,
    ) -> None:
        self._data_source = data_source

    async def __call__(self, update: Update) -> bool:
        admin_list = await self._data_source.get_admin_ids()
        return update.from_user.id in admin_list
