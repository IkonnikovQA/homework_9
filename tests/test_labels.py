import allure
from allure_commons.types import Severity
from selene import browser, by, be

@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Ikonnikov')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
def test_step():
    with allure.step('Открываем гит'):
        browser.open('https://github.com/')

    with allure.step('Заходим в профиль пользователя'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('IkonnikovQA/homework_9')
        browser.element('#query-builder-test').submit()

    with allure.step('Открываем репозиторий'):
        browser.element(by.link_text('IkonnikovQA/homework_9')).click()

    with allure.step('Находим issues'):
        browser.element('#issues-tab').click()
        browser.element(by.partial_text('#1')).should(be.visible)