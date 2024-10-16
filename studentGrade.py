#ask the user for some information
name = input("Name:")
section = input("Section:")
prelimGrade = float(input("Prelim grade:"))
midtermGrade = float(input("Midterm grade:"))
finalsGrade = float(input("Finals grade:"))

#multiply them to 33.33%
final_prelim_Grade = prelimGrade * (33.33 / 100)
final_midterm_Grade = midtermGrade * (33.33 / 100)
final_finals_Grade =  finalsGrade * (33.33 / 100)

#calculate the fanal grade
calculate = final_prelim_Grade + final_midterm_Grade + final_finals_Grade

#convert the answer to whole number
final_Grade = round(calculate)



if final_Grade >= 99 and final_Grade <= 100:
    print(f"Final Grade = {final_Grade} GPA = 1.00")
    
elif final_Grade >= 96 and final_Grade <= 98:
    print(f"Final Grade = {final_Grade} GPA = 1.25")
    
elif final_Grade >= 93 and final_Grade <= 95:
    print(f"Final Grade = {final_Grade} GPA = 1.50")
    
elif final_Grade >= 90 and final_Grade <= 92:
    print(f"Final Grade = {final_Grade} GPA = 1.75")
    
elif final_Grade >= 87 and final_Grade <= 89:
    print(f"Final Grade = {final_Grade} GPA = 2.00")
    
elif final_Grade >= 84 and final_Grade <= 86:
    print(f"Final Grade = {final_Grade} GPA = 2.25")
    
elif final_Grade >= 81 and final_Grade <= 83:
    print(f"Final Grade = {final_Grade} GPA = 2.50")
    
elif final_Grade >= 78 and final_Grade <= 80:
    print(f"Final Grade = {final_Grade} GPA = 2.75")
    
elif final_Grade >= 75 and final_Grade <= 77:
    print(f"Final Grade = {final_Grade} GPA = 3.00")
    
elif final_Grade < 75:
    print(f"Final Grade = {final_Grade} GPA = 5.00")
    
else:
    print("Please enter a valid number.")