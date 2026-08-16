def resistor_label(colors):
    color_list = {'black': 0,
                  'brown': 1,
                  'red': 2,
                  'orange': 3,
                  'yellow': 4,
                  'green': 5,
                  'blue': 6,
                  'violet': 7,
                  'grey': 8,
                  'white': 9}
    toler_list = {'grey' : 0.05,
                  'violet' : 0.1,
                  'blue' : 0.25,
                  'green' : 0.5,
                  'brown' : 1,
                  'red' : 2,
                  'gold' : 5,
                  'silver' : 10}
    if len(colors) == 1:
        unit = 'ohms'
        return f'{color_list[colors[0]]} {unit}'
    if len(colors) == 4:
        total = color_list[colors[0]]*10 + color_list[colors[1]]
        final = total * (10 ** color_list[colors[2]])
        tolerance = toler_list[colors[3]]
    else:
        total = color_list[colors[0]]*100 + color_list[colors[1]]*10 + color_list[colors[2]]
        final = total * (10 ** color_list[colors[3]])
        tolerance = toler_list[colors[4]]

    if final>=(10**9):
        value = final/(10**9)
        unit = "gigaohms"
    elif final>=(10**6):
        value = final/(10**6)
        unit = "megaohms"
    elif final>=(10**3):
        value = final/(10**3)
        unit = "kiloohms"
    else:
        value = final
        unit = "ohms"
    return f'{value:g} {unit} ±{tolerance}%'
    