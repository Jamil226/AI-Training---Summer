# Project Setup Guide

This project uses **Conda** for environment management, `requirements.txt` for Python dependencies, and a `.env` file for storing environment variables.

## 📦 Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)
- Python 3.11+ (managed via Conda)
- `.env` file (included in this directory)
- `requirements.txt` (included)

---

## Step-by-Step Setup

### 1. Create and Activate a Conda Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. List all Packages/Libraries

```bash
conda list
```
