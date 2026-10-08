secret = input("Enter secret message: ")
coded = input("Enter coded message: ")

if secret in coded:
    print("Secret message found!")
else:
    print("Secret message not found!")