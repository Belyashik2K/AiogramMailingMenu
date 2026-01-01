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
from .ui.middlewares.outer.database import DBMiddleware
from .ui.middlewares.outer.service import MailingServiceMiddleware
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
            button_callback_data: str | None = None,
    ) -> None:
        self._router = router
        self._data_source = data_source
        self._command = command
        self._button_callback_data = button_callback_data
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

    @property
    def button_callback_data(self) -> str:
        return self._button_callback_data

    async def _setup_middlewares(
            self,
            mailing_router: Router
    ) -> None:
        db_middleware = DBMiddleware(
            database_helper=self._db_helper,
            data_source=self._data_source,
        )
        service_middleware = MailingServiceMiddleware()

        all_middlewares = [
            db_middleware,
            service_middleware,
        ]

        for middleware in all_middlewares:
            mailing_router.message.middleware(middleware)
            mailing_router.callback_query.middleware(middleware)

    async def setup(self) -> None:
        async with self._db_helper.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        mailing_router = await register_handlers(
            router=self._router,
            command=self._command,
            button_callback_data=self._button_callback_data,
            texts=self._menu_texts,
        )
        await self._setup_middlewares(mailing_router)
