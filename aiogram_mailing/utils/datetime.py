from datetime import (
    datetime,
    timezone,
)


def get_current_dt() -> datetime:
    dt = datetime.now(tz=timezone.utc)
    return dt.replace(microsecond=0, tzinfo=None)
