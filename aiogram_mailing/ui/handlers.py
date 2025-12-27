from typing import TYPE_CHECKING

from aiogram import (
    Router,
    F,
    types,
)
from aiogram.fsm.context import FSMContext

from aiogram_mailing.core.services.mailing import MailingService
from aiogram_mailing.ui.config import DEFAULT_PARSE_MODE
from aiogram_mailing.ui.keyboards.builders.main import main_mailing_menu_keyboard
from aiogram_mailing.ui.keyboards.callbacks import MailingMainMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMainMenuActionEnum
from aiogram_mailing.ui.texts import MailingMenuTexts
from aiogram_mailing.ui.utils.texts import build_menu_text


async def register_handlers(
        router: Router,
        command: str,
        texts: MailingMenuTexts
) -> Router:
    mailing_router = Router(name="aiogram_mailing_menu")
    router.include_router(mailing_router)

    @mailing_router.message(F.text == f"/{command}")
    async def mailing_menu(
            message: types.Message,
            state: FSMContext,
    ) -> None:
        await state.clear()
        await message.answer(
            texts.messages.mailing_main_menu,
            reply_markup=main_mailing_menu_keyboard(texts.buttons),
            parse_mode=DEFAULT_PARSE_MODE
        )

    @mailing_router.callback_query(
        MailingMainMenuCallback.filter(
            F.action.is_(MailingMainMenuActionEnum.GET_ALL_MAILINGS)
        )
    )
    async def get_all_mailings_menu(
            callback: types.CallbackQuery,
            am_mailing_service: MailingService,
    ) -> None:
        try:
            mailings = await am_mailing_service.get_all_mailings()
        except Exception as e: # TODO: specify exception
            await callback.answer(
                texts.errors.no_mailings_found,
            )
            return

    @mailing_router.callback_query(
        MailingMainMenuCallback.filter(
            F.action.is_(MailingMainMenuActionEnum.CLOSE)
        )
    )
    async def close_mailing_menu(
            callback: types.CallbackQuery, state: FSMContext
    ) -> None:
        await state.clear()
        await callback.message.delete()

    return mailing_router
