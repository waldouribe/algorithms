class MyString(str):
    def all_unique_chars(self):
        # ASCII has 256 chars
        char_present = [False]*256
        for char in self:
            ascii_value = ord(char)
            if char_present[ascii_value]:
                return False
            char_present[ascii_value] = True
        return True

    def rotation(another_sting):
        return True

    def anagram(self, another_string):
        char_count = [0]*256
        length = len(self)

        if length != len(another_string):
            return False

        for char in self:
            ascii_value = ord(char)
            char_count[ascii_value] += 1

        for char in another_string:
            ascii_value = ord(char)
            if char_count[ascii_value] <= 0:
                return False
            char_count[ascii_value] -= 1

        return True



        
