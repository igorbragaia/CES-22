def email_log(email):
    def email_log_decorator(func):
        def func_wrapper(name):
            try:
                return func(name)
            except Exception as e:
                return "Error {0}! an email was sent to {1}".format(e, email)
        return func_wrapper
    return email_log_decorator


@email_log("igorbragaia@gmail.com")
def no_errors_method(str):
    return str


@email_log("igorbragaia@gmail.com")
def errors_method(str):
    print(x)
    return str


print(no_errors_method("go!"))
print(errors_method("go!"))