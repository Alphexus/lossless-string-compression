# Lossless String Compression
## A simple way to compress strings at no cost using Python.

### Demo
```
import compression

phrase = "to be or not to be, that is the question"
compressed, key = compression.compress(phrase)

print("Bytes before compression: %s, Bytes after compression: %s"%(str(len(phrase)), str(len(compressed))))
```

### Output
```
Bytes before compression: 40, Bytes after compression: 26
```

