from behave import given, when, then
from utils import Utils
import time
from nose.tools import assert_equal
from pages.header_page import HeaderPages
from pages.result_page import ResultsPage

utils = Utils()
header_page = HeaderPages()
result_page = ResultsPage()

@given(u'que acesso o site Python')
def step_impl(context):
    utils.nav("http://www.python.org")
    time.sleep(3)

@given(u'preencho o input de pesquisa')
def step_impl(context):
    header_page.preencher_input_busca('python')

@when(u'clico no botão de pesquisar')
def step_impl(context):
    header_page.click_bnt_go()

@then(u'devo visualizar os resultados da pesquisar')
def step_impl(context):
    assert_equal(result_page.get_text_title(),'Search Python.org')
    time.sleep(3)
    utils.drive.close()

