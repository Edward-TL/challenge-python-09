from typing import List


class Solution:
    

    def duplicate_zeros(self, arr: List[int]):
        # AQUÍ VA TU SOLUCIÓN
        zeros = 0
        original_length = len(arr)  #No '-1' beacues is used only at 'For's, and they use < not <= 
        new_length = original_length

        if original_length > 0:    #Just in case i have 1 element on the array
            element = 0
            while element in range(0, new_length):      #I only need to check the last value that would fit on the new array
                if arr[element] == 0:
                    zeros += 1
                    new_length = original_length - zeros    #And here's how i know if it would fit
                
                element += 1
        else:
            if arr[0] == 0:
                    zeros += 1

        check_position = original_length - zeros - 1 #Because of arr[0]
        modified_position = original_length - 1 #Because of arr[0]
        
        if zeros == 1:      #Imaging that the only 0 is the last, it won't change
            check_value = arr[modified_position]

            if check_value == 0:
                zeros = 0


        while zeros > 0 and check_position >= 0:
            check_value = arr[check_position]       #I know I could use the arr, but this was easier for debugging

            if check_value != 0:
                arr[modified_position] = check_value

            if check_value == 0:
                arr[modified_position] = check_value #It's 0 but in the new position
                modified_position -= 1               #Move in position
                arr[modified_position] = check_value #It's 0 but in the new position
                zeros -= 1

            check_position -= 1
            modified_position -= 1