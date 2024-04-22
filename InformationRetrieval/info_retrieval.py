import re
import matplotlib.pyplot as plt
import numpy as np

words_number = 0
with open('novel.txt', 'r', encoding='utf-8') as file:
    sample_text = file.read().lower()

# creating a list where every word is separated , excluding numbers
words_and_numbers = re.findall(r'\w+', sample_text)
words = [word for word in words_and_numbers if not re.match(r'\d', word)]

# count every word's number
for word in words:
    words_number += 1

# create a dictionary to store every word's frequency
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# sorting the (key : value) -> (word : word_freq) pair of the dictionary created before
sorted_words = {key: value for key, value in
                sorted(word_freq.items(), key=lambda data: data[1], reverse=True)}

# calculating the value of constant (const) ,
# using the most common word (the) ,
# where const equals the rank of word times its frequency

most_freq_word = max(word_freq, key=word_freq.get)
print(f"The most frequent word is : {most_freq_word}")
freq_of_most_freq_word = word_freq[most_freq_word]
print(f"Frequency of the most frequent word is : {freq_of_most_freq_word}")

const = freq_of_most_freq_word * 1
print(f"const = {round(const)}")

print("---------------------------------------")

top_50_words = list(sorted_words.keys())[:51]
top_50_freqs = list(sorted_words.values())[:50]
top_50_pairs = dict(zip(top_50_words, top_50_freqs))

top_50_words.remove("s")

log_words = np.log(np.arange(1, 51))
log_freqs = np.log(top_50_freqs)

# create a Bar Plot for the top 50 words

plt.figure(figsize=(12, 6))
plt.bar(top_50_words , top_50_freqs)
plt.title("Bar plot diagram for the top 50 words")
plt.xlabel("freq")
plt.ylabel("term")
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()

# create a log-log diagram for the top 50 words
plt.figure(figsize=(12,6))
plt.loglog(top_50_words , top_50_freqs)
plt.xscale("log")
plt.yscale("log")
plt.title("Log - log diagram for term vs freq graph for top 50 words")
plt.xlabel("term")
plt.ylabel("freq")
plt.tight_layout()
plt.show()

# another one

plt.figure(figsize=(12, 6))
plt.loglog(log_words, log_freqs, marker='o', linestyle='-')
plt.title("Log - log diagram for the top 50 words")
plt.xlabel("freq")
plt.ylabel("term")
plt.grid(True)
plt.show()
