from flask import Flask, request, jsonify
from fetch_papers import fetch_papers, save_to_csv

app = Flask(__name__)

# ✅ Home route for API
@app.route('/')
def home():
    return "Welcome to the PubMed API! Use /fetch?query=your_query to search."

# ✅ API Endpoint
@app.route('/fetch', methods=['GET'])
def fetch():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    papers = fetch_papers(query)
    return jsonify(papers)

# ✅ Run Flask only when the script is executed directly
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run Flask API for PubMed.")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    app.run(debug=args.debug)
