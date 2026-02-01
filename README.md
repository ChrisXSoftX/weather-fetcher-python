# 🌦️ Weather Fetcher Python

A robust, production-ready Python script for fetching and structuring weather data. This project demonstrates API integration, professional logging, and data persistence.

## 🚀 Features
- **API Integration:** Fetches real-time data from Open-Meteo API.
- **Data Structuring:** Converts raw JSON into a simplified, storage-friendly format.
- **Error Handling:** Includes specific exceptions for timeouts and HTTP errors.
- **Logging:** Generates an audit trail (`scraper.log`) for monitoring and debugging.
- **Polite Scraping:** Uses custom headers and time delays to respect API limits.

## 🛠️ Tech Stack
- **Language:** Python 3.10+
- **Libraries:** `requests`, `json`, `logging`, `time`

## 📦 Installation & Usage
1. Clone the repo:
   ```bash
   git clone [https://github.com/Solotech/weather-fetcher-python.git](https://github.com/Solotech//weather-fetcher-python.git)
2. Run the script:
Bash
python weather-fetcher.py
3. Check data.json for results and scraper.log for execution details.
