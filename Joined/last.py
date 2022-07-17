from html2image import Html2Image
import time

hti = Html2Image()
while True:
    hti.screenshot(url="https://www.google.com/maps/@9.9950524,76.2921638,21z/data=!5m1!1e1", save_as="google.jpg")
    time.sleep(20)
