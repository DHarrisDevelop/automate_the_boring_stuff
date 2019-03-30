def listbreaker(list):
        output = ""
        current_pos = 1
        for item in list:
                if current_pos != 1:
                        output += ", "
                if current_pos == len(list):
                        output += "and "
                output += item
                current_pos += 1
        return output

spam = ['apples', 'bananas', 'tofu', 'cats']
favorite_things = ['breakfast at tiffanys', 'bottles of bubbles', 'girls with tattoos who like getting in trouble', 'lashes and diamonds', 'ATM machines']

print(listbreaker(spam))
print(listbreaker(favorite_things))
