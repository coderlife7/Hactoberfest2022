test_str = "Cricket"

print ("The original string is : " + test_str)

all_freq = {}
for i in test_str:
    
    
    if i in all_freq:
         
        
        all_freq[i] += 1
    else:
        
        
        all_freq[i] = 1
        res = max(all_freq, key = all_freq.get)

# printing result
print ("The maximum of all characters in " +test_str+ " is : " + str(res))
