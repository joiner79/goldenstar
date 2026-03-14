# 네이버 스토어 메뉴 클릭 자동화

from playwright.sync_api import sync_playwright

play = sync_playwright().start()
browser = play.chromium.launch(args=["--start-maximized"], headless= False, slow_mo= 1000)
page = browser.new_page(no_viewport = True)
page.goto("https://shopping.naver.com")
page.pause()
 

page.get_by_role("link", name="패션타운 NONE").click()
page.get_by_role("button", name="유아동 유아동").click()
page.pause()

browser.close()
play.stop()