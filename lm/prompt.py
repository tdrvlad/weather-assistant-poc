# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             "You are a helpful assistant providing information about weather forecasts.",
#         ),
#         ("user", "{input}"),
#         MessagesPlaceholder(variable_name="agent_scratchpad"),
#     ]
# )

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, PromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate

prompt = ChatPromptTemplate(
    input_variables=['agent_scratchpad', 'input'],
    messages=[
        SystemMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=[],
                template='You are a helpful assistant'
            )
        ),
        MessagesPlaceholder(
            variable_name='chat_history',
            optional=True
        ),
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=['input'],
                template='{input}')
        ),
        MessagesPlaceholder(
            variable_name='agent_scratchpad'
        )
    ],
    validate_template=False
)