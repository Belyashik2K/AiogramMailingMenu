from aiogram.types import (
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_mailing.ui.config import MENU_AUTHOR_URL
from aiogram_mailing.ui.keyboards.builders.common import close_button
from aiogram_mailing.ui.keyboards.callbacks import MailingMainMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMainMenuActionEnum
from aiogram_mailing.ui.texts.base import MailingMenuButtons


def main_mailing_menu_keyboard(texts: MailingMenuButtons) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text=texts.mailing_list,
        callback_data=MailingMainMenuCallback(
            action=MailingMainMenuActionEnum.GET_ALL_MAILINGS
        )(),
    )
    keyboard.button(
        text=texts.create_mailing,
        callback_data=MailingMainMenuCallback(
            action=MailingMainMenuActionEnum.CREATE_MAILING
        )(),
    )
    keyboard.button(
        text=texts.menu_author_link,
        url=MENU_AUTHOR_URL,
    )
    keyboard.add(close_button(texts))

    keyboard.adjust(1, repeat=True)

    return keyboard.as_markup()
