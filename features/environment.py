# -- FILE: features/environment.py
# CONTAINS: Browser fixture setup and teardown
from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = webdriver.Firefox()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

@fixture
def browser_chrome(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    context.browser = webdriver.Chrome()
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()

def before_all(context):
    use_fixture(browser_chrome, context)
    # -- NOTE: CLEANUP-FIXTURE is called after after_all() hook.
