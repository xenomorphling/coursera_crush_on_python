# def is_palindrome(input_string):
#   input_string = input_string.replace(" ", "");
#   input_string = input_string.lower();
#   new_string = ""
#   reverse_string = ""
#   for letter in input_string:
#     new_string += letter
#     reverse_string = letter + reverse_string
#   if new_string == reverse_string:
#   	return True
#   return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def convert_distance(miles):
#   km = miles * 1.6 
#   result = "{} miles equals {:.1f} km".format(miles, km);
#   return result

# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


# def group_list(group, users):
#   members = str(users).replace("[","")
#   members = members.replace("]","")
#   members = members.replace("'","")
#
#   return ((group) + ": " + members)
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"



# def full_emails(people):
#   result = []
#   for email, name in people:
#     result.append("{} <{}>".format(name, email))
#   return result
# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))


# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#   print(len(animal))
#   chars += len(animal)
# print("Total characters: {}, Average langth: {}".format(chars, chars/len(animals)))

# winners = ["Ashley", "Dylan", "Reese"]
# for index, person in enumerate(winners):
#   print("{} - {}".format(index + 1, person))

# def skip_elements(elements):
#   result = ([])
#   for index, element in enumerate(elements):
#     if index % 2 == 0:
#       result += element
#   print(result)

# # print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(["Orange", "Pineapple", "Strawberry", "Kiwi", "Peach"])) # Should be ['Orange', 'Strawberry', 'Peach']

# multiples = []
# for x in range(1, 11):
#   multiples.append(x*7)
# print(multiples)

# multiples = [x*7 for x in range(1, 11)]
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [x for x in range(0, 101) if x % 3 == 0]
# print(z)

# def odd_numbers(n):
#   return [x for x in range(0, n+1) if x % 2 == 1]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []

# Quiz

