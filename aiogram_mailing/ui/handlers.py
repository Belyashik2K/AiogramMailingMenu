from typing import TYPE_CHECKING

from aiogram import (
    Router,
    F,
    types,
)
from aiogram.fsm.context import FSMContext

from aiogram_mailing.ui.config import DEFAULT_PARSE_MODE
from aiogram_mailing.ui.keyboards.builders.main import main_mailing_menu_keyboard
from aiogram_mailing.ui.keyboards.callbacks import MailingMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMenuActionEnum
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
        await message.answer(
            texts.messages.mailing_menu,
            reply_markup=main_mailing_menu_keyboard(texts.buttons),
            parse_mode=DEFAULT_PARSE_MODE
        )

    @mailing_router.callback_query(
        MailingMenuCallback.filter(
            F.action.is_(MailingMenuActionEnum.CLOSE)
        )
    )
    async def close_mailing_menu(
            callback: types.CallbackQuery,
            state: FSMContext
    ):
        await state.clear()
        await callback.message.delete()
