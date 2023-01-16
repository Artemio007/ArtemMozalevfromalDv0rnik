### Задание 2 (I)
Написать функцию, которая возвращает среднее геометрическое для чисел `a` и `b` (не использовать модуль math). Выполните обработку исключений при помощи `try-except`.

### Задание 3 (I)
Пусть есть 3 функции которые вызываются в следующей последовательности
bzz -> bar -> foo. В функции `foo()` возникают исключения `ZeroDivisionError` и `IndexError`. Перехватите исключение `ZeroDivisionError` в функции `bar`, а `IndexError` в функции `bzz`

```python
def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)

def bar(a):
    foo(a)

def bzz(a):
    bar(a)
```

### Задание 4(II)
Создайте консольную программу для доказательства гипотезы Гольдбаха. Программа принимает число для ввода и вывода результата. При вводе ‘q’ программа должна завершится.
```python
Input: 4
Output: 2 2

Input: 6
Output: 3 3
```