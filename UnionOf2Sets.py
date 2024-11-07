#Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        combined=a+b
        union_result=sorted(set(combined))
        return union_result
