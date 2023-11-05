def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        print(f"Функція {func.__name__} була викликана {wrapper.call_count} раз(ів)")
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def decorator_answer():
    print("Виконую функцію")

decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
decorator_answer()
