class MailingMenuError(Exception):
    def __init__(self, message: str = "An error occurred in the mailing menu.") -> None:
        self.message = message
        super().__init__(self.message)
