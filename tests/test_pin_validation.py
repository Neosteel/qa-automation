import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.new_customer_page import NewCustomerPage
from utils.excel_reader import read_excel_file


@pytest.mark.parametrize("invalid_pin, expected_message",
read_excel_file("test_data/pin_test_data.xlsx"))

def test_invalid_pin(browser_page, invalid_pin , expected_message):
    try: 
        login_page = LoginPage(browser_page)
        login_page.login("mngr658217", "ezaqupY")
        browser_page.wait_for_load_state("networkidle")
        browser_page.goto("https://demo.guru99.com/V4/manager/addcustomerpage.php")

        new_customer_page = NewCustomerPage(browser_page)
        new_customer_page.enter_pin_details(invalid_pin)

        expect(browser_page.locator('#message6')).to_have_text(expected_message)

    except Exception as e:
        print(f"Failed test : {e}")
        raise