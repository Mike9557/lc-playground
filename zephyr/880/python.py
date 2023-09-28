class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        index = 0
        count = 0
        base = 0
        last_c = ''
        while True:
            if base + 1 == k and 'a' <= s[index] <= 'z':
                return s[index]
            if 'a' <= s[index] <= 'z':
                last_c = s[index]
                index += 1
                count += 1
                base += 1
            else:
                repeat = int(s[index])
                i = 1
                while i < repeat:
                    if base + count > k:
                        index = 0
                        count = 0
                        break
                    elif base + count == k:
                        return last_c
                    else:
                        i += 1
                        base += count
                else:
                    count = count * i
                    index += 1