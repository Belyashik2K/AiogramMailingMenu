![Без имени-1](https://github.com/Belyashik2K/AiogramMailingMenu/assets/126521808/caad0e9c-3063-4709-9a58-bb5336965a74)

> Мультифункциональное модульное меню рассылки для ботов на aiogram v3.x.x

# Russian
## О меню
**Мультифункциональное** **модульное** **меню** **рассылки** **для aiogram v3.x.x** с **полной** поддержкой **форматирования**, **гибкой** настройкой и поддержкой **различных** **медиа**

### Преимущества
* **Полная** **поддержка** форматирования Markdown в Telegram
* **Поддержка** 7 типов **медиа**
   * _Фотография_
   * _Видеозапись_
   * _Аудиозапись_
   * _GIF-изображение_
   * _Голосовое сообщение_
   * _Видеосообщение_
   * _Документ_
* **Полная автономность** – вся **информация** о **рассылке** хранится в **отдельной** **базе** данных _PostgreSQL_ или _SQLite_, в зависимости от вашего выбора
* **Дополнительные** **параметры** рассылки **автоматически** **подстраиваются** под тип файла, используемого в рассылке
* **Отслеживание** **информации** о запущенной рассылке в режиме **реального** **времени**

## Установка
**1.** **Клонируйте** этот репозиторий в свой проект.
```
git clone https://github.com/Belyashik2K/AiogramMailingMenu.git .
```
**2.** **Установите** необходимые **зависимости** для работы меню
```python
pip install sqlalchemy[asyncio] aiogram
```
**3.** **Откройте** mailing/config.py и **замените** **данные** **переменных** своими, **например:**
```python
admin_menu_data = 'back_to_admin' # Callback data для кнопки «↪️ Назад» (возврат в админ-меню)
mailing_button_data = 'mailing' # Callback data для открытия меню рассылки
is_postgres = True # Если вы хотите использовать PostgreSQL + asyncpg — оставьте все как есть, но если вы хотите использовать SQLite + aiosqlite — установите параметр в значение False.
...
DB_INSTANCE = database # Объект класса вашей базы данных, в котором хранятся пользовательские данные (user_ids) (импортирован из другого файла).
BOT_INSTANCE = bot # Объект вашего бота (импортирован из другого файла)
```
**4.** Откройте **класс** для **взаимодействия** с **базой** **данных** и добавьте в него 3 функции. Имя функций должно **строго соответствовать** названию в примере.
  * **get_users_count()**
```python
# Example
async def get_users_count(self) -> int:
    """Получение количества пользователей в базе данных
    
    Returns:
        int: Количество пользователей в базе данных"""
    async with self.session() as session:
        stmt = select(User.user_id)
        result = await session.execute(stmt)
        return len(result.fetchall())
```
 * **get_users_list()**
```python
# Example
async def get_users_list(self) -> list[int]:
    """Получение всех user_id из базы данных
    
    Returns:
        list[int]: Список всех user_id из базы данных"""
    async with self.session() as session:
        stmt = select(User.user_id)
        result = await session.execute(stmt)
        return [user_id[0] for user_id in result]
```
  * **get_admins()**
```python
# Example
async def get_admins(self) -> list[int]:
    """Получение списка всех user_id администраторов бота

    Если информация об администраторах хранится не в базе данных, вы можете использовать следующую реализацию:
        async def get_admins(self) -> list[int]:
            return [123456789, 987654321]
    
    Returns:
        list[int]: Список всех user_id администраторов бота"""
    async with self.session() as session:
        stmt = select(User.user_id).where(User.is_admin == True)
        result = await session.execute(stmt)
        return [user_id[0] for user_id in result]
```
**5.** **Откройте** свой **основной** файл и **импортируйте** все функции из модуля рассылки.
```python
from mailing import *
```
**6.** **Подключите** **роутер** рассылки к диспетчеру
```python
import asyncio

from initialization import dp, bot
from mailing import *

async def main():
    dp.include_router(mailing_router)
    # ...
    # Здесь Ваш код...
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```
**7.** **Создайте** **кнопку** с данными, которые вы установили в _mailing/config.py_, и **создайте** **обработчик**, который **обрабатывает** кнопку возврата в админ-меню.
```python
@user_router.message(Command('admin'))
async def admin_menu(message: types.Message):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await message.answer(text="Админ-меню. Но только с одной кнопкой.", reply_markup=markup.as_markup())

@user_router.callback_query(F.data=="back_to_admin")
async def back_to_admin_menu(call: types.CallbackQuery):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await call.message.edit_text(text="Админ-меню. Но только с одной кнопкой.", reply_markup=markup.as_markup())
```
8. Если все шаги выполнены **правильно**, значит меню рассылки **успешно** **установлено**.

# English
## About menu
**Modular** **mailing** **menu** for Aiogram v3.x.x with formatting support, **flexible** configuration and **support** for various **media**

### Advantages
* **Full** **support** for **Markdown** Telegram formatting
* Support for 7 types of media
  * _Photo_
  * _Video_
  * _Audio_
  * _GIF_
  * _Voice_
  * _Video note_
  * _Document_
* **Full autonomy** - all information about the mailing is stored in a separate PostgreSQL or SQLite database
* **Additional** mailing **options** are **automatically** **adjusted** to the type of file used in the mailing
* **Tracking** information about a launched mailing **in real-time**

## Installatiion
**1.** **Clone** this repo **to your own project**
```
git clone https://github.com/Belyashik2K/AiogramMailingMenu.git .
```
**2.** **Install** the **necessary** **dependencies** for the menu **to work**
```python
pip install sqlalchemy[asyncio] aiogram
```
**3.** **Open** _mailing/config.py_ and **replace** **vars** data **with** **your own**, **example**
```python
admin_menu_data = 'back_to_admin' # Callback data for "↪️ Назад" button (back to admin menu)
mailing_button_data = 'mailing' # Callback data for mailing menu button
is_postgres = True # If you wanna use PostgreSQL + asyncpg - leave this as is, but if you wanna use SQLite + aiosqlite - set parameter to False
...
DB_INSTANCE = database # The object of your database class that stores user data (user_ids) (imported from another file)
BOT_INSTANCE = bot # The object of your bot (imported from another file)
```
**4.** **Open** your **class** **for interact with database** and **add** 3 **functions** into it. The name of the functions must **strictly correspond** to the name in the example.
  * **get_users_count()**
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
  * **get_users_list()**
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
  * **get_admins()**
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
**5.** **Open** your **main** **file** and **import** **all** functions from **mailing**
```python
from mailing import *
```
**6.** **Include** **mailing** **router** in dispatcher
```python
import asyncio

from initialization import dp, bot
from mailing import *

async def main():
    dp.include_router(mailing_router)
    # ...
    # Here is your own code
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
```
**7.** **Create** **inline** **button** with data, which you set in_ mailing/config.py_ and **create** **handler** which **handle** **callback** of **exit** button
```python
@user_router.message(Command('admin'))
async def admin_menu(message: types.Message):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await message.answer("Admin-menu. But with only one button.", reply_markup=markup.as_markup())

@user_router.callback_query(F.data=="back_to_admin")
async def back_to_admin_menu(call: types.CallbackQuery):
  markup = InlineKeyboardBuilder()
  markup.button(text="Mailing", callback_data="mailing")
  await call.message.edit_text(text="Admin-menu. But with only one button.", reply_markup=markup.as_markup())
```
**8.** If **all** the steps **have** **been** **completed**, then the **mailing** **menu** has been **successfully installed**.
