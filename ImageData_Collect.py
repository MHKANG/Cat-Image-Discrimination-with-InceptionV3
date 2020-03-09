from google_images_download import google_images_download
from selenium import webdriver

import ssl
ssl._create_default_https_context = ssl._create_unverified_context
driver = 'C:/ProgramData/Anaconda3/chromedriver.exe'
def imageCrawling(keyword, dir,driver):
    response = google_images_download.googleimagesdownload()

    arguments = {"keywords":keyword,
                 "limit":800,
                 "print_urls":True,
                 "no_directory":True,
                 "size":"medium",
                 "format":"jpg",
                 "chromedriver":driver,
                 "output_directory":dir}
    paths = response.download(arguments)
    print(paths)
"""
imageCrawling("페르시안고양이", './Persian', driver)
imageCrawling("먼치킨고양이", './Munchkin', driver)
imageCrawling("랙돌고양이", './Ragdoll', driver)
imageCrawling("아메리칸숏트헤어", './AmericanShortHair', driver)
imageCrawling("브리티쉬 쇼트헤어", './British', driver)
imageCrawling("시암고양이", './Siamese', driver)
imageCrawling("스코티시폴드", './ScottishFold', driver)
imageCrawling("russianblue", './RussianBlue', driver)
imageCrawling("britishshorthaircat", './british2', driver)
imageCrawling("Persiancat", './Persian2', driver)
imageCrawling("munchkincat", './Munchkin2', driver)
imageCrawling("Ragdollcat", './Ragdoll2', driver)
imageCrawling("Americanshorthaircat", './AmericanShortHair2', driver)
imageCrawling("RussianBluecat", './RussianBlue2', driver)
"""

imageCrawling("ScottishFoldCat", './ScottishFold2', driver)

