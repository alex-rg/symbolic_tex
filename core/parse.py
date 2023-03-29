import sys
import os
import subprocess
import argparse
import re
import numpy as np
from framework import *
from constants import *

printable_cnt = 0


class PyCode:

    code_exec = "\\code"
    code_print = "\\codep"

    def __init__(self, beg, code_start, end, type_, text):

        self.offset = beg
        self.code_start = code_start - beg
        self.len = end - beg  # не включая '}'

        self.type = type_

        self.printable = type_ == self.code_print
        self.code = text[beg:end]
        self.code = self.code[self.code_start:]
        self.code_ori = text[beg:end + 1]
        self.section = self.code_ori
        self.code_ori = self.code_ori[self.code_start:self.len]

        if self.printable == 1:

            global printable_cnt
            tmp = list(filter(None, self.code.split("\n")))
            last_el = ""

            for line in tmp[::-1]:
                if line[0] != " " and line[0] != "\t" and line[0] != "\n":
                    last_el = line
                    break

            if len(last_el) == 0:
                self.code += "\nres[" + str(printable_cnt) + "] = ''"  
            else:
                self.code += "\nfrom framework import *\nres[" + str(printable_cnt) + "] = latex(" + last_el + ")" 
                
            printable_cnt += 1

    def get_code(self):
        return self.code

    def get_code_ori(self):
        return self.code_ori

    def get_section(self):
        return self.section

    def get_end_pos(self):
        return self.offset + self.len

    def get_type(self):
        return self.type

    def get_line_no(self, n, text, size):
        a = text[: size + self.offset].count("\n")
        return a + n


def balance(text):

    s = 1

    for i in range(len(text)):
        if text[i] == "{":
            s += 1
        elif text[i] == "}":
            s -= 1
        if s == 0:
            return i

    return -1


def delete_comms(text):

    while 1 == 1:

        tmp = text.find("#")
        if tmp != -1:
            next_line = text[tmp:].find("\n")
            if next_line != -1:
                text = text[:tmp] + text[tmp + next_line:]
            else:
                text = text[:tmp]
        else:
            break

    return text


def find_pycode(text):

    imp = text.find(PyCode.code_exec)
    if text[imp + len(PyCode.code_exec)] == "p":
        type_ = PyCode.code_print
    else:
        type_ = PyCode.code_exec
    beg = text[imp:].find("{") + imp
    end = balance(text[beg + 1:]) + beg + 1

    return PyCode(imp, beg + 1, end, type_, text)


def delete_coms_def(text):

    text = text.replace(tex_comms[0], "")
    text = text.replace(tex_comms[1], "")
    return text


def check_exec_result(res, text, all_code, size, file_name):

    if res['error'] == "True":  # => ошибка
        res = res['descr']

        if (
            res.split("\n")[-2] ==
            "TypeError: latex() missing 1 required positional argument: 'expr'"
        ):

            print("Error: using \\codep without any final expression")
            exit(1)

        r = res.split()
        code = all_code.split("\n")
        text_s = text.split("\n")

        offset = 4

        for i in range(len(r)):

            if r[i] == '"<string>",':

                line_n = int(r[i + 2].replace(",", "")) + offset - 1
                err_code = code[line_n - 1]
                n = 0

                for j in range(0, line_n - 1):
                    if err_code in code[j] and "latex" in code[j]:
                        continue
                    else:
                        n += code[j].count(err_code)

                n = code[: line_n - 1].count(err_code)
                t = text.replace(err_code, "#" * len(err_code), n)
                pos = t.find(err_code)
                line_n = t[:pos].count("\n") + 1
                r[i + 2] = str(line_n) + ","
                r[i] = file_name + ","

        trb = ""
        sp = ""
        j = 0

        for i in res:

            if i != " " and i != "\n" and sp != "":
                if j < len(r):
                    trb += r[j] + sp
                else:
                    trb += sp
                sp = ""
                j += 1
            elif i == " " or i == "\n":
                sp += i

        if j == len(r) - 1:
            trb += r[-1]

        trb = trb.replace(
            '  File "run_prog.py", line ' +
            str(offset) +
            ", in <module>\n    exec('''\n",
            "",
        )
        print(trb)

        exit(1)
    else:
        del res['error']
        return 0


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Python to latex parser.")
    parser.add_argument(
        "file", metavar="LatexCode.tex", type=str,
        help="path to .tex file to be parsed"
    )
    parser.add_argument(
        "--keep_json",
        help="keeps data.json after running", action="store_true"
    )
    parser.add_argument(
        "--test_mode",
        help="renames output file to test.tex (will be deletep)", action="store_true"
    )
    args = parser.parse_args()

    tex_f = args.file

    with open(tex_f, encoding = 'utf-8') as f:
        text = f.read()

    text = delete_coms_def(text)
    text = delete_comms(text)

    cur_code = []
    size = 0
    output = []
    all_code = "print('{')"

    for i in range(text.count(PyCode.code_exec)):
        cur_code.append(find_pycode(text[size:]))
        all_code += "\n" + cur_code[i].get_code()
        size += cur_code[i].get_end_pos()

    all_code += "\nprint('}')"

    new_text = text

    with open("run_prog.py", "w") as f:
        all_code = runprog_code[0] + all_code + runprog_code[1]

        f.write(all_code)
        f.close()

    # ./.venv/bin/python - для отладки
    res = subprocess.check_output([interpreter(), "run_prog.py"], text=True)[:-1]
    
    import json
    with open('data.json', 'r') as fp:
        res = json.load(fp)

    check_exec_result(res, text, all_code, size, tex_f)  # обратока ошибок

    #d = json.loads(res.replace("\\", "\\\\"))
    d = res
    d = {int(k): v for k, v in d.items()}

    t = 0

    for i in range(len(cur_code)):

        if cur_code[i].get_type() == cur_code[i].code_print:

            new_text = new_text.replace(cur_code[i].get_section(), d[t], 1)
            t += 1

        else:

            new_text = new_text.replace(cur_code[i].get_section(), "", 1)

    if args.test_mode:
        new_name = "test.tex"
    else:
        new_name = tex_f.replace(".", "_new.")

    with open(new_name, encoding='utf-8', mode="w") as f:

        f.write(new_text)
        f.close()

    os.remove("run_prog.py")

    if not args.keep_json:
        os.remove("data.json")
    
