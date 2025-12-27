from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Enum,
    Text,
    JSON,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from aiogram_mailing.database.mixins import IntPKMixin
from aiogram_mailing.database.enums import MailingStatusEnum
from aiogram_mailing.database.models.base import Base
from aiogram_mailing.core.utils import get_current_dt

if TYPE_CHECKING:
    from .media import MailingMediaModel
    from .button import MailingButtonModel


class MailingModel(IntPKMixin, Base):
    __tablename__ = "mailings"

    text: Mapped[str | None] = mapped_column(Text)
    link_preview_options: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    status: Mapped[MailingStatusEnum] = mapped_column(
        Enum(MailingStatusEnum, native_enum=False),
        default=MailingStatusEnum.DRAFT,
        index=True
    )
    created_at: Mapped[datetime] = mapped_column(
        default=get_current_dt,
    )
    scheduled_at: Mapped[datetime | None] = mapped_column()
    started_at: Mapped[datetime | None] = mapped_column()
    finished_at: Mapped[datetime | None] = mapped_column()

    media: Mapped[list["MailingMediaModel"]] = relationship(
        back_populates="mailing",
        lazy="selectin",
        cascade="all, delete-orphan",
    )
    buttons: Mapped[list["MailingButtonModel"]] = relationship(
        back_populates="mailing",
        lazy="selectin",
        cascade="all, delete-orphan",
    )
