from typing import TYPE_CHECKING

from sqlalchemy import (
    String,
    ForeignKey,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from aiogram_mailing.database.mixins import IntPKMixin
from aiogram_mailing.database.models.base import Base

if TYPE_CHECKING:
    from .mailing import MailingModel


class MailingButtonModel(IntPKMixin, Base):
    __tablename__ = "mailing_buttons"

    mailing_id: Mapped[int] = mapped_column(
        ForeignKey("mailings.id"), index=True
    )
    text: Mapped[str] = mapped_column(
        String(32)
    )
    url: Mapped[str | None] = mapped_column(
        String(256)
    )
    callback_data: Mapped[str | None] = mapped_column(
        String(64)
    )
    copy_text_on_click: Mapped[bool] = mapped_column(
        default=False
    )

    mailing: Mapped["MailingModel"] = relationship(
        back_populates="buttons",
        lazy="joined"
    )
