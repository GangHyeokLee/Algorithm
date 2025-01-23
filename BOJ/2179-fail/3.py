n = int(input())

trie = dict()
words = [input() for _ in range(n)]


def make_trie(word, node, idx):
    if idx == len(word):
        if "end" in node:
            node["end"].append(word)
        else:
            node["end"] = [word]
        return
    if word[idx] not in node:
        node[word[idx]] = {}
    make_trie(word, node[word[idx]], idx + 1)


for word in words:
    make_trie(word, trie, 0)
