def label(colors):
    color_list = {"black": 0,
                  "brown": 1,
                  "red": 2,
                  "orange": 3,
                  "yellow": 4,
                  "green": 5,
                  "blue": 6,
                  "violet": 7,
                  "grey": 8,
                  "white": 9}
    total = color_list[colors[0]]*10 + color_list[colors[1]]
    zeros = "0"*color_list[colors[2]]
    final = int(str(total)+zeros)
    if final == 0:
        return "0 ohms"
    elif final%(10**9)==0:
        result = final//(10**9)
        return str(result) + " gigaohms"
    elif final%(10**6)==0:
        result = final//(10**6)
        return str(result) + " megaohms"
    elif final%(10**3)==0:
        result = final//(10**3)
        return str(result) + " kiloohms"
    else:
        return str(final) + " ohms"
