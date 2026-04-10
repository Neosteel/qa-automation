from playwright.sync_api import sync_playwright, expect 




def test_login_bank_url():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.guru99.com/V4")
        page.locator('[name="uid"]').fill("mngr658217")
        page.locator('[name="password"]').fill("ezaqupY")
        page.locator('[name="btnLogin"]').click()
        expect(page).to_have_url("https://demo.guru99.com/V4/manager/Managerhomepage.php")


def test_login_fail():
    '''login test fail ''' 
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.guru99.com/V4")
        page.locator('[name="uid"]').fill("mngr658217")
        page.locator('[name="password"]').fill("abcb")
        ''' add alert listener '''
        dialog_message = []
        page.on("dialog", lambda dialog: (dialog_message.append(dialog.message), dialog.dismiss()))
        '''click login button '''
        page.locator('[name="btnLogin"]').click()
        page.wait_for_timeout(2000)
        assert dialog_message[0] == "User or Password is not valid"
