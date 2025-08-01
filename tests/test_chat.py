from app.app import app
from unittest.mock import patch, MagicMock

# Fake OpenAI response
def fake_completion(*_, **__):
    fake = MagicMock()
    fake.choices = [MagicMock(message=MagicMock(content="Hi, I am a bot"))]
    return fake

# Patch OpenAI client call to return the fake response
@patch("app.app.client.chat.completions.create", side_effect=fake_completion)
def test_chat_endpoint(_mock):
    c = app.test_client()
    r = c.post("/chat", json={"question": "Hello?"})
    assert r.status_code == 200
    assert r.get_json()["AI CHAT REPLY"] == "Hi, I am a bot"
