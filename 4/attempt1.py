class Solution:
    
    def median_of_list(self, sorted_list:  List[int]) -> List[Union[float, int]]:
        #return the median and the length of the first half of the list
        length = len(sorted_list)
        
        #check if length is even
        if (length % 2) == 0:
            return [ (sorted_list[ int(length/2) - 1] + sorted_list[ int(length/2) ]  )/ 2.0, int(length/2)   ]
        else:
            return  [sorted_list[int(length/2)], int(length/2) ]       
       

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        
        start_num1 = int(0)
        end_num1 = int(len_nums1 - 1)
        
        start_num2 = int(0)
        end_num2 = int(len_nums2 - 1)
               
        #edge case of 2 length 1 lists
        if len_nums1 ==1 and len_nums2 ==1:
            return (nums1[0] + nums2[0]) /2.0
        
        #edge case of an empty list
        if len_nums2 == 0:
            return self.median_of_list(nums1)[0]
        elif len_nums1 == 0:
            return self.median_of_list(nums2)[0]
        
        counter=int(0)
        max_size_of_n_plus_m = int(2000) 
        
        while True:
            print("loop")
            print(start_num1)
            print(end_num1)
        
            print(start_num2)
            print(end_num2)
            if counter == 2000:
                break
            counter += 1
            
            if  (end_num1 + 1 - start_num1 ) <= int(2) or (end_num2 + 1 - start_num2) <= int(2):
                while True:
                    if counter == 2000:
                        break
                    counter += 1
                    #check if end of one list is below (or equal) to the start of the other, if so we can concatenate them and just find the median
                    if nums1[end_num1] <= nums2[start_num2]:
                        temp_list = nums1[start_num1:end_num1 + 1] + nums2[start_num2:end_num2 +1]
                        return self.median_of_list(temp_list)[0]

                    elif nums2[end_num2] <= nums1[start_num1]:
                        temp_list = nums2[start_num2:end_num2 +1] + nums1[start_num1:end_num1 + 1]
                        return self.median_of_list(temp_list)[0]

                    #compare the start elements of the two lists and disard lowest 
                    if nums1[start_num1] <= nums2[start_num2]:
                        start_num1+= 1
                    else:
                        start_num2+= 1
                    if nums1[end_num1] <= nums2[end_num2]:
                        end_num2 -= 1
                    else:
                        end_num1 -= 1

            #get medians of each list         
            median1_current, length1_first_half_current = self.median_of_list( nums1[start_num1:end_num1 + 1] )
            median2_current, length2_first_half_current = self.median_of_list( nums2[start_num2:end_num2 + 1] )
            
            #get which length is smaller
            if length1_first_half_current >= length2_first_half_current:
                smallest_length =  length2_first_half_current
            else: 
                smallest_length =  length1_first_half_current
           
            #if the medians are the same then the median of both together is that.
            if median1_current == median2_current:
                return median1_current

            #discard first half of list1 by changing start num
            #discard same number of elements from the end of list2
            elif median1_current < median2_current:
                start_num1 += smallest_length 
                end_num2 -= smallest_length

            else:
                #discard second half of list1 by changing end num
                #discard same umber of elenets from the start of list2
                #via symmetry the length of the first half current must be the same as the second half
                end_num1 -= smallest_length
                start_num2 += smallest_length
  