print("Welcome","to", "Python","programming", sep="-")
name = "Carlos Victor de Alcantara Carleial"
age = 29.0
title= "Software Engineer"
favorite_programming_language = "Java, Python, Go, Javascript"
if age < 30:
    print("Name: " + name)
    print("Age: " + str(age))
    print("Title: " + title)

languages = favorite_programming_language.split(",")
print("Favorite Languages: " + str(languages))


