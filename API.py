import requests
import pandas as pd

# This function handles fetching and processing the data
def fetch_and_process_news(api_key):
    """Fetches news from NewsAPI, processes it, and saves it to a CSV."""
    
    url = f'https://newsapi.org/v2/everything?q=technology&apiKey={api_key}'
    
    print("Fetching news from NewsAPI...")
    response = requests.get(url)

    if response.status_code == 200:
        print("Successfully fetched the news!")
        data = response.json()
        articles = data.get('articles', [])

        if articles:
            df = pd.DataFrame(articles)
            df.to_csv('technology_news.csv', index=False)
            print("News data has been saved to technology_news.csv")
            
            print("\n--- Found Technology Articles ---")
            for index, row in df.head(5).iterrows():
                title = row.get('title', 'No Title')
                source_dict = row.get('source', {})
                source_name = source_dict.get('name', 'No Source')
                print(f"- {title} (Source: {source_name})")
        else:
            print("No articles found in the response.")
    else:
        print(f"\n--- FAILED TO FETCH NEWS ---")
        print(f"Status Code: {response.status_code}")
        print(f"Error Message: {response.text}")

# This is the main part of the script that runs everything
if __name__ == "__main__":
    # PASTE YOUR NEW, SECRET API KEY HERE
    API_KEY = '063f0f96bcdd40368d6fa0b45c7d5964'
    
    fetch_and_process_news(API_KEY)
    print("\nScript finished.")