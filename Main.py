import data
import pytest
import time
from urban_routes_page import UrbanRoutesPage
from selenium import webdriver

class TestUrbanRoutes:

    driver = None
    initial_header = None
    final_header = None


    @classmethod
    def setup_class(cls):

        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()# desired_capabilities=capabilities
        cls.driver.implicitly_wait(20)


    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    # Step 2: Select the comfort rate
    @pytest.mark.sleep(10)
    def test_select_comfort(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ask_for_taxi()
        routes_page.click_comfort_button()
        assert self.driver.find_element(*routes_page.comfort_selected).get_property('class') != "tcard active"

    # Step 3: Add Telephone Number
    def test_add_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_number()
        routes_page.fill_number_field()
        routes_page.click_next_field()
        routes_page.verification_code()
        routes_page.click_confirm_button()
        assert self.driver.find_element(*routes_page.number_field).get_property('value') == data.phone_number

    # Step 4 Add a card
    def test_add_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_pay_method()
        routes_page.click_add_card()
        routes_page.fill_add_number()
        routes_page.fill_add_code()
        routes_page.click_other_place_tab()
        routes_page.click_confirm_card_button()
        routes_page.click_close_button()
        assert self.driver.find_element(*routes_page.add_code).get_property('value') == data.card_code

    # Step 5: Send messsage to driver
    def test_send_message_driver(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_message_driver()
        assert self.driver.find_element(*routes_page.message_driver).get_property('value') == data.message_for_driver

    # Step 6: Ask for Blanket and tissues
    def test_click_Blanket_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.ask_blankets_tissues()

    # Step 7: Order two ice creams
    def test_click_ice_cream_order(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ice_cream_order()
        routes_page.click_ice_cream_order()

    # Step 8: Looking for a taxi
    def test_click_search_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_search_taxi()

    # Step 9: Optional waiting time and click button details
    def test_wait_click_details_button(self):
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(30)
        routes_page.click_details_button()

        time.sleep(100)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

