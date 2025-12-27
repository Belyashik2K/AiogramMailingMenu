from typing import TYPE_CHECKING

from aiogram import (
    Router,
    F,
    types,
)
from aiogram.fsm.context import FSMContext

if TYPE_CHECKING:
    from .main import AiogramMailingMenu


async def register_handlers(
        menu: "AiogramMailingMenu",
) -> None:
    mailing_router = Router(name=__name__)
    menu.router.include_router(mailing_router)

    @mailing_router.message(F.text.is_(f"/{menu.command}"))
    async def mailing_menu(message: types.Message, state: FSMContext):
        await state.clear()
        await message.answer("Mailing menu will be here soon!")
