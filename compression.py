from symbols import collection


def getUniqueSymbol(string, blacklist):
	for symbol in collection.split():
		if not symbol in blacklist and not symbol in string:
			return symbol

	return None

def findRepeated(string):
  output = ""
  for i in range(1, len(string)-1):
    substr = string[:i]
    if string.find(substr, i+1) != -1:
      output = substr
    else:
      break

  return output

def getAllRepeateds(text):
  output = []
  while True:
    repeated = findRepeated(text)
    if repeated and len(repeated) > 1:
      output.append(repeated)
      text = text.replace(repeated, "")
    elif len(text) > 1:
      text = text[1:]
    else:
      break
      
  return output


def compress(str):
  compressionKey = {}
  blacklist = []
  duplicates = getAllRepeateds(str)
  for dup in duplicates:
    newSymbol = getUniqueSymbol(str, blacklist)
    if newSymbol != None:
      compressionKey[newSymbol] = dup
      blacklist.append(newSymbol)
      str = str.replace(dup, newSymbol)
    else:
      break

  return str, compressionKey

   
def decompress(str, key):
  for s in key:
    str=str.replace(s, key[s])
	
  return str
