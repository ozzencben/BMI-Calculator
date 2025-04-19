import tkinter

window = tkinter.Tk()
window.geometry("500x500")
window.title("BMI Calculate")
window.resizable(width=False, height=False)
window.config(bg="AntiqueWhite3")

kg_label = tkinter.Label(text="Enter your weight (kg)", width=20, font=("Montserrat", 14, "normal"), bg="AntiqueWhite3")
kg_label.place(relx=0.5, rely=0.2, anchor=tkinter.N)

kg_entry = tkinter.Entry(width=20,font=("montserrat", 15), relief=tkinter.FLAT)
kg_entry.place(relx=0.5, rely=0.29, anchor=tkinter.N)
kg_entry.focus()

cm_label = tkinter.Label(text="Enter your height (cm)", width=20, font=("Montserrat", 14, "normal"), bg="AntiqueWhite3")
cm_label.place(relx=0.5, rely=0.4, anchor=tkinter.N)

cm_entry = tkinter.Entry(width=20,font=("montserrat", 15), relief=tkinter.FLAT)
cm_entry.place(relx=0.5, rely=0.49, anchor=tkinter.N)

def BMI_calculate():
    try:
        kg = float(kg_entry.get())
        cm = float(cm_entry.get())
        bmi = kg / (cm / 100)**2
        return bmi
    except ValueError:
        result_label.config(text="Please enter numerical values")
        cm_entry.delete(0, tkinter.END)
        kg_entry.delete(0, tkinter.END)
        return None
    except ZeroDivisionError:
        result_label.config(text="Height cannot be zero.")
        cm_entry.delete(0, tkinter.END)
        kg_entry.delete(0, tkinter.END)
        return None

def calculate_btn_click():
    category = ""
    detail = ""
    result_BMI = BMI_calculate()
    if result_BMI is not None:
        if result_BMI <= 18.5:
            category = "Low weight"
            detail = "Your weight is low compared to your height. It is recommended that you consult a specialist to gain healthy weight."
        elif result_BMI <= 25:
            category = "Normal weight"
            detail = "Your weight is in a healthy range for your height. Continue your healthy lifestyle habits."
        elif result_BMI <= 30:
            category = "Overweight"
            detail = "Your weight is higher than the healthy range for your height. It may be beneficial to review your nutrition and exercise habits to reach a healthy weight."
        elif result_BMI <= 35:
            category = "Obesity (Class I)"
            detail = "You are in the first stage of obesity. It is important to talk to a health professional to learn about appropriate treatment and lifestyle changes to protect your health."
        elif result_BMI <= 40:
            category = "Obesity (Class II)"
            detail = "You are in the second stage of obesity. The risks to your health have increased. It is recommended that you consult a healthcare professional for a comprehensive evaluation and treatment plan."
        else:
            category = "Obesity (Class III)"
            detail = "This condition, also known as morbid obesity, can lead to serious health problems. It is vital that you contact a healthcare professional immediately and seek medical attention."

        result_label.config(text=f"BMI : {result_BMI:.2f} \n {category} \n {detail}", justify="left", wraplength=450)

calculate_btn = tkinter.Button(text="Calculate", font=("montserrat", 13, "bold"), relief=tkinter.FLAT, cursor="hand2", command=calculate_btn_click)
calculate_btn.place(relx=0.5, rely=0.6, anchor=tkinter.N)

result_label = tkinter.Label(font=("Montserrat", 14, "normal"), bg="AntiqueWhite3", justify="left") # justify="left" eklendi
result_label.place(relx=0.5, rely=0.7, anchor=tkinter.N) # rely değeri güncellendi

window.mainloop()