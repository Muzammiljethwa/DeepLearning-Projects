from langchain_community.vectorstores import FAISS
from config import embeddings, llm
from pprint import pprint
from langchain.retrievers.document_compressors import FlashrankRerank
from langchain.retrievers import ContextualCompressionRetriever
from langchain_core.prompts import ChatPromptTemplate

compressor = FlashrankRerank()

def get_vectoreDB(file_path:str):
    
    path = f"vectors/{file_path}".replace(".pdf","").replace("data/","")
    vectoreStore = FAISS.load_local(
                            path,
                            embeddings,
                            allow_dangerous_deserialization=True
                        )
        
    vectoreStore_as_retriever = vectoreStore.as_retriever(
                                    search_type="similarity",
                                    search_kwargs={
                                        "k": 10,
                                        "include_metadata": True
                                    }
                                )
    
    #ReRanker
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor,
        base_retriever=vectoreStore_as_retriever
        )
            
    return compression_retriever


system_prompt = """
You are a Medical Chatbot named as Medi. Your task is to assist as a doctor.

Your tasks are given below:
- Answer the given question from the given context. If the question is out of context from medical feild, just tell the user "I don't know about it".
- If the question is related to medical field and not relevent to context, then generate by your own self 
- If the question is about the context given, explain the user according to the most relevent context.
- Explain the user a proper short Answer, don't copy the whole context, explain it by your self.
- If someone ask your name, so tell them

Remember to answer in a precise way and to the point as a doctor.

query: '''{query}'''
"""

PROMPT = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "context: '''{context}'''")
    ]
)

llm_chain = PROMPT | llm
vectoreDB = get_vectoreDB("data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf")

def ask_ai(query):
    docs  = vectoreDB.invoke(query)

    context_text = "\n\n---\n\n".join([doc.page_content for doc in docs])

    response = llm_chain.invoke({
                        "context": context_text,
                        "query" : query
                        }
                    )
    return response.content