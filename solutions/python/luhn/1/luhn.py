class Luhn:
    def __init__(self, card_num):
        card_num = card_num.replace(" ","")
        digit = []
        for c in card_num:
            if not c.isdigit():
                self.digit = []
                return
            digit.append(int(c))
        for i in range(len(digit)-2,-1,-2):
            digit[i] *= 2
            if digit[i] > 9:
                digit[i] = digit[i]-9
        self.digit = digit

    def valid(self):
        if len(self.digit) < 2:
            return False
        return sum(self.digit)%10 == 0
