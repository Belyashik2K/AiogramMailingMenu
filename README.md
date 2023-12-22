# Mailing menu for Telegram bots on Aiogram v3.x.x
> Multifunctional mailing menu, compatible with any Aiogram v3.x.x bot
<p align="center">
  <img src="https://github.com/Belyashik2K/AiogramMailingMenu/assets/126521808/c2060702-6c25-4b74-9792-a76ca16d8862" />
</p>

## About menu
Modular mailing menu for Aiogram v3.x.x with formatting support, flexible configuration and support for various media

### Advantages
* Full support for Markdown Telegram formatting
* Support for 7 types of media
  * Photo
  * Video
  * Audio
  * GIF
  * Voice
  * Video note
  * Document
* Full autonomy - all information about the mailing is stored in a separate PostgreSQL or SQLite database
* Additional mailing options are automatically adjusted to the type of file used in the mailing
* Tracking information about a launched mailing in real-time

## Installation
1. Clone this repo to your own project
```
git clone https://github.com/Belyashik2K/AiogramMailingMenu.git .
```
2. Open mailing/config.py and replace vars data with your own, example
```python
admin_menu_data = 'back_to_admin' # Callback data for "↪️ Назад" button (back to admin menu)
mailing_button_data = 'mailing' # Callback data for mailing menu button
is_postgres = True # If you wanna use PostgreSQL + asyncpg - leave this as is, but if you wanna use SQLite + aiosqlite - set parameter to False
...
DB_INSTANCE = database # The object of your database class that stores user data (user_ids) (imported from another file)
BOT_INSTANCE = bot # The object of your bot (imported from another file)
```
3. Open your class for interact with database and add 3 functions into it. The name of the functions must <b>strictly correspond</b> to the name in the example.
  * get_users_count()
```python
# Example
async def get_users_count(self) -> int:
    """Get users count in database
    
    Returns:
        int: Users count"""
    async with self.session() as session:
        stmt = select(User.user_id)
        result = await session.execute(stmt)
        return len(result.fetchall())
  ```
  * get_users_list()
```python
# Example
async def get_users_list(self) -> list[int]:
    """Get all users' ids
    
    Returns:
        list[int]: List of users' ids"""
    async with self.session() as session:
        stmt = select(User.user_id)
        result = await session.execute(stmt)
        return [user_id[0] for user_id in result]
```
  * get_admins()
```python
# Example
async def get_admins(self) -> list[int]:
    """Get all ID of admins

    If info about admins is not in database, you may use this method:
        async def get_admins(self) -> list[int]:
            return [123456789, 987654321]
    
    Returns:
        list[int]: List of admins' ids"""
    async with self.session() as session:
        stmt = select(User.user_id).where(User.is_admin == True)
        result = await session.execute(stmt)
        return [user_id[0] for user_id in result]
```
4. Open your main file and import all functions from mailing
```python
from mailing import *
```
5. Include mailing router in dispatcher
```python
import asyncio

from initialization import dp
from mailing import *

async def main():
    dp.include_router(mailing_router)
    # ...
    # Here is your own code
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```
6. Create inline button with data, which you set in mailing/config.py and create handler which handle callback of exit button
```python
@user_router.message(Command('admin'))
async def admin_menu(message: types.Message):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await message.answer("Admin-menu. But with only one button.", reply_markup=markup)

@user_router.callback_query(F.data=="back_to_admin")
async def back_to_admin_menu(call: types.CallbackQuery):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await message.answer("Admin-menu. But with only one button.", reply_markup=markup)
```
7. If all the steps have been completed, then the mailing menu has been successfully installed.
