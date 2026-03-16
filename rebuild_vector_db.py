import chromadb

client = chromadb.Client()

client.delete_collection("website_embeddings")

print("Old Vector DB Deleted")