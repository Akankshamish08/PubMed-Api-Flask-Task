# PubMed Research Paper Fetcher 

This project provides a Flask-based API and a CLI tool to fetch research papers from PubMed using a given search query. Users can retrieve results in JSON format or save them as a CSV file.
The project is authored by Akanksha Mishra with help of LLM tools like chatgpt and Deepseek.

## Features
- Fetch research papers from PubMed using a query.
- Save results as a CSV file.
- Command-line interface (CLI) support.
- Flask API for easy access to research papers.
- Debug mode for additional logging.

---

## Prerequisites
Make sure you have the following installed:
- Python 3.12 or later
- Virtual environment tool (recommended: `venv` or `Poetry`)

---

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/pubmed-api.git
cd pubmed-api
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
Or, if using Poetry:
```bash
poetry install
```

---

## Running the Application

### 1. Running the Flask API
To start the Flask API server, use the following command:
```bash
python app.py --debug
```
The API will run on `http://127.0.0.1:5000/`.

#### API Endpoints
| Method | Endpoint | Description |
|--------|------------|-------------|
| GET | `/fetch?query=<search_term>` | Fetch research papers based on a query |

Example:
```bash
curl "http://127.0.0.1:5000/fetch?query=machine+learning"
```
Response:
```json
[
  { "title": "Paper 1", "authors": "Author A", "year": 2023 },
  { "title": "Paper 2", "authors": "Author B", "year": 2024 }
]
```

---

### 2. Using the CLI Tool
The CLI tool allows fetching research papers and saving them to a CSV file.

#### Usage:
```bash
python fetch_cli.py "machine learning" -f results.csv --debug
```
#### Arguments:
| Argument | Description |
|----------|-------------|
| `query` | (Required) Search query for PubMed |
| `-f, --file` | (Optional) Save results to a CSV file |
| `-d, --debug` | (Optional) Enable debug mode |

#### Example:
```bash
python fetch_cli.py "deep learning" -f papers.csv --debug
```
Output:
```
[DEBUG] Fetching papers for query: deep learning
[DEBUG] Fetched papers: [{'title': 'Paper 1'}, {'title': 'Paper 2'}]
[DEBUG] Results saved to papers.csv
```

---

## Troubleshooting
### 1. `ModuleNotFoundError: No module named 'flask'`
Ensure Flask is installed:
```bash
pip install flask
```
If using Poetry:
```bash
poetry add flask
```

### 2. `poetry: command not found`
Ensure Poetry is installed:
```bash
pip install poetry
```
Then, install dependencies:
```bash
poetry install
```

### 3. API Not Working (404 Error)
- Make sure the server is running (`python app.py --debug`).
- Check that you are using the correct endpoint (`/fetch?query=<term>`).

---

## Contributing
Feel free to fork the repository and create a pull request with improvements!

---

## License
This project is licensed under the MIT License.

