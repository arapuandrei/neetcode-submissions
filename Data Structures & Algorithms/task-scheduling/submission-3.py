class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from heapq import heappush,heappop
        q = []
        cooldown = []
        fmap = {}
        for i in tasks:
            if i not in fmap.keys():
                fmap[i]=1
            else:
                fmap[i]+=1
        for i in fmap.keys():
            heappush(q,(-fmap[i],i))
        c=0
        while q or cooldown:
            c+=1
            #print("c",c,"q",q,"cooldown",cooldown,"fmap",fmap)
            if cooldown and c == cooldown[0][0]:
                ccounter,pproces = heappop(cooldown)
                heappush(q,(-fmap[pproces],pproces))
            if q:
                counter, process = heappop(q)
                #print(counter,process)
                fmap[process] -= 1
                if fmap[process]>0:
                    heappush(cooldown,(c+n+1,process))
                
            else:
                #print("idle")
                pass
            
        return c

        