def Sudokou(sequence):
    count = 0
    if type(sequence) is list:
       for i in sequence:
           if i != 0:
             count += 1
           else:
               continue
       if count >= 17:
           return True
       else:
           return False
    else:
        return 0
print(Sudokou([0,0,4,0,0,6,0,7,9,0,0,0,0,0,0,6,0,2,0,5,6,0,9,2,3,0,0,0,7,8,0,6,1,0,3,0,5,0,9,0,0,0,4,0,6,0,2,0,5,4,0,8,9,0,0,0,7,4,1,0,9,2,0,1,0,5,0,0,0,0,0,0,8,4,0,6,0,0,1,0,0]))