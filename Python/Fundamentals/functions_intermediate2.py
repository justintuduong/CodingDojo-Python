#x = [ [5,2,3], [10,8,9] ]
#students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
#]
#sports_directory = {
#    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
#}
#z = [ {'x': 10, 'y': 20} ]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

#x[1][0] = 15
#print(x)

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'

#students[0]['last_name'] = "Bryant"
#print(students)

# 3. In the sports_directory, change 'Messi' to 'Andres'

#sports_directory['soccer'][0] = "Andres"
#print(sports_directory)


# 4. Change the value 20 in z to 30
#z[0]['y'] = 30
#print(z)

#--------------------------------------------------

#students = [
#            {'first_name':  'Michael', 'last_name' : 'Jordan'},
#            {'first_name' : 'John', 'last_name' : 'Rosales'},
#            {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#            {'first_name' : 'KB', 'last_name' : 'Tonel'}
#            ]

#def iterateDictionary(arr):
#    for x in range(len(arr)):
#        print(students[x])
#
#iterateDictionary(students)


#bonus --------
#def iterateDictionary(arr):
#    for x in range(len(arr)):
#        print("first_name {} , last_name {}".format(students[x]['first_name'], students[x]['last_name']))
#
#iterateDictionary(students)

#--------------------------------------------------

#def iterateDictionary2(key_name, some_list):
#    for x in range(len(some_list)):
#        print(some_list[x][key_name])
#
#iterateDictionary2('first_name', students)
#iterateDictionary2('last_name', students)

#--------------------------------------------------


#dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
#}
#
#def printInfo(some_dict):
#    for key in some_dict:
#        print(len(some_dict[key]) ,key)
#        for value in some_dict[key]:
#            print(value)
#printInfo(dojo)


#def printInfo(some_dict):
#    for key in some_dict:
#        print(len(some_dict[key]) ,key, some_dict[key])
#
#printInfo(dojo)

#def printInfo(some_dict):
#    for x in range(len(some_dict)):
#        if x == 0:
#            print(f"{len(some_dict['locations'])} LOCATIONS {some_dict['locations']}")
#        elif x== 1:
#            print(f"{len(some_dict['instructors'])} INSTRUCTORS {some_dict['instructors']}")
#
#printInfo(dojo)

    
