# Word search (Advanced):
# ----------------------

# 1. Given a string 'theText' (could be a large, multiline string)
#     -> Option 1 (easier) - you can define this in code
#     -> Option 2 (more difficult) - you can read this from a text file
    
# 2. Given a second string that contains a particular word, 'searchTerm'
#     -> Option 1 - you can hard-code this 
#     -> Option 2 - you can ask the user to enter a word 

# 3. Search through theText and count all instances of searchTerm
# (Hint - look at the string.split() method which returns a list of strings
#       - look at the for item in list: looping mechanism for examples of 
#         how to iterate through a list of strings

def WordSearch(theText, WordToSearch):
    #theText = "Please, enter a string to search words dog cat mouse horse another cat and another horse and mouse again"
    #WordToSearch = input("Please enter a word to search in the text above: ")

    TextList = theText.split()
    wordcount=0

    for i in TextList:
        if (WordToSearch==i):
            wordcount+=1

    print(f" The word {WordToSearch} is found {wordcount} times in the Text")

#WordSearch("Please, enter a string to search words dog cat mouse horse another cat and another horse and mouse again","123")


def WordSearchFromFile(fileName, WordToSearch):
    
        f = open("demofile.txt", "r")
        wordcount=0
        Text=""
        for x in f:
           Text=Text+x 
        f.close()

        TextList = Text.split()
        for i in TextList:
            if (WordToSearch==i):
                wordcount+=1

        print(f" The word {WordToSearch} is found {wordcount} times in the Text")
    
WordSearchFromFile("demofile.txt","horse")
        