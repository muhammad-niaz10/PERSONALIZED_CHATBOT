from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

#client = chromadb.Client()

#client = chromadb.Client(Settings(
 #   persist_directory="./chroma_db"  # make it persistent
#))

client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(
    name="website_embeddings"
)

def chunking(text, chunk_size=400, overlap=50):

    chunks = []
    start = 0

    while start < len(text):

        end = start + chunk_size
        chunks.append(text[start:end])

        start += chunk_size - overlap

    return chunks


model = SentenceTransformer("all-MiniLM-L6-v2")


def embedding(text):
    enocded=model.encode(text)
    return enocded.tolist()


def store(chunks,website_id):
    for i,chunk in enumerate(chunks):
        existing = collection.get()
        counter = len(existing['ids'])

        vector=embedding(chunk)
        collection.add(
            ids=[str(counter+i)],
            documents=[chunk],
            embeddings=[vector],
            metadatas=[{"website_id": str(website_id)}]
            
        )
        counter+=1        


def process_text(text,website_id):
    chunks = chunking(text)
    store(chunks,website_id)

    return {"status": "success", "chunks_stored": len(chunks), "text" : text }


def retrieve_top_chunks(query_vector,user_website_ids, n=3):
    user_website_ids = [str(i) for i in user_website_ids]
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n,
        include=["documents", "distances"],
        where={"website_id": {"$in": user_website_ids}}
    )
    documents = results['documents'][0] 
    return documents
