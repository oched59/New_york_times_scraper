from ny_news_extract import *
import time


print("Extracting article hyperlinks...")




# Gets all the latest URL's from the NY Times Technology Section
content_string = get_content_string(my_url)
starts, ends = find_occurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)



for url in url_list:
    print("Article URL: " + str(url))

    print("------------------------------------------------")
    time.sleep(7)  # Allows user to get through all the text.

# Closing Messages
print()
print("The articles have been successfully extracted!")
print("In total, we were able to extract " + str(len(url_list)) + " different articles!")
