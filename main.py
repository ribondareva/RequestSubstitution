import time

from selenium.webdriver.chrome.options import Options
from seleniumwire import undetected_chromedriver as uc

from config import settings


def interceptor(request):
    if request.url == settings.REPLACED_URL:
        print('Changed')
        request.create_response(
            status_code=200,
            headers={'Content-Type': 'text/html; charset=UTF-8'},
            body=settings.BODY,
        )


options = Options()
options.add_argument('--ignore-certificate-errors')
driver = uc.Chrome(version_main=126, options=options)
driver.request_interceptor = interceptor
driver.get(settings.URL)
time.sleep(500)
