"""
Below you will find broken pieces of code, do you think you can spot all the errors and fix them? Don't forget to use the debugging skills that you have learned so far!

If you think this stuff is too easy for you, you can try to see if you can master the VS Code debugger! Just click the link above and get started.
"""

# 1
greeting="Hello World!"

if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
                
# 2
author = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}
for author Date in author.items{}:
    print("%s" % author + " died in " + "%d." + Date)

             
# 3
year=int.input("Greetings! What is your year of origin? ")

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 && year < 2020:
    print ("That's totally the present!")
elif
    print ("Far out, that's the future!!")
           
# 4
classy_Person:
def __initalize__(self, first_name, last_name):
    self.first = first_name
    self.last = last_name
def speak(self):
    print("My name is "self.first" + "self.last"")

me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.self.speak
           
# 5
exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: ")

exam_three = str(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
sum = 0
for grade in grades:
  sum = sum + grade

avg = sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter_grade is "F":
    print("Student is failing.")
else:
    print("Student is passing.")