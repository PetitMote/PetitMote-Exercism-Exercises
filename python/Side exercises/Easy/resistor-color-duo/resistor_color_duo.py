def value(colors):
    array_colors = [
        "black",
        "brown",
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "violet",
        "grey",
        "white"]

    number1 = str(array_colors.index(colors[0]))
    number2 = str(array_colors.index(colors[1]))
    resistance = int(number1 + number2)

    return resistance
