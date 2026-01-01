from aiogram_mailing.ui.texts.base import (
    MailingMenuTexts,
    MailingMenuButtons,
    MailingMenuMessages,
    MailingMenuErrors,
)

# ========= BUTTONS =========

RU_BUTTONS = MailingMenuButtons(
    start_mailing="📩 Начать рассылку",
    preview_mailing="👀 Предпросмотр",
    edit_mailing_text="✍️ Текст",
    manage_mailing_media="🖼️ Медиа",
    manage_mailing_buttons="📌 Кнопки",
    reset_mailing="🔄 Сбросить информацию о рассылке",
    mailing_list="📋 Список рассылок",
    create_mailing="➕ Создать рассылку",
    menu_author_link="с ❤️‍🔥 от Belyashik2K",
    back="🔙 Назад",
    close_menu="❌ Закрыть меню",
)
# ============================

# ========= MESSAGES =========

mailing_main_menu_text = """
📬 *Меню управления рассылками*

Выберите действие в меню ниже:
"""
mailing_info_text = """
*Информация о рассылке №{mailing_id}:*
— 📄 Текст: {text_exists}
— 🖼️ Медиа: {current_media_count}/{max_media_count}
— 📌 Кнопок: {current_buttons_count}/{max_buttons_count}
— {scheduled_at_info}
"""

mailing_scheduled_at = "⏰ Рассылка *запланирована* на: `{scheduled_at}`"
mailing_not_scheduled = "⏰ Рассылка *не запланирована*"

RU_MESSAGES = MailingMenuMessages(
    mailing_main_menu=mailing_main_menu_text,
    mailing_info_text=mailing_info_text,
    mailing_scheduled_at=mailing_scheduled_at,
    mailing_not_scheduled=mailing_not_scheduled,
)

# ============================

# ========= ERRORS =========

RU_ERRORS = MailingMenuErrors(
    no_mailings_found="⚠️ Нет доступных для просмотра рассылок",
)

# ============================

# ======== COMBINED TEXTS ========

RU_TEXTS = MailingMenuTexts(
    buttons=RU_BUTTONS,
    messages=RU_MESSAGES,
    errors=RU_ERRORS,
)

# ================================
