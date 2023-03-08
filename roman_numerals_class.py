class RomanNumerals:
    @staticmethod
    def to_roman(num):
        roman = ''
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                roman += symbols[i]
        return roman

    @staticmethod
    def from_roman(roman):
        values = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        num = 0
        i = 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in values:
                num += values[roman[i:i+2]]
                i += 2
            else:
                num += values[roman[i]]
                i += 1
        return num
