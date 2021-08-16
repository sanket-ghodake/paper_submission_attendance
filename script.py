import os
'''
There is paper conducted in online manner, where student submitted scan copy of solved question paper.
Teacher downloaded files in respective folders of classes and subjects. 
The typical file has name as "roll_no name class div subject"
Program helps teacher to find out easily who submitted paper and who not after he/she saves files in respective directories.
'''

def attendence_data(class_string, class_total_student):
    vi_b_hindi = os.listdir(
        fr"C:\Users\August Paper\{class_string}")
    VI_B_Hindi_student = class_total_student
    VI_B_Hindi_paper_attendance = {"present": [], "absent": []}
    for i in vi_b_hindi:
        VI_B_Hindi_paper_attendance["present"].append(int(i[0:2]))
    temp = VI_B_Hindi_paper_attendance["present"]
    for i in range(1, VI_B_Hindi_student):
        if i in temp:
            continue
        VI_B_Hindi_paper_attendance["absent"].append(i)

    VI_B_Hindi_paper_attendance["absent"].sort()
    VI_B_Hindi_paper_attendance["present"].sort()
    print(f"{class_string} -")
    print("Present -",VI_B_Hindi_paper_attendance["present"])
    print("Absent -",VI_B_Hindi_paper_attendance["absent"])
    print("Total Presnt - ", len(VI_B_Hindi_paper_attendance["present"]))
    print("Total Absent - ", len(VI_B_Hindi_paper_attendance["absent"]), end='\n\n')

    # TODO why below line give error
    # print(f"Total present -{len(VI_B_Hindi_paper_attendance["present"])} Total absent - {len(VI_B_Hindi_paper_attendance["absent"])}")


if __name__ == '__main__':
    VI_B_Hindi = ("VI B Hindi", 57)
    VI_C_Hindi = ("VI C Hindi", 61)
    VII_B_Marathi = ("VII B Marathi", 55)
    VII_C_Hindi = ("VII C Hindi", 54)
    classes = [VI_B_Hindi,VI_C_Hindi,VII_B_Marathi,VII_C_Hindi]
    for i in classes:
        attendence_data(i[0],i[1])
