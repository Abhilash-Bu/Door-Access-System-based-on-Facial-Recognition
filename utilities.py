from selenium import webdriver
import random
from twilio.rest import Client

def otp_generator(admin_number): # OTP GENERATOR


    OTP = random.randint(1000, 9999)  # GENERATED OTP BETWEEN THESE NUMBERS
    client = Client("ACac894ed035a5a30f5341cf148efee445", "7dc2a905cec0947ed09b8b6140748e6a")
    client.messages.create(to=[admin_number], from_="+13236133608", body=OTP)

    return OTP

def whatsApp_user_details(name,emp_id,admin='Admin'): # VERIFICATION DETAILS REQUEST FROM USER

    driver = webdriver.Chrome("chromedriver")
    driver.get("https://web.whatsapp.com/")

    if (input("Enter y after scanning whatsapp web\n") == 'y'):
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(admin))
        user.click()
        textbox = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
        textbox.send_keys("Name : {}\nEmployee ID : {}\nPlease process my request of adding new facial biometric"
                          .format(name,emp_id))
        button = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button")
        button.click()

if __name__ == '__main__':
    pass