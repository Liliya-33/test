import time


def test_find_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button.is_displayed(), 'No find!'
    time.sleep(5)

