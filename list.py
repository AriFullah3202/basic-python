# লিস্টে অনেক রকমের ডাটা টাইপ থাকে ।
# এবং শুরুতে , শেষে third bracket থাকবে ।

firtlist = ['lenebo' , 33 , '83']
print(firtlist) # ['lenebo' , 33 , 83]
print(type(firtlist)) # <class 'list'>

course = ['Math', 'Science', 'History', 'English', 'Geography']
print(len(course))

#access item
print('list item is ' , course[4]) # output Geography এটা জিরো থেকে শুরু হয় ।
print('list item' , course[-4]) # output Science এটা উল্টো দিক থেকে query করে

# Range
print("Range:", course[2:5])   # Output: ['History', 'English', 'Geography']
print("Range:", course[:5])    # Output: ['Math', 'Science', 'History', 'English', 'Geography']
print("Range:", course[5:])    # Output: []

# Negative range
print("Range:", course[-2:])   # Output: ['English', 'Geography']
print("Range:", course[:-2])   # Output: ['Math', 'Science', 'History']

# Item value change
course[1] = 40
print('New list:', course)   # Output: ['Math', 40, 'History', 'English', 'Geography']
# Insert method
course.insert(0, "aiQuest")
print('New inserted list:', course)   # Output: ['aiQuest', 'Math', 40, 'History', 'English', 'Geography']
# Append method
course.append("study marts")
print('Append:', course)   # Output: ['aiQuest', 'Math', 40, 'History', 'English', 'Geography', 'study marts']
# Remove method
course.remove('Math')
print('Remove:', course)   # Output: ['aiQuest', 40, 'History', 'English', 'Geography', 'study marts']
# Pop method
course.pop(2)
print('Pop:', course)   # Output: ['aiQuest', 40, 'English', 'Geography', 'study marts']
# Del keyword
del course[3]
print('Del:', course)   # Output: ['aiQuest', 40, 'Geography', 'study marts']
# Sort method
alphabetic = ['python', 'django', 'ML']
alphabetic.sort()
print('Sorted:', alphabetic)   # Output: ['ML', 'django', 'python']
