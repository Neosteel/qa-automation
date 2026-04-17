import pytest 
from pages.login_page import LoginPage
from pages.new_customer_page import NewCustomerPage
from playwright.sync_api import expect
import re
from datetime import datetime

def test_add_new_customer(browser_page):
    try:
        login_page = LoginPage(browser_page)
        login_page.login("mngr658217", "ezaqupY")
        browser_page.wait_for_load_state("networkidle")
        expect(browser_page).to_have_url("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        browser_page.goto("https://demo.guru99.com/V4/manager/addcustomerpage.php")
         
        ''' creating random email id '''
        unique_email = f"neo{datetime.now().strftime('%Y%m%d%H%M%S')}@gmail.com"
        
        new_customer_page = NewCustomerPage(browser_page)
        new_customer_page.add_customer(
        customer_name="neo",
        gender="m",
        Date_of_birth="2026-04-09",
        address="11559 oaklawn usa",
        city="jacksonville",
        state="Florida",
        pin="322196",
        mobile_number="9046551272",
        email = unique_email,
        password="Test@1234"
        )
        browser_page.wait_for_timeout(2000)
        browser_page.screenshot(path="debug.png")
        expect(browser_page).to_have_url(re.compile("insrtCustomer|CustomerRegMsg"), timeout=10000)
    except Exception as e:
        print(f"Test failed: {e}")
        raise
'''parameterized  data driven testing ''' 
@pytest.mark.parametrize("invalid_name, expected_message", [
    ("1234", "Numbers are not allowed"),
    ("name@#$", "Special characters are not allowed"),
    ("   ", "First character can not have space")
])


def test_invalid_customer_name(browser_page,invalid_name, expected_message):
    try: 
        login_page = LoginPage(browser_page)
        login_page.login("mngr658217", "ezaqupY")
        browser_page.wait_for_load_state("networkidle")
        expect(browser_page).to_have_url("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        browser_page.goto("https://demo.guru99.com/V4/manager/addcustomerpage.php")
        
        '''enter invalid data in customer name field : numbers '''
        new_customer_page = NewCustomerPage(browser_page) 
        new_customer_page.enter_customer_name(invalid_name)
        browser_page.locator('[name="name"]').press("Tab")
      
        expect(browser_page.locator('#message')).to_have_text(expected_message)

    except Exception as e:
        print(f"Test failed : {e}")
        raise
