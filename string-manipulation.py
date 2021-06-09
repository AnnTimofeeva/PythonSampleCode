# PascalCaseString = "PascalCaseString"
# camelCaseString = "camelCaseString"

# Pascal_To_Camel_String = PascalCaseString[0].lower()+PascalCaseString[1:]
# Camel_To_Pascal_String = camelCaseString[0].upper()+camelCaseString[1:]

# print("Pascal to camel string: "+Pascal_To_Camel_String)
# print("Camel to Pascal string: "+Camel_To_Pascal_String)


# ibanDecoder
#     A Irish IBAN consists of 22 alpha-numeric characters:
#      - 2 letter country code
#      - 2 digit checksum number
#      - 4 characters from the bank's SWIFT/BIC or bank identification number
#      - 6 digit code for the bank branch
#      - 8 digit code for the bank account number
     
#     Write some code that takes a 22 character IBAN number and extracts 
#     the 5 pieces of information from IBAN (country, checksum, BIC, branch, a/c num)

def camel2Pascal(camelText):

    pascalText = camelText[0].upper()+camelText[1:]
    return pascalText

def testcamel2Pascal(test_number, inputText):
    print(f"{test_number}. Camel case = {inputText}")
    print(f"{test_number}. Pascal case = {camel2Pascal(inputText)}")

testcamel2Pascal(1, "OneTwoThree")
testcamel2Pascal(2, "1TwoThree")




# IBANString = "IE12345678901234567890"

# country = IBANString[0:2]
# checksum = IBANString[2:4]
# BIC = IBANString[4:8]
# Branch = IBANString[8:14]
# AccountNumber = IBANString[14:]

# print("Country: "+country+" checksum: "+checksum+ " BIC: "+BIC+ " branch: "+Branch+ " Account number "+AccountNumber)