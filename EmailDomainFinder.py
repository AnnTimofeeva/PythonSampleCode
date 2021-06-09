# Email domain name finder - version 1.
# ------------------------------------

# Write a function: parseEmail(emailAddress) which takes a single parameter, 'emailAddress'.
# The parameter should be an email address in the form: username@domain.ext
# Separate the address into two components and print each of these separately
#    1. The username
#    2. The domain and extension
   
# (Hint: See if you can find the index of the 'at' symbol)

# What test inputs can you give to your function to make sure it is 
# working as expected?

def parseEmail(emailAddress):
    index = emailAddress.find("@")
    if (index<0):
        print("Wrong email format")
        return False
    else: 
        
        print("The user name is: "+emailAddress[0:index])
        print("The domain and extension is "+ emailAddress[index+1:])
        return True



def parseEmailversion2(emailAddress):
    index = emailAddress.find("@")
    if (index<0):
        print("Wrong email format")
        return False
    else: 
        EmailAddressAfterAt= emailAddress[index+1:]
        index2 =  EmailAddressAfterAt.find(".") 
        print(index2) 
        print("The user name is: "+emailAddress[0:index])
        print("The domain is "+ EmailAddressAfterAt[0:index2])
        print("The extension is "+ EmailAddressAfterAt[index2+1:])
        return True



parseEmailversion2("anna@tim123.gmail")    


# Email domain name finder - version 2.
# ------------------------------------

# Update the parseEmail() function to also separate out the extension segment
# of the domain.

# What additional tests, if any would you add to test this version of the function.