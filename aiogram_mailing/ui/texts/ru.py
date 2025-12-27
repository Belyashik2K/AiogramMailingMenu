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
    schedule_mailing="⏰ Запланировать",
)
# ============================

# ========= MESSAGES =========

mailing_menu_text = """
📬 *Меню рассылки*

Выберите действие ниже:
"""

RU_MESSAGES = MailingMenuMessages(
    mailing_menu=mailing_menu_text
)

# ============================

# ========= ERRORS =========

RU_ERRORS = MailingMenuErrors()

# ============================

# ======== COMBINED TEXTS ========

RU_TEXTS = MailingMenuTexts(
    buttons=RU_BUTTONS,
    messages=RU_MESSAGES,
    errors=RU_ERRORS,
)

# ================================
