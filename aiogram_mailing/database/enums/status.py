from enum import (
    StrEnum,
    auto,
)


class MailingStatusEnum(StrEnum):
    ACTIVE = auto()
    PAUSED = auto()
    COMPLETED = auto()
    CANCELLED = auto()
    SCHEDULED = auto()
    DRAFT = auto()
