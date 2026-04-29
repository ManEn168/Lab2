#def calculate_bmi(height,weight):
#    print("Height =" + height))
#    print("Weight =" + weight))

#calculate_bmi(weight=" 57", height=" 1.73")    



def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    calculate_bmi = weight / (height*height)
    print (calculate_bmi)

    if calculate_bmi < 18.5:
        print("Underweight")
    elif (calculate_bmi >=18.5) and (calculate_bmi<=25.0):
        print("Normal Weight")
    elif calculate_bmi>25.0:
        print("OverWeight")



calculate_bmi(weight= 57, height= 1.73)    