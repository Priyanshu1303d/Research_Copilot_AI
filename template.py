import logging
import os 
from pathlib import Path

logging_config = logging.basicConfig(level=logging.INFO , format="[%(asctime)s] : %(message)s" )


project_name = 'Research_Copilot_AI'

list_of_files = [
    f"Backend/__init__.py",
    f"Backend/main.py",
    f"Backend/database.py",
    f"Backend/models.py",
    f"Backend/schema.py",
    f"Backend/routers/__init__.py",
    f"Backend/routers/chats.py",
    f"Backend/routers/documents.py",
    f"Backend/routers/threads.py",
    f"Backend/routers/auth.py",
    f"Backend/graphs/__init__.py",
    f"Backend/graphs/conversational.py",
    f"Backend/graphs/ingestion.py",
    f"Backend/utils/__init__.py",
    f"Backend/utils/embeddings.py",
    f"Backend/graphs/pinecone_security.py",
    f"Backend/graphs/security.py",
    f"Backend/requirements.txt",
    f"Backend/Dockerfile",
    f"Frontend/__init__.py",
    f"Frontend/Home/__init__.py",
    f"Frontend/Threads/__init__.py",
    f"Frontend/Documents/__init__.py",
    f"Frontend/utils/__init__.py",
    f"Frontend/requirements.txt",
    f"Dockerfile",
    f"requirements.txt",
    f"README.md",
    f".env"
]


for i in list_of_files:
    file_path = Path(i)

    file_dir , file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)

        logging.info(f"Created the directory: {file_dir} for the file : {file_name}")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path , "w") as f:
            pass

        logging.info(f"Created the empty file : {file_name}")

    else:
        logging.info(f"{file_name} :  already exists") 

   