from abc import ABC, abstractmethod
from typing import Awaitable


class UserDataSource(ABC):

    @abstractmethod
    def get_users_count(self) -> Awaitable[int]:
        """Get users count."""
        ...

    @abstractmethod
    def get_user_ids(self) -> Awaitable[list[int]]:
        """Get all user ids for mailing."""
        ...

    @abstractmethod
    def get_admin_ids(self) -> Awaitable[list[int]]:
        """Get all admin ids."""
        ...

