# This program has been coded by Avinash Shandlilya in JUPYTER NOTEBOOK.

name = input("Enter your name: ");
standard = int(input("Enter your Class: "));
subject = input("Enter the subject to know your grade: ");
marks_in_sub = int(input("Enter the marks: "));
# code for giving grades:
if marks_in_sub >= 90:
    print("Congratulations!",name,"your grade is A+ in",subject,"and you've successfully qualified",standard,"th class.");    
elif marks_in_sub >= 80 and marks_in_sub < 90:
    print("Congratulations!",name,"your grade is A in",subject,"and you've successfully qualified",standard,"th class.");    
elif marks_in_sub >= 70 and marks_in_sub < 80:
    print("Congratulations!",name,"your grade is B+ in",subject,"and you've successfully qualified",standard,"th class.");  
elif marks_in_sub >= 60 and marks_in_sub < 70:
    print("Congratulations!",name,"your grade is B in",subject,"and you've successfully qualified",standard,"th class.");  
elif marks_in_sub >= 50 and marks_in_sub < 60:
    print("Congratulations!",name,"your grade is C in",subject,"and you've successfully qualified",standard,"th class.");
elif marks_in_sub >= 40 and marks_in_sub < 50:
    print("Congratulations!",name,"your grade is D in",subject,"and you've successfully qualified",standard,"th class.");
else:
    print("Sorry!",name,"your grade is F in",subject,"and you've not qualified",standard,"th class.");
    
# End of the code
