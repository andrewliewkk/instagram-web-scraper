# Prerequisite: selenium python package and chromedriver version for your google chrome
import time
from selenium import webdriver

query = "kf1kart"
print("Querying hashtag: " + query)

# Open google chrome & navigate to url, options changed to prevent adapter failed error
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver.exe')
driver.get("https://www.instagram.com/explore/tags/" + query + "/")


#scroll to bottom of page to load all html elements, add all posts in posts array
SCROLL_PAUSE_TIME = 3
posts = []
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        links = driver.find_elements_by_tag_name('a')
        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post and post not in posts:
                posts.append(post)
        break
    last_height = new_height
    links = driver.find_elements_by_tag_name('a')
    for link in links:
        post = link.get_attribute('href')
        if '/p/' in post and post not in posts:
            posts.append(post)
print(len(posts))
#foreach post, get comments and store into comments array
comments = []
for post in posts:
    spans = []
    driver.get(post)
    elements = driver.find_elements_by_tag_name('span')
    for element in elements:
        the_class = element.get_attribute('class')
        if the_class == "":
            spans.append(element)
    comments.append(spans[2].get_attribute('innerText'))

print(len(comments))
for comment in comments:
    print(comment)
    print("---")