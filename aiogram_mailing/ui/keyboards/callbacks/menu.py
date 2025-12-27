from enum import (
    StrEnum,
    auto,
)

from aiogram_mailing.ui.keyboards.callbacks.base import CustomCallbackData


class MailingMainMenuActionEnum(StrEnum):
    # START = auto()
    # PREVIEW = auto()
    # EDIT_TEXT = auto()
    # MANAGE_MEDIA = auto()
    # MANAGE_BUTTONS = auto()
    # RESET = auto()
    GET_ALL_MAILINGS = auto()
    CREATE_MAILING = auto()
    CLOSE = auto()


class MailingMainMenuCallback(CustomCallbackData, prefix="mailing_main_menu"):
    action: MailingMainMenuActionEnum
