from phone_list_br import PhoneListBr

text = (
    "I like the phone number 551296221117 and the number 551197789877 but I think"
    "the number 125186248 is not really a phone number"
)
print(text)
phone_list = PhoneListBr(text)

print(phone_list)
print(phone_list.phone_list)
