"""
examples

@when('the user searches for "{phrase}"')
def step_impl(context, phrase):
    search_input = context.browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)
 
@then('results are shown for "{phrase}"')
def step_impl(context, phrase):
    links_div = context.browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    search_input = context.browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase
"""

import time

from behave import *
from selenium.common.exceptions import (NoAlertPresentException,
                                        NoSuchElementException,
                                        TimeoutException)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as cond
from selenium.webdriver.support.ui import WebDriverWait

ROCKETMILES_HOME = "https://www.rocketmiles.com"
LOCATION_TO_SELECT = "Peoria, IL, USA"
OPENING_MODAL_CLOSE_XPATH = '//div[@id="new-sign-up-modal"]//button[@class="close"]'
SUBMIT_BUTTON = (
    '//button[@class="rm-btn-orange search-submit-btn"]/span[@class="ng-scope"]'
)


@given("a web browser is at the rocketmiles home page")
def step_impl(context):
    context.browser.get(ROCKETMILES_HOME)
    time.sleep(20)
    try:
        # Remove initial modal if present
        context.browser.find_element(By.XPATH, '//div[@id="new-sign-up-modal"]')
        context.browser.find_element(By.XPATH, OPENING_MODAL_CLOSE_XPATH).click()
    except NoSuchElementException:
        # This modal is only displayed on first startup so
        # we don't expect to see it for subsequent tests
        pass


@given("the location is blank")
def step_impl(context):
    location_dropdown = context.browser.find_element(By.NAME, "locationSearch")
    location_dropdown.clear()
    wait_for_it(context.browser, location_dropdown)
    selected_location = location_dropdown.text
    assert selected_location == ""


@when("a search is initiated")
def step_impl(context):
    submit_btn = context.browser.find_element(By.XPATH, SUBMIT_BUTTON)
    click_on_it(context.browser, submit_btn)
    time.sleep(4)


@then("the missing location error is shown")
def step_impl(context):
    location_error_modal = context.browser.find_element(
        By.XPATH, '//div[@class="popover-inner"]//div[@class="popover-content ng-binding"]'
    )
    wait_for_it(context.browser, location_error_modal)
    time.sleep(4)


@given("the reward program is blank")
def step_impl(context):
    rewards_dropdown = context.browser.find_element(By.NAME, "programAutosuggest")
    rewards_dropdown.clear()
    wait_for_it(context.browser, rewards_dropdown)
    selected_program = rewards_dropdown.text
    assert selected_program == ""


@given("the location is not blank")
def step_impl(context):
    location_dropdown = context.browser.find_element(By.NAME, "locationSearch")
    location_dropdown.click()
    time.sleep(4)
    location_dropdown.send_keys(LOCATION_TO_SELECT[:-4])
    time.sleep(4)
    location_dropdown.send_keys(Keys.ARROW_DOWN + Keys.RETURN)
    time.sleep(4)
    selected_location = location_dropdown.text
    print("selected_location is {}".format(selected_location))
    assert selected_location == LOCATION_TO_SELECT


@then("the missing reward program error is shown")
def step_impl(context):
    reward_error_modal = context.browser.find_element(
        By.XPATH, '//div[@class-="popover-title"]a//div[@class="popover-content"]'
    )
    wait_for_it(context.browser, reward_error_modal)



@When("blank")
def step_impl(context):
    raise NotImplementedError("STEP: blank")
    pass


def click_on_it(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.click()
    action.perform()


def wait_for_it(driver, element):
    try:
        WebDriverWait(driver, 10).until(cond.visibility_of(element))
    except (NoAlertPresentException, TimeoutException) as py_ex:
        print("Alert not present")
        print(py_ex)
        print(py_ex.args)

    return element
