from urllib.request import urlopen
import time


def get_load_time(url):
    

    if ("https" or "http") in url:  # Checking for a protocol
        open_this_url = urlopen(url)  # Opens the url
    else:
        open_this_url = urlopen("https://" + url)  
    start_time = time.time()  # Time stamp before the reading of url starts
    open_this_url.read()  # Reading the url you entered
    end_time = time.time()  # Time stamp after the reading of the url
    open_this_url.close()  
    time_to_load = end_time - start_time

    return time_to_load


if __name__ == '__main__':
    url = input("Enter a URL here to test its loading time: ")
    print(f"\nThe time taken to load {url} is {get_load_time(url):.2} seconds.")