from enum import (
    StrEnum,
    auto,
)

from aiogram_mailing.ui.keyboards.callbacks.base import CustomCallbackData


class MailingMenuActionEnum(StrEnum):
    START = auto()
    PREVIEW = auto()
    EDIT_TEXT = auto()
    MANAGE_MEDIA = auto()
    MANAGE_BUTTONS = auto()
    SCHEDULE = auto()
    RESET = auto()
    CLOSE = auto()


class MailingMenuCallback(CustomCallbackData, prefix="mailing_menu"):
    action: MailingMenuActionEnum
