def recite(start_verse: int, end_verse: int) -> list[str]:
    """Returns the lyrics from 'The Twelve Days of Christmas' as a list of verses."""
    if start_verse < 1 or end_verse > 12 or end_verse < start_verse:
        raise ValueError("Invalid start and/or end verse")
    else:
        return [get_verse(number) for number in range(start_verse, end_verse + 1)]


def get_verse(number: int) -> str:
    """Return the verse from 'The Twelve Days of Christmas' corresponding to 'number'."""
    days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh",
            "twelfth"]
    verse = "On the " + days[number - 1] + " day of Christmas my true love gave to me:"
    gifts = [" a Partridge in a Pear Tree.", " two Turtle Doves,", " three French Hens,", " four Calling Birds,",
             " five Gold Rings,", " six Geese-a-Laying,", " seven Swans-a-Swimming,", " eight Maids-a-Milking,",
             " nine Ladies Dancing,", " ten Lords-a-Leaping,", " eleven Pipers Piping,", " twelve Drummers Drumming,"]
    if number == 1:
        verse = verse + gifts[0]
    else:
        verse = verse + "".join([gift for gift in gifts[number - 1:0:-1]]) + " and" + gifts[0]
    return verse
