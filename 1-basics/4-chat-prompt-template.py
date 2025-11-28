from langchain.prompts import ChatPromptTemplate
from langchain.openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

system = ("system", "You're an assistant that answers question in a {style} style")
user = ("user", "{question}")

chat_prompt = ChatPromptTemplate([system, user])

messages = chat_prompt.format_messages(style ="funny", question="How is Alan Turing?")

for msg in messages:
    print(f"{msg.type}: {msg.content}")

model = ChatOpenAI(model="gpt-5-mini", temperature=0.5)
result = model.invoke(messages)
print(result.content)