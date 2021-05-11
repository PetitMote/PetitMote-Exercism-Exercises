# Thank you @IsaacG for the review (first of a series !)

def convert(number: int) -> str:
    raindrops = ""
    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"

    if not raindrops:
        raindrops = str(number)
    return raindrops
