import requests

API_URL = "http://127.0.0.1:8000"


def signup(name, email, password):

    data = {
        "name": name,
        "email": email,
        "password": password
    }

    res = requests.post(f"{API_URL}/create_user", json=data)

    return res


def login(email, password):

    data = {
        "email": email,
        "password": password
    }

    res = requests.post(f"{API_URL}/login", json=data)

    return res


def add_website(url, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "url": url
    }

    res = requests.post(
        f"{API_URL}/addurl",
        json=data,
        headers=headers
    )

    return res


def chat(message, token):

    headers = {
        "Authorization": f"Bearer {token}"
    }

    data = {
        "message": message
    }

    res = requests.post(
        f"{API_URL}/chat",
        json=data,  
        headers=headers
    )

    return res