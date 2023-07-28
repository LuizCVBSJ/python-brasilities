import re


class PhoneListBr:
    def __init__(self, number):
        self.phone_list = []
        if self.phone_search(number):
            self.phone_list.append(self.phone_search(number))
        else:
            raise ValueError("No valid phone number!")

    def __str__(self):
        for phone in self.phone_list:
            return self.format_phone_number(str(phone))

    @staticmethod
    def phone_search(number):
        pattern = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        search = re.search(pattern, number)
        return search

    @staticmethod
    def format_phone_number(number):
        search = PhoneListBr.phone_search(number)
        if search.group(1):
            answer = "+{}({})9{}-{}".format(
                search.group(1), search.group(2), search.group(3), search.group(4)
            )
        else:
            answer = "({})9{}-{}".format(
                search.group(2), search.group(3), search.group(4)
            )
        return answer
