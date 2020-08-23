import time
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request

# Helper function to scroll to the bottom of the page
def scroll(driver, timeout):
    scroll_pause_time = timeout
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


# Page containing all episode links
url = "https://www.bitchute.com/channel/pr4xis5eizure/"

driver = webdriver.Chrome("D:\PATH helper\chromedriver.exe")
driver.get(url)

scroll(driver, 1)
# Once scroll returns bs4 parsers the page_source
mainSoup = BeautifulSoup(driver.page_source, features="html.parser")

episodeLinks = []
episodeNames = []

for link in mainSoup.find_all("a"):
    if "PENN & TELLER" in str(link.string):
        episodeNames.append(link.string)
        episodeLinks.append(link.get("href"))

# Remove duplicates
episodeLinks = set(episodeLinks)
episodeNames = list(set(episodeNames))

# Base video url
videoUrl = "https://www.bitchute.com/"

# Go through all links and download the videos
for link in episodeLinks:
    # Navigate to video page
    driver.get(videoUrl + link)
    videoSoup = BeautifulSoup(driver.page_source, features="html.parser")

    # Find source for video
    video = videoSoup.find("source", type="video/mp4")

    # Title has to be parsed this way to create valid file names
    title = videoSoup.find("h1", {"class": "page-title"}).string
    fileName = title.replace(":", "").replace(".", "").replace(" ", "") + ".mp4"

    try:
        print("Starting download for {}...".format(title))
        urllib.request.urlretrieve(video.get("src"), fileName)
        print("Episode downloaded!")
    except Exception as e:
        print(e)
