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

from behave import * 
from selenium.webdriver.common.keys import Keys

ROCKETMILES_HOME = 'https://www.rocketmiles.com'

@given('a web browser is at the rocketmiles home page')
def step_impl(context):
    context.browser.get(ROCKETMILES_HOME)

@given('the location is blank')
def step_impl(context):
    raise NotImplementedError('STEP: the location is blank')    
    pass

@given('the location is not blank')
def step_impl(context):
    raise NotImplementedError('STEP: the location is not blank')    
    pass

@given('the reward program is blank')
def step_impl(context):
    raise NotImplementedError('STEP: the reward program is blank')    
    pass

@When('a search is initiated')
def step_impl(context):
    raise NotImplementedError('STEP: When a search is intitiated')    
    pass

@then('the missing location error is shown')
def step_impl(context):
    raise NotImplementedError('STEP: the missing location error is shown')    
    pass

@then('the missing reward program error is shown')
def step_impl(context):
    raise NotImplementedError('STEP: the missing reward program error is shown')    
    pass

@When('blank')
def step_impl(context):
    raise NotImplementedError('STEP: blank')    
    pass

