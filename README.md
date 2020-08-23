# Bullshit-Downloader
> I came across a website that contains all of the episodes for the TV show *[Penn & Teller: Bullshit.](https://www.imdb.com/title/tt0346369/)* I decided that instead of downloading each episode one by one I would write a Python script to do it for me. Using selenium and BeautifulSoup, this is the solution I came up with. 


## Clone
- Clone repo to your local machine using `https://github.com/BryanBorge/bullshit-downloader.git`

## Installation and Setup
- Repo contains all code required to get started

> Install BeautifulSoup 
````shell
pip install BeautifulSoup4
````

> Install Selenium 
````shell
pip install selenium
````

> Install urllib python3
````shell
pip install urllib3
````

> Configure Chrome webdriver
- Find which version of chrome you are running and download the correct [driver](https://chromedriver.chromium.org/downloads)
- Add the Chrome webdriver to the PATH and use
  `driver = webdriver.Chrome()` 
  or point to its location and use 
  `driver = webdriver.Chrome("C:\Path to chromedriver.exe")`
