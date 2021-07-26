##Step1: importing the necessary libraries
import os
import random as r

#Step 2: changing the directory to universe path
#note: I've replaced every / with // due to "unicode error" occured with me
os.chdir('D:\\01 Courses\\00 As Student\\01 CDSP\\04 Lecture 04\\Thanos\\Universe')

#step 3: listing all elements in the universe inside the list named "lst1"
lst1 = os.listdir()

#step 4: Choose 1/2 of elements randomly to be removed and save them in lst2
lst2 = r.sample(lst1,int(len(lst1)/2))

#step 5: remove all elements in lst2
#print(lst2)
for i in lst2:
    os.remove(i)
    
#step 6: checking that 1/2 of universe have been removed by listing elements
#inside the universe and making sure the number of elements is reduced by 1/2
lst1 = os.listdir()
print(lst1)
print(len(lst1))
