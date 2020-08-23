# Bullshit-Downloader
> I came across a website that contains all of the episodes for the TV show *[Penn & Teller: Bullshit.](https://www.imdb.com/title/tt0346369/)* I decided that instead of downloading each episode one by one I would write a Python script to do it for me. Using [Selenium](https://selenium-python.readthedocs.io/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [urllib](https://docs.python.org/3/library/urllib.html), this is the solution I came up with. 


## Clone
- Clone repo to your local machine using `https://github.com/BryanBorge/bullshit-downloader.git`

## Installation and Setup
- Repo contains all code required to get started, you just need to install the libraries. 

> Install BeautifulSoup 
````shell
pip install BeautifulSoup4
````

> Install Selenium 
````shell
pip install selenium
````

> Install urllib with python3
````shell
pip install urllib3
````

> Configure Chrome webdriver
- Find which version of chrome you are running and download the correct [driver](https://chromedriver.chromium.org/downloads)
- Add the Chrome webdriver to the PATH and use
  ```python
  driver = webdriver.Chrome() 
  ````
  or point to its location and use 
    ```python
  driver = webdriver.Chrome("C:\Path to chromedriver.exe")
   ````

## Usage
- Once the above steps are complete, run the script using VS code or similar. 
- A Chrome window should pop up and begin to scroll on the site followed by downloading each video file. 

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © Bryan Borgesano.
