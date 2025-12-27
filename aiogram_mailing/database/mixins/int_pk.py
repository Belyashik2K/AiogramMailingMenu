from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class IntPKMixin:
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )