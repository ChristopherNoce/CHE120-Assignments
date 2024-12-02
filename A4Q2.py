#Christopher Noce
#21143999

filename = "CharlesDickens-OliverTwist.txt"

#Opens the file and read its content
with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()

words = text.split() #splits the entire text into separate words

cleaned_words = [] #make all non-alphabet characters removed and convert all to lowercase to prevent false numbers due to case sensitivity
for word in words:
    cleaned_word = ""
    for char in word: #for each character in each word...
        if char.isalpha():  #keep only alphabetical characters
            cleaned_word += char #adds only the alphabetical characters and forms a new word. Ex: Oliver, becomes oliver (free of comma and capitals)
    if cleaned_word:  # Add only non-empty words
        cleaned_words.append(cleaned_word.lower()) #adds the lowercase version of the alphabet only words to the list

word_counts = {} #dictionary to count word occurences
for word in cleaned_words: #for each word in the list of cleaned up words
    if word in word_counts: #if the word is already in the dictionary
        word_counts[word] += 1 #increase counter by 1 for repeated word
    else:
        word_counts[word] = 1 #adds new word to the dictionary with a counter of 1 (first appearance)

most_common_words = [] #list of most common words
for _ in range(5):  #find top 5 words
    max_word = None #initialize variable
    max_count = 0 #itialize variable
    for word in word_counts:
        if word_counts[word] > max_count: #updates if a word with a higher frequency is found
            max_count = word_counts[word]
            max_word = word
    if max_word:
        most_common_words.append((max_word, max_count)) #created a tuple with the word and the word count
        del word_counts[max_word]  #remove from dictionary after finding, to get to the next highest. Source: https://www.w3schools.com/python/gloss_python_remove_dictionary_items.asp

#Display the results
print(f"The 5 words with the highest frequency in file '{filename}' are:")
i = 1
for word, count in most_common_words:
    print(f"{i}: '{word}' appears {count} times.")
    i += 1
