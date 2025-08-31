# Automated News Aggregator ETL Pipeline

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![AWS](https://img.shields.io/badge/AWS%20S3-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-blueviolet.svg)

A simple, automated ETL (Extract, Transform, Load) pipeline that fetches technology news from a live API and stores it in AWS S3.

## 📋 Project Description
This project demonstrates a fundamental cloud data engineering workflow. The pipeline ingests raw data, performs basic transformations, and loads the result into a secure, scalable cloud storage service.

### Workflow
The script performs the following actions:
`[NewsAPI] ---> [Python Script (Pandas, Boto3)] ---> [technology_news.csv] ---> [AWS S3 Bucket]`

1.  **Extract:** Fetches the latest technology news from the [NewsAPI.org](https://newsapi.org/) service.
2.  **Transform:** Uses the Pandas library to structure the raw JSON data into a clean, tabular format.
3.  **Load:** Saves the data locally as a `.csv` file and then uploads that file to a private bucket in AWS S3.

## 🛠️ Tech Stack
* **Language:** Python
* **Cloud Provider:** Amazon Web Services (AWS)
* **Key Libraries & Services:**
  * **Pandas:** For data manipulation.
  * **Requests:** For making HTTP requests to the API.
  * **Boto3:** The AWS SDK for Python, used for interacting with S3.
  * **AWS S3:** For object storage in the cloud.

## ⚙️ Setup and Configuration

To run this project, you need to have your environment configured correctly.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ANUJ-GAUTAM26/news-aggregator-pipeline.git](https://github.com/ANUJ-GAUTAM26/news-aggregator-pipeline.git)
    cd news-aggregator-pipeline
    ```
2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure AWS Credentials:**
    Ensure you have the AWS CLI installed and have configured your credentials with an IAM user that has S3 access.
    ```bash
    aws configure
    ```
4.  **Create a `config.ini` file:**
    Create a file named `config.ini` and add your credentials. This keeps your secrets out of the main script.
    ```ini
    [newsapi]
    api_key = YOUR_SECRET_API_KEY

    [aws]
    s3_bucket_name = your-unique-s3-bucket-name
    ```
5.  **Create a `.gitignore` file:**
    It is crucial to create a `.gitignore` file and add `config.ini` to it. This prevents your secret keys from being accidentally uploaded to GitHub.

## ▶️ How to Run
Execute the main script from the root directory of the project:
```bash
python news_pipeline.py
