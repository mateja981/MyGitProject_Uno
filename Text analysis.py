def funcAnalyze(text):
    words=text.split()
    dictWords = {}
    wordsNum = len(words)
    avgLen = sum(len(word) for word in words)/wordsNum
    for word in words:
        dictWords[word] = dictWords.get(word,0) + 1
    mostCommon = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Most common words in the text:")
    for word, wordCount in mostCommon:
        print(f"{word}: {wordCount}")
    print("Average word lenght is: " + str(avgLen))
    print("Number of words is: " + str(wordsNum))

    #Added Com
    #Test for the new branch
    #Stats about words
    with open('Stats.txt', 'w') as f:
        for word,wordCount in mostCommon:
            percentage = wordCount * 100 / len(words)
            f.write(f"{word}:{percentage:.2f}%\n")
    
    f.close()

                    
        

print("Enter the name of the text file to analyze: ")
dir = input()
try:
    fileData = open(dir)
    fileText = fileData.read()
    fileData.close()
    funcAnalyze(fileText)

except FileNotFoundError:
    print("A file with that name does not exist")
