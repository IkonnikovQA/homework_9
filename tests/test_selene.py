from selene import browser, by, be


def test_selene():
    browser.open('https://github.com/')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('IkonnikovQA/allure-example')
    browser.element('#query-builder-test').submit()

    browser.element(by.link_text('eroshenkoam/allure-example')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#76')).should(be.visible)