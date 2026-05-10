Usama - BSCS23164

# PDC-Sp24-BSCS23164-Usama
**Student:** Usama  
**Student ID:** BSCS23164  
**Course:** Parallel and Distributed Computing (PDC)  
**Assignment:** Building Resilient Distributed Systems

## Problem Solved
**Problem 3 — Fault Tolerance (The Frozen Server)**
In modern distributed systems, a slow external dependency (like an LLM API) can block the entire backend. This project implements a **Circuit Breaker Pattern** to prevent cascading failures.

## Project Structure
| File | Purpose |
| --- | --- |
| `main.py` | FastAPI backend with Circuit Breaker and Student ID Header |
| `circuit_breaker.py` | Logic for CLOSED, OPEN, and HALF_OPEN states |
| `mock_llm.py` | Separate server simulating a slow/crashed AI service |
| `test_without_fix.py` | Proves the server hangs when LLM fails without protection |
| `test_with_fix.py` | Proves the Circuit Breaker trips and returns fallbacks instantly |

## How to Run

### Step 1: Install Dependencies
```bash
pip install fastapi uvicorn httpx requests
```

### Step 2: Start Servers (Open 2 Terminals)
- **Terminal 1**: Start the Mock LLM: `python mock_llm.py`
- **Terminal 2**: Start the Main Backend: `python main.py`

### Step 3: Run the Tests (Terminal 3)
- **To see the failure**: `python test_without_fix.py`
- **To see the resilience**: `python test_with_fix.py`

## Verify the X-Student-ID Header
Visit `http://127.0.0.1:8000/` and check the **Response Headers** in your browser's Network Tab. Every response includes:
`X-Student-ID: BSCS23164`

## API Endpoints
- `GET /generate-summary`: Calls LLM (protected by circuit breaker)
- `GET /circuit-status`: View current state of the circuit
- `POST /circuit-reset`: Manually reset the circuit to CLOSED
