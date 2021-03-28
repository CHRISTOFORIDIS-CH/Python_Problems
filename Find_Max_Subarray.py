import random
import  time


def find_max_sum_of_subarray(a): #finding sums

      temp = 0
      max = 0
      for i in a:
          if i <= 0:
              temp = 0
              continue
          else:
              temp += i
          if temp > max:
              max = temp
      return max


def find_middle(b): #find middle of big list
    middle = len(b) // 2
    a = True
    while(True):
        if b[middle] <= 0:
            break
        else:
            middle += 1
    return middle




#count time
start_time = time.time()
#creating big list
list = [random.randrange(-100, 100, 1) for i in range(10000000)]
#divide and conquer
middle = find_middle(list)
left = list[:middle]
right = list[middle:]
print("The list: "+str(list))
print("The left max: "+str(find_max_sum_of_subarray(left)))
print("The right max: "+str(find_max_sum_of_subarray(right)))
print("Normal max: "+ str(find_max_sum_of_subarray(list)))
print("--- %s seconds ---" % (time.time() - start_time))
