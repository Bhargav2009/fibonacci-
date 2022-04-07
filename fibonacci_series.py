from tkinter import *
root = Tk()

root.title("fibonacci series")
root.geometry("400x400")

label_series = Label(root,text="fibonacci series: ")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    
    while(counter<=num):
        label_series["text"]+=str(sum)+" "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        
    label_flower["text"]="flower is fully blomed"
    label_spiral["text"]="spiral in right direction are "+ str(first_no)+ " and the spirals in left directions are " + str(second_no)+ "\n The total spirals are "+str(sum)

btn = Button(root,text="show Fibonnacci series",command = fibonacci)
    
btn.pack()
label_flower.pack()
label_spiral.pack()
label_series.pack()
    
root.mainloop()