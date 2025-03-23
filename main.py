from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import Radiobutton
from tkinter import messagebox


def search(about):
    global image

    s_or_t = about[0]
    g_or_b = about[1]
    e_or_h = about[2]
    bc_or_dc = about[3]
    file_table = open('input.txt', "r")
    input_file = file_table.readlines()

    for x in input_file:
        each_song = x.split()
        for i in range(len(each_song)):
            if each_song[0] == s_or_t and each_song[1] == g_or_b and each_song[2] == e_or_h and each_song[3] == bc_or_dc:
                final_result = ''

                for i in range(len(each_song)):
                    if i >= 4:
                        final_result += each_song[i] + ' '
                name_image = "{}.jpeg".format(each_song[-1])
                image = ImageTk.PhotoImage(file=name_image)
                label = Label(window, image=image, height=360, width=610, bg='#f2dff7')
                label.place(relx=0.02, rely=0.2)
                if name_image == "Упс!.jpeg":
                    label2 = Label(window, text = "К сожалению, хореографии, соответствующий\n выбранным тобой критериям, пока не существует", bg='#f2dff7', font=("Helvetica", 17))
                    label2.place(relx=0.2, rely=0.1)
                title1 = Label(window, text=final_result, bg='#f2dff7', font=("Helvetica", 30))
                title1.pack()


                f = open('output.txt', 'w')
                f.close()
                break
    file_table.close()


def results():
    infile = open('output.txt', "r")
    profile_list = infile.readlines()
    about = profile_list[0].split()
    infile.close()
    search(about)


def concept():
    def second_des():
        rad1.destroy()
        rad2.destroy()
        next_question.destroy()
        title.destroy()
        if selected.get() == 1:
            file_info = open('output.txt', "a")
            file_info.write('bc')
            file_info.close()
            results()
        elif selected.get() == 2:
            file_info = open('output.txt', "a")
            file_info.write('dc')
            file_info.close()
            results()
    def check2():
        if selected.get() != 1 and selected.get() != 2:
            messagebox.showwarning('Ошибка', 'Выбери')
            return
        else:
            second_des()
    title.configure(text='Какие концепты в K-pop обычно нравятся тебе больше?')
    title.place(relx=0.1, rely=0.1)
    selected = IntVar()
    rad1 = Radiobutton(window, text='светлые концепты типа girl/boy next door'
                    ' с весёлой\n и лёгкой мелодией', value=1, variable=selected)
    rad2 = Radiobutton(window, text='гёрл-краш или что-то из тёмных концептов с '
     'мощными\n припевами и громким инструменталом', value=2, variable=selected)
    rad1.place(relx=0.25, rely=0.3)
    rad2.place(relx=0.25, rely=0.4)
    next_question = Button(window, text="следующий "
                                        "вопросик", command=lambda: check2())
    next_question.place(relx=0.38, rely=0.5)


def easy_or_hard():
    def third_des():
        rad1.destroy()
        rad2.destroy()
        next_question.destroy()
        if selected.get() == 1:
            file_info = open('output.txt', "a")
            file_info.write('easy ')
            file_info.close()
            concept()
        elif selected.get() == 2:
            file_info = open('output.txt', "a")
            file_info.write('hard ')
            file_info.close()
            concept()
    def check2():
        if selected.get() != 1 and selected.get() != 2:
            messagebox.showwarning('Ошибка', 'Выбери')
            return
        else:
            third_des()
    title.configure(text='Какой уровень сложности должен быть у хореографии?')
    title.place( rely=0.1)
    selected = IntVar()
    rad1 = Radiobutton(window, text='низкий', value=1, variable=selected)
    rad2 = Radiobutton(window, text='высокий', value=2, variable=selected)
    rad1.place(relx=0.3, rely=0.3)
    rad2.place(relx=0.3, rely=0.35)

    next_question = Button(window, text="следующий вопросик", command=lambda: check2())
    next_question.place(relx=0.38, rely=0.5)


def girls_or_boys():
    def second_des():
        rad1.destroy()
        rad2.destroy()
        next_question.destroy()
        if selected.get() == 1:
            file_info = open('output.txt', "a")
            file_info.write('girls ')
            file_info.close()
            easy_or_hard()
        elif selected.get() == 2:
            file_info = open('output.txt', "a")
            file_info.write('boys ')
            file_info.close()
            easy_or_hard()
    def check2():
        if selected.get() != 1 and selected.get() != 2:
            messagebox.showwarning('Ошибка', 'Выбери')
            return
        else:
            second_des()
    title.configure(text='Какую хореографию обычно тебе нравится учить больше?')
    title.place(relx=0.08, rely=0.1)
    selected = IntVar()
    rad1 = Radiobutton(window, text='хореографию женских групп', value=1, variable=selected)
    rad2 = Radiobutton(window, text='хореографию мужских групп', value=2, variable=selected)
    rad1.place(relx=0.3, rely=0.3)
    rad2.place(relx=0.3, rely=0.35)
    next_question = Button(window, text="следующий вопросик", command=lambda: check2())
    next_question.place(relx=0.38, rely=0.5)


