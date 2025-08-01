python -m venv .venv
source .venv/bin/activate (mac/Linux)
.\.venv\Scripts\activate (Windows).
pip install -r requirements.txt
python -m app.app

curl -Method POST -Uri "http://127.0.0.1:5000/chat" -Headers @{ "Content-Type" = "application/json" } -Body '{"question":"What is DevOps?"}'

docker build -t llm-chat:dev .
docker run -it --rm -p 5000:5000 --env-file .env llm-chat:dev

