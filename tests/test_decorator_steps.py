import allure
from selene import browser, by, be


def test_decorator_steps():
    open_main_page()
    search_for_repository('IkonnikovQA/homework_9')
    go_to_repository('IkonnikovQA/homework_9')
    open_issues_tab()
    should_see_with_number('#1')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')
@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo)
    browser.element('#query-builder-test').submit()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()

@allure.step('Открываем таб issues')
def open_issues_tab():
    browser.element('#issues-tab').click()

@allure.step('Проверяем наличие ишью с номером {number}')
def should_see_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)