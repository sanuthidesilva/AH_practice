import tkinter as tk

root = tk.Tk()
root.geometry('500x500')
root.title('kinter Hub')

# main frame/essentailly the body of the page that will change
main_frame = tk.Frame()


# the three different pages:
page1 = tk.Frame(main_frame)
page1_lb = tk.Label(master=page1,
                    text='Page 1',
                    font=('bold', 25))
page1_lb.pack(pady=100)


page2 = tk.Frame(main_frame)
page2_lb = tk.Label(master=page2,
                    text='Page 2',
                    font=('bold', 25))
page2_lb.pack(pady=100)


page3 = tk.Frame(main_frame)
page3_lb = tk.Label(master=page3,
                    text='Page 3',
                    font=('bold', 25))
page3_lb.pack(pady=100)

main_frame.pack(fill=tk.BOTH, expand=True)

pages = [page1, page2, page3]
count = 0


def moveNext():
    global count

# only move to the next page if you're not on the last page
    if not count > len(pages)-2:

        for p in pages:
            p.pack_forget()

        count += 1
        page = pages[count]
        page.pack(fill=tk.BOTH, expand=True)


def moveBack():
    global count

    if not count == 0:

        for p in pages:
            p.pack_forget()

        count -= 1
        page = pages[count]
        page.pack(fill=tk.BOTH, expand=True)


# this frame is where the buttons are and would not change
bottom_frame = tk.Frame(root)

# back button
back_btn = tk.Button(master=bottom_frame,
                     text='Back',
                     font=('Bold', 15),
                     bg='#89CFF0',
                     fg='black',
                     width='10',
                     command=moveBack)

back_btn.pack(side=tk.LEFT, padx=10, pady=20)

# next button
next_btn = tk.Button(master=bottom_frame,
                     text='Next',
                     font=('Bold', 15),
                     bg='#89CFF0',
                     fg='black',
                     width='10',
                     command=moveNext)

next_btn.pack(side=tk.RIGHT, padx=10, pady=20)

bottom_frame.pack(side=tk.BOTTOM, padx=10)


root.mainloop()
