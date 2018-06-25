str = "hello"
print(str)
str_with_quotes = 'Hello World'
print(str_with_quotes)
str_with_double_quote = """Hello World"""
print(str_with_double_quote)
# capitalize : Hello
print("capitalize :", str.capitalize())
# casefold : hello
print("casefold :", str.casefold())
# Checking if isalnum:  True
print("Checking if isalnum: ", str.isalnum())
# Checking if isalpha:  False
print("Checking if isalpha: ", str_with_quotes.isalpha())
# Checking if isidentifier:  False
print("Checking if isidentifier: ", str_with_quotes.isidentifier())
