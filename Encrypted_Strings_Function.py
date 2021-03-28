#if they cant be shifted they stay the same spaces are ignored if something other than string isa passed return 0 all prashes are capital letters
def split(word):
    return list(word)


def Shift_String(text, shift):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U","V", "W", "X", "Y", "Z"]
    if type(text) is str:
       chars = split(text)
       for j in range(len(chars)):
         for i in range(len(alphabet)):
           if alphabet[i].__eq__(chars[j]):
               if i+shift+1 > len(alphabet):
                   break
               else:
                chars.pop(j)
                try:
                  chars.insert(j, alphabet[i+shift])
                except IndexError:
                    print("")
                finally:
                    break
       #just to see i could do that in upper fors
       WordToReturn = ""
       for e in chars:
          WordToReturn += e
       return WordToReturn
    else:
        return 0


print(Shift_String("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25))
