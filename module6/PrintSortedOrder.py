# Print  the Sorted Words. 

def printSortedOrder(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    print("Sentence after sorting words:", printSortedOrder(sentence))