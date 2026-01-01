from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class MailingMenuButtons:
    start_mailing: str
    preview_mailing: str
    edit_mailing_text: str
    manage_mailing_media: str
    manage_mailing_buttons: str
    reset_mailing: str

    mailing_list: str
    create_mailing: str
    menu_author_link: str

    back: str
    close_menu: str


@dataclass(slots=True)
class MailingMenuMessages:
    mailing_main_menu: str

    mailing_info_text: str
    mailing_scheduled: str
    mailing_not_scheduled: str

    property_set: str
    property_not_set: str


@dataclass(slots=True)
class MailingMenuErrors:
    no_mailings_found: str


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
