# symbolic_tex
Tex preprocessor with symbolic computations

Программа состоит из двух частей:
"парсер" (выделяет в tex-овском документе код на python/<you name it>, выполняет его, и результат выполнения подставляет в документ) и "анализатор" --- некоторый фреймворк для удобного использования систем компьтерной математики при наборе математических текстов.

Требования к парсеру:
1. Документ должен корректно собираться даже если парсер не отработал;
1. Корректная обработка ошибок: в сообщении об ошибке должно указываться место в исподном документе;
1. Возможность добавление как однострочного кода, так и многострочного; как с выводом, так и без него (\py{}, \pyc{});
1. Возможность использования в коде любых символов, допустимых для языка программирования;
1. (желательно) возможность добавлять код "inline", то есть так, чтобы до и/или после кода в строке следовал текст документа.
1. (желательно) для работы парсера не требуется подключать никаких дополнительных пакетов latex.
1. Незначительное время работы парсера (не более 2 x время сборки документа).
1. (Желательно) возможность перейти на другой язык программирования.