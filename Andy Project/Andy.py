import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser, filedialog,messagebox
import os

main_application = tk.Tk()
main_application.geometry("800x600")
main_application.title("Andy")
    
main_menu=tk.Menu()
    
new_icon = tk.PhotoImage(file="new.png")
open_icon = tk.PhotoImage(file="open.png")
save_icon = tk.PhotoImage(file="save.png")
save_as_icon = tk.PhotoImage(file="saves_as.png")
exit_icon = tk.PhotoImage(file="exit.png")
    
file = tk.Menu(main_menu,tearoff = False)
    
    
#Edit Menu icon
    
copy_icon = tk.PhotoImage(file="copy.png")
paste_icon = tk.PhotoImage(file="paste.png")
cut_icon = tk.PhotoImage(file="cut.png")
clear_icon = tk.PhotoImage(file="clear.png")
find_icon = tk.PhotoImage(file="find.png")
    
edit = tk.Menu(main_menu,tearoff = False)
    
tool_bar = tk.PhotoImage(file = "tool_bar.png")
status_bar = tk.PhotoImage(file = "status_bar.png")
    
view = tk.Menu(main_menu,tearoff = False)
    
#color image
light_theme = tk.PhotoImage(file = "lightblue.png")
light_plus_icon = tk.PhotoImage(file = "violet.png")
dark_theme = tk.PhotoImage(file = "blue.png")
red_theme = tk.PhotoImage(file = "red.png")
monokia_theme = tk.PhotoImage(file = "yellowgreen.png")
night_theme = tk.PhotoImage(file = "green.png")
    
color_theme = tk.Menu(main_menu,tearoff = False)

theme_choose=tk.StringVar()

#Color theme set
color_icons=(light_plus_icon,light_theme,dark_theme,red_theme,monokia_theme,night_theme)
    
color_dict = {
       'Light Default' :('#000000',"affffff"),
       'Light Plus' :('#474747','#e0e0e0'),
       'Dark' :('#c4c4c4','#2d2d2d'),
       'Red' :('#2d2d2d','#ffe8e8'),
       'Monokai' :('#d3b774','#474747'),
       'Night Blue' :('#ededed','#6b9dc2')
}
    
main_menu.add_cascade(label = "File",menu = file)
main_menu.add_cascade(label = "Edit",menu = edit)
main_menu.add_cascade(label = "View",menu = view)
main_menu.add_cascade(label = "Color Theme",menu = color_theme )
    
tool_bar_label = ttk.Label(main_application)
tool_bar_label.pack(side = tk.TOP,fill = tk.X)
    
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar_label,width = 30,textvariable = font_family,state = "readonly")
font_box["values"] = font_tuple
font_box.current(font_tuple.index("Arial"))
font_box.grid(row = 0,column = 0,padx = 5,pady=5)
    
#Size box
    
size_variable = tk.IntVar()
font_size = ttk.Combobox(tool_bar_label,width = 20,textvariable = size_variable,state ="readonly" )
font_size["values"] = tuple(range(8,100,2))
font_size.current(4)
font_size.grid(row = 0,column = 1,padx = 5 )
    
## bold button
bold_icon = tk.PhotoImage(file = "bold.png")
bold_btn = ttk.Button(tool_bar_label,image=bold_icon)
bold_btn.grid(row = 0,column = 2,padx = 5)

# italic button
italic_icon=tk.PhotoImage(file="Italy.jpg")
italic_btn=ttk.Button(tool_bar_label,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
    
##underline button
underline_icon=tk.PhotoImage(file="underline.png")
underline_btn=ttk.Button(tool_bar_label,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)
    
## font_color button
font_color_icon=tk.PhotoImage(file="font_color.png")
font_color_btn=ttk.Button(tool_bar_label,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)
    
##align left
align_left_icon=tk.PhotoImage(file="left_align.png")
align_left_btn=ttk.Button(tool_bar_label,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

##align center
align_center_icon=tk.PhotoImage(file="center_align.png")
align_center_btn=ttk.Button(tool_bar_label,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

##align right
align_right_icon=tk.PhotoImage(file="right_align.png")
align_right_btn=ttk.Button(tool_bar_label,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)


# text editor
text_editor = tk.Text(main_application)
text_editor.config(wrap="word",relief=tk.FLAT)

scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side = tk.RIGHT,fill = tk.Y)
text_editor.pack(fill = tk.BOTH,expand = True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

#Font family and function
font_now="Arial"
font_size_now=16

def change_font(main_application):
    global font_now
    font_now = font_family.get()
    text_editor.configure(font=(font_now,font_size_now))
    
def change_size(main_application):
    global font_size_now
    font_size_now = size_variable.get()
    text_editor.configure(font=(font_now,font_size_now))

    
font_box.bind("<<ComboboxSelected>>",change_font)    
font_size.bind("<<ComboboxSelected>>",change_size)


#bold function

def bold_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["weight"] == 'normal':
        text_editor.configure(font=(font_now,font_size_now,"bold"))
    if text_get.actual()["weight"] == 'bold':
        text_editor.configure(font=(font_now,font_size_now,"normal"))
        
        
        
bold_btn.configure(command=bold_fun)        

def Italic_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["slant"] == 'roman':
        text_editor.configure(font=(font_now,font_size_now,"italic"))
    if text_get.actual()["slant"] == 'italic':
        text_editor.configure(font=(font_now,font_size_now,"roman"))
        
italic_btn.configure(command=Italic_fun)   


def under_line_fun():
    text_get=tk.font.Font(font=text_editor["font"])
    if text_get.actual()["underline"] == 0:
        text_editor.configure(font=(font_now,font_size_now,"underline"))
    if text_get.actual()["underline"] == 1:
        text_editor.configure(font=(font_now,font_size_now,"normal"))
        
underline_btn.configure(command=under_line_fun)   

def Color_choose():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=Color_choose)

def align_left():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("left",justify = tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"left")
    
align_left_btn.configure(command = align_left) 

def align_center():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("center",justify = tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"center")
    
align_center_btn.configure(command = align_center) 

def align_right():
    text_get_all = text_editor.get(1.0,"end")
    text_editor.tag_config("right",justify = tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_get_all,"right")
    
align_right_btn.configure(command = align_right)    



#status bar word and character count

status_bars = ttk.Label(main_application,text = "Status bar")
status_bars.pack(side=tk.BOTTOM)

text_change = False

def change_word(event=None):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        word = len(text_editor.get(1.0,"end-1c").split())
        chararcter = len(text_editor.get(1.0,"end-1c").replace(" ",""))
        status_bars.config(text = f"character :{chararcter} word :{word}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change_word)    
    
#color theme function 


#light_theme = tk.PhotoImage(file = "lightblue.png")
#light_plus_icon = tk.PhotoImage(file = "violet.png")
#dark_theme = tk.PhotoImage(file = "blue.png")
#red_theme = tk.PhotoImage(file = "red.png")
###color_theme = tk.Menu(main_menu,tearoff = False)

#theme_choose=tk.stringVar()

#Color theme set
#color_icons=(light_theme,light_plus_icon,dark_theme,red_theme,monokia_theme,night_theme)
    
#color_dict = {
#       'lightblue' :('#000000',"affffff"),
#       'Violet' :('#a116f2','#e0e0e0'),
#       'Blue' :('#324ec9','#2d2d2d'),
#      'Red' :('#de3121','#ffe8e8'),
#       'Yellow Green' :('#b6d629','#474747'),
#       'Green' :('#329c2a','#6b9dc2')
#}

def change_theme():
    get_theme = theme_choose.get()
    colour_tuple = color_dict.get(get_theme)
    fg_color,bg_color = colour_tuple[0].colour_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
    
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i,image = color_icons[count],compound = tk.LEFT,command = change_theme)
    count +=1
    
#View menu


#tool_bar and status_bar hide


#tool_bar_label = ttk.Label(main_application)
#tool_bar_label.pack(side = tk.TOP,fill = tk.X)

#status_bars = ttk.Label(main_application,text = "Status bar")
#status_bars.pack(side=tk.BOTTOM)

show_status_bar=tk.BooleanVar()
show_status_bar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar_label.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bars.pack_forget()
        tool_bar_label.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bars.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_status_bar
    if show_status_bar:
        status_bars.pack_forget()
        show_status_bar=False
    else:
        status_bars.pack(side=tk.BOTTOM)
        show_status_bar=True

view.add_checkbutton(label = "Tool Bar",onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label = "Status Bar",onvalue=True,offvalue=0,variable=show_status_bar,image=status_bar,compound=tk.LEFT,command=hide_statusbar)
    
#Edit menu

edit.add_command(label="Copy",image = copy_icon,compound = tk.LEFT,accelerator = "Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label="Paste",image = paste_icon,compound = tk.LEFT,accelerator = "Ctrl+P",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label="Cut",image = cut_icon,compound = tk.LEFT,accelerator = "Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label="Clear",image = clear_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tk.END))

def find_fun(event=None):
    
    def find():
        word=find_input.get()
        text_editor.tag_remove("match","1.0",tk.END)
        matches=0
        if word:
            start_pos="1.0"
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add("match",start_pos,end_pos)
                matches += 1
                start_pos=end_pos
                text_editor.tag_config('match',foreground="red",background="blue")
        
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
        
        
    
    find_popup=tk.Toplevel()
    find_popup.geometry("450x200")
    find_popup.title("find word")
    find_popup.resizable(0,0)
    
    #frame for find
    find_fram=ttk.Labelframe(find_popup,text="Find and Replace word")
    find_fram.pack(pady=20)
    
    #label
    text_find=ttk.Label(find_fram,text="Find")
    text_replace=ttk.Label(find_fram,text="Replace")
    
    #entrybox
    find_input=ttk.Entry(find_fram,width=30)
    replace_input=ttk.Entry(find_fram,width=30)
    
    #button
    find_button=ttk.Button(find_fram,text="find",command=find)
    replace_button=ttk.Button(find_fram,text="Replace",command=replace)
    
    #text label grid
    text_find.grid(row=0,column=0,padx=4,pady=4)
    text_replace.grid(row=1,column=0,padx=4,pady=4)
    
    #entry grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    
    #button grid
    find_button.grid(row=2,column=0,padx=8,pady=4)
    replace_button.grid(row=2,column=1,padx=8,pady=4)
    
edit.add_command(label="Find",image = find_icon,compound = tk.LEFT,accelerator = "Ctrl+F",command=find_fun)
    
#File menu

text_url = " "

def new_file(event = None):
    global text_url
    text_editor.delete(1.0,tk.END)


file.add_command(label="New",image = new_icon,compound = tk.LEFT,accelerator = "Ctrl+N",command=new_file)


def open_file(event = None):
    global text_url
    text_url = filedialog.askopenfilename(initialdir = os.getcwd(),title="select file",filetypes=(("Text file","*.txt"),("All files","*.*"))) 
    try:
        with open(text_url,"r") as for_read:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,for_read.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(text_url))
    
