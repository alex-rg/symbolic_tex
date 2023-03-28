import re
from behave import *
import os
from subprocess import Popen, PIPE

in_file = ".venv/bin/python"
arg1 = "parse.py"
arg2 = "--test_mode"

@given('подготовили тестовый файл "{file}"')
def step_impl(context, file):
    context.file = 'tests/input/' + file
    tmp = re.findall(r'\d+', file)
    file = open('tests/output/out_' + str(tmp[0]) + '.tex',mode='r')
    context.out_file = file.read()

@when('запускаем приложение')
def step_impl(context):
    p = Popen([in_file, arg1, context.file, arg2], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    file = open('test.tex',mode='r')
    context.output = file.read()
    os.remove("test.tex")

@then('сравниваем результаты')
def step_impl(context):

    assert context.output == context.out_file
