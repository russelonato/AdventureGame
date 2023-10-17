from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
import warnings
import json
import sys
from game import start

warnings.simplefilter('ignore')

with open("config.json") as f:
    config = json.load(f)

memory = ConversationBufferWindowMemory(memory_key="chat_history")

memory.clear()

llm_chain = LLMChain(
    llm=OpenAI(openai_api_key=config["apikey"]),
    prompt=PromptTemplate(
        input_variables=["chat_history", "human_input"],
        template=open(config["template"]).read()
    ),
    memory=memory
)

start(llm_chain)
print(memory.chat_memory.messages)