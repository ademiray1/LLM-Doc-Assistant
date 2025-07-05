from langchain.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama


from shared.loaders import load_document


def process_query(filename, content, prompt):
    try:
        print(f"[DEBUG] Processing: {filename}")
        docs = load_document(filename, content)
        print(f"[DEBUG] Loaded {len(docs)} documents")
 
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vectordb = FAISS.from_documents(docs, embeddings)
        print(f"[DEBUG] Vectorstore created")
 
        retriever = vectordb.as_retriever()
        llm = Ollama(model="mistral")
        print(f"[DEBUG] Running QA chain")
 
        chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
        result = chain.run(prompt)
        return result
 
    except Exception as e:
        print("[ERROR] Crash in process_query():", str(e))
        raise


# def process_query(filename, content, prompt):
#     docs = load_document(filename, content)
#     embeddings = OllamaEmbeddings(model="nomic-embed-text")
#     vectordb = FAISS.from_documents(docs, embeddings)
#     retriever = vectordb.as_retriever()
#     llm = Ollama(model="mistral")
#     qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
#     return qa.run(prompt)

