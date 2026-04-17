class NewCustomerPage:

    def __init__(self, page):
        self.page = page
        self.customer_name = '[name="name"]'
        self.gender = '[name="rad1"][value="m"]'
        self.Date_of_birth = '[name="dob"]'
        self.address = '[name="addr"]'
        self.city  ='[name="city"]'
        self.state = '[name="state"]'
        self.pin = '[name="pinno"]'
        self.mobile_number = '[name="telephoneno"]'
        self.email = '[name="emailid"]'
        self.password = '[name="password"]'
        self.submit = '[name="sub"]'

    def add_customer(self, customer_name , gender,Date_of_birth, address, city,state, pin , mobile_number , email , password):
        self.page.locator(self.customer_name).fill(customer_name)
        self.page.locator(self.gender).click()
        self.page.locator(self.Date_of_birth).type("04/09/2026")
        self.page.locator(self.address).fill(address)
        self.page.locator(self.city).fill(city)
        self.page.locator(self.state).fill(state)
        self.page.locator(self.pin).fill(pin)
        self.page.locator(self.mobile_number).fill(mobile_number)
        self.page.locator(self.email).fill(email)
        self.page.locator(self.password).fill(password)
        self.page.locator(self.submit).click()


    def enter_customer_name(self, customer_name):
        self.page.locator(self.customer_name).fill(customer_name)

    def enter_pin_details(self, pin):
        self.page.locator(self.pin).fill(pin)
        self.page.locator(self.pin).press("Tab")


