from fastapi import FastAPI, Request, HTTPException
import httpx
import asyncio
from circuit_breaker import CircuitBreaker

# 1. MANDATORY MIDDLEWARE (BSCS23164)
STUDENT_ID = "BSCS23164"

app = FastAPI(title="StudySync Resilient Backend - Usama")

@app.middleware("http")
async def add_student_id_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Student-ID"] = STUDENT_ID
    return response

# Initialize Circuit Breaker
llm_breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=10)
LLM_URL = "http://127.0.0.1:8001/generate"

async def call_external_llm():
    # SET TIMEOUT TO 5s so it fails when Mock LLM takes 10s
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            response = await client.get(LLM_URL)
            return response.json()
        except Exception as e:
            # This exception trips the Circuit Breaker
            raise Exception(f"External API Timeout/Error: {e}")

@app.get("/")
async def root():
    return {"message": "API Online", "student": "Usama", "id": STUDENT_ID}

@app.get("/generate-summary")
async def generate_summary(protected: bool = True):
    if not protected:
        return await call_external_llm()
    try:
        return await llm_breaker.call(call_external_llm)
    except Exception as e:
        return {
            "response": "Fallback: AI is busy. Using cached knowledge.",
            "error": "External Service Timeout",
            "circuit_state": llm_breaker.state.value
        }

if __name__ == "__main__":
    import uvicorn
    print(f"Starting Main Backend on http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
