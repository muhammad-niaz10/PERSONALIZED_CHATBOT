import chromadb

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="website_embeddings")

result = collection.get(include=["documents", "metadatas"])

print("Total documents stored:", len(result['ids']))
print("="*60)

for i, (doc_id, doc, meta) in enumerate(zip(result['ids'], result['documents'], result['metadatas'])):
    print(f"\n--- Chunk {i+1} ---")
    print(f"ID      : {doc_id}")
    print(f"Website : {meta}")
    print(f"Text    : {doc[:300]}") 
    print("-"*60)