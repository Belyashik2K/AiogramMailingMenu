from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from aiogram_mailing.database.mixins import IntPKMixin
from aiogram_mailing.database.models.base import Base


class MailingSchemaVersion(IntPKMixin, Base):
    __tablename__ = "mailing_schema_version"

    version: Mapped[int] = mapped_column()
