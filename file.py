from tkinter import *

root = Tk()

t = Text(root, width = 60, height = 25)


t.grid(row=6, column=0, columnspan=10)

def table_without_file():
    t.delete(1.0, END)

    n = number_entry.get()
    n1 = int(n)
    start = start_entry.get()
    start1 = int(start)
    end = end_entry.get()
    end1 = int(end)
    
    if start<end:
        for i in range(start1,end1+1):
            s = str(n1) + "X" + str(i) + "=" + str(n1*i)
            print(n1,"X",i,"=",n1*i)
            t.insert(END, "{} \n".format(s))

    elif start>end:
        for i in range(start1,end1,-1):
            s = str(n1) + "X" + str(i) + "=" + str(n1 * i)
            print(n1, "X", i, "=", n1 * i)
            t.insert(END, "{} \n".format(s))


def table_with_file():
    t.delete(1.0, END)
    n = number_entry.get()
    n1 = int(n)
    start = start_entry.get()
    start1 = int(start)
    end = end_entry.get()
    end1 = int(end)
    
    name = file_entry.get()
    file=open(name,"a")

    if start<end:
        for i in range(start1,end1+1):
            s = str(n1) + "X" + str(i) + "=" + str(n1*i)
            file.write(s)
            file.write("\n")
            print(n1,"X",i,"=",n1*i)
            t.insert(END, "{} \n".format(s))
                

    elif start>end:
        for i in range(start1,end1,-1):
            s = str(n1) + "X" + str(i) + "=" + str(n1 * i)
            file.write(s)
            file.write("\n")
            print(n1, "X", i, "=", n1 * i)
            t.insert(END, "{} \n".format(s))

    file.close()


number_label = Label(root, text="Enter number here :--")
number_label.grid(row=1, column=0)
number_entry = Entry(root, text="")
number_entry.grid(row=1, column=1)

start_label = Label(root, text="Enter start bound :--")
start_label.grid(row=2, column=0)
start_entry = Entry(root, text="")
start_entry.grid(row=2, column=1)

end_label = Label(root, text="Enter end bound :--")
end_label.grid(row=3, column=0)
end_entry = Entry(root, text="")
end_entry.grid(row=3, column=1)

file_label = Label(root, text="Name you file:--")
file_label.grid(row=4, column=0)
file_entry = Entry(root, text="")
file_entry.grid(row=4, column=1)


print_with_button = Button(root, text="Get table with file", command=table_with_file)
print_with_button.grid(row=5, column=0)

print_without_button = Button(root, text="Get table without file", command=table_without_file)
print_without_button.grid(row=5, column=1)



root.mainloop()
