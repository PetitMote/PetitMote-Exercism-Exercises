import re


class PhoneNumber:
    def __init__(self, number):
        cleaned_number = re.sub("\D", "", number)
        len_number = len(cleaned_number)
        check_format = True

        if len_number < 10 or len_number > 11:
            check_format = False
        elif len_number == 11 and cleaned_number[0] != "1":
            check_format = False
        else:
            if len_number == 11:
                cleaned_number = cleaned_number[1:]
            if not re.search("[2-9]\d{2}[2-9]\d{6}", cleaned_number):
                check_format = False

        if not check_format:
            raise ValueError("This is not a valid phone number")
        else:
            self.number = cleaned_number
            self.area_code = cleaned_number[:3]

    def pretty(self) -> str:
        return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
