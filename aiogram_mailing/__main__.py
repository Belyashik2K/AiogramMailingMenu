import os
from pathlib import Path
from typing import Literal

from aiogram import (
    Router,
)

from .database.helper import SQLAlchemyDatabaseHelper
from .database.models.base import Base
from aiogram_mailing.core.interfaces import MailingUsersSource
from .ui.handlers import register_handlers
from .ui.texts import MailingMenuTexts


class AiogramMailingMenu:

    def __init__(
            self,
            router: Router,
            data_source: MailingUsersSource,
            *,
            command: str = 'mailing',
            database_path: str | Path = Path('data/aiogram_mailing.db'),
            menu_language: Literal['en', 'ru'] = 'ru',
    ) -> None:
        self._router = router
        self._data_source = data_source
        self._command = command
        self._database_path = self._validate_path(database_path)
        self._menu_texts: MailingMenuTexts = MailingMenuTexts.from_code(menu_language)

        self._db_helper = SQLAlchemyDatabaseHelper(self._database_path)

    @staticmethod
    def _validate_path(path: str | Path) -> str:
        path = Path(path)

        if path.is_dir():
            raise ValueError("storage_path must be a file, not a directory")

        path.parent.mkdir(parents=True, exist_ok=True)

        if not os.access(path.parent, os.W_OK):
            raise ValueError("Directory is not writable")

        if path.suffix not in (".sqlite", ".sqlite3", ".db"):
            raise ValueError("Storage must have one of extensions: .sqlite, .sqlite3, .db")

        return str(path)

    @property
    def router(self) -> Router:
        return self._router

    @property
    def data_source(self) -> MailingUsersSource:
        return self._data_source

    @property
    def command(self) -> str:
        return self._command

    @property
    def database_path(self) -> str:
        return self._database_path

    async def setup(self) -> None:
        async with self._db_helper.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        await register_handlers(self, self._menu_texts)
