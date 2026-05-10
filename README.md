Usama Naeem - BSCS23164

# PDC-Sp24-BSCS23164-Naeem

## Overview
This repository contains the implementation of a resilient distributed system backend for the StudySync assignment. It specifically addresses **Problem 3: Fault Tolerance** by implementing a **Circuit Breaker Pattern**.

## Features
- **FastAPI Middleware**: Injects `X-Student-ID: BSCS23164`.
- **Circuit Breaker**: Manages failures and prevents server hangs.

## How to Run
1. `pip install fastapi uvicorn httpx requests`
2. `python mock_llm.py` (Terminal 1)
3. `python main.py` (Terminal 2)
4. `python test_with_fix.py` (Terminal 3)
