import requests
import time

URL = "http://127.0.0.1:8000/generate-summary?protected=false"

print("--- TESTING WITHOUT FIX (Naive Architecture) ---")
print("1. Please ensure Mock LLM is set to 'CRASHED' (run python mock_llm.py)")
print("2. Sending request to /generate-summary without protection...")

try:
    start = time.time()
    # This will hang for 5 seconds (timeout set in main.py)
    resp = requests.get(URL, timeout=10)
    print(f"Response received in {time.time()-start:.2f}s: {resp.text}")
except requests.exceptions.Timeout:
    print(f"FAILED: Request timed out after 10s. The server was blocked!")
except Exception as e:
    print(f"Error: {e}")
