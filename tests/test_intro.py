from playwright.sync_api import expect


def test_login_bank_url(browser_page):
    browser_page.locator('[name="uid"]').fill("mngr658217")
    browser_page.locator('[name="password"]').fill("ezaqupY")
    browser_page.locator('[name="btnLogin"]').click()
    expect(browser_page).to_have_url("https://demo.guru99.com/V4/manager/Managerhomepage.php")


def test_login_fail(browser_page):
    '''login test fail'''
    dialog_message = []
    browser_page.on("dialog", lambda dialog: (dialog_message.append(dialog.message), dialog.dismiss()))
    browser_page.locator('[name="uid"]').fill("mngr658217")
    browser_page.locator('[name="password"]').fill("abcb")
    browser_page.locator('[name="btnLogin"]').click()
    browser_page.wait_for_timeout(2000)
    assert dialog_message[0] == "User or Password is not valid"


def test_empty_userid_password(browser_page):
    '''empty fields test'''
    dialog_message = []
    browser_page.on("dialog", lambda dialog: (dialog_message.append(dialog.message), dialog.dismiss()))
    browser_page.locator('[name="uid"]').fill("")
    browser_page.locator('[name="password"]').fill("")
    browser_page.locator('[name="btnLogin"]').click()
    browser_page.wait_for_timeout(2000)
    assert dialog_message[0] == "User or Password is not valid"