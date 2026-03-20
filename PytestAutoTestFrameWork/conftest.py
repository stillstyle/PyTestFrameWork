import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from selenium import webdriver
from py._xmlgen import html

_driver = None

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when in ('call', 'setup') and (report.failed or report.skipped):
        screen_img = _driver.get_screenshot_as_base64()
        html_img = f'<div><img src="data:image/png;base64,{screen_img}" style="width:600px"/></div>'
        extra.append(pytest_html.extras.html(html_img))
    report.extra = extra
    report.description = str(item.function.__doc__)

@pytest.fixture(scope='module')
def driver():
    global _driver
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()