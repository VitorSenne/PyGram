from page_objects import PageElement


def like(hashtag):

    for index in range(1, 3):
        PageElement.webdriver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);'
        )

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'fotos' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            liked = driver.find_element_by_css_selector('[aria-label=Curtir]')
            liked.click()
            driver.execute_script('window.scrollTo(0, 300);')
