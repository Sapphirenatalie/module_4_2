# Пространство имен
# Ваша задача:
# Создайте новую функцию def test_function
# Создайте другую функцию внутри функции inner_function,
# функция должна печатать значение "Я в области видимости функции test_function"
# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function
# и посмотрите на результат выполнения программы


d = 1


def test_function():
    d = 10

    def inner_function():
        d = 'local'
        print("Я в области видимости функции test_function")

    inner_function()


test_function()
