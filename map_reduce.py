from random import *
numbers= [1,2,3,4,5,6,7,8,9]
filter_result= list(filter(lambda item: item % 2==0, numbers))
print("filtered data list :%s" % filter_result)
map_result= list(map(lambda item :item *2 ,filter_result))
print("mapped data list: %s " % map_result)

from functools import reduce
reduce_result= reduce(lambda x,y: x+y, map_result)
print("reduced data list :%s" % reduce_result)
