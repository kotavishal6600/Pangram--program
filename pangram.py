def ispangram(str):
    alphabet=("abcdefghijklmnopqrstuvwxyz")
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
string=input("please enter the sentence")
if(ispangram(string)==True):
    print("the input is a pangram")
else:
    print("the given input is not a pangram")
