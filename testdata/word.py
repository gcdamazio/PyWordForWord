import os


class WordForWord:

    def __init__(self):
        pass



    #Methods

    #1. func print(filename) - Reads the contents of a file, line by line, and creates a String object, making sure all the newline are preserved

    def printFile(filename):
        file = open(filename, "r") # Opens the file in read mode.
        content = ""
        for line in file:
            content = content + line
        print(content)
    printFile('/Users/gdamazio/Desktop/Projects/PyWordForWord/testdata/testdata1.txt')
 #2. fun wc(String input)- Count the number of characters in a file, number of words, number of lines.
 # Returns an tuple with the number os lines, words and characters.
    def wordCount(countFile):
        num_words = 0
        num_charc = 0
        num_lines = 0
        with open(countFile, 'r') as f: #open the file and call f (f is the name of the variable)
            for line in f:
                line = line.strip(os.linesep) #separating a line from \n(new line) character and storing again in line
                wordslist = line.split() #splitting the line
                num_lines = num_lines +1 # incrementing value of num_lines
                num_words = num_words + len(wordslist) #incrementing value of a num_word. Ex. Bill is handsome
                num_charc = num_charc + sum(1 for c in line if c not in (os.linesep, ' '))  # incrementint the value of num_charc. if os.linesep is not a space
        print("Number of words in text file: ",num_words)
        print("Number of lines in text file: ",num_lines)
        print("Number of characters in text file: ", num_charc)
        my_tuple = (num_lines, num_words, num_charc)
        return my_tuple     
    wordCount('/Users/gdamazio/Desktop/Projects/PyWordForWord/testdata/testdata4.txt')

    #def countNumber(String input):
        #pass
 #3. func wordFrequency(String inut) word count.words in the string, prduce a dic.with (str word, int numOfTimes)
    


 # 4. func letterFrequency(String input) letter frequency, write a program that collects the frequency of each letter within the input. produces a dictionary with letters as the key, number of occurences as value.

   