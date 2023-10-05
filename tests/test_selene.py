from selene import browser, by, be


def test_selene():
    browser.open('https://github.com/')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('IkonnikovQA/homework_9')
    browser.element('#query-builder-test').submit()

    browser.element(by.link_text('IkonnikovQA/homework_9')).click()

    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#1')).should(be.visible)