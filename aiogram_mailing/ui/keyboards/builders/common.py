from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_mailing.ui.keyboards.callbacks import MailingMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMenuActionEnum
from aiogram_mailing.ui.texts.base import MailingMenuButtons


def close_button(texts: MailingMenuButtons) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text=texts.close_menu,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.CLOSE
        )()
    )


def close_keyboard(texts: MailingMenuButtons) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        close_button(texts)
    )
    return builder.as_markup()
