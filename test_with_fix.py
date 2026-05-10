import requests
import time

URL = "http://127.0.0.1:8000/generate-summary?protected=true"

print("--- TESTING WITH FIX (Circuit Breaker) ---")
print("Simulating 4 rapid calls while LLM is down...")

for i in range(4):
    start = time.time()
    resp = requests.get(URL)
    data = resp.json()
    duration = time.time() - start
    
    state = data.get("circuit_state", "CLOSED")
    msg = data.get("response")
    
    print(f"Call {i+1}: Duration: {duration:.2f}s | State: {state} | Response: {msg[:30]}...")

print("\nNotice that after 3 failures, the 4th call was INSTANT because the circuit was OPEN.")
