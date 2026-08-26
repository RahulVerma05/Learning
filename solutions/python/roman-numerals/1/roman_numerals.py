def roman(number):
    number_dict = {1000:"M",
                   900 : "CM",
                  500 : "D",
                  400 : "CD",
                  100 : "C",
                  90 : "XC",
                  50 : "L",
                  40: "XL",
                  10 : "X",
                  9 : "IX",
                  5 : "V",
                  4 : "IV",
                  1 : "I"}
    roman_con = []
    for key in number_dict:
        while (number-key) >= 0:
            roman_con.append(number_dict[key])
            number = number-key

    return "".join(roman_con)