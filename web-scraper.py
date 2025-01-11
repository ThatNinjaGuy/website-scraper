from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool
import urllib.parse
import json

# Set up the Web Scraper Agent
web_scraper = Agent(
    role="Web Scraper",
    goal="Scrape the entire real estate website efficiently",
    backstory="You are an expert web scraper capable of extracting data from complex websites.",
    tools=[ScrapeWebsiteTool()],
    verbose=True,
)

# Set up the Data Analyzer Agent
data_analyzer = Agent(
    role="Data Analyzer",
    goal="Extract and organize specific real estate information",
    backstory="You are skilled at parsing and organizing data from raw HTML content.",
    verbose=True,
)


def scrape_real_estate(website_url):
    scraping_task = Task(
        description=f"Scrape the real estate website at {website_url} and return the raw HTML content for the various properties listed on the page.",
        agent=web_scraper,
        expected_output="Raw HTML content of the property listings on the website",
    )

    analysis_task = Task(
        description=f"""
        Extract the following information for each property listing:
        - Name: Look for the most prominent heading or title within each listing
        - Price: Search for elements containing currency symbols or price-related keywords
        - Location: Find elements with location-related information, often near the property name
        - Features: Find elements with property feature related keywords like carpet area, status, floor, built up area, etc. Provide only the information that is available in the HTML.
        
        Use structural patterns and common real estate terminology to identify relevant information.
        Analyze the overall layout and recurring patterns in the HTML to locate property listings.
        Ensure that the output is a list of dictionaries, each containing the name, price, location, and features of a property.
        """,
        agent=data_analyzer,
        expected_output="List of dictionaries with property name, price, location, and features",
    )

    real_estate_crew = Crew(
        agents=[web_scraper, data_analyzer],
        tasks=[scraping_task, analysis_task],
        verbose=True,
    )

    result = real_estate_crew.kickoff()

    # Convert the result to text format using the __str__ method of CrewOutput
    result_data = str(result)

    # Extract hostname from the URL and replace dots with dashes
    hostname = urllib.parse.urlparse(website_url).hostname.replace(".", "-")

    # Save the result to a file named after the modified hostname with .md extension
    with open(f"{hostname}.md", "w") as file:
        file.write(result_data)

    return result_data


# Example usage
result = scrape_real_estate(
    website_url="https://www.magicbricks.com/property-for-sale-in-kolkata-pppfs"
)
print(result)
