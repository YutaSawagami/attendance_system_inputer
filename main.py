import datetime
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

USER_ID = os.getenv("USER_ID")
PASSWORD = os.getenv("PASSWORD")
URL = os.getenv("URL")


def auto_input_attendance_system():
    try:
        comfirm()
        options = Options()
        # 処理が終了してもブラウザを閉じない設定
        options.add_experimental_option('detach', True)

        # 実行時にブラウザを立ち上がらせたくなければ以下のコメントアウトを解除
        # options.add_argument('--headless')

        driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=options)
        driver.get(URL)
        user_id_field = driver.find_element_by_id("TextStaffNo")
        user_id_field.send_keys(USER_ID)
        password_field = driver.find_element_by_id("TextPassword")
        password_field.send_keys(PASSWORD)
        driver.find_element_by_id('BtnOk').click()

        driver.find_element_by_id('ImgBtnMenuMonth').click()
        today = datetime.date.today().strftime("%m/%d")
        driver.find_element_by_link_text(today).click()

        text_comment = driver.find_element_by_name('TextComment')
        text_comment.clear()
        text_comment.send_keys("在宅勤務")
        driver.find_element_by_name('BtnOkSigndayedit').click()
        driver.find_element_by_id('BtnOk').click()

        time.sleep(3)
        Alert(driver).accept()
        print("Successfully done.")
    except Exception as e:
        print(e)


def comfirm():
    print("Do you start program? Please input 'y' or 'n'.")
    user_input = input()
    if user_input == "y":
        return None
    elif user_input == "n":
        sys.exit()
    else:
        print("Invalid input.")
        comfirm()


if __name__ == "__main__":
    auto_input_attendance_system()
