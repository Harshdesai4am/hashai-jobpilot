from app.ai_client import AIClient

client = AIClient()

response = client.ask(
    "Introduce yourself in one sentence."
)

print(response)