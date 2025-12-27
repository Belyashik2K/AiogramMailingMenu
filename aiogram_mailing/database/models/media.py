from typing import TYPE_CHECKING

from sqlalchemy import (
    ForeignKey,
    Enum,
    Text,
)
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)

from aiogram_mailing.database.models.base import Base
from aiogram_mailing.enums import MediaTypeEnum
from ..mixins import IntPKMixin

if TYPE_CHECKING:
    from .mailing import MailingModel


class MailingMediaModel(IntPKMixin, Base):
    __tablename__ = "mailing_media"
    
    mailing_id: Mapped[int] = mapped_column(
        ForeignKey("mailings.id"), index=True
    )
    type: Mapped[MediaTypeEnum] = mapped_column(
        Enum(MediaTypeEnum, native_enum=False),
    )
    file_id: Mapped[str] = mapped_column(Text)

    mailing: Mapped["MailingModel"] = relationship(
        back_populates="media",
        lazy="joined"
    )
