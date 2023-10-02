# try: something that might cause an exception
# except: do this if there was an exception, exception here basically means error
# else: do this if there were no exception
# finally: do this no matter what happens

# with open("a_file.text") as file:
#     file.read()
# if i run above codes, i will get error, because the a_file.text doesnt exist.this is a FileNotFound error.

try:
    # try to open below file, if it doesnt work out, then go to except.
    file = open("a_file.txt")
except:
    # with this open and "w", if this a_file doesnt exist, then it will create this file. and allow you write something inside it.
    file = open("a_file.txt", "w")
    file.write("somthing")
# if not specify the exception, like FileNotFoundError, TypeError, you will see the curly line under "except" indicating that "too broad exception clause, then what would happen:
# if it is a bare exception, it will ignore all the other exceptions. for example:
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["sfdfdgfhf"])
# except:
#     file = open("a_file.txt", "w")
#     file.write("somthing")
# with above code, because the a_file already exists, the print statement should generate another exception, as the key doesnt exist in a_dictionary.
# however, via running this code, we got nothing. thats because in our except only one exception mentioned which is the existence of a_file.
# as it is already there, so the except clause didnt get trigered.thats why we need to specify the error after except.
# to get it right
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sfdfdgfhf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("somthing")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    # if the thing that trying in "try" all get successful. in this case, if this a_file doesnt exist, this else statement will be skipped.
    content = file.read()
    print(content)
finally:
    # no matter what happens before, this fianlly will be trigered.
    file.close()
    print("File was closed")

    raise TypeError("THis is an error  that i made up")

height = float(input("height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("human height should not be over 3 meters")

bmi = weight/height ** 2
