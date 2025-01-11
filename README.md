# Real Estate Web Scraper Using CrewAI

## Introduction

This application is a specialized web scraper designed to extract real estate data from property listing websites using CrewAI. It employs a multi-agent system that coordinates between web scraping and data analysis tasks to efficiently collect and organize property information.

## Features

- Automated web scraping of real estate listings
- Intelligent data extraction of property details including:
  - Property names
  - Prices
  - Locations
  - Property features
- Automatic file output generation based on website hostname
- Multi-agent coordination using CrewAI

## Components

The application uses two specialized agents:

1. **Web Scraper Agent**: Responsible for efficiently crawling the real estate website and extracting raw HTML content.

2. **Data Analyzer Agent**: Processes the raw HTML to extract structured property information.

## Tools & Dependencies

- **CrewAI**: Framework for creating and coordinating AI agents
- **CrewAI Tools**: Provides the ScrapeWebsiteTool for web scraping
- **urllib**: Handles URL parsing and manipulation
- **json**: Manages data serialization

## How It Works

1. The system initializes two specialized agents:
   - A Web Scraper agent equipped with web scraping tools
   - A Data Analyzer agent for parsing and organizing the extracted data

2. The process follows two main tasks:
   - First task scrapes the raw HTML content from the specified website
   - Second task analyzes the content to extract specific property information

3. The extracted data includes:
   - Property names
   - Price information
   - Location details
   - Available property features

4. Results are automatically saved to a markdown file named after the website's hostname

## Setup & Installation

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### 2. Installation Steps

1. Clone the repository:

```bash
git clone https://github.com/ThatNinjaGuy/website-scraper
cd website-scraper
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

This will install:

- langchain-community
- crewai and crewai[tools]
- requests
- beautifulsoup4
- python-dotenv
- langchain-experimental
- duckduckgo-search
- html2text

### 3. Environment Configuration

1. Create a `.env` file in the root directory:

```bash
touch .env
```

2. Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual OpenAI API key.

> ⚠️ **Security Note**: Never commit your `.env` file to version control. Make sure it's included in your `.gitignore`.

## Running the Scraper

1. Ensure all dependencies are installed and `.env` file is configured
2. Run the scraper:

```bash
python web-scraper.py
```

## Output

The scraper generates a markdown file containing the extracted information. The filename is automatically generated based on the website's hostname (e.g., `www-magicbricks-com.md`).

## Important Notes

- Ensure you have the required dependencies installed
- Verify that you have permission to scrape the target website
- Be mindful of the website's robots.txt file and scraping policies
- Consider implementing rate limiting for production use
- Keep your API keys secure and never share them publicly
- The scraper requires an active internet connection

## Troubleshooting

Common issues and solutions:

- If you get an API key error, verify your `.env` file is properly configured
- If dependencies fail to install, try upgrading pip: `pip install --upgrade pip`
- For SSL certificate errors, ensure your Python installation has proper SSL certificates

## License

[Your License Here]
