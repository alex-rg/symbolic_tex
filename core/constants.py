from abc import ABC, abstractmethod
import platform

runprog_code = [
"""
import traceback
try:
    exec('''
from framework import *
res = {'error' : 'False'}
""", 
"""
import json
with open('data.json', 'w') as fp: 
	json.dump(res, fp)''')
except:
    import json
    res = {'error' : 'True'}
    res['descr'] = traceback.format_exc()
    with open('data.json', 'w') as fp: 
        json.dump(res, fp)
"""
]

tex_comms = ["\\long\\def\\code#1{}", "\\long\\def\\codep#1{}"]

def interpreter():
    if platform.system() == 'Windows':
        return "python"
    else:
        ".venv/bin/python"
    