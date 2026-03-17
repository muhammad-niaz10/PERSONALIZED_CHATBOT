TASK : RAG_CHATBOT_WITH_DATABASE

WORKFLOW :
create a database in postgresql with 3 tables
signup and save the user in database
did login authentication then give the user a token 
protect the routes using authentication
create a addurl endpoint where user add the url of website and automatically web scrap in the backend and store that data in the database
with login user id
i use the logic if the user has already add the url which is stored in database with user id LLM give the answer 
using rag otherwise normal LLM will generate answer
i stored the chat history of the user in my postgresql 

WORKFLOW OF RAG WITH WEBSCRAPPING :
the user add the url 
the text will be extract from the url using beautifulsoap
the text will divide into chunks 
chunks will be converted into vector/embeddings using sentencetransformer
that embeddings will store in the vector database using chromadb
the user will ask the question it will convert into the vector then that vector will match in the vectordb the most similiar chunks will
extract and then that chunks and user question will go the LLM and it wiil generate answer

ERRORS I FACED :
during the user chat endpoint the problem i faced that i did not save the chunks with website ids using metadata in chromadb which cause
not to give the accurate answer using rag so i delete the previous chromadb and create the new vectordb which solves my problem








