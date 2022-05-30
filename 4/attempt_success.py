class Solution:
    
    
    def median_of_list(self, sorted_list:  List[int]) -> float:
        length = len(sorted_list)
        
        #check if length is even
        if (length % 2) == 0:
            return (sorted_list[ int(length/2) - 1] + sorted_list[ int(length/2) ]  )/ 2.0
        else:
            return  sorted_list[int(length/2)]       
       

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        start_num1 = int(0)
        end_num1 = int(len_nums1 - 1)
        
        start_num2 = int(0)
        end_num2 = int(len_nums2 - 1)
        
        median_found = False
        
        #edge case of 2 length 1 lists
        if len_nums1 ==1 and len_nums2 ==1:
            return (nums1[0] + nums2[0]) /2.0
        
        #edge case of an empty list
        if len_nums2 == 0:
            return self.median_of_list(nums1)
        elif len_nums1 == 0:
            return self.median_of_list(nums2)
        
        counter=int(0)
        max_size_of_n_plus_m = int(2000)
        
        while median_found != True:
            if counter == 2000:
                break
            counter += 1
              
            #check if end of one list is below (or equal) to the start of the other, if so we can concatenate them and just find the median
            if nums1[end_num1] <= nums2[start_num2]:
                temp_list = nums1[start_num1:end_num1 + 1] + nums2[start_num2:end_num2 +1]
                return self.median_of_list(temp_list)
            
            elif nums2[end_num2] <= nums1[start_num1]:
                temp_list = nums2[start_num2:end_num2 +1] + nums1[start_num1:end_num1 + 1]
                return self.median_of_list(temp_list)

            #compare the start elements of the two lists and disard lowest 
            if nums1[start_num1] <= nums2[start_num2]:
                start_num1+= 1
            else:
                start_num2+= 1
            if nums1[end_num1] <= nums2[end_num2]:
                end_num2 -= 1
            else:
                end_num1 -= 1
                
                


                

                
            
        
        
                        
        