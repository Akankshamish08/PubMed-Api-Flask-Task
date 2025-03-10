import argparse
from fetch_papers import fetch_papers, save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results (CSV)")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode") 

    args = parser.parse_args()
    papers = fetch_papers(args.query)

    if args.file:
        save_to_csv(papers, args.file)
        if args.debug:
            print(f"[DEBUG] Results saved to {args.file}")
    if args.debug:
        print("[DEBUG] Fetching papers for query:", args.query)
    else:
        print(papers)

if __name__ == "__main__":
    main()
