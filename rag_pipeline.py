from app.embeddings import embedding,retrieve_top_chunks
import google.generativeai as genai
from app.core.config import GEMINI_KEY
import re
from app.schemas import WebsiteURL
from app.models import Websites


genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(context, question):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer only based on the above context.
"""

    response = model.generate_content(prompt)

    clean_response = re.sub(r"[^A-Za-z0-9\s]", "", response.text)

    clean_response = clean_response.replace("\\n", "\n")

    text=re.sub(r"\s+"," ",clean_response).strip()



    return text

        
def gemini_answer(question):
    response=model.generate_content(question)
    gemini_reply=response.text
    
    clean_response = re.sub(r"[^A-Za-z0-9\s]", "", gemini_reply)

    clean_response = clean_response.replace("\\n", "\n")

    text=re.sub(r"\s+"," ",clean_response).strip()

    return {"reply":text , "mode" : "general"}

def ask(question,current_user,db):


    websites = db.query(Websites).filter(Websites.user_id == current_user.id).all()


    if not websites:
        return gemini_answer(question)

    user_website_ids = [str(w.id) for w in websites]  

    embed = embedding(question)

    top_chunks = retrieve_top_chunks(embed,user_website_ids)
    text = "\n".join(top_chunks) 


    answer =generate_answer(text,question)

    return {"reply": answer, "mode": "website"}