from aiogram.types import (
    InlineKeyboardMarkup
)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from aiogram_mailing.ui.config import MENU_AUTHOR_URL
from aiogram_mailing.ui.keyboards.builders.common import (
    close_button,
    back_button,
)
from aiogram_mailing.ui.keyboards.callbacks import MailingMainMenuCallback
from aiogram_mailing.ui.keyboards.callbacks.menu import (
    MailingMainMenuActionEnum,
    ManageMailingActionEnum,
    ManageMailingCallback,
)
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


def manage_mailing_keyboard(
        texts: MailingMenuButtons,
        mailing_id: int,
) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.button(
        text=texts.start_mailing,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.START
        )(),
    )
    keyboard.button(
        text=texts.preview_mailing,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.PREVIEW
        )(),
    )
    keyboard.button(
        text=texts.edit_mailing_text,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.EDIT_TEXT
        )(),
    )
    keyboard.button(
        text=texts.manage_mailing_media,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.MANAGE_MEDIA
        )(),
    )
    keyboard.button(
        text=texts.manage_mailing_buttons,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.MANAGE_BUTTONS
        )(),
    )
    keyboard.button(
        text=texts.reset_mailing,
        callback_data=ManageMailingCallback(
            mailing_id=mailing_id,
            action=ManageMailingActionEnum.RESET
        )(),
    )

    keyboard.add(
        back_button(
            texts,
            callback_data=MailingMainMenuCallback(
                action=MailingMainMenuActionEnum.OPEN
            )()
        )
    )
    keyboard.add(close_button(texts))
    keyboard.adjust(1, 1, 3, 1, 1)

    return keyboard.as_markup()
