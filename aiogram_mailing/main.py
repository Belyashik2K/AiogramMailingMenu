from aiogram import (
    Bot,
    Dispatcher,
)

from .database import Database
from .interfaces import UserDataSource
from .mailing import register_handlers
from .utils.mailing import MailingFunctions


class AiogramMailingMenu:

    def __init__(
            self,
            bot_instance: Bot,
            dispatcher_instance: Dispatcher,
            data_source: UserDataSource,
            custom_command: str = "mailing",
            custom_database_path: str = "mailing_db.sqlite3",
    ) -> None:
        self._bot = bot_instance
        self._dp = dispatcher_instance
        self._data_source = data_source
        self._command = custom_command
        self._database_path = None

        self._validate_path(custom_database_path)

    def _validate_path(self, path: str) -> None:
        if not path.endswith(".sqlite3"):
            raise ValueError("Database path must end with .sqlite3")
        self._database_path = path

    @property
    def bot(self) -> Bot:
        return self._bot

    @property
    def dispatcher(self) -> Dispatcher:
        return self._dp

    @property
    def data_source(self) -> UserDataSource:
        return self._data_source

    @property
    def command(self) -> str:
        return self._command

    @property
    def database_path(self) -> str:
        return self._database_path

    async def setup(self) -> None:
        db = Database(
            database_url=self.database_path
        )
        await db.create_tables()

        sender = MailingFunctions(
            bot=self.bot,
            data_source=self.data_source,
            mailing_database=db
        )

        await register_handlers(sender, db, self)
        print("Mailing menu is set up!")
