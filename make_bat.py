import os
print "This is a simple program that creates another batch program which makes the python programs easily accessible."
print "Enter \"null\"(empty) to exit."
files= []
while True:
    a = str(raw_input("Your python file name? *.py "))
    if a =="":
        break
    if a =="help":
        pass
    file_name = a
    files.append(a)
    write_msg = "\nif \"%~1\"==\"{0}\" (\n\t goto {0})\n".format(file_name)
    with open('temp_1.txt','a+') as file_1:
        file_1.write(write_msg)
        file_1.close()
    msg_towrite= "\n:{0}\npython {0}.py\ngoto end\n".format(file_name)
    with open('temp_2.txt','a+') as file_2:
        file_2.write(msg_towrite)
        file_2.close
with open('temp_1.txt','r') as fil_1, open('temp_2.txt','r') as fil_2, open('p.bat','a+') as fil_3:
    fil_3.write("@echo off\nif \"%~1\"==\"\" (\n\tgoto blank)")
    add_help = "\nif \"%~1\"==\"help\" (\n\tgoto help)\n"
    add_files ="\nif \"%~1\"==\"files\" (\n\tgoto files)\ngoto end"
    add_help_func ="\n:help\n echo Type the file name without extension to open the python program\np [file_name]\nset /p= \ngoto end\n"
    add_files_func ="\n:files\n echo Files:\n"
    for file_ in files:
        add_files_func += "echo " + file_ + "\n"
    add_files_func += "goto end\n"
    add_blank_func = "\n:blank\ngoto help\n"
    fil_3.write(fil_1.read()+add_help+add_files+add_files_func+add_blank_func+add_help_func+fil_2.read())
    fil_3.write("\n:end\n@echo off")
os.system('del temp_1.txt temp_2.txt')
