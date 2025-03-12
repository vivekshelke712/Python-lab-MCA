# Write a Python function That Accepts a Sentence as Input and Removes All Duplicate Words.  

def removeDuplicateWords(sentence):
    words = sentence.split()
    uniqueWords = set(words)
    return " ".join(uniqueWords)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Sentence after removing duplicate words:", removeDuplicateWords(sentence))
