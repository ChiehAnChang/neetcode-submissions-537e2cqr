class Solution:

    def encode(self, strs) -> str:
        res = ""

        for each_s in strs:
            length = len(each_s)
            res += (str(length) + "s" + each_s)
        
        return res


    def decode(self, s) -> List[str]:
        length = ""
        find_s = False
        ctn = 0
        each_string = ""
        res = []

        for each_char in s:
            if not find_s:
                if each_char == "s":          
                    find_s = True
                    ctn = int(length)        
                    length = ""              
                    if ctn == 0:            
                        res.append("")      
                        find_s = False      
                    continue
                length += each_char          
            else:
                if ctn > 0:
                    each_string += each_char  
                    ctn -= 1
                    if ctn == 0:
                        res.append(each_string)
                        each_string = ""
                        find_s = False     
        return res
