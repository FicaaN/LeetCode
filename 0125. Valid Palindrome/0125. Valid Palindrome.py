class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Converting the entire string into lowercase letters
        lowercase_string = s.lower()
        # Here we're applying filter to the lowercase string and checking,
        # if every character (char) is alphanumeric (isalnum)
        cleaned_lowercase_string = ''.join(filter(lambda char: char.isalnum(), lowercase_string))

        return cleaned_lowercase_string == cleaned_lowercase_string[::-1]