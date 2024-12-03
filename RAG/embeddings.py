from langchain_community.document_loaders import PyMuPDFLoader
from langchain_community.vectorstores import FAISS
from config import embeddings

def create_vectoreDB(file_path:str):
        try:  
            loader = PyMuPDFLoader(file_path=file_path)
            documents = loader.load()
            
            # Process the text to remove "\n\n" and "   "
            for doc in documents:
                doc.page_content = doc.page_content.replace("\n \n", "").replace("   ", "").replace("----", "").replace("====", "")
                
            vectorstore = FAISS.from_documents(
                                            documents, 
                                            embedding=embeddings
                                        )
            
            path = f"vectors/{file_path}".replace(".pdf","").replace("data/","")
            vectorstore.save_local(path)
            
            print(f"VectoreStore has been created at: {path}")
            return {"status": "completed"}
            
        except Exception as e:
            print(str(e))
            return None 
        
        
# create_vectoreDB("data/Oldcastle-KnowldgeBase.pdf")