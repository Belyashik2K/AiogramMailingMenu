from aiogram_mailing.database.models import MailingModel
from aiogram_mailing.ui.texts.base import MailingMenuMessages


def build_mailing_info_text(
        mailing: MailingModel,
        texts: MailingMenuMessages,
) -> str:
    text_exists = texts.property_set if mailing.text else texts.property_not_set
    current_media_count = 0
    current_buttons_count = 0
    max_media_count = 10
    max_buttons_count = 5

    if mailing.scheduled_at:
        scheduled_at_info = texts.mailing_scheduled.format(
            scheduled_at=mailing.scheduled_at.strftime("%Y-%m-%d %H:%M:%S")
        )
    else:
        scheduled_at_info = texts.mailing_not_scheduled

    return texts.mailing_info_text.format(
        mailing_id=mailing.id,
        text_exists=text_exists,
        current_media_count=current_media_count,
        max_media_count=max_media_count,
        current_buttons_count=current_buttons_count,
        max_buttons_count=max_buttons_count,
        scheduled_at_info=scheduled_at_info,
    )
