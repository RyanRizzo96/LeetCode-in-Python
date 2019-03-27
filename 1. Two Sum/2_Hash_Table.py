class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for i, n in enumerate(nums): 
            print(i, n)
            if n in my_dict:
                return [my_dict[n], i]
            my_dict[target-n] = i       #{difference: position}
            print(my_dict)
            
            
            
#  print(i, n)    print(target-n)     print(my_dict)
#       (0, 2)          26-2 = 24           {24, 0}          
#       (1, 7)          26-7 = 19           {19, 1}
#       (2, 11)         26-11= 15           {15, 2}
#       (3, 15)         26-15= 11           {11, 3}
