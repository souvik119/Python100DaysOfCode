#How to not make the program crash upon encountering errors
#example - FileNotFound error, KeyError, IndexError, TypeError....

#We can catch exceptions when something goes wrong, fail more gracefully
#try, except, else, finally

#Try - something that might cause an exception
#Except - do this if there was an exception
#Else - do this if there was no exceptions
#Finally - do this no matter what happens


# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["wrongkey"])
# except FileNotFoundError: #only use except is not good coding, this will not catch all errors, want specific exceptions
#     #print("There was an error")
#     #create the file if it does nto exist
#     file = open("a_file.txt", mode="w")
#     file.write("Something.....")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("This is a made up error") #raise your own exception


height = float(input("Height : "))
weight = float(input("Weight : "))

if height > 3:
    raise ValueError("Human height should not be greater than 3m")

