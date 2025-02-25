from src.data_collection.fetch_pubmed_data import fetch_pubmed_articles

def test_fetch_pubmed_articles():
    query = "diabetes"
    articles = fetch_pubmed_articles(query, max_results=10)
    
    assert len(articles) > 0, "No articles fetched"
    assert "title" in articles[0], "Missing 'title' field in results"
