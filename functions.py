import random

# read words from text file(words.txt) and return them as a list
def read_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = [word.strip() for word in file.readlines()]
    return words

# write a list of words to a text file (one word per line)
def write_words_to_file(file_path, words):
    with open(file_path, 'w', encoding='utf-8') as file:
        for word in words:
            file.write(word + '\n')

# build a markov chain from a list of words
# state size is the number of words used to predict the next word
def build_markov_chain(words, stateSize=1):
    markov_chain = {}
    for i in range(len(words) - stateSize):
        prefix = tuple(words[i:i + stateSize])
        suffix = words[i + stateSize]
        if prefix not in markov_chain:
            markov_chain[prefix] = []
        markov_chain[prefix].append(suffix)
    return markov_chain

# if there is a "!collect_messages" command in words.txt, this function will remove that command in words.txt to avoid trouble
def words_cleanup(words_path):
    words = read_words_from_file(words_path)

    updated_words = []
    for word in words:
        if '!collect_messages' not in word:
            updated_words.append(word)

    write_words_to_file(words_path, updated_words)

# generate random weird text using markov chain
def generate_text(markov_chain, stateSize, length=45):
    current_prefix = random.choice(list(markov_chain.keys()))
    generated_words = list(current_prefix)

    for _ in range(length):
        next_word = random.choice(markov_chain.get(current_prefix, []))
        generated_words.append(next_word)
        current_prefix = tuple(generated_words[-stateSize:])

    return ' '.join(generated_words)