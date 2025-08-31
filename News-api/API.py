import configparser
import logging
import requests
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_data(api_key):
    """Fetches news data from the NewsAPI."""
    url = f'https://newsapi.org/v2/everything?q=technology&apiKey={api_key}'
    logging.info("Fetching news from NewsAPI...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Successfully fetched the news.")
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch news: {e}")
        return None

def transform_and_save_locally(data, local_filename="technology_news.csv"):
    """Transforms data and saves it as a CSV locally."""
    articles = data.get('articles', [])
    if not articles:
        logging.warning("No articles found in the response.")
        return False, None
    
    df = pd.DataFrame(articles)
    relevant_df = df[['source', 'author', 'title', 'publishedAt']]
    
    try:
        relevant_df.to_csv(local_filename, index=False)
        logging.info(f"News data saved locally to {local_filename}")
        return True, local_filename
    except IOError as e:
        logging.error(f"Failed to save file locally: {e}")
        return False, None

def upload_to_s3(local_filename, bucket_name, s3_filename):
    """Uploads a file to an S3 bucket."""
    s3 = boto3.client('s3')
    try:
        logging.info(f"Uploading {local_filename} to S3 bucket {bucket_name}...")
        s3.upload_file(local_filename, bucket_name, s3_filename)
        logging.info("Upload Successful.")
    except FileNotFoundError:
        logging.error(f"The file {local_filename} was not found.")
    except NoCredentialsError:
        logging.error("Credentials not available. Please configure AWS CLI.")
    except Exception as e:
        logging.error(f"An error occurred during S3 upload: {e}")

def main():
    """Main function to run the ETL pipeline."""
    logging.info("ETL pipeline started.")
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    api_key = config['newsapi']['api_key']
    s3_bucket = config['aws']['s3_bucket_name']
    
    raw_data = fetch_data(api_key)
    
    if raw_data:
        success, file_path = transform_and_save_locally(raw_data)
        if success:
            upload_to_s3(file_path, s3_bucket, file_path)
            
    logging.info("ETL pipeline finished.")

if __name__ == "__main__":
    main()