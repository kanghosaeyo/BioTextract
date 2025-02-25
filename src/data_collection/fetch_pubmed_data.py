from pymed import PubMed
from src.data_collection.config import PUBMED_API_EMAIL, TOOL_NAME
from src.data_collection.utils import save_to_csv


def fetch_pubmed_articles(query, max_results=100):
    """
    Fetch articles from PubMed based on a query.
    
    Parameters:
        query (str): Search query for PubMed.
        max_results (int): Maximum number of results to fetch.
    
    Returns:
        list: List of article metadata dictionaries.
    """
    pubmed = PubMed(tool=TOOL_NAME, email=PUBMED_API_EMAIL)
    results = pubmed.query(query, max_results=max_results)
    
    articles = []
    for article in results:
        article_dict = article.toDict()
        articles.append({
            "title": article_dict.get("title"),
            "abstract": article_dict.get("abstract"),
            "authors": ", ".join([author.get("lastname", "") for author in article_dict.get("authors", [])]),
            "pub_date": article_dict.get("publication_date"),
            "doi": article_dict.get("doi")
        })
    
    return articles

if __name__ == "__main__":
    # Example usage
    query = "cancer AND treatment"
    max_results = 50
    articles = fetch_pubmed_articles(query, max_results)

    # Save results to CSV
    save_to_csv(articles, filename="pubmed_cancer_treatment.csv")
