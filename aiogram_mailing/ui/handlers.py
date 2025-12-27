from typing import TYPE_CHECKING

from aiogram import (
    Router,
    F,
    types,
)
from aiogram.fsm.context import FSMContext

from aiogram_mailing.ui.config import DEFAULT_PARSE_MODE
from aiogram_mailing.ui.texts import MailingMenuTexts

if TYPE_CHECKING:
    from aiogram_mailing.__main__ import AiogramMailingMenu


async def register_handlers(
        menu: "AiogramMailingMenu",
        texts: MailingMenuTexts
) -> None:
    mailing_router = Router(name=__name__)
    menu.router.include_router(mailing_router)

    @mailing_router.message(F.text == f"/{menu.command}")
    async def mailing_menu(message: types.Message, state: FSMContext):
        await state.clear()
        await message.answer(texts.messages.mailing_menu, parse_mode=DEFAULT_PARSE_MODE)
