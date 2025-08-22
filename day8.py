s = input("Enter a sentence: ")
words = s.strip().split()
words.reverse()

result = " ".join(words)

print("Reversed string:", result)