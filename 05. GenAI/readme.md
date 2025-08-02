## Run Streamlit in Virtual Environment

```
python3 -m venv .venv

```

## Step-by-Step: Create Local venv in Current Directory

### 1. Create the virtual environment

```
python3 -m venv .venv

```

This will create a folder named `.venv` inside your current directory.

### 2. Activate the environment

```
source .venv/bin/activate

```

This will create a folder named `.venv` inside your current directory.

### 3. Install dependencies

```
pip install streamlit requests
```

### 4. Run the Streamlit App

```
streamlit run ollama_chat_app.py
```

### Testing Ollama API with Postman

This guide shows how to use **Postman** to interact with a **locally running Ollama LLM** (like `gemma:2b` or `llama3`) using the `/api/generate` endpoint.

---

**Prerequisites**

- Ollama is installed and running
- A model is pulled and ready (e.g., `gemma:2b`, `llama3`)
- You’ve started the model with:
  ```bash
  ollama run gemma:2b
  ```
- Send a POST request to:

  ```bash
  http://localhost:11434/api/generate
  ```

  **Step-by-Step Instructions**

1. Open Postman
   Launch Postman on your machine.
2. Set Request Type and URL
   Method: **POST**
   URL:**http://localhost:11434/api/generate**

3. Set Headers
   Go to the Headers tab and add:
   Key: **Content-Type**
   Value: **application/json**
4. Set Request Body
   Go to the Body tab:

   - Select raw
   - Choose JSON as the format
   - Paste the following example:

   ```
   {
    "model": "gemma:2b",
    "prompt": "What is the capital of Islamabad?",
    "temperature": 0.7,
    "stream": false,
    "options": {
        "num_predict": 100
    }
   }

   ```

5. Send the Request
   Click the Send button.
   You should receive a JSON response like:
   ```
    {
        "model": "gemma:2b",
        "created_at": "2025-08-02T09:15:01.559275Z",
        "response": "The capital of Pakistan is Islamabad. It is also the political and administrative capital of the country.",
        "done": true,
        "done_reason": "stop",
        "context": [
            968,
            2997,
            235298,
            559,
            235298,
            15508,
            235313,
            1645,
            108,
            1841,
            603,
            573,
            6037,
            576,
            18641,
            235336,
            107,
            235248,
            108,
            235322,
            2997,
            235298,
            559,
            235298,
            15508,
            235313,
            2516,
            108,
            651,
            6037,
            576,
            18641,
            603,
            124604,
            235265,
            1165,
            603,
            1170,
            573,
            6269,
            578,
            19323,
            6037,
            576,
            573,
            3170,
            235265
        ],
        "total_duration": 3334919417,
        "load_duration": 1820461375,
        "prompt_eval_count": 29,
        "prompt_eval_duration": 849681750,
        "eval_count": 20,
        "eval_duration": 661980583
    }
   ```
