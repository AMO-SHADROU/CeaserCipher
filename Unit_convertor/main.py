import tkinter

window = tkinter.Tk()
window.title("Miles to Km Convertor")
window.config(padx=40, pady=40)

label1 = tkinter.Label(window, text="is equal to")
label1.grid(row=1, column=0)
label_mile = tkinter.Label(window, text="Miles")
label_mile.grid(row=0, column=2)
label_km = tkinter.Label(window, text="Km")
label_km.grid(row=1, column=2)
label_km_result = tkinter.Label(window, text="0")
label_km_result.grid(column=1, row=1)

miles_entry = tkinter.Entry(window, width=7)
miles_entry.grid(row=0, column=1)


def calculate():
    miles = float(miles_entry.get())
    km = round(miles * 1.609, 1)
    label_km_result.config(text=str(km))



button1 = tkinter.Button(window, text="Calculate", command=calculate)
button1.grid(column=1, row=2)

window.mainloop()
