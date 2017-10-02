from Crawler import Crawler

if __name__ == "__main__":
    import os
    driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib/chromedriver.exe')
    save_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'tmp')
    Crawler(driver_path, save_path).crawl()


