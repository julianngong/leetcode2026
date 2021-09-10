class Solution(object):
    def by_value(self,item):
        return item[1]
    
    def intToRoman(self, num):
        output = ''
        symbols = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        for key, value in sorted(symbols.items(), key=self.by_value, reverse=True):
            output = output + (key * (num/value))
            num = num - (value*(num/value))
        return(output)
            
            
            
        
        
        
