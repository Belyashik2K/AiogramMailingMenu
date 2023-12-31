# CHECK THE README.MD BEFORE STARTING

class Config:
    # Set your own callback data for you mailing button here
    # If you don't know what you're doing, don't change this
    # and create new buttons with the same callback data
    admin_menu_data = "SET_YOUR_OWN" # Callback data for back to admin menu button
    mailing_button_data = "SET_YOUR_OWN" # Callback data for mailing menu button 

    class DB:
        # If you want to use sqlite, set this to False, else set this to True
        is_postgres = True

        # Don't change this if you don't know what you're doing
        DB_DRIVER = "postgresql+asyncpg" if is_postgres else "sqlite+aiosqlite"
        # Postgres user (if you use sqlite, you can leave this as is)
        DB_USER = "postgres" 
        # Postgres password (if you use sqlite, you can leave this as is)
        DB_PASSWORD = "postgres"
        # Postgres host (if you use sqlite, you can leave this as is)
        DB_HOST = "localhost"
        # Postgres port (if you use sqlite, you can leave this as is)
        DB_PORT = "5432"
        # Postgres/sqlite database name (if you use sqlite, don't change this if you don't know what you're doing)
        DB_NAME = "mailing" if is_postgres else "mailing/database/mailing.db"

        # Don't change this if you don't know what you're doing
        DB_URL = f"{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" if is_postgres else f"{DB_DRIVER}:///{DB_NAME}"

    class UserDB:
        # Set DB_INSTANCE to your database instance with users data
        # All information about the necessary functions 
        # in the Database class can be found in the README.MD
        DB_INSTANCE = None

    class Bot:
        # Set BOT_INSTANCE to your bot instance
        BOT_INSTANCE = None