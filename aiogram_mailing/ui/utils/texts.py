from aiogram_mailing.database.models import MailingModel
from aiogram_mailing.ui.texts.base import MailingMenuMessages


def build_menu_text(
        mailing: MailingModel,
        texts: MailingMenuMessages,
        max_media_count: int,
        max_buttons_count: int,
) -> str:
    return "42"
    # """Build mailing menu text."""
    # text_exists = "✅ Есть" if True else "❌ Нет"
    # current_media_count = 0
    # current_buttons_count = 0
    #
    # if mailing.scheduled_at:
    #     scheduled_at_info = texts.mailing_scheduled_at.format(
    #         scheduled_at=mailing.scheduled_at.strftime("%Y-%m-%d %H:%M:%S")
    #     )
    # else:
    #     scheduled_at_info = texts.mailing_not_scheduled
    #
    # return texts.mailing_main_menu.format(
    #     text_exists=text_exists,
    #     current_media_count=current_media_count,
    #     max_media_count=max_media_count,
    #     current_buttons_count=current_buttons_count,
    #     max_buttons_count=max_buttons_count,
    #     scheduled_at_info=scheduled_at_info,
    # )
