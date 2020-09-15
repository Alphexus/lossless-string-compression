# Lossless String Compression
### A simple way to compress strings at no cost using Python.


#### Demo
```py
import compression

phrase = "to be or not to be, that is the question"
compressed, key = compression.compress(phrase)

def utf8len(s):
  return len(s.encode('utf-8'))

print("Uncompressed: " + phrase)
print("Compressed: " + compressed)
print("Bytes before compression: %s, Bytes after compression: %s"%(utf8len(phrase), utf8len(compressed)))
```

#### Output
```
Uncompressed: to be or not to be, that is the question
Compressed: 0 or no10,2a1is2e question
Bytes before compression: 40, Bytes after compression: 26
```

