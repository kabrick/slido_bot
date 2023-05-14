from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager


class SlidoBot:
    def __init__(self):
        # initialize the chrome tab in incognito mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.minimize_window()
        self.failure_rate = 0
        self.is_join_button_clicked = False
        self.is_choice_selected = False
        self.is_submit_button_clicked = False

    def closeBrowser(self):
        self.driver.close()

    def vote(self):
        # add the url for the vote
        self.driver.get("https://app.sli.do/event/w96GLZqWXD5Z2Tro5hRtMv/live/polls")

        # sleep while the page loads fully
        time.sleep(7)

        while self.is_join_button_clicked is False:
            self.click_join_button()

        while self.is_choice_selected is False:
            self.select_choice()

        while self.is_submit_button_clicked is False:
            self.click_submit_button()

    def click_join_button(self):
        try:
            click_elem = self.driver.find_element(By.XPATH, "//*[@data-test-id='join-in-button']")
            click_elem.click()
            self.failure_rate = 0
            self.is_join_button_clicked = True
        except:
            self.failure_rate = self.failure_rate + 1

            if self.failure_rate > 5:
                raise Exception("Failure rate is above 5 for click_join_button")
            else:
                time.sleep(5)

    def select_choice(self):
        try:
            click_elem = self.driver.find_element(By.XPATH, "//span[text()='Streamline Health']")
            click_elem.click()
            time.sleep(2)
            self.failure_rate = 0
            self.is_choice_selected = True
        except:
            self.failure_rate = self.failure_rate + 1

            if self.failure_rate > 5:
                raise Exception("Failure rate is above 5 for click_choice")
            else:
                time.sleep(5)

    def click_submit_button(self):
        try:
            btn_elem = self.driver.find_element(By.XPATH, "//*[@id='poll-submit-button']")
            btn_elem.click()
            time.sleep(5)
            self.failure_rate = 0
            self.is_submit_button_clicked = True
        except:
            self.failure_rate = self.failure_rate + 1

            if self.failure_rate > 5:
                raise Exception("Failure rate is above 5 for click_submit_button")
            else:
                time.sleep(5)


def main():
    votes = 2000

    for i in range(1, votes + 1):
        try:
            slid_bot = SlidoBot()
            slid_bot.vote()
            slid_bot.closeBrowser()
            print("Votes: " + str(i))
        except:
            print("Failed at: " + str(i))

if __name__ == "__main__":
    print("Voting...")
    main()
