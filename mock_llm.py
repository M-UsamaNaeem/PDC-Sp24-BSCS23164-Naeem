from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/generate")
async def generate():
    # BY DEFAULT: Simulate a slow AI service (10 seconds)
    # This will trigger the Circuit Breaker in the main app
    print("Received request... simulating 10s delay")
    await asyncio.sleep(10)
    return {"response": "AI Summary: Done after 10 seconds."}

if __name__ == "__main__":
    print("Mock LLM Server running on http://127.0.0.1:8001")
    print("Status: SLOW MODE (Default for testing)")
    uvicorn.run(app, host="127.0.0.1", port=8001)
