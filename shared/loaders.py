from langchain.document_loaders import UnstructuredPowerPointLoader, PyPDFLoader, Docx2txtLoader
from langchain.schema import Document
import tempfile
 
def load_document(filename, content) -> list[Document]:
    suffix = filename.split('.')[-1].lower()
    print('this is filename',filename)
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(content)
        tmp_path = tmp.name
 
    if suffix == "pdf":
        return PyPDFLoader(tmp_path).load()
    elif suffix == "docx":
        return Docx2txtLoader(tmp_path).load()
    elif suffix in ("ppt", "pptx"):
        return UnstructuredPowerPointLoader(tmp_path).load()
    elif suffix == "txt":
        with open(tmp_path, "r") as f:
            return [Document(page_content=f.read())]
    else:
        raise ValueError("Unsupported file type")
