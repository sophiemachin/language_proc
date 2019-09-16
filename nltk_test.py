import nltk

sentence = """I shot an elephant in my pyjamas"""

tokens = nltk.word_tokenize(sentence)
print(tokens)

tagged = nltk.pos_tag(tokens)
print(tagged[0:6])

entities = nltk.chunk.ne_chunk(tagged)

print(entities)
