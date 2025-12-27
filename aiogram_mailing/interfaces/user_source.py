from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Sequence,
)


class MailingUsersSource(ABC):

    @abstractmethod
    async def count_recipients(self) -> int:
        """Get users count to whom mailing will be sent.

        Function should return total number of users to whom mailing will be sent.

        Returns:
            int: Total number of users.
        """
        ...

    @abstractmethod
    async def get_recipients(self) -> Sequence[int]:
        """Get all user IDs to whom mailing will be sent.

        Returns:
            Sequence[int]: Sequence of user ids.
        """
        ...

    @abstractmethod
    async def get_admins(self) -> Sequence[int]:
        """Get IDs of admins with access to the mailing menu.

        Admin in this context is a user who has access to the mailing menu.

        Returns:
            Sequence[int]: Sequence of admin ids.
        """
        ...
