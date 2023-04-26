# symbolic_tex
## [Документация к коду](https://korolev-am.github.io/symbolic_tex_docs/index.html)

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

Требования к анализатору -- поддержка следующих математических объектов:
* рациональные и иррациональные числа;
* символы переменные;
* выражения;
* матрицы:
  + числовые;
  + символьные;
  + символьные символьного размера (например, матрицы размера n);
  + блочные;
* функции (конкретные, например, sin(x) и абстрактные, например, f(t), полиномы);
* уравнения и системы уравнений:
  + линейные и дифференциальные;

Требования к объектам:
* Числа:
    * проведение арифметических операций;
    * форматированный вывод (например, дробей -- \\code{a=Frac(1,5)}\\codep{a.value(high=False)}).
* Символы:
    * возможность добавления акцентов (черта, волна, звездочка и т.п.). Пример: \\code{a = Symb('x')}\\codep{a.accent('tilde')}. -> \\tilde{x}.
* Выражения:
    * форматированный вывод с возможностью контроля порядка элементов в выражении, частичном вычислении и т.п. Пример:
      \\code{a=1,b=2,c=3}\codep{a+b+c}=\\codep{(a+b).value + c} = \\codep{(a+b+c).value} -> a + b + c = 3 + c = 6.\
* Матрицы:
    * арифметические операции; пример: \\code{A=Matrix(name='A', value=[[1,2,3],[4,5,6]])}\\codep{2*A}=\\codep{(2*A).value}.
    * обращение (возможно, кроме символьных с символьным размером).
    * форматированный вывод:
        + для числовых матриц:
            * форматирование вывода дробей
            * различные виды скобок
        + для символьных символьного размера:
            * контроль количества выводимых элементов;
* Функции:
    * элементарные функции;
    * замена аргумента; например, \code{a = Func('f', arg='x')}\codep{f} -> f(x)  \codep{f(Symb('a') + Symb('b'))} -> f(a+b).
    * дифференцирование;
    * интегрирование.
* Уравнения:
    * преобразования уравнений (замена переменных и т.п.).
    * вычисление решений, где возможно;
    * форматированный вывод (поэлементно, с обозначением матриц и т.п.).
    
Так же необходимо реализовать "Генератор": функция Generate(cnt : int, code : str, ...), которая будет генерировать code cnt раз.
  + Добавить возможность обращения к уже существующей ячейке с кодом вместо копирования кода в переменную.
  + Добавить возможность передачи кода для каждой итерации генератора, например как массив строк (те, чтобы у каждой итерации был разный код).
  + Добавить возможность изменения кода в зависимости от номера итерации.
  
