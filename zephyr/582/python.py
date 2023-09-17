class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        l = collections.deque([kill])
        ans = []
        while len(l) > 0:
            try:
                k = l.popleft()
                i = ppid.index(k)
                while i != -1:
                    l.append(pid[i])
                    ppid.pop(i)
                    pid.pop(i)
                    i = ppid.index(k)
            except:
                pass
            ans.append(k)
        return ans