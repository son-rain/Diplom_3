import random
import string

import pytest
import requests
from selenium import webdriver

from data import Urls


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    browser.maximize_window()

    yield browser

    browser.quit()


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@pytest.fixture(scope='module')
def generate_registration_data():
    email = f'{generate_random_string(10)}@yandex.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)

    data = {
        "email": email,
        "password": password,
        "name": name
    }
    return data


@pytest.fixture(scope='module')
def create_user_data(generate_registration_data):
    data = generate_registration_data
    response = requests.post(Urls.CREATE_USER_POST_URL, data)
    token = response.json()['accessToken']
    data.pop('name')
    yield data
    headers = {'Authorization': token}
    requests.delete(Urls.DELETE_USER_URL, headers=headers)



