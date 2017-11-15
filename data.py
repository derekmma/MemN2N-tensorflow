import os
from collections import Counter

def read_data(fname, count, word2idx):
    # read file content if there is a file at the path
    if os.path.isfile(fname):
        with open(fname) as f:
            lines = f.readlines()
    else:
        raise("[!] Data %s not found" % fname)

    # save all words in the file to array `words`
    # this is somehow the words' dictionary
    words = []
    for line in lines:
        words.extend(line.split())

    if len(count) == 0:
        count.append(['<eos>', 0])

    count[0][1] += len(lines)
    # get unqiue words among all words
    count.extend(Counter(words).most_common())

    # save all words as id in the word2idx dict
    # 'end of sentence' represent by '<eos>' 
    if len(word2idx) == 0:
        word2idx['<eos>'] = 0

    for word, _ in count:
        if word not in word2idx:
            word2idx[word] = len(word2idx)

    # represent all sentences as vector of words' id
    data = list()
    for line in lines:
        for word in line.split():
            index = word2idx[word]
            data.append(index)
        data.append(word2idx['<eos>'])

    print("Read %s words from %s" % (len(data), fname))
    return data
