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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ROCKETMILES_HOME = 'https://www.rocketmiles.com'
location_to_select = 'Peoria, IL, USA'


@given('a web browser is at the rocketmiles home page')
def step_impl(context):
    context.browser.get(ROCKETMILES_HOME)
    time.sleep(20)
    

@given('the location is blank')
def step_impl(context):
    location_dropdown = context.browser.find_element(By.NAME, 'locationSearch')
    location_dropdown.clear()
    selected_location = location_dropdown.text
    assert(selected_location == '')


@when('a search is initiated')
def step_impl(context):
    context.browser.find_element(By.TAG_NAME, 'Button')


@then('the missing location error is shown')
def step_impl(context):
    pass

@given('the reward program is blank')
def step_impl(context):
    rewards_dropdown = context.browser.find_element(By.NAME, 'programAutosuggest')
    rewards_dropdown.clear()
    selected_program = rewards_dropdown.text
    assert(selected_program == '')


@given('the location is not blank')
def step_impl(context):
    search_input = context.browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)
    pass

@then('the missing reward program error is shown')
def step_impl(context):
    pass

@When('blank')
def step_impl(context):
    raise NotImplementedError('STEP: blank')    
    pass

