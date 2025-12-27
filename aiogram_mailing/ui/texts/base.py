from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class MailingMenuButtons:
    start_mailing: str
    preview_mailing: str
    edit_mailing_text: str
    manage_mailing_media: str
    manage_mailing_buttons: str
    schedule_mailing: str


@dataclass(slots=True)
class MailingMenuMessages:
    mailing_menu: str


@dataclass(slots=True)
class MailingMenuErrors:
    ...


@dataclass(slots=True)
class MailingMenuTexts:
    buttons: MailingMenuButtons
    messages: MailingMenuMessages
    errors: MailingMenuErrors

    @classmethod
    def from_code(cls, code: Literal['en', 'ru']) -> "MailingMenuTexts":
        from aiogram_mailing.ui.texts.ru import RU_TEXTS

        mapped_code_to_texts = {
            "ru": RU_TEXTS,
        }

        return mapped_code_to_texts[code]