def check(description):
    if input_field.get() == '':
        messagebox.showwarning('Ошибка', 'Введи своё имя')
        return
    else:
        description.destroy()
        solo_or_team()


def solo_or_team():
    def first_des():
        def first_plus_des():
            file_info = open('output.txt', "a")
            file_info.write('team')
            file_info.write(str(selected2.get() + 1) + ' ')
            file_info.close()
            rad11.destroy()
            rad22.destroy()
            rad3.destroy()
            rad4.destroy()
            rad5.destroy()
            rad6.destroy()
            rad7.destroy()
            rad8.destroy()
            rad9.destroy()
            next_question1.destroy()
            girls_or_boys()
        rad1.destroy()
        rad2.destroy()
        next_question.destroy()
        if selected.get() == 1:
            file_info = open('output.txt', "a")
            file_info.write('solo ')
            file_info.close()
            girls_or_boys()
        elif selected.get() == 2:
            title.configure(text='Сколько в команде человек, включая тебя?')
            title.place(relx=0.2, rely=0.1)
            name_entry.destroy()
            next_question.destroy()
            input_field.destroy()
            btn.destroy()
            selected2 = IntVar()
            rad11 = Radiobutton(window, text='2', value=1, variable=selected2)
            rad22 = Radiobutton(window, text='3', value=2, variable=selected2)
            rad3 = Radiobutton(window, text='4', value=3, variable=selected2)
            rad4 = Radiobutton(window, text='5', value=4, variable=selected2)
            rad5 = Radiobutton(window, text='6', value=5, variable=selected2)
            rad6 = Radiobutton(window, text='7', value=6, variable=selected2)
            rad7 = Radiobutton(window, text='8', value=7, variable=selected2)
            rad8 = Radiobutton(window, text='9', value=8, variable=selected2)
            rad9 = Radiobutton(window, text='10+', value=9, variable=selected2)

            rad11.place(relx=0.3, rely=0.25)
            rad22.place(relx=0.3, rely=0.3)
            rad3.place(relx=0.3, rely=0.35)
            rad4.place(relx=0.3, rely=0.4)
            rad5.place(relx=0.3, rely=0.45)
            rad6.place(relx=0.3, rely=0.5)
            rad7.place(relx=0.3, rely=0.55)
            rad8.place(relx=0.3, rely=0.6)
            rad9.place(relx=0.3, rely=0.65)

            next_question1 = Button(window, text="следующий вопросик", command=first_plus_des)
            next_question1.place(relx=0.4, rely=0.8)
    def check2():
        if selected.get() != 1 and selected.get() != 2:
            messagebox.showwarning('Ошибка', 'Выбери')
            return
        else:
            first_des()
    title.configure(text='Ты учишь хореографию в одиночку или в команде?')
    title.place(relx=0.1, rely=0.1)
    name_entry.destroy()
    input_field.destroy()
    btn.destroy()
    selected = IntVar()
    rad1 = Radiobutton(window, text='в одиночку', value=1, variable=selected)
    rad2 = Radiobutton(window, text='в команде', value=2,  variable=selected)
    rad1.place(relx=0.3, rely=0.3)
    rad2.place(relx=0.3, rely=0.35)
    next_question = Button(window, text="следующий вопросик", command=lambda: check2())
    next_question.place(relx=0.38, rely=0.5)

window = Tk()
myColor = '#f2dff7'
window.title("dance prescription")
window.geometry("650x500")
window['background'] = myColor
window.minsize(width=650, height=500)
window.maxsize(width=650, height=500)

title = Label(window, text="Какую хореографию тебе выучить следующей?", bg=myColor, font=("Helvetica", 20))
title.place(relx=0.15, rely=0.1)

description = Label(window, text="Если ты занимаешься кавер-дэнсом, то тебе точно знакома дилемма о том,\n "
                                 "что ты не знаешь, какую хореографию выучить следующей. Хореографий в K-pop\n "
                                 "бесконечное множество, и это может сбивать с толку. Мы создали этот тест для того,\n "
                                 "чтобы избавить тебя от этой проблемы. В этом тесте 72 результата — 72 потенциальные\n"
                                 "хореографии, которые ты сможешь выучить. Отвечай на вопросы и получи хореографию,\n"
                                 "которая подходит именно тебе!\n", bg=myColor, font=("Helvetica", 12))
description.place(relx=0.1, rely=0.5)
name_entry = Label(window, text="Введи своё имя:", bg=myColor, font=("Helvetica", 12))
name_entry.place(relx=0.41, rely=0.2)
input_field = Entry(window, width=15)
input_field.place(relx=0.36, rely=0.3)
input_field.focus()
btn = Button(window, text="ввод", command = lambda: check(description))
btn.place(relx=0.6, rely=0.305)


window.mainloop()
