import os


class WordForWord:
    frequency = {} 


    #Methods

    #1. func print(filename) - Reads the contents of a file, line by line, and creates a String object, making sure all the newline are preserved

    def printFile(self, filename):
        file = open(filename, "r") #The line file = open(filename, "r") tells the computer to open a file (a document stored in the computer) whose name we pass as filename. The "r" part means we’re only going to read it, not change it.
        content = "" #we make an empty string called content. Then we go through each line in the file with a for loop. This loop lets us take one line at a time from the file and add it to content.
        for line in file:
            content = content + line #adds each line from the file to the content variable. This means every line gets attached to the end of the previous one, so in the end, content holds all the text in the file.
        print(content) #hows everything we read from the file on the screen, so we can see what’s in it!

 #2. fun wc(String input)- Count the number of characters in a file, number of words, number of lines.
 # Returns an tuple with the number os lines, words and characters.
    def wordCount(self, countFile):
        num_words = 0
        num_charc = 0
        num_lines = 0
        with open(countFile, 'r') as f: # tells the computer to open the file we want to count. We call this file f so it’s easier to work with. The 'r' means we’re reading, not changing anything.
            for line in f: #use a for loop to go line-by-line through the file.
                line = line.strip(os.linesep) #removes any "new line" symbols (\n) from each line. These symbols just mean "move to the next line," so we don’t count them as words or letters.
                wordslist = line.split() #breaks up each line into words and puts them in a list. Then we add the number of words in that line to num_words
                num_lines = num_lines +1 # incrementing value of num_lines
                num_words = num_words + len(wordslist) #incrementing value of a num_word. Ex. Bill is handsome
                num_charc = num_charc + sum(1 for c in line if c not in (os.linesep, ' '))  # incrementing the value of num_charc. if os.linesep is not a space | goes through each letter in the line and counts it if it’s not a space or a new line. This way, we’re only counting real letters, numbers, and symbols.
        print("Number of words in text file: ",num_words)
        print("Number of lines in text file: ",num_lines)
        print("Number of characters in text file: ", num_charc)
        my_tuple = (num_lines, num_words, num_charc)
        return my_tuple     


 #3. func wordFrequency(String input) word count.words in the string, produce a dic.with (str word, int numOfTimes)

    def wordFrequency(self, filename):
            frequency = {}  # Initialize an empty dictionary to hold word frequencies
            with open(filename, 'r') as f:
                for line in f:
                    words = line.split()  # Split the line into words
                    for word in words:
                        word = word.lower()  # Make the word lowercase to avoid case sensitivity
                        if word in frequency:
                            frequency[word] += 1  # If the word is already in the dictionary, increment its count
                        else:
                            frequency[word] = 1  # If it's a new word, add it to the dictionary with a count of 1
            print("Word Frequency:", frequency)
            return frequency

    

 # 4. func letterFrequency(String input) letter frequency, write a program that collects the frequency of each letter within the input. produces a dictionary with letters as the key, number of occurences as value.

wordforword = WordForWord()
wordforword.printFile('/Users/gdamazio/Desktop/Projects/PyWordForWord/testdata/testdata1.txt')
wordforword.wordCount('/Users/gdamazio/Desktop/Projects/PyWordForWord/testdata/testdata4.txt')
wordforword.wordFrequency('/Users/gdamazio/Desktop/Projects/PyWordForWord/testdata/testdata4.txt')