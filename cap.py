# Write a program that capitalizes the first letter of each word in a given sentence

def capitalize_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    # Capitalize the first letter of each word and join them back into a sentence
    capitalized_sentence = ' '.join(word.capitalize() for word in words)
    return capitalized_sentence
sentence = "hello world, this is a test sentence."
capitalized_sentence = capitalize_words(sentence)
print(capitalized_sentence)