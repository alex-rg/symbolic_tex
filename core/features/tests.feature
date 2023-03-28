Feature: Тесты для каждого класса

  Scenario: TexSymbol
      Given подготовили тестовый файл "in_1.tex"
      When запускаем приложение
      Then сравниваем результаты

  Scenario: TexNumber
      Given подготовили тестовый файл "in_2.tex"
      When запускаем приложение
      Then сравниваем результаты

  Scenario: TexFraction
      Given подготовили тестовый файл "in_3.tex"
      When запускаем приложение
      Then сравниваем результаты

  Scenario: TexMatrix
      Given подготовили тестовый файл "in_4.tex"
      When запускаем приложение
      Then сравниваем результаты