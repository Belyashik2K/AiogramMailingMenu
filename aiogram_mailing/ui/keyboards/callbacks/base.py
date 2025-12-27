from aiogram.filters.callback_data import CallbackData


class CustomCallbackData(CallbackData, prefix="custom"):

    def __call__(self, *args, **kwargs) -> str:
        return self.pack()
