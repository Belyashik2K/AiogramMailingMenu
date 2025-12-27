from aiogram.types import (
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_mailing.ui.keyboards.builders.common import close_button
from aiogram_mailing.ui.keyboards.callbacks import MailingMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import MailingMenuActionEnum
from aiogram_mailing.ui.texts.base import MailingMenuButtons


def main_mailing_menu_keyboard(texts: MailingMenuButtons) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text=texts.start_mailing,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.START
        )(),
    )
    keyboard.button(
        text=texts.preview_mailing,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.PREVIEW
        )(),
    )
    keyboard.button(
        text=texts.edit_mailing_text,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.EDIT_TEXT
        )(),
    )
    keyboard.button(
        text=texts.manage_mailing_media,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.MANAGE_MEDIA
        )(),
    )
    keyboard.button(
        text=texts.manage_mailing_buttons,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.MANAGE_BUTTONS
        )(),
    )
    keyboard.button(
        text=texts.schedule_mailing,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.SCHEDULE
        )(),
    )
    keyboard.button(
        text=texts.reset_mailing,
        callback_data=MailingMenuCallback(
            action=MailingMenuActionEnum.RESET
        )(),
    )

    keyboard.add(close_button(texts))

    keyboard.adjust(1, 1, 3, 1, 1, 1)

    return keyboard.as_markup()
