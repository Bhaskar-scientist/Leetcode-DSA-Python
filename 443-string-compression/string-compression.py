class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0

        while i < len(chars):
            current_char = chars[i]
            count = 0 

            while i < len(chars) and current_char == chars[i]:
                count += 1
                i += 1
            chars[write] = current_char
            write += 1

            if count > 1:
                for x in str(count):
                    chars[write] = x
                    write +=1
        
        return write




        