# COVID-19-Data-Scraper
A Python-based web scraping project to extract and process real-time COVID-19 statistics from the Worldometers Coronavirus page. The project gathers key global and country-wise data, such as total cases, deaths, and recoveries, and organizes them into a structured format using a Pandas 
DataFrame.

Features:-Scrapes real-time COVID-19 data from Worldometers.

Extracts:-Total global cases, deaths, and recoveries.Country-wise statistics like total cases, deaths, recoveries, active cases, and more.Processes and organizes the data into a tabular format using Pandas.Parses HTML efficiently using BeautifulSoup and lxml.Ready for further analysis or visualization.

Technologies Used :-
Python: Core programming language.
BeautifulSoup: For parsing and navigating HTML.
Requests: For fetching webpage content.
Pandas: For tabular data processing and analysis.
lxml: For fast and efficient HTML parsing.

How It Works
Web Scraping:Fetches the Worldometers Coronavirus page using the requests library.Parses the HTML content with BeautifulSoup.
Data Extraction:Collects global statistics (total cases, deaths, recoveries).Scrapes the country-wise table of COVID-19 statistics.
Data Organization:Extracted table headers (e.g., "Country", "Total Cases", "Deaths", etc.) are used to create a Pandas DataFrame.Row-wise data is added to the DataFrame for easy access and analysis
