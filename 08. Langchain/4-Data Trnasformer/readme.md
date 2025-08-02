### Langchain API Keys:

https://smith.langchain.com/o/3e5654ab-e8dd-5429-a106-f453c374aa3d/settings/apikeys

# Project Setup Guide

This project uses **Conda** for environment management, `requirements.txt` for Python dependencies, and a `.env` file for storing environment variables.

## 📦 Prerequisites

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/)
- Python 3.11+ (managed via Conda)
- `.env` file (included in this directory)
- `requirements.txt` (included)

---

## 🔧 Step-by-Step Setup

### 1. Create and Activate a Conda Environment

```bash
conda create --name myenv python=3.12 -y
conda activate myenv
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. List all Packages/Libraries

```bash
conda list
```
