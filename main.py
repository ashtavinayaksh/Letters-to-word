from itertools import permutations 

def Assembly(letters):
     # We put each character from the input string into a list.
     letterList = []
     for char in letters:
          letterList.append(char)


     
     # Get all permutations of length of "lenght" if the lenght of the word is only one character it wont count it
     y = 0
     tupleList = []
     while y < len(letterList):
          lenght = len(letterList) - y
          
          if lenght <= 1:
               break
          
          perm = permutations(letterList, lenght) 
          
          # we put all the obtained permutations in a list
          for i in list(perm): 
               tupleList.append(i)

          y += 1
     
     # Makes strings from the tuples and puts them in a list
     n = 0
     resultsList = []
     while n < len(tupleList):
          string = "".join(tupleList[n])
          resultsList.append(string)
          n += 1

     return resultsList

     

myInput = input("Input letters: ")
results = Assembly(myInput)



# We need to import and read the dictionary file and compare the strings

with open("dict.txt", "r") as file:
     dictList = []
     for line in file:
          line = line.rstrip()
          dictList.append(line)
     

print(list(set(results) & set(dictList)))

# idea: select only line containing letters