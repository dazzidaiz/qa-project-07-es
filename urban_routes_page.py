import data
from selenium.webdriver.common.by import By
from Helpers import retrieve_phone_code

class UrbanRoutesPage:

    # Step 1: Enter Addresses
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Step 2: Select the comfort rate
    ask_for_taxi = (By.XPATH, "//button[@class ='button round']")
    comfort_button = (By.XPATH, "//div[text()='Comfort'][1]")
    comfort_selected = (By.XPATH, "//div[@class = 'tcard active']")

    # Step 3: Add phone Number
    phone_number = (By.XPATH, "//div[text()='Número de teléfono'][1]")
    number_field = (By.ID, 'phone')
    next_field = (By.XPATH, "(//button[@type='submit'])[1]")
    id_code = (By.ID, 'code')
    confirm_button = (By.XPATH, "(//button[@type='submit'])[2]")

    # Step 4 Add a card
    pay_method = (By.XPATH, "//div[@class='pp-text']")
    add_card = (By.XPATH, "//div[@class='pp-plus-container']")
    add_number = (By.ID, 'number')
    add_code = (By.XPATH, "(//input[@id='code'])[2]")
    other_place_tab = (By.CSS_SELECTOR, "div[class='card-wrapper']")
    confirm_card_button = (By.XPATH, "//button[text()='Agregar']")
    close_button = (By.XPATH, "(//button[@class='close-button section-close'])[3]")

    # Step 5: Messsage driver
    message_driver = (By.ID, 'comment')

    # Step 6: Ask for Blanket and tissues
    blankets_tissues = (By.XPATH, "(//span[@class='slider round'])[1]")

    # Step 7: Order two ice creams
    ice_cream_order = (By.XPATH, "(//div[@class='counter-plus'])[1]")

    # Step 8: Looking for a taxi
    search_taxi = (By.CSS_SELECTOR, "span[class='smart-button-main']")

    # Step 9 Optional Wait and Click button Details
    details_button = (By.XPATH, ".//img[@src='/static/media/burger.7f0605c2.svg']")

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.driver.get(data.urban_routes_url)
        self.set_from(address_from)
        self.get_from()
        self.set_to(address_to)
        self.get_to()

    def click_ask_for_taxi(self):
        self.driver.find_element(*self.ask_for_taxi).click()

    # Step 2: Select the comfort rate
    def click_comfort_button(self):
        self.driver.find_element(*self.comfort_button).click()

    # Step 3: Add Telephone Number
    def click_phone_number(self):
        self.driver.find_element(*self.phone_number).click()

    def fill_number_field(self):
        self.driver.find_element(*self.number_field).send_keys(data.phone_number)

    def click_next_field(self):
        self.driver.find_element(*self.next_field).click()

    def verification_code(self):
        self.driver.find_element(*self.id_code).send_keys(retrieve_phone_code(self.driver))

    def click_confirm_button(self):
        self.driver.find_element(*self.confirm_button).click()

    # Step 4 Add a card
    def click_pay_method(self):
        self.driver.find_element(*self.pay_method).click()

    def click_add_card(self):
        self.driver.find_element(*self.add_card).click()

    def fill_add_number(self):
        self.driver.find_element(*self.add_number).send_keys(data.card_number)

    def fill_add_code(self):
        self.driver.find_element(*self.add_code).send_keys(data.card_code)

    def click_other_place_tab(self):
        self.driver.find_element(*self.other_place_tab).click()

    def click_confirm_card_button(self):
        self.driver.find_element(*self.confirm_card_button).click()

    def click_close_button(self):
        self.driver.find_element(*self.close_button).click()

    # Step 5: Send messsage to driver
    def set_message_driver(self):
        self.driver.find_element(*self.message_driver).send_keys(data.message_for_driver)

    # Step 6: Ask for Blanket and tissues
    def ask_blankets_tissues(self):
        self.driver.find_element(*self.blankets_tissues).click()

    # Step 7: Order two ice creams
    def click_ice_cream_order(self):
        self.driver.find_element(*self.ice_cream_order).click()

    # Step 8: Looking for a taxi
    def click_search_taxi(self):
        self.driver.find_element(*self.search_taxi).click()

    # Step 9: Optional click button details
    def click_details_button(self):
        self.driver.find_element(*self.details_button).click()




