from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

id="이메일"
pw="비번"
comment_good="항상 재밌고 유익한 수업을 해주십니다!"
comment_fix="없습니다!"

driver = webdriver.Chrome('C:/Users/USER/Downloads/chromedriver_win32/chromedriver.exe')
driver.get("http://benedu.co.kr/")

id_blank=driver.find_element_by_id("loginID")
id_blank.click()
id_blank.send_keys(id)

pw_blank = driver.find_element_by_id("loginPW")
pw_blank.click()
pw_blank.send_keys(pw)
pw_blank.send_keys(Keys.RETURN)

time.sleep(10)
driver.get("http://benedu.co.kr/StudySurvey/Survey")
teachers = driver.find_elements_by_class_name("teacher")
for teacher in teachers:
    try:
        teacher.click()
        time.sleep(2)
        radios = driver.find_elements_by_xpath("//span[text() = '매우 그렇다']")
        for radio in radios:
            radio.click()

        sentences = driver.find_elements_by_class_name("form-control")
        good = True
        for sentence in sentences:
            sentence.click()
            if good:
                sentence.send_keys(comment_good)
                good=False
            else:
                sentence.send_keys(comment_fix)

        time.sleep(3)
        submit = driver.find_element_by_id("btn-submit")
        submit.click()

        ok = driver.find_element_by_xpath("//button[text() = '확인']")
        print(ok)
        ok.click()

        time.sleep(2)
    except:
        print("Failed")
