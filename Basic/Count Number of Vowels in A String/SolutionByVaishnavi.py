#To count the vowels in a string
def CountVowels(str):

    count = 0
    vowels = ['A','E','I','O','U','a','e','i','o','u']
    for i in str:
        if i in vowels:
            count  += 1   
    print(count)
    
str = input('String= ')
CountVowels(str)
