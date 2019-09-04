#def biggieSize(li):
#    for i in range(0,len(li)):
#        if li[i] > 0:
#            li[i] = "big"
#    return li
#print(biggieSize([-1,3,5,-5]))


#def countPositives(li):
#    count=0
#    for x in range(len(li)):
#        if li[x] > 0:
#            count+=1
#    return li, count
#
#print(countPositives([-1,1,1,1]))
#print(countPositives([1,6,-4,-2,-7,-2]))

#def sumTotal(li):
#    sum = 0
#    for x in li:
#        sum+= x
#    return sum
#
#print(sumTotal([1,2,3,4]))
#print(sumTotal([6,3,-2]))

#def average(li):
#    sum = 0
#    for x in li:
#        sum += x
#    return sum/len(li)
#
#print(average([1,2,3,4]))

#def length(li):
#    return len(li)
#
#print(length([37,2,1,-9]))
#print(length([]))

#def minimum(li):
#    if li == []:
#        return False
#    minimum = li[0]
#    for x in range(len(li)):
#        if x < minimum:
#            minimum = x
#    return minimum
#
#
#print(minimum([37,2,1,-9]))
#print(minimum([]))

#def maximum(li):
#    if li == []:
#        return False
#    maximum = li[0]
#    for x in range(len(li)):
#        if x > maximum:
#            maximum = x
#    return maximum
#
#print(maximum([37,2,1,-9]))
#print(maximum([]))

#def ultimateAnalysis(li):
#
#    dic = {
#        'sumTotal': 0,
#        'average': 0,
#        'minimum': li[0],
#        'maximum': li[0],
#        'length': 0
#}
#    dic['length'] = len(li)
#    for x in li:
#        dic['sumTotal']+= x
#        dic['average'] = dic['sumTotal']/dic['length']
#        if x < dic['minimum']:
#            dic['minimum'] = x
#        if x > dic['maximum']:
#            dic['maximum'] = x
#    return dic
#print(ultimateAnalysis([37,2,1,-9]))

#def reverseList (li):
#
#    for x in range(len(li)//2):
#        temp = li[len(li) -1 -x]
#        li[len(li) - 1 - x] = li[x]
#        li[x] = temp
#
#    return li
#
#print(reverseList([37,2,1,-9]))







