import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def check_health():
    try:
        resp = requests.get(f"{BASE_URL}/")
        print(f"[Health Check] Status: {resp.status_code}, Header: {resp.headers.get('X-Student-ID')}")
    except:
        print("[Health Check] FAILED")

def trigger_fixed_llm():
    start = time.time()
    resp = requests.get(f"{BASE_URL}/fixed-llm")
    print(f"[Protected LLM] Time: {time.time()-start:.2f}s, Response: {resp.json().get('response')[:25]}...")

if __name__ == "__main__":
    print("--- Starting Simulation for Usama (BSCS23164) ---")
    check_health()
    for i in range(4):
        print(f"Request {i+1}:")
        trigger_fixed_llm()
