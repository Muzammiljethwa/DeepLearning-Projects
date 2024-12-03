from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

import os
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = ""
model_name = os.getenv("MODEL_NAME")
embedding_model = os.getenv("EMBEDDING_MODEL")

llm = ChatOpenAI(model=model_name)
embeddings = OpenAIEmbeddings(model=embedding_model)
