from langchain.memory import PostgresChatMessageHistory
from dotenv import load_dotenv
import os
import uuid

# Load variables from .env file so that the database client has access to the database credentials
load_dotenv()

db = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_pass = os.getenv('POSTGRES_PASSWORD')
db_host = os.getenv('POSTGRES_HOST')
db_port = os.getenv('POSTGRES_PORT')


def get_session_history(session_id=None) -> PostgresChatMessageHistory:
    if session_id is None:
        session_id = uuid.uuid4()
    history = PostgresChatMessageHistory(
        connection_string=f"postgresql://{db_user}:{db_pass}@{db_host}/{db}",
        session_id=session_id,
    )
    return history
