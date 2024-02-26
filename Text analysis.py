def funcAnalyze(text):
    words=text.split()
    dictWords = {}
    for word in words:
        dictWords[word] = dictWords.get(word,0) + 1
    mostCommon = sorted(dictWords.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Most common words in the text:")
    for word, wordCount in mostCommon:
        print(f"{word}: {wordCount}")


print("Enter the name of the text file to analyze: ")
dir = input()
try:
    fileData = open(dir)
    fileText = fileData.read()
    fileData.close()
    funcAnalyze(fileText)

except FileNotFoundError:
    print("A file with that name does not exist")
