from operator import ne


class even:
    def __init__(self):
        self.count=1
    def __iter__(self):
        return self    
    def __next__(self):
        while (self.count<=10):
            val=self.count
            self.count+=1
            if(val%2==0):
                return val
        raise StopIteration        
val=even()
for i in range(10):
    print(next(val))
    



        