file.add_command(label="Open",image = open_icon,compound = tk.LEFT,accelerator = "Ctrl+O",command=open_file)

def save_file(event =  None):
    global text_url
    try:
        if text_url:
            content = str(text_editor.get(1.0,tk.END))
            with open(text_url,"w",encoding="utf-8") as for_read:
                for_read.write(content)
        else:
            text_url = filedialog.asksaveasfile(mode ="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
            content2 = text_editor.get(1.0,tk.END)
            text_url.write(content2)
            text_url.close()
    except:
        return
            
file.add_command(label="Save",image = save_icon,compound = tk.LEFT,accelerator = "Ctrl+S",command= save_file)

def Save_as_file(event=None):
    global text_url
    try:
        content=text_editor.get(1.0,tk.END)
        text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
        text_url.write(content)
        text_url.close()
    except:
        return
        
file.add_command(label="Save as",image = save_as_icon,compound = tk.LEFT,accelerator = "Ctrl+Alt+S",command=Save_as_file)

def Exit_fun(event=None):
    global text_url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel("warning","Do you want to save this file")
            if mbox is True:
                if text_url:
                    content=text_editor.get(1.0,tk.END)
                    with open(text_url,"w",encoding="utf-8") as for_read:
                        for_read.write(content)
                        main_application.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    text_url=filedialog.asksaveasfile(mode="w",defaultextension="txt",filetypes=(("Text file","*.txt"),("All files","*.*")))
                    text_url.write(content2)
                    text_url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except: 
        return
                    
file.add_command(label="Exit",image = exit_icon,compound = tk.LEFT,accelerator = "Ctrl+",command=Exit_fun)
    
main_application.config(menu = main_menu)
    
main_application.mainloop()