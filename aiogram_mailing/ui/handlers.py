from typing import TYPE_CHECKING

from aiogram import (
    Router,
    F,
    types,
)
from aiogram.fsm.context import FSMContext

from aiogram_mailing.core.services.mailing import MailingService
from aiogram_mailing.ui.config import DEFAULT_PARSE_MODE
from aiogram_mailing.ui.keyboards.builders.main import (
    main_mailing_menu_keyboard,
    manage_mailing_keyboard,
)
from aiogram_mailing.ui.keyboards.callbacks import MailingMainMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMainMenuActionEnum
from aiogram_mailing.ui.texts import MailingMenuTexts
from aiogram_mailing.ui.utils.texts import (
    build_mailing_info_text,
)


async def register_handlers(
        router: Router,
        command: str,
        button_callback_data: str | None,
        texts: MailingMenuTexts
) -> Router:
    mailing_router = Router(name="aiogram_mailing_menu")
    router.include_router(mailing_router)

    @mailing_router.callback_query(
        F.data == button_callback_data,
        F.data.is_not(None)
    )
    @mailing_router.callback_query(
        MailingMainMenuCallback.filter(
            F.action.is_(MailingMainMenuActionEnum.OPEN)
        ),
    )
    @mailing_router.message(F.text == f"/{command}")
    async def mailing_menu(
            update: types.Message | types.CallbackQuery,
            state: FSMContext,
    ) -> None:
        if isinstance(update, types.Message):
            message = update
        else:
            message = update.message
            await message.delete()
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
        except Exception as e:  # TODO: specify exception
            await callback.answer(
                texts.errors.no_mailings_found,
            )
            return

    @mailing_router.callback_query(
        MailingMainMenuCallback.filter(
            F.action.is_(MailingMainMenuActionEnum.CREATE_MAILING)
        )
    )
    async def create_mailing_menu(
            callback: types.CallbackQuery,
            am_mailing_service: MailingService,
    ) -> None:
        mailing = await am_mailing_service.create_mailing()
        menu_text = build_mailing_info_text(
            mailing=mailing,
            texts=texts.messages,
        )
        await callback.message.edit_text(
            menu_text,
            reply_markup=manage_mailing_keyboard(texts.buttons, mailing.id),
            parse_mode=DEFAULT_PARSE_MODE
        )


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
