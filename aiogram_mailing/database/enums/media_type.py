from enum import (
    StrEnum,
    auto,
)


class MediaTypeEnum(StrEnum):
    PHOTO = auto()
    VIDEO = auto()
    AUDIO = auto()
    ANIMATION = auto()
    VOICE = auto()
    VIDEO_NOTE = auto()
    DOCUMENT = auto()
