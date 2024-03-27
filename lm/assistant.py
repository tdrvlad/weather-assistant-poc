from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain.agents import create_openai_functions_agent
from lm.memory import get_session_history
from lm_tools import tools
from lm.prompt import prompt
from dotenv import load_dotenv
import uuid

# Load variables from .env file so that langchain has access to OpenAI API key
load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")
agent = RunnableWithMessageHistory(
    runnable=AgentExecutor(
        agent=create_openai_functions_agent(model, tools, prompt),
        tools=tools,
        verbose=True
    ),
    get_session_history=lambda session_id: get_session_history(session_id),
    input_messages_key="input",
    history_messages_key="chat_history",
)


class Assistant:
    def __init(self, openai_model_id="gpt-3.5-turbo"):
        self.model = ChatOpenAI(model=openai_model_id)
        self.agent = RunnableWithMessageHistory(
            runnable=AgentExecutor(
                agent=create_openai_functions_agent(model, tools, prompt),
                tools=tools,
                verbose=True
            ),
            get_session_history=lambda session_id: get_session_history(session_id),
            input_messages_key="input",
            history_messages_key="chat_history",
        )

    def __call__(self, input_string: str, session_id: str = None):
        if session_id is None:
            session_id = str(uuid.uuid4())
        output = agent.invoke(
            {"input": input_string},
            config={
                "configurable": {"session_id": session_id}
            }
        )
        return session_id, output["output"]


def test():
    assistant = Assistant()
    sess_id, response = assistant("How are you?")
    print(response)
    _, response = assistant("That's not what I asked", session_id=sess_id)
    print(response)


if __name__ == '__main__':
    test()
