import compression

phrase = "to be or not to be, that is the question"
print("Phrase before compression: " + phrase)
print("Bytes before compression: " + str(len(phrase)))
compressed, key = compression.compress(phrase)
print("Phrase after compression: " + compressed)
print("Bytes after compression: " + str(len(compressed)))
print("Key for decompression: ", key)

normal = compression.decompress(compressed, key) # Decompress using key
print(normal)
