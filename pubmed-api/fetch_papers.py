import requests
import pandas as pd

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_papers(query, max_results=10):
    """Fetch research papers from PubMed based on a query."""
    
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    
    response = requests.get(PUBMED_API_URL, params=params)
    
    if response.status_code != 200:
        print("Error fetching PubMed data.")
        return []
    
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    
    if not paper_ids:
        print("No papers found for the given query.")
        return []

    # Fetch paper details
    details_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    details_response = requests.get(PUBMED_FETCH_URL, params=details_params)

    if details_response.status_code != 200:
        print("Error fetching paper details.")
        return []

    papers = details_response.json().get("result", {})

    results = []
    for paper_id in paper_ids:
        paper = papers.get(paper_id, {})
        results.append({
            "PubmedID": paper_id,
            "Title": paper.get("title", "N/A"),
            "Publication Date": paper.get("pubdate", "N/A"),
            "Authors": ", ".join([author["name"] for author in paper.get("authors", []) if "name" in author]),
            "Affiliation": paper.get("source", "N/A")
        })

    return results

def save_to_csv(papers, filename="output.csv"):
    """Save fetched papers to a CSV file."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

