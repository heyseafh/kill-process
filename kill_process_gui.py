#-*- coding:utf-8 -*-
# @Author:heysea
# @Time:2021/7/15

from tkinter import * 	#python3.x这个模块内置了
import tkinter.filedialog	#操作通用对话框
import tkinter.messagebox
from tkinter import scrolledtext	#python 3.x用这个方式导入模块(带有滚动条的输入框)
import os

def kill_process():
	application_name = ent_name.get()	#获得从输入框输入的要杀掉的进程名称
	# application_name = input("input process name：") 
	# application_name = 'Motrix'
	if not application_name:
		tkinter.messagebox.showerror('警告','请输入要杀掉的进程名')
		return
	listBox.delete(0,END)
	command = "tasklist | findstr {}".format(application_name)
	kill_command = "taskkill /t /f /im "
	result = os.popen(command,'r')
	result_print = result.read()
	if len(result_print) == 0:
		result = "{}相关进程不存在".format(application_name)
		listBox.insert(END,result)
		# print("{}相关进程不存在".format(application_name))
	else:
		# print(result_print)
		listBox.insert(END,result_print)
	pid = result_print.split(' ')
	pid = [i for i in pid if(len(str(i)) !=0 )] #去掉list中的空元素，那么第二个元素就一定是pid
	# print(pid)
	try:
		for i in range(1,len(pid)+1,5):
			kill_command_x = kill_command + str(pid[i])
			kill_result = os.popen(kill_command_x,'r')
			kill_result_print = kill_result.read()
			# print(kill_result_print)
			if len(kill_result_print) == 0:
				result = "{}相关进程已经被删除".format(application_name)
				listBox.insert(END,result)
				# print("{}相关进程已经被删除".format(application_name))
			else:
				listBox.insert(END,kill_result_print)
				# print(kill_result_print)
	except:
		result_end = "kill process{} end".format(application_name)
		listBox.insert(END,result_end)
		 # print("kill process {} end".format(application_name))


if __name__ == '__main__':
	
	root = Tk()	#创建窗口（创建tkinter对象）
	root.title("kill process")	#设置gui名称
	root.geometry("+600+300")	#设置窗口大小(**x**),设置窗口位置第一个加号后的是横分辨率，第二个是纵分辨率
	Label(root,text='请输入要kill的进程名').grid()	#设置提示词grid()的横纵坐标没设置就是0,0
	ent_name = Entry(root)	#创建单行文本输入框
	ent_name.grid(row=0,column=1)	#显示/布局 输入框 pack 布局方式不能同grid布局方式一起用，row设置横坐标，column设置纵坐标
	btn = Button(root,text='执行',command=kill_process)	#添加执行按钮并命名为执行
	btn.grid(row=0,column=2)
	listBox = Listbox(root,width=60)
	listBox.grid(row=1,columnspan=6)	#合并单元格，因为grid()是excel布局
	root.resizable(width=False, height=False)	#设置窗口是否可变长、宽，True：可变，False：不可变
	root.mainloop()	#显示窗口
