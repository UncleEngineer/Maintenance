import os
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import Notebook
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import sqlite3
import tkinter.font as tkFont
#from report14 import *
# --------------------
# matplotlib on tk
global allpartlist
#import matplotlib as mpl
import tkinter as tk
from tkinter import ttk
#import matplotlib.backends.tkagg as tkagg
#from matplotlib.backends.backend_agg import FigureCanvasAgg

# --------------Graph plot-------------------
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm, cm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, TableStyle, Image
from reportlab.lib import colors
from reportlab.lib.pagesizes import  A4, landscape
#Add font
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import subprocess

class Report(object):
    def __init__ (self):
        self.width, self.height = A4

    def run(self, pdfname, data_inform2, data_som, data_tool):
        #crete main canvas
        self.c = canvas.Canvas(pdfname, pagesize=A4)

        #call
        self.drawText(data_infrom2, data_som, data_tool)
        self.drawTable()

        #save canvas to pdf
        self.c.save()
        print("create " + pdfname)
#--------------------------------------------------------------------------------------------------------------------------
    def drawText(self, data_infrom, data_som, data_tool):
        #inifont
        pdfmetrics.registerFont(TTFont('nomalFont', 'THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('boldFont', 'THSarabunNew Bold.ttf'))
        styles=getSampleStyleSheet()
        styleN = styles["Normal"]
        styleT = styles["Title"]

        #top
        ptext = Paragraph("<font size=18 name='boldFont'>HCI-QF-OPE-02-06 Rev.02</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 60 *mm, 283 *mm)
        ptext = Paragraph("<font size=18 name='boldFont'>บริษัท ไฮแคร์อินเตอร์เนชั่นแนล จำกัด</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -50 *mm, 268 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>แผนก ซ่อมบำรุง/ซ่อมบำรุงกลาง/ซ่อมบำรุง Line ผลิต</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -50 *mm, 261 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>ส่วนงานซ่อมบำรุง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 50 *mm, 268 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>ใบแจ้งซ่อม/ใบสั่งทำ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 50 *mm, 261 *mm)

        #สำหรับพนักงานแจ้งซ่อม
        ptext = Paragraph("<font size=16 name='boldFont'>สำหรับพนักงานแจ้งซ่อม</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 253 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>แผนก : " + data_infrom[0] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -70 *mm, 247 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>ลักษณะงาน : [ " + data_infrom[1][0] + " ]ทำใหม่  [ "+ data_infrom[1][1] + " ]ซ่อม  [ "+ data_infrom[1][2] + " ]เพิ่มเติม  [ "+ data_infrom[1][3] + " ]อื่นๆ </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 40 *mm, 247 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>ความต้องการ : [ " + data_infrom[2][0] + " ]ด่วน  [ "+ data_infrom[2][1] + " ]ปกติ  [ "+ data_infrom[2][2] + " ]รอได้  </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 32 *mm, 241 *mm)

        ptext = Paragraph("<font size=16 name='nomalFont'>วันที่ต้องการ : " + data_infrom[3] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 28 *mm, 235 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>ชื่อเครื่องจักร : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -80 *mm, 225 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[4] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -40 *mm, 225 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>บริเวณที่เสีย : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -80 *mm, 219 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[5] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -40 *mm, 219 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>วัน/เดือน/ปี</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 35 *mm, 225 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[6] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 35 *mm, 219 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>เวลาที่แจ้ง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 80 *mm, 225 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[7] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 80 *mm, 219 *mm)

        ptext = Paragraph("<font size=18 name='boldFont'>อาการ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -76 *mm, 208 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[8] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 17 *mm, 212 *mm)

        ptext = Paragraph("<font size=16 name='nomalFont'>ลงชื่อ : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -80 *mm, 195 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[9] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -50 *mm, 195 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>ผู้แจ้ง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -20 *mm, 195 *mm)

        ptext = Paragraph("<font size=16 name='nomalFont'>ลงชื่อ : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 20 *mm, 195 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[10] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 50 *mm, 195 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>ผู้รับแจ้ง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 80 *mm, 195 *mm)

        ptext = Paragraph("<font size=16 name='nomalFont'>" + data_infrom[11] +"   เวลาที่รับแจ้ง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 50 *mm, 190 *mm)

        #ส่วนสำหรับพนักงานซ่อมบำรุง
        ptext = Paragraph("<font size=16 name='boldFont'>ส่วนสำหรับพนักงานซ่อมบำรุง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -70 *mm, 185 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>สาเหตุที่เสีย</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -76 *mm, 172 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[0] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 17 *mm, 176 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>รายละเอียดการตรวจซ่อม</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -77 *mm, 159 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[1] +"</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 17 *mm, 162 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>อุปกรณ์ที่ใช้</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -76 *mm, 130 *mm)
        ptext = Paragraph("<font size=14 name='boldFont'>ลำดับ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -54 *mm, 148 *mm)
        ptext = Paragraph("<font size=14 name='boldFont'>รายการ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 10 *mm, 148 *mm)
        ptext = Paragraph("<font size=14 name='boldFont'>จำนวน/หน่วย</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 80 *mm, 148 *mm)

        s_line = 141
        for i in range(len(data_tool)):
            ptext = Paragraph("<font size=14 name='nomalFont'>" + data_tool[i][0] +"</font>", styleT)
            ptext.wrapOn(self.c, self.width, self.height)
            ptext.drawOn(self.c, -54 *mm, s_line *mm)
            ptext = Paragraph("<font size=14 name='nomalFont'>" + data_tool[i][1] +"</font>", styleT)
            ptext.wrapOn(self.c, self.width, self.height)
            ptext.drawOn(self.c, 10 *mm, s_line *mm)
            ptext = Paragraph("<font size=14 name='nomalFont'>" + data_tool[i][2] +"</font>", styleT)
            ptext.wrapOn(self.c, self.width, self.height)
            ptext.drawOn(self.c, 80 *mm, s_line *mm)
            s_line -= 7

        ptext = Paragraph("<font size=14 name='boldFont'>อุปกรณ์ที่นำมาเปลี่ยน : [ " + data_som[2][0] + " ]เหมือนเดิม  [ "+ data_som[2][1] + " ]เปลี่ยนแปลงไปจาก</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -50 *mm, 95 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[3] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 85 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>วัน/เดือน/ปี ที่ซ่อมเสร็จ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -76 *mm, 70 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>เวลาที่ใช้</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -30 *mm, 70 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[4] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 63 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>จาก</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -45 *mm, 63 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[5] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -45 *mm, 56 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>ถึง</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -15 *mm, 63 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[6] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -15 *mm, 56 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>[" + data_som[7] + "] Break Down จาก " + data_som[8] + " ถึง " + data_som[9] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -60 *mm, 49 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>ผู้รายงาน : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 20 *mm, 63 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[10] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 60 *mm, 63 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>ผู้ตรวจรับงาน : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 23 *mm, 56 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[11] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 60 *mm, 56 *mm)

        ptext = Paragraph("<font size=14 name='boldFont'>ผู้ตรวจสอบ : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 22 *mm, 49 *mm)
        ptext = Paragraph("<font size=14 name='nomalFont'>" + data_som[12] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 60 *mm, 49 *mm)
#--------------------------------------------------------------------------------------------------------------------------
    def drawTable(self):
        # 1 line = 20
        #top
        self.c.line(360,820,560,820)
        self.c.line(360,800,560,800)
        self.c.line(360,820,360,800)
        self.c.line(560,820,560,800)
        
        #ชื่อบริษัท
        self.c.line(30,780,560,780)
        self.c.line(30,760,560,760)
        self.c.line(30,740,560,740)
        self.c.line(295,780,295,740)

        #ชื่อเครื่องจักร
        self.c.line(30,660,560,660)
        self.c.line(295,640,560,640)
        self.c.line(30,620,560,620)
        self.c.line(295,660,295,620)
        self.c.line(480,660,480,620)

        #อาการ
        self.c.line(30,580,560,580)
        self.c.line(130,600,560,600)
        self.c.line(130,620,130,580)

        #สาเหตุที่เสีย
        self.c.line(30,520,560,520)
        self.c.line(130,500,560,500)
        self.c.line(30,480,560,480)
        self.c.line(130,520,130,480)

        #รายละเอียดการตรวจซ่อม
        self.c.line(30,480,560,480)
        self.c.line(130,460,560,460)
        self.c.line(30,440,560,440)
        self.c.line(130,480,130,440)

        #อุปกรณ์ที่ใช้
        self.c.line(30,440,560,440)
        self.c.line(130,420,560,420)
        self.c.line(130,400,560,400)
        self.c.line(130,380,560,380)
        self.c.line(130,360,560,360)
        self.c.line(130,340,560,340)
        self.c.line(130,320,560,320)
        self.c.line(30,300,560,300)
        self.c.line(130,440,130,300)
        self.c.line(160,440,160,300)
        self.c.line(480,440,480,300)

        #อุปกร์ที่นำมาเปลี่ยน
        self.c.line(30,220,560,220)

        #bot
        self.c.line(295,220,295,140)
        self.c.line(30,160,295,160)
        self.c.line(130,220,130,160)
        self.c.line(130,200,295,200)
        self.c.line(130,180,295,180)
        self.c.line(212.5,200,212.5,160)
        self.c.line(30,140,560,140)

        #เส้นหน้าหลัง
        self.c.line(30,780,30,140)
        self.c.line(560,780,560,140)
#--------------------------------------------------------------------------------------------------------------------------
#############################################################################


def genreport():

	try:
		ts = TVRecord.selection()
		x = TVRecord.item(ts)
		print(x['values'][0])
		idsearch = x['values'][0]
		
		
	except:
		pass	

	with conn:
		c.execute("SELECT * FROM record_fix WHERE ID = ?",([idsearch]))
		print('############################')
		rawdata = c.fetchall()

	global data_infrom2
	global data_som
	global data_tool

	if rawdata[0][3] == 'ทำใหม่':
		typework = ['/',' ',' ',' ',]
	elif rawdata[0][3] == 'ซ่อม':
		typework = [' ','/',' ',' ',]
	elif rawdata[0][3] == 'เพิ่มเติม':
		typework = [' ',' ','/',' ',]
	else:
		typework = [' ',' ',' ','/',]

	if rawdata[0][4] == 'ด่วน':
		typework2 = ['/',' ',' ']
	elif rawdata[0][4] == 'ปกติ':
		typework2 = [' ','/',' ']
	else:
		typework2 = [' ',' ','/']

	if rawdata[0][15] == 'เหมือนเดิม':
		typework3 = ['/',' ']
	else:
		typework3 = [' ','/']


	data_infrom2 = [rawdata[0][2],typework,typework2,rawdata[0][5],rawdata[0][6],rawdata[0][7],rawdata[0][9],rawdata[0][10],rawdata[0][8],rawdata[0][1],rawdata[0][11],rawdata[0][12]]
	data_som = [rawdata[0][13],rawdata[0][14],typework3,rawdata[0][16],rawdata[0][17],rawdata[0][18],rawdata[0][19],'/',rawdata[0][20],rawdata[0][21],rawdata[0][22],rawdata[0][23],rawdata[0][24]]
	

	try:
		partlist0 = rawdata[0][-1].split(',')
		data_tool = []
		print("PARTLIST 0: ",partlist0)
		for j,i in enumerate(partlist0):
			
			data11 = [str(j+1)]

			data2 = i.split('+')
			data11.extend(data2)
			data_tool.append(data11)
		print("ALLPARTLISTSEND",data_tool)
	except:
		data_tool = [['1','ลูกปืน','1 ตลับ'],['2','สายไฟ','5 เมตร'],['3','ไขควง','6 ด้าม'],['4','เคเบิลไทร์','1 ถุง']]

		

	

	#data_infrom2 = ['Maintenance',['/',' ',' ',' ',],[' ',' ','/'],'20-08-2018','Roller Owen','Bearing','15-07-2018','20.30','ลูกปืนแตก','สมชาย','ผู้จัดการ','15.00']
	#data_som = ['ขนาดการบำรุงรักษา','ตรวจซ่อมอย่างละเอียด',[' ','/'],'เปลี่ยนลูกปืน','2018-07-01','12.00','15.00','/','18.00','20.50','นาย ผู้รายงาน','นาย ผู้ตรวจรับ','นางสาว ผู้ตรวจสอบ']
	#data_tool = [['1','ลูกปืน','1 ตลับ'],['2','สายไฟ','5 เมตร'],['3','ไขควง','6 ด้าม'],['4','เคเบิลไทร์','1 ถุง']]

	dt1 = datetime.now().strftime('%Y-%m-%d %H%M%S')
	reportname = 'Breakdown-'+dt1+'.pdf'

	Report().run(reportname, data_infrom2, data_som, data_tool)

	messagebox.showinfo('Report Exporting',reportname + ' was Exported')
	subprocess.Popen(reportname,shell=True)



class linegraph:

	def __init__(self,gui,listx,listy,width,height,row,column):
		self.x = listx
		self.y = listy
		self.gui = gui
		self.width = width
		self.height = height
		self.row = row
		self.column = column
		self.plotgraphline()

	def draw_figure(self,canvas, figure, loc=(0, 0)):

	    figure_canvas_agg = FigureCanvasAgg(figure)
	    figure_canvas_agg.draw()
	    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
	    figure_w, figure_h = int(figure_w), int(figure_h)
	    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

	    # Position: convert from top-left anchor to center anchor
	    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

	    # Unfortunately, there's no accessor for the pointer to the native renderer
	    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

	    return photo
	def plotgraphline(self):
		canvas = tk.Canvas(self.gui, width=self.width, height=self.height)
		canvas.grid(row=self.row,column=self.column)

		# b1 = ttk.Button(self.gui, text='Update')
		# b1.grid(row=1,column=0, sticky='E')

		X = [0,1,2,3,4,5]# self.x
		Y = [100,200,400,300,500,100] #self.y

		fig = mpl.figure.Figure(figsize=(4, 3))
		ax = fig.add_axes([0, 0, 1, 1])
		#--------------TYPE GRAPH-----------------
		ax.bar(X, Y)

		count = len(X)
		for i in range(count):
			ax.text(X[i],Y[i],str(Y[i]))

		# Keep this handle alive, or else figure will disappear
		fig_x, fig_y = 10, 10
		fig_photo = self.draw_figure(canvas, fig, loc=(fig_x, fig_y))
		fig_w, fig_h = fig_photo.width(), fig_photo.height()

		# Add more elements to the canvas, potentially on top of the figure
		# canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
		canvas.create_text(200, 50, text="Zero-crossing", anchor="s")


# -----------------------------Class Template-----------------------------
class BT:

	def __init__(self,gui,text,cm,rw,cl):
		self.text = text
		self.gui = gui
		self.cm = cm
		self.rw = rw
		self.cl = cl
		self.BT1()

	def BT1(self):
		B = ttk.Button(self.gui,text=self.text,command=eval(self.cm))
		B.grid(row=self.rw, column=self.cl,padx=5,pady=5,ipadx=10,ipady=10)


class LB:

	def __init__(self,gui,text,rw,cl,st):
		self.text = text
		self.gui = gui
		self.text = text
		self.rw = rw
		self.cl = cl
		self.st = st
		self.LB1()

	def LB1(self):
		L = ttk.Label(self.gui,text=self.text,font=('TH Sarabun New',13))
		L.grid(row=self.rw, column=self.cl,padx=5,pady=5,sticky=self.st)


class ET:

	def __init__(self,gui,textv,rw,cl,st):
		self.gui = gui
		self.text = textv
		self.rw = rw
		self.cl = cl
		self.st = st
		self.ET1()

	def ET1(self):
		self.E = ttk.Entry(self.gui,textvariable=self.text,font=('TH Sarabun New',15),width=22)
		self.E.grid(row=self.rw, column=self.cl,padx=5,pady=5,sticky=self.st)

	def focus1(self):
		self.E.focus()


class CB:

	def __init__(self,gui,itemlist,rw,cl,st):
		self.gui = gui
		self.itemlist = itemlist
		self.rw = rw
		self.cl = cl
		self.st = st
		self.sp_type = None
		self.CB1()

	def CB1(self):
		#SPAD_type = ['อะไหล่','วัสดุสิ้นเปลือง']
		combofont=('TH Sarabun New', '15')
		GUI.option_add('*TCombobox*Listbox.font', combofont)

		self.sp_type = ttk.Combobox(self.gui, values = self.itemlist, font=('TH Sarabun New', 15))
		self.sp_type.set(self.itemlist[0])
		self.sp_type.grid(row=self.rw, column=self.cl,padx=5,pady=5,sticky=self.st)

	def gets(self):
		self.sp_type.get()


# -----------------------------Database-----------------------------
global conn
global c

dbname = 'DB-Stock.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

# -----------------------------Create Table------------------------------
c.execute(""" CREATE TABLE IF NOT EXISTS record_fix (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				rec_requestor text,
				rec_department text,
				rec_cate text,
				rec_imp text,
				rec_req_date text,
				rec_machine text,
				rec_area text,
				rec_problem text,
				rec_broke_date text,
				rec_broke_time text,
				rec_recorder text,
				rec_record_time text,
				rec_cause text,
				rec_fix_detail text,
				rec_part_c text,
				rec_part_change_detail text,
				rec_finish_date text,
				rec_use_begin_time text,
				rec_use_end_time text,
				rec_break_begin_time text,
				rec_break_end_time text,
				rec_reporter text,
				rec_checker text,
				rec_manager text,
				rec_partlist text

	      )	""")


c.execute("""CREATE TABLE IF NOT EXISTS partlist_list (

			ID INTEGER PRIMARY KEY AUTOINCREMENT ,
			 pr_name text,
			 pr_quantity integer
			 			
			)""")


c.execute(""" CREATE TABLE IF NOT EXISTS department (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				dep_code text,
				dep_name text

	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS linepd (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				linepd_code text,
				linepd_name text

	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS machine (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				machine_code text,
				machine_line text,
				machine_name text,
				machine_detail text,
				machine_installdate text
	      )	""")


c.execute(""" CREATE TABLE IF NOT EXISTS partlist (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				partlist_code text,
				partlist_name text,
				partlist_model text,
				partlist_price real,
				partlist_quantity integer,
				partlist_machine text,
				partlist_supplier text
	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS breakdown (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				breakdown_code text,
				breakdown_title text,
				breakdown_department text,
				breakdown_machine text,
				breakdown_partlist text,
				breakdown_cost real,
				breakdown_request text,
				breakdown_responsible text,
				breakdown_date text
	      )	""")


c.execute(""" CREATE TABLE IF NOT EXISTS preventive (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				preventive_code text,
				preventive_title text,
				preventive_department text,
				preventive_machine text,
				preventive_partlist text,
				preventive_cost real,
				preventive_responsible text,
				preventive_date text
	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS officer (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				officer_code text,
				officer_name text,
				officer_department text
			
	      )	""")


# ----------------------GUI----------------------------

GUI = Tk()
GUI.state('zoomed')
# GUI.attributes('-fullscreen', True)
# w, h = GUI.winfo_screenwidth(), GUI.winfo_screenheight()
# GUI.geometry("%dx%d+0+0" % (w, h))
GUI.geometry('1366x730+30+30')
GUI.title('Uncle Engineer')

# -------------CONFIG FONT TAB,COMBO,BUTTON,TREEVIEW------------------
f = tkFont.Font(family='TH Sarabun New', size=15)
s = ttk.Style()
s.configure('.', font=f)
combofont=('TH Sarabun New', '15')
GUI.option_add('*TCombobox*Listbox.font', combofont)
s = ttk.Style()
s.configure('my.TButton', font=('TH Sarabun New', 15))
style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))


def tab():
	global Tab
	global F0
	global F1
	global F2
	global F3
	global F4
	global F5
	global F6
	global F7
	global F8
	Tab = Notebook(GUI, height=730)
	F0 = Frame(Tab, width=200, height=500)
	F1 = Frame(Tab, width=200, height=500)
	F2 = Frame(Tab, width=200, height=500)
	F3 = Frame(Tab, width=200, height=500)
	F4 = Frame(Tab, width=200, height=500)
	F5 = Frame(Tab, width=200, height=500)
	F6 = Frame(Tab, width=200, height=500)
	F7 = Frame(Tab, width=200, height=500)
	F8 = Frame(Tab, width=200, height=500)
	# font=('TH Sarabun New',20)
	Tab.add(F8, text='บันทึกการซ่อมบำรุง')
	Tab.add(F0, text='ซ่อมบำรุงเชิงป้องกัน')
	Tab.add(F1, text='ซ่อมด่วน')
	Tab.add(F2, text='เจ้าหน้าที่')
	Tab.add(F3, text='แผนก')
	Tab.add(F4, text='ไลน์ผลิต')
	Tab.add(F5, text='เครื่องจักร')
	Tab.add(F6, text='อะไหล่')
	#Tab.add(F7, text='สรุป')
	Tab.pack(fill=BOTH, padx=10, pady=10)


tab()


# ------------SUB TAB-------------
TabF8 = Notebook(F8, height=730)

F81 = Frame(TabF8, width=700, height=730)
F82 = Frame(TabF8, width=700, height=730)

TabF8.add(F82, text='รายงาน')
TabF8.add(F81, text='บันทึกรายการ')
TabF8.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF0 = Notebook(F0, height=700)

F01 = Frame(TabF0, width=200, height=500)
F02 = Frame(TabF0, width=200, height=500)

TabF0.add(F02, text='รายการ')
TabF0.add(F01, text='บันทึกรายการ')
TabF0.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF1 = Notebook(F1, height=700)

F11 = Frame(TabF1, width=200, height=500)
F12 = Frame(TabF1, width=200, height=500)

TabF1.add(F12, text='รายการ')
TabF1.add(F11, text='บันทึกรายการ')
TabF1.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF2 = Notebook(F2, height=700)

F21 = Frame(TabF2, width=200, height=500)
F22 = Frame(TabF2, width=200, height=500)

TabF2.add(F22, text='รายการ')
TabF2.add(F21, text='บันทึกรายการ')
TabF2.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF3 = Notebook(F3, height=700)

F31 = Frame(TabF3, width=200, height=500)
F32 = Frame(TabF3, width=200, height=500)

TabF3.add(F32, text='รายการ')
TabF3.add(F31, text='บันทึกรายการ')
TabF3.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF4 = Notebook(F4, height=700)

F41 = Frame(TabF4, width=200, height=500)
F42 = Frame(TabF4, width=200, height=500)

TabF4.add(F42, text='รายการ')
TabF4.add(F41, text='บันทึกรายการ')
TabF4.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF5 = Notebook(F5, height=700)

F51 = Frame(TabF5, width=200, height=500)
F52 = Frame(TabF5, width=200, height=500)

TabF5.add(F52, text='รายการ')
TabF5.add(F51, text='บันทึกรายการ')
TabF5.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------
TabF6 = Notebook(F6, height=700)

F61 = Frame(TabF6, width=200, height=500)
F62 = Frame(TabF6, width=200, height=500)

TabF6.add(F62, text='รายการ')
TabF6.add(F61, text='บันทึกรายการ')
TabF6.pack(fill=BOTH, padx=10, pady=10)
# --------------------------------------------


# ---------------GET DATA FROM DATABASE TO LIST BOX---------------

# dep = ['Maintenance','Production']
dep = []
global prev_department
def getdepartment():
	global dep
	dep = []
	try:
		with conn:
			c.execute("SELECT dep_name FROM department")
			deps = c.fetchall()

		for i in deps:
			dep.append(i[0])

		prev_department = ttk.Combobox(F01, values = dep, font=('TH Sarabun New', 15))
		prev_department.set('Department')
		prev_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')
		break_department = ttk.Combobox(F11, values = dep, font=('TH Sarabun New', 15))
		break_department.set('Department')
		break_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')
		off_department = ttk.Combobox(F21, values = dep, font=('TH Sarabun New', 15))
		off_department.set('Department')
		off_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')
		rec_department = ttk.Combobox(LBF1, values = dep, font=('TH Sarabun New', 15))
		rec_department.set('ระบุแผนก')
		rec_department.grid(row=1, column=1,padx=5,pady=5, sticky='w')

	except:
		pass


getdepartment()
print(dep)

# mach = ['Machine','Production']
mach = []
global prev_machine


def getmachine():
	global mach
	mach = []
	try:
		with conn:
			c.execute("SELECT machine_name FROM machine")
			machs = c.fetchall()

		for i in machs:
			mach.append(i[0])

		prev_machine = ttk.Combobox(F01, values = mach, font=('TH Sarabun New', 15))
		prev_machine.set('Machine')
		prev_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')
		break_machine = ttk.Combobox(F11, values = mach, font=('TH Sarabun New', 15))
		break_machine.set('Machine')
		break_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')
		part_mach = ttk.Combobox(F61, values = mach, font=('TH Sarabun New', 15))
		part_mach.set('Machine')
		part_mach.grid(row=5, column=1,padx=5,pady=5, sticky='w')
		rec_machine = ttk.Combobox(LBF1, values = mach, font=('TH Sarabun New', 15))
		rec_machine.set('ระบุเครื่องจกัร')
		rec_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')

	except:
		pass

# prev_department = ttk.Combobox(F01, values = dep, font=('TH Sarabun New', 15))
# prev_department.set('Maintenance')
# prev_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')


getmachine()
print(mach)


# linep = ['Linepd','Production']
linep = []
global mach_line


def getlinepd():
	global linep
	linep = []
	try:
		with conn:
			c.execute("SELECT linepd_name FROM linepd")
			lineps = c.fetchall()

		for i in lineps:
			linep.append(i[0])

		mach_line = ttk.Combobox(F51, values = linep, font=('TH Sarabun New', 15))
		mach_line.set('Line Production')
		mach_line.grid(row=1, column=1,padx=5,pady=5, sticky='w')

	except:
		pass


getlinepd()
print(linep)


# ---------------GET DATA FROM DATABASE TO LIST BOX (END)---------------

def expxl():
	pass


def menu():
	menubar = Menu(GUI)
	# ----------------Menu File > Export to Excel > Exit---------
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Export to PDF', command=expxl)
	filemenu.add_separator()
	filemenu.add_command(label='Upload to Server', command=expxl)
	filemenu.add_command(label='Exit', command=GUI.quit)

	menubar.add_cascade(label='File', menu=filemenu)
	# ----------------Menu File > Export to Excel > Exit---------
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Bar', command=expxl)
	filemenu.add_command(label='Line', command=expxl)
	filemenu.add_separator()
	filemenu.add_command(label='Graph', command=GUI.quit)

	menubar.add_cascade(label='Summary', menu=filemenu)

	# Spare Part Menu
	sparepartmenu = Menu(menubar, tearoff=0)
	sparepartmenu.add_command(label='Add Spare Part', command=expxl, accelerator="Ctrl+Q")
	sparepartmenu.add_command(label='View Spare Part', command=expxl, accelerator="Ctrl+Q")
	menubar.add_cascade(label='Spare Part', menu=sparepartmenu)

	# Update Menu , accelerator="Ctrl+X"
	up_sparepartmenu = Menu(menubar, tearoff=0)
	up_sparepartmenu.add_command(label='Update Department', command=getdepartment)
	up_sparepartmenu.add_command(label='Update Machine', command=getmachine)
	up_sparepartmenu.add_command(label='Update Linepd', command=getlinepd)
	up_sparepartmenu.add_command(label='Update', command=expxl)
	up_sparepartmenu.add_command(label='Count Spare Part', command=expxl)
	menubar.add_cascade(label='Update', menu=up_sparepartmenu)

	GUI.config(menu=menubar)


menu()


def clear_entry():
	rec_requestor.set("")
	rec_department.set("ระบุแผนก")
	rec_machine.set("ระบุเครื่องจักร")
	rec_area.set("")
	rec_problem.delete('1.0',END)
	rec_broke_time.set("")
	rec_recorder.set("")
	rec_record_time.set("")
	rec_cause.delete('1.0',END)
	rec_fix_detail.delete('1.0',END)
	rec_part_change_detail.delete('1.0',END)
	rec_use_begin_time.set("")
	rec_use_end_time.set("")
	rec_break_begin_time.set("")
	rec_break_end_time.set("")
	rec_reporter.set("")
	rec_checker.set("")
	rec_manager.set("")
	allpartlist = []

def add_record(event=None):
	# print(preventive_date.get())
	def confirm():
		
		if rec_categories.get() == 1:
			rec_cate = "ทำใหม่"
		elif rec_categories.get() == 2:
			rec_cate = "ซ่อม"
		elif rec_categories.get() == 3:
			rec_cate = "เพิ่มเติม"
		else:
			rec_cate = "อื่น ๆ"

		print(rec_cate)

		if rec_important.get() == 1:
			rec_imp = "ด่วน"
		elif rec_important.get() == 2:
			rec_imp = "ปกติ"
		else:
			rec_imp = "รอได้"

		print(rec_imp)

		if rec_part_changed.get() == 1:
			rec_part_c = "เหมือนเดิม"
		else:
			rec_part_c = "เปลี่ยนแปลงไปจาก"

		print(rec_part_c)

		################
		textformpartlist = ''
		global allpartlist

		for i in allpartlist:
			xx = i[0] + '+'+i[1]+','
			print("THIS IS XX: ",xx)
			textformpartlist += xx

		print("PARTLIST TEXT: ",textformpartlist)



		################

		with conn:
			c.execute("""INSERT INTO record_fix VALUES (

				:ID,\
				:rec_requestor,\
				:rec_department,\
				:rec_cate,\
				:rec_imp,\
				:rec_req_date,\
				:rec_machine,\
				:rec_area,\
				:rec_problem,\
				:rec_broke_date,\
				:rec_broke_time,\
				:rec_recorder,\
				:rec_record_time,\
				:rec_cause,\
				:rec_fix_detail,\
				:rec_part_c,\
				:rec_part_change_detail,\
				:rec_finish_date,\
				:rec_use_begin_time,\
				:rec_use_end_time,\
				:rec_break_begin_time,\
				:rec_break_end_time,\
				:rec_reporter,\
				:rec_checker,\
				:rec_manager,\
				:rec_partlist

				)""",

			          {'ID':None,
			           'rec_requestor': rec_requestor.get(),
			           'rec_department': rec_department.get(),
			           'rec_cate': rec_cate,
			           'rec_imp': rec_imp,
			           'rec_req_date': rec_req_date.get(),
			           'rec_machine': rec_machine.get(),
			           'rec_area': rec_area.get(),
			           'rec_problem': rec_problem.get("1.0",END),
			           'rec_broke_date': rec_broke_date.get(),
			           'rec_broke_time': rec_broke_time.get(),
			           'rec_recorder': rec_recorder.get(),
			           'rec_record_time': rec_record_time.get(),
			           'rec_cause': rec_cause.get("1.0",END),
			           'rec_fix_detail': rec_fix_detail.get("1.0",END),
			           'rec_part_c': rec_part_c,
			           'rec_part_change_detail': rec_part_change_detail.get("1.0",END),
			           'rec_finish_date': rec_finish_date.get(),
			           'rec_use_begin_time': rec_use_begin_time.get(),
			           'rec_use_end_time': rec_use_end_time.get(),
			           'rec_break_begin_time': rec_break_begin_time.get(),
			           'rec_break_end_time': rec_break_end_time.get(),
			           'rec_reporter': rec_reporter.get(),
			           'rec_checker': rec_checker.get(),
			           'rec_manager': rec_manager.get(),
			           'rec_partlist':textformpartlist[:-1]
			           }
			          )
		conn.commit()
		print('Success')
		allpartlist = []

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()




global prlist
prlist = []

global prname, prquan, pr_name, pr_quantity, PRE2, PRE3

global allpartlist
allpartlist = []

def add_partlist_list(event=None):


	def getstock():


		def getsparepart(event):
			try:
				ts = TVPartlst.selection()
				x = TVPartlst.item(ts)
				print(x['values'][0])
				texttoset = "{}-{} {}".format(x['values'][0],x['values'][1],x['values'][2])
				pr_name.set(texttoset)
				GUIPL.withdraw()
				
			except:
				pass


		GUIPL = Toplevel()
		GUIPL.geometry('820x300+100+50')

		# Treview
		LB1 = ttk.Label(GUIPL,text='เลือกอะไหล่')
		TVFPartlst = Frame(GUIPL, width=200)
		TVFPartlst.grid(row=0,column=1,pady=20)

		TVHPartlst= ['รหัส','ชื่ออะไหล่','รุ่น','ราคา','จำนวน','เครื่องจักร','ผู้จำหน่าย']
		TVHPaW = [(80,80),(200,200),(80,80),(80,80),(80,80),(150,150),(170,170)]

		# TREEVIEW----------------------

		TVPartlst = ttk.Treeview(TVFPartlst,columns=TVHPartlst, show="headings", height=8)
		for i,col in enumerate(TVHPartlst):
			TVPartlst.heading(col, text=col.title())
			TVPartlst.column(col,minwidth=TVHPaW[i][0],width=TVHPaW[i][1],anchor=N)

		TVPartlst.pack(fill=BOTH)
		

		try:
			with conn:
				c.execute("""SELECT * FROM partlist""")
				tvpalist = c.fetchall()
			conn.commit()
			print(tvpalist)
			print('Success')
		except:
			pass

		try:
			x = TVPartlst.get_children()
			count = len(x)
			for z in range(count):
				TVPartlst.delete(x[z])

		except:
			pass
		print(tvpalist)

		for it in tvpalist:
			TVPartlst.insert('','end',values=it[1:])

		TVPartlst.bind('<Double-1>',getsparepart)


		GUIPL.mainloop()



	def add_pr():
		prlist = [PRE2.get(),PRE3.get()]
		allpartlist.append(prlist)
		print(prlist)
		sparelist1.insert('','end',values=prlist)
		print(allpartlist)




	GUI_PR = Toplevel()
	GUI_PR.geometry('350x300+300+50')
	#------------Variables-------------

	pr_code = StringVar()
	pr_name = StringVar()
	pr_quantity = StringVar()
	pr_quantity.set('1')


	# LT1 = ['ลำดับ','รายการ','จำนวน']
	LT1 = ['ชื่ออะไหล่','จำนวน']

	for i,j in enumerate(LT1):
		L1 = ttk.Label(GUI_PR, text=j)
		L1.grid(row=i, column=0,pady=5,padx=5,sticky='nw')


	# PRE1 = ttk.Entry(GUI_PR, textvariable=pr_code, font=('TH Sarabun New',15))
	# PRE1.grid(row=0, column=1, padx=5, pady=5)

	PRE2 = ttk.Entry(GUI_PR, textvariable=pr_name, font=('TH Sarabun New',15))
	PRE2.grid(row=0, column=1, padx=5, pady=5)

	BSEARCH = ttk.Button(GUI_PR, text='...',width=5,command=getstock).grid(row=0, column=2, padx=5, pady=5)

	PRE3 = ttk.Entry(GUI_PR, textvariable=pr_quantity, font=('TH Sarabun New',15))
	PRE3.grid(row=1, column=1, padx=5, pady=5)

	PRB1 = ttk.Button(GUI_PR, text='เพิ่ม',command=add_pr)
	PRB1.grid(row=2, column=1, padx=5, pady=5)


	GUI_PR.mainloop()


def clearprlist():
	for item in sparelist1.get_children():
		sparelist1.delete(item)

	allpartlist = []




def test_print():
	if rec_categories.get() == 1:
		rec_cate = "ทำใหม่"
	elif rec_categories.get() == 2:
		rec_cate = "ซ่อม"
	elif rec_categories.get() == 3:
		rec_cate = "เพิ่มเติม"
	else:
		rec_cate = "อื่น ๆ"

	print(rec_cate)

	if rec_important.get() == 1:
		rec_imp = "ด่วน"
	elif rec_important.get() == 2:
		rec_imp = "ปกติ"
	else:
		rec_imp = "รอได้"

	print(rec_imp)

	if rec_part_changed.get() == 1:
		rec_part_c = "เหมือนเดิม"
	else:
		rec_part_c = "เปลี่ยนแปลงไปจาก"

	print(rec_part_c)

	print(rec_problem.get("1.0",END))


def print_record():
	pass


def updatesparepart():
	try:
		with conn:
			c.execute("""SELECT * FROM sparepart_list""")
			sp_list = c.fetchall()
		conn.commit()
		print('Success')
	except:
		pass

	try:
		x = sparelist.get_children()
		count = len(x)
		for z in range(count):
			sparelist.delete(x[z])

	except:
		pass


	for it in sp_list:
		sparelist.insert('', 'end', values=it[1:])


def officerpopup():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_requestor.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()
#########################################################

def officerpopup():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_requestor.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()

#########################################################



# -----------------------------Tab8-----------------------------
# ---------LABEL FRAME 01 -------------------
LBF1 = LabelFrame(F81, text='สำหรับพนักงานแจ้งซ่อม', font=('TH Sarabun New', 15))
LBF1.grid(row=0, column=0, padx=5, pady=5, sticky='N')

RLB1 = LB(LBF1, "ผู้แจ้งซ่อม", 0, 0, 'w')
global rec_requestor
rec_requestor = StringVar()
#RE1 = ET(LBF1, rec_requestor, 0, 1, 'w')
RE1 = ttk.Entry(LBF1, textvariable=rec_requestor,font=('TH Sarabun New',13),width=18)
RE1.grid(row=0, column=1, padx=5, pady=5, sticky='w')

BOFF = ttk.Button(LBF1, text='...',command=officerpopup,width=3)
BOFF.grid(row=0, column=1, padx=5, pady=5, sticky='e')

RLB2 = LB(LBF1, "แผนก", 1, 0, 'w')
rec_department = ttk.Combobox(LBF1, values = dep, font=('TH Sarabun New', 15))
rec_department.set('ระบุแผนก')
rec_department.grid(row=1, column=1,padx=5,pady=5, sticky='w')



RLB5 = LB(LBF1, "วันที่ต้องการ", 2, 0, 'w')
rec_req_date = DateEntry(LBF1, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
rec_req_date.grid(row=2, column=1, padx=5, pady=5, sticky='w')

RLB6 = LB(LBF1, "ชื่อเครื่องจักร", 3, 0, 'w')
rec_machine = ttk.Combobox(LBF1, values = mach, font=('TH Sarabun New', 15))
rec_machine.set('ระบุเครื่องจักร')
rec_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')

RLB7 = LB(LBF1, "บริเวณที่เสีย", 4, 0, 'w')
rec_area = StringVar()
RE7 = ET(LBF1, rec_area, 4, 1, 'w')

RLB8 = ttk.Label(LBF1, text='อาการเสีย').grid(row=5,column=0,padx=5,pady=5,sticky='NW')
rec_problem = Text(LBF1, height=2, width=40,font=('TH Sarabun New',13))
rec_problem.grid(row=5,column=1,padx=5,pady=5)


RLB3 = LB(LBF1, "ลักษณะงาน", 6, 0, 'e')
rec_categories = IntVar()
rec_categories1 = Radiobutton(LBF1, text = "ทำใหม่", variable=rec_categories, value=1, font=('TH Sarabun New', 13))
rec_categories1.place(x=80, y=270)
rec_categories2 = Radiobutton(LBF1, text = "ซ่อม", variable=rec_categories, value=2, font=('TH Sarabun New', 13))
# rec_categories2.grid(row=6, column=2,padx=5,pady=5, sticky='w',columnspan=3)
rec_categories2.place(x=140, y=270)
rec_categories3 = Radiobutton(LBF1, text = "เพิ่มเติม", variable=rec_categories, value=3, font=('TH Sarabun New', 13))
# rec_categories3.grid(row=6, column=3,padx=5,pady=5, sticky='w',columnspan=3)
rec_categories3.place(x=200, y=270)
rec_categories4 = Radiobutton(LBF1, text = "อื่น ๆ", variable=rec_categories, value=4, font=('TH Sarabun New', 13))
# rec_categories4.grid(row=6, column=4,padx=5,pady=5, sticky='w',columnspan=3)
rec_categories4.place(x=250, y=270)
rec_cate = 0

RLB4 = LB(LBF1, "ความต้องการ", 7, 0, 'e')
rec_important = IntVar()
rec_important1 = Radiobutton(LBF1, text = "ด่วน", variable=rec_important, value=1, font=('TH Sarabun New', 13))
rec_important1.place(x=80, y=310)
rec_important2 = Radiobutton(LBF1, text = "ปกติ", variable=rec_important, value=2, font=('TH Sarabun New', 13))
# rec_important2.grid(row=7, column=2,padx=5,pady=5, sticky='w')
rec_important2.place(x=140, y=310)
rec_important3 = Radiobutton(LBF1, text = "รอได้", variable=rec_important, value=3, font=('TH Sarabun New', 13))
# rec_important3.grid(row=7, column=3,padx=5,pady=5, sticky='w')
rec_important3.place(x=200, y=310)
rec_imp = 0




RLB9 = LB(LBF1, "วันที่เสีย", 8, 0, 'w')
rec_broke_date = DateEntry(LBF1, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
rec_broke_date.grid(row=8, column=1, padx=5, pady=5, sticky='w')

RLB10 = LB(LBF1, "เวลาที่แจ้ง", 9, 0, 'w')
rec_broke_time = StringVar()
RE10 = ET(LBF1, rec_broke_time, 9, 1, 'w')

RLB11 = LB(LBF1, "ผู้รับแจ้ง", 10, 0, 'w')

global rec_recorder
rec_recorder = StringVar()
#RE11 = ET(LBF1, rec_recorder, 10, 1, 'w')

#***************************************************************

def officerpopup2():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_recorder.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()


RE1 = ttk.Entry(LBF1, textvariable=rec_recorder,font=('TH Sarabun New',13),width=18)
RE1.grid(row=10, column=1, padx=5, pady=5, sticky='w')

BOFF = ttk.Button(LBF1, text='...',command=officerpopup2,width=3)
BOFF.grid(row=10, column=1, padx=5, pady=5, sticky='e')

#***************************************************************

RLB12 = LB(LBF1, "เวลาที่รับแจ้ง", 11, 0, 'w')
rec_record_time = StringVar()
RE12 = ET(LBF1, rec_record_time, 11, 1, 'w')

# ---------LABEL FRAME 02 -------------------
LBF2 = LabelFrame(F81, text='สำหรับพนักงานส่วนซ่อมบำรุง', font=('TH Sarabun New', 15), width=915, height=600)
LBF2.grid(row=0, column=1,columnspan=3, padx=5, pady=5, sticky='NW',ipadx=0, ipady=0)
# LBF2.place(x=400,y=5)

RLB13 = ttk.Label(LBF2, text='สาเหตุที่เสีย')
# RLB13.grid(row=0,column=0,padx=5,pady=5,sticky='NW')
RLB13.place(x=10,y=10)
rec_cause = Text(LBF2, height=1.2, width=100,font=('TH Sarabun New',14))
# rec_cause.grid(row=0,column=1,padx=5,pady=5,columnspan=3)
rec_cause.place(x=180,y=10)

RLB14 = ttk.Label(LBF2, text='รายละเอียดการตรวจซ่อม')
# RLB14.grid(row=1,column=0,padx=5,pady=5,sticky='NW')
RLB14.place(x=10,y=50)
rec_fix_detail = Text(LBF2, height=1.2, width=100,font=('TH Sarabun New',14))
# rec_fix_detail.grid(row=1,column=1,padx=5,pady=5,columnspan=3)
rec_fix_detail.place(x=180,y=50)


RLB15 = ttk.Label(LBF2, text='อุปกรณ์ที่ใช้')
# RLB15.grid(row=2,column=0,padx=5,pady=5,sticky='NW')
RLB15.place(x=10,y=90)
style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))

sparepartheader1= ['รายการ','จำนวน/หน่วย']
sparelist_width1 = [(200,200),(100,100)]

sparelist1 = ttk.Treeview(LBF2,columns=sparepartheader1, show="headings", height=6)

for i,col in enumerate(sparepartheader1):
	sparelist1.heading(col, text=col.title())
	sparelist1.column(col,minwidth=sparelist_width1[i][0],width=sparelist_width1[i][1],anchor=N)

# sparelist1.grid(row=2,column=1,padx=5,pady=5, columnspan=1)
sparelist1.place(x=180,y=90)

AddB1 = ttk.Button(LBF2,text='เพิ่มอุปกรณ์ที่ใช้...', style='my.TButton',command=add_partlist_list)
# AddB1.grid(row=2,column=4,padx=5,pady=5,sticky='e')
AddB1.place(x=550,y=100)
# clearlist()
CB1 = ttk.Button(LBF2,text='ล้าง', style='my.TButton',command=clearprlist)
# CB1.grid(row=2,column=5,padx=5,pady=5,columnspan=2,sticky='W')
CB1.place(x=550,y=150)

# ------------------------------------------------------------------------
# RLB16 = LB(LBF2, "อุปกรณ์ที่นำมาเปลี่ยน", 3, 0, 'w')
RLB16 = ttk.Label(LBF2,text="อุปกรณ์ที่นำมาเปลี่ยน").place(x=10,y=250)
rec_part_changed = tk.IntVar()
rec_part_changed1 = tk.Radiobutton(LBF2, text = "เหมือนเดิม", variable=rec_part_changed, value=1, font=('TH Sarabun New', 15))
# rec_part_changed1.grid(row=3, column=1,padx=5,pady=5, sticky='w')
rec_part_changed1.place(x=180,y=250)
rec_part_changed2 = tk.Radiobutton(LBF2, text = "เปลี่ยนแปลงไปจาก", variable=rec_part_changed, value=2, font=('TH Sarabun New', 15))
# rec_part_changed2.grid(row=4, column=1 ,padx=5,pady=5, sticky='w')
rec_part_changed2.place(x=180,y=290)
rec_part_c = 0

rec_part_change_detail = Text(LBF2, height=2.4, width=35,font=('TH Sarabun New',14))
# rec_part_change_detail.grid(row=5, column=1,padx=5,pady=5)
rec_part_change_detail.place(x=180,y=330)

# RLB17 = LB(LBF2, "วัน/เดือน/ปี ที่ซ่อมเสร็จ", 3, 3, 'e')
RLB17 = ttk.Label(LBF2,text="วัน/เดือน/ปี ที่ซ่อมเสร็จ").place(x=500,y=250)
rec_finish_date = DateEntry(LBF2, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
rec_finish_date.place(x=640,y=255)
# rec_finish_date.grid(row=3, column=4, padx=5, pady=5, sticky='w')

# RLB18 = LB(LBF2, "เวลาที่ใช้ จาก", 4, 3, 'e')
RLB18 = ttk.Label(LBF2,text="เวลาที่ใช้ จาก").place(x=500,y=290)
rec_use_begin_time = StringVar()
# RE18 = ET(LBF2, rec_use_begin_time, 4, 4, 'w')
RE18 = ttk.Entry(LBF2,textvariable=rec_use_begin_time,font=('TH, Sarabun New',12)).place(x=640,y=290)

# RLB19 = LB(LBF2, "ถึง", 4, 5, 'w')
RLB19 = ttk.Label(LBF2,text="เวลาที่ใช้ ถึง").place(x=500,y=330)
rec_use_end_time = StringVar()
# RE19 = ET(LBF2, rec_use_end_time, 4, 6, 'w')
RE19 = ttk.Entry(LBF2,textvariable=rec_use_end_time,font=('TH, Sarabun New',12)).place(x=640,y=330)

# RLB20 = LB(LBF2, "Break Down  เวลาจาก", 5, 3, 'ne')
RLB20 = ttk.Label(LBF2,text="Break Down  เวลาจาก").place(x=500,y=370)
rec_break_begin_time = StringVar()
# RE20 = ET(LBF2, rec_break_begin_time, 5, 4, 'nw')
RE20 = ttk.Entry(LBF2,textvariable=rec_break_begin_time,font=('TH, Sarabun New',12)).place(x=640,y=370)

# RLB21 = LB(LBF2, "ถึง", 5, 5, 'nw')
RLB21 = ttk.Label(LBF2,text="Break Down  เวลาถึง").place(x=500,y=410)
rec_break_end_time = StringVar()
# RE21 = ET(LBF2, rec_break_end_time, 5, 6, 'nw')
RE21 = ttk.Entry(LBF2,textvariable=rec_break_end_time,font=('TH, Sarabun New',12)).place(x=640,y=410)

# RLB22 = LB(LBF2, "ผู้รายงาน", 6, 0, 'e')
RLB22 = ttk.Label(LBF2,text="ผู้รายงาน").place(x=5,y=400)
rec_reporter = StringVar()
# RE22 = ET(LBF2, rec_reporter, 6, 1, 'w')
RE22 = ttk.Entry(LBF2,textvariable=rec_reporter,font=('TH Sarabun New',12),width=18).place(x=180,y=400)

#***************************************************************

def officerpopup3():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_reporter.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()




BOFF = ttk.Button(LBF2, text='...',command=officerpopup3,width=3).place(x=300,y=395)


#***************************************************************

# RLB23 = LB(LBF2, "ผู้ตรวจรับงาน", 7, 0, 'e')
RLB23 = ttk.Label(LBF2,text="ผู้ตรวจรับงาน").place(x=5,y=440)
rec_checker = StringVar()
# RE23 = ET(LBF2, rec_checker, 7, 1, 'w')
RE23 = ttk.Entry(LBF2,textvariable=rec_checker,font=('TH Sarabun New',12),width=18).place(x=180,y=440)


#***************************************************************

def officerpopup4():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_checker.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()




BOFF = ttk.Button(LBF2, text='...',command=officerpopup4,width=3).place(x=300,y=435)


#***************************************************************
# RLB24 = LB(LBF2, "ผู้จัดการ", 8, 0, 'e')
RLB24 = ttk.Label(LBF2,text="ผู้จัดการ").place(x=5,y=480)
rec_manager = StringVar()
# RE24 = ET(LBF2, rec_manager, 8, 1, 'w')
RE24 = ttk.Entry(LBF2,textvariable=rec_manager,font=('TH Sarabun New',12),width=18).place(x=180,y=480)


#***************************************************************

def officerpopup5():


	def getofficer(event):
		try:
			ts = TVOff2.selection()
			x = TVOff2.item(ts)
			officer = (x['values'][1])
			rec_manager.set(officer)
			GUIOFF.withdraw()
		except:
			messagebox.showinfo('เลือกเจ้าหน้าที่','เลือกเจ้าหน้าที่โดยการดับเบิลคลิก')


	GUIOFF = Toplevel()
	GUIOFF.title('เลือกเจ้าหน้าที่')
	GUIOFF.geometry('400x600+100+100')
	
	# Treview
	TVFOff = Frame(GUIOFF, width=200)
	TVFOff.grid(row=8,column=1,pady=20)

	TVHOff2= ['รหัส','ชื่อ','แผนก']
	TVHOW2 = [(80,80),(200,200),(120,120)]

	# TREEVIEW----------------------

	TVOff2 = ttk.Treeview(TVFOff,columns=TVHOff2, show="headings", height=20)
	for i,col in enumerate(TVHOff2):
		TVOff2.heading(col, text=col.title())
		TVOff2.column(col,minwidth=TVHOW2[i][0],width=TVHOW2[i][1],anchor=N)

	TVOff2.pack(fill=BOTH)

	TVOff2.bind('<Double-1>', getofficer)

	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff2.get_children()
		count = len(x)
		for z in range(count):
			TVOff2.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff2.insert('','end',values=it[1:])

	GUIOFF.mainloop()




BOFF = ttk.Button(LBF2, text='...',command=officerpopup5,width=3).place(x=300,y=475)


#***************************************************************

# RB1 = BT(LBF2, 'บันทึกข้อมูล', 'add_record', 9, 1)
RB1 = ttk.Button(LBF2, text="บันทึกข้อมูล", style='my.TButton', command=add_record).place(x=450,y=470)
# RB2 = BT(LBF2, 'เคลียร์', 'clear_entry', 9, 2)
RB2 = ttk.Button(LBF2, text="เคลียร์", style='my.TButton', command=clear_entry).place(x=600,y=470)

# ------------------TREEVIEW Record--------------------
def updaterecord():
	try:
		with conn:
			c.execute("""SELECT * FROM record_fix""")
			recordlist = c.fetchall()
		conn.commit()
		print(recordlist)
		print('Success')
	except:
		pass

	try:
		x = TVRecord.get_children()
		count = len(x)
		for z in range(count):
			TVRecord.delete(x[z])

	except:
		pass
	print(recordlist)

	for it in recordlist:
		TVRecord.insert('','end',values=it[0:])
# Treview

TVFRecord = Frame(F82, width=1366, height=730)
# TVFRecord.grid(row=0,column=0,pady=20)
TVFRecord.place(x=5,y=5)

# TVHRecord = ['รหัส','ผู้แจ้งซ่อม','แผนก','วันที่ต้องการ','ลักษณะงาน','ความต้องการ','ชื่อเครื่องจักร','บริเวณที่เสีย','อาการเสีย','วันที่เสีย','เวลาที่แจ้ง','ผู้รับแจ้ง','เวลาที่รับแจ้ง','สาเหตุที่เสีย','รายละเอียดการตรวจซ่อม','อุปกรณ์ที่นำมาเปลี่ยน','รายละเอียดการเปลี่ยนแปลง','วันที่ซ่อมเสร็จ','เวลาที่ใช้ จาก','เวลาที่ใช้ ถึง','Break Down เวลา จาก','Break Down เวลา ถึง','ผู้รายงาน','ผู้ตรวจรับ','ผู้จัดการ']

TVHRecord = ['ID Record','ผู้แจ้งซ่อม','แผนก','ลักษณะงาน','ความต้องการ','วันที่ต้องการ','ชื่อเครื่องจักร','บริเวณที่เสีย','อาการเสีย','วันที่เสีย','เวลาที่แจ้ง']

TVHPW = [(80,80),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120)]

# TREEVIEW----------------------


TVRecord = ttk.Treeview(TVFRecord,columns=TVHRecord, show="headings", height=20)


for i,col in enumerate(TVHRecord):
	TVRecord.heading(col, text=col.title())
	TVRecord.column(col,minwidth=TVHPW[i][0],width=TVHPW[i][1],anchor=N)

# TVRecord.pack(fill=BOTH)
TVRecord.place(x=5,y=5)
# TVRecord.grid(row=1,column=0)

hsb = ttk.Scrollbar(TVFRecord, orient="horizontal", command=TVRecord.xview)
# hsb = ttk.Scrollbar(TVFRecord, orient="horizontal")
# hsb.pack(fill=X)
hsb.place(x=5,y=435)
# hsb.config(command=TVRecord.xview)
TVRecord.config(xscrollcommand=hsb.set)


update_record = ttk.Button(TVFRecord,text='อัพเดต', style='my.TButton',command=updaterecord)
# update_record.pack(side=LEFT,padx=5,pady=5)
# update_record.grid(row=8,column=1)
update_record.place(x=550,y=450)
print_record = ttk.Button(TVFRecord,text='ออกรายงาน', style='my.TButton',command=genreport)
# print_record.pack(side=LEFT,padx=5,pady=5)
# print_record.grid(row=8,column=2)
print_record.place(x=700,y=450)

updaterecord()

# scrollbary = Scrollbar(TVRecord)
# scrollbary.pack(side=RIGHT, fill=Y)

# -----------------------------Tab0-----------------------------


# ------Label and Entry------
PLB1 = LB(F01, "Preventive Code", 0, 0, 'w')
prev_code = StringVar()
PE1 = ET(F01, prev_code, 0, 1, 'w')
PLB2 = LB(F01, "Preventive Title", 1, 0, 'w')
prev_title = StringVar()
PE2 = ET(F01, prev_title, 1, 1, 'w')


PLB3 = LB(F01, "Preventive Department", 2, 0, 'w')

# prev_department = StringVar()
# PE3 = ET(F0, prev_department, 2, 1, 'w')
# gui,itemlist,rw,cl,st

prev_department = ttk.Combobox(F01, values = dep, font=('TH Sarabun New', 15))
prev_department.set('Department')
prev_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')

PLB4 = LB(F01, "Preventive Machine", 3, 0, 'w')
# prev_machine = StringVar()
# PE4 = ET(F01, prev_machine, 3, 1, 'w')
prev_machine = ttk.Combobox(F01, values = mach, font=('TH Sarabun New', 15))
prev_machine.set('Machine')
prev_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')


# preventive_date
LLB3 = LB(F01, "Date Planing", 4, 0, 'w')
preventive_date = DateEntry(F01, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
preventive_date.grid(row=4, column=1, padx=5, pady=5, sticky='w')


PLB5 = LB(F01, "Preventive Partlist", 5, 0, 'w')
prev_partlist = StringVar()
PE5 = ET(F01, prev_partlist, 5, 1, 'w')
PLB6 = LB(F01, "Preventive Cost", 6, 0, 'w')
prev_cost = StringVar()
PE6 = ET(F01, prev_cost, 6, 1, 'w')
PLB7 = LB(F01, "Preventive Responsible", 7, 0, 'w')
prev_responsible = StringVar()
PE7 = ET(F01, prev_responsible, 7, 1, 'w')


def add_preventive(event=None):
	print(preventive_date.get())
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO preventive VALUES (
	
					:ID,\
					:preventive_code,\
					:preventive_title,\
					:preventive_department,\
					:preventive_machine,\
					:preventive__partlist,\
					:preventive_cost,\
					:preventive_responsible,\
					:preventive_date
					)""",

				          {'ID':None,
							'preventive_code': prev_code.get(),
							'preventive_title': prev_title.get(),
							'preventive_department': prev_department.get(),
							'preventive_machine': prev_machine.get(),
							'preventive__partlist': prev_partlist.get(),
							'preventive_cost': int(prev_cost.get()),
							'preventive_responsible': prev_responsible.get(),
							'preventive_date':preventive_date.get()
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
PB1 = BT(F01, 'Add', 'add_preventive', 8, 1)


# ------------------TREEVIEW Preventive--------------------
def updateprev():
	try:
		with conn:
			c.execute("""SELECT * FROM preventive""")
			tvplist = c.fetchall()
		conn.commit()
		print(tvplist)
		print('Success')
	except:
		pass

	try:
		x = TVPrev.get_children()
		count = len(x)
		for z in range(count):
			TVPrev.delete(x[z])

	except:
		pass
	print(tvplist)

	for it in tvplist:
		TVPrev.insert('','end',values=it[1:])
# Treview

TVFPrev = Frame(F02, width=200)
TVFPrev.grid(row=8,column=1,pady=20)

TVHPrev= ['รหัส','ชื่อแผนงาน','แผนก','ชื่อเครื่องจักร','รายการวัสดุ','ค่าใช้จ่าย','รับผิดชอบโดย','วันที่']
TVHPW = [(80,80),(200,200),(120,120),(120,120),(250,250),(70,70),(100,100),(80,80)]

# TREEVIEW----------------------

TVPrev = ttk.Treeview(TVFPrev,columns=TVHPrev, show="headings", height=20)
for i,col in enumerate(TVHPrev):
	TVPrev.heading(col, text=col.title())
	TVPrev.column(col,minwidth=TVHPW[i][0],width=TVHPW[i][1],anchor=N)

TVPrev.pack(fill=BOTH)
addtowithdraw = ttk.Button(TVFPrev,text='อัพเดต', style='my.TButton',command=updateprev)
addtowithdraw.pack(padx=5,pady=5)

updateprev()
# --------------WITHDRAW LIST------------------
# wd_approved = (:app) WHERE wd_id = (:code)"

# -----------------------------Tab0 End-----------------------------


# -----------------------------Tab1-----------------------------
# ------Label and Entry------
BLB1 = LB(F11, "Breakdown Code", 0, 0, 'w')
break_code = StringVar()
BE1 = ET(F11, break_code, 0, 1, 'w')
BLB2 = LB(F11, "Breakdown Title", 1, 0, 'w')
break_title = StringVar()
BE2 = ET(F11, break_title, 1, 1, 'w')
BLB3 = LB(F11, "Breakdown Department", 2, 0, 'w')
# break_department = StringVar()
# BE3 = ET(F11, break_department, 2, 1, 'w')
break_department = ttk.Combobox(F11, values = dep, font=('TH Sarabun New', 15))
break_department.set('Department')
break_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')


BLB4 = LB(F11, "Breakdown Machine", 3, 0, 'w')
# break_machine = StringVar()
# BE4 = ET(F11, break_machine, 3, 1, 'w')
break_machine = ttk.Combobox(F11, values = mach, font=('TH Sarabun New', 15))
break_machine.set('Machine')
break_machine.grid(row=3, column=1,padx=5,pady=5, sticky='w')

# breakdown_date
BLB0 = LB(F11, "Date Planing", 4, 0, 'w')
break_date = DateEntry(F11, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
break_date.grid(row=4, column=1, padx=5, pady=5, sticky='w')


BLB5 = LB(F11, "Breakdown Partlist", 5, 0, 'w')
break_partlist = StringVar()
BE5 = ET(F11, break_partlist, 5, 1, 'w')
BLB6 = LB(F11, "Breakdown Cost", 6, 0, 'w')
break_cost = StringVar()
BE6 = ET(F11, break_cost, 6, 1, 'w')
BLB7 = LB(F11, "Breakdown Request", 7, 0, 'w')
break_request = StringVar()
BE7 = ET(F11, break_request, 7, 1, 'w')
BLB8 = LB(F11, "Breakdown Responsible", 8, 0, 'w')
break_responsible = StringVar()
BE8 = ET(F11, break_responsible, 8, 1, 'w')


def add_breakdown():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO breakdown VALUES (
	
					:ID,\
					:breakdown_code,\
					:breakdown_title,\
					:breakdown_department,\
					:breakdown_machine,\
					:breakdown_partlist,\
					:breakdown_cost,\
					:breakdown_request,\
					:breakdown_responsible,\
					:breakdown_date
					)""",

				          {'ID':None,
				           'breakdown_code': break_code.get(),
				           'breakdown_title': break_title.get(),
				           'breakdown_department': break_department.get(),
				           'breakdown_machine': break_machine.get(),
				           'breakdown_partlist': break_partlist.get(),
				           'breakdown_cost': int(break_cost.get()),
				           'breakdown_request': break_request.get(),
				           'breakdown_responsible': break_responsible.get(),
				           'breakdown_date': break_date.get()
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
BB1 = BT(F11, 'Add', 'add_breakdown', 9, 1)


# ------------------TREEVIEW Breakdown--------------------
def updatebreak():
	try:
		with conn:
			c.execute("""SELECT * FROM breakdown""")
			tvblist = c.fetchall()
		conn.commit()
		print(tvblist)
		print('Success')
	except:
		pass

	try:
		x = TVBreak.get_children()
		count = len(x)
		for z in range(count):
			TVBreak.delete(x[z])

	except:
		pass
	print(tvblist)

	for it in tvblist:
		TVBreak.insert('','end',values=it[1:])


# Treview
TVFBreak = Frame(F12, width=200)
TVFBreak.grid(row=8,column=1,pady=20)

TVHBreak= ['รหัส','ชื่อแผนงาน','แผนก','ชื่อเครื่องจักร','รายการวัสดุ','ค่าใช้จ่าย','ต้องการ','รับผิดชอบโดย','วันที่']
TVHBW = [(80,80),(200,200),(120,120),(120,120),(250,250),(70,70),(70,70),(100,100),(80,80)]

# TREEVIEW----------------------

TVBreak = ttk.Treeview(TVFBreak,columns=TVHBreak, show="headings", height=20)
for i,col in enumerate(TVHBreak):
	TVBreak.heading(col, text=col.title())
	TVBreak.column(col,minwidth=TVHBW[i][0],width=TVHBW[i][1],anchor=N)

TVBreak.pack(fill=BOTH)
addtobreak = ttk.Button(TVFBreak,text='อัพเดต', style='my.TButton',command=updatebreak)
addtobreak.pack(padx=5,pady=5)

updatebreak()
# -----------------------------Tab1 End-----------------------------

# -----------------------------Tab2-----------------------------
# ------Label and Entry------
OLB1 = LB(F21, "Officer Code", 0, 0, 'w')
off_code = StringVar()
OE1 = ET(F21, off_code, 0, 1, 'w')
OLB2 = LB(F21, "Officer Name", 1, 0, 'w')
off_name = StringVar()
OE2 = ET(F21, off_name, 1, 1, 'w')
OLB3 = LB(F21, "Officer Department", 2, 0, 'w')
# off_department = StringVar()
# OE3 = ET(F21, off_department, 2, 1, 'w')
off_department = ttk.Combobox(F21, values = dep, font=('TH Sarabun New', 15))
off_department.set('Department')
off_department.grid(row=2, column=1,padx=5,pady=5, sticky='w')


def add_officer():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO officer VALUES (
	
					:ID,\
					:officer_code,\
					:officer_name,\
					:officer_department
					)""",

				          {'ID':None,
				           'officer_code': off_code.get(),
				           'officer_name': off_name.get(),
				           'officer_department': off_department.get()
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
OB1 = BT(F21, 'Add', 'add_officer', 3, 1)


# ------------------TREEVIEW Officer--------------------
def updateofficer():
	try:
		with conn:
			c.execute("""SELECT * FROM officer""")
			tvolist = c.fetchall()
		conn.commit()
		print(tvolist)
		print('Success')
	except:
		pass

	try:
		x = TVOff.get_children()
		count = len(x)
		for z in range(count):
			TVOff.delete(x[z])

	except:
		pass
	print(tvolist)

	for it in tvolist:
		TVOff.insert('','end',values=it[1:])


# Treview
TVFOff = Frame(F22, width=200)
TVFOff.grid(row=8,column=1,pady=20)

TVHOff= ['รหัส','ชื่อ','แผนก']
TVHOW = [(80,80),(200,200),(120,120)]

# TREEVIEW----------------------

TVOff = ttk.Treeview(TVFOff,columns=TVHOff, show="headings", height=20)
for i,col in enumerate(TVHOff):
	TVOff.heading(col, text=col.title())
	TVOff.column(col,minwidth=TVHOW[i][0],width=TVHOW[i][1],anchor=N)

TVOff.pack(fill=BOTH)
addtooff = ttk.Button(TVFOff,text='อัพเดต', style='my.TButton',command=updateofficer)
addtooff.pack(padx=5,pady=5)

updateofficer()
# -----------------------------Tab2 End-----------------------------

# -----------------------------Tab3-----------------------------
# ------Label and Entry------
DLB1 = LB(F31, "Department Code", 0, 0, 'w')
dep_code = StringVar()
DE1 = ET(F31, dep_code, 0, 1, 'w')
DLB2 = LB(F31, "Department Name", 1, 0, 'w')
dep_name = StringVar()
DE2 = ET(F31, dep_name, 1, 1, 'w')


def add_department():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO department VALUES (
	
					:ID,\
					:dep_code,\
					:dep_name
					)""",

				          {'ID':None,
				           'dep_code': dep_code.get(),
				           'dep_name': dep_name.get(),
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
DB1 = BT(F31, 'Add', 'add_department', 2, 1)


# ------------------TREEVIEW Department--------------------
def updatedep():
	try:
		with conn:
			c.execute("""SELECT * FROM department""")
			tvdlist = c.fetchall()
		conn.commit()
		print(tvdlist)
		print('Success')
	except:
		pass

	try:
		x = TVDep.get_children()
		count = len(x)
		for z in range(count):
			TVDep.delete(x[z])

	except:
		pass
	print(tvdlist)

	for it in tvdlist:
		TVDep.insert('','end',values=it[1:])


# Treview
TVFDep = Frame(F32, width=200)
TVFDep.grid(row=8,column=1,pady=20)

TVHDep= ['รหัส','ชื่อแผนก']
TVHDW = [(80,80),(200,200)]

# TREEVIEW----------------------

TVDep = ttk.Treeview(TVFDep,columns=TVHDep, show="headings", height=20)
for i,col in enumerate(TVHDep):
	TVDep.heading(col, text=col.title())
	TVDep.column(col,minwidth=TVHDW[i][0],width=TVHDW[i][1],anchor=N)

TVDep.pack(fill=BOTH)
addtodep = ttk.Button(TVFDep,text='อัพเดต', style='my.TButton',command=updatedep)
addtodep.pack(padx=5,pady=5)

updatedep()
# -----------------------------Tab3 End-----------------------------

# -----------------------------Tab4-----------------------------
# ------Label and Entry------
LLB1 = LB(F41, "Linepd Code", 0, 0, 'w')
linepd_code = StringVar()
LE1 = ET(F41, linepd_code, 0, 1, 'w')
LLB2 = LB(F41, "Linepd Name", 1, 0, 'w')
linepd_name = StringVar()
LE2 = ET(F41, linepd_name, 1, 1, 'w')


def add_linepd():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO linepd VALUES (
	
					:ID,\
					:linepd_code,\
					:linepd_name
					)""",

				          {'ID':None,
				           'linepd_code': linepd_code.get(),
				           'linepd_name': linepd_name.get(),
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
LB1 = BT(F41, 'Add', 'add_linepd', 2, 1)


# ------------------TREEVIEW Linepd--------------------
def updateline():
	try:
		with conn:
			c.execute("""SELECT * FROM linepd""")
			tvllist = c.fetchall()
		conn.commit()
		print(tvllist)
		print('Success')
	except:
		pass

	try:
		x = TVLine.get_children()
		count = len(x)
		for z in range(count):
			TVLine.delete(x[z])

	except:
		pass
	print(tvllist)

	for it in tvllist:
		TVLine.insert('','end',values=it[1:])


# Treview
TVFLine = Frame(F42, width=200)
TVFLine.grid(row=8,column=1,pady=20)

TVHLine= ['รหัส','ชื่อไลน์ผลิต']
TVHLW = [(80,80),(200,200)]

# TREEVIEW----------------------

TVLine = ttk.Treeview(TVFLine,columns=TVHLine, show="headings", height=20)
for i,col in enumerate(TVHLine):
	TVLine.heading(col, text=col.title())
	TVLine.column(col,minwidth=TVHLW[i][0],width=TVHLW[i][1],anchor=N)

TVLine.pack(fill=BOTH)
addtoline = ttk.Button(TVFLine,text='อัพเดต', style='my.TButton',command=updateline)
addtoline.pack(padx=5,pady=5)

updateline()
# -----------------------------Tab4 End-----------------------------


# -----------------------------Tab5-----------------------------
# ------Label and Entry------
MLB1 = LB(F51, "Machine Code", 0, 0, 'w')
mach_code = StringVar()
ME1 = ET(F51, mach_code, 0, 1, 'w')
MLB2 = LB(F51, "Machine Line", 1, 0, 'w')
# mach_line = StringVar()
# ME2 = ET(F51, mach_line, 1, 1, 'w')
mach_line = ttk.Combobox(F51, values = linep, font=('TH Sarabun New', 15))
mach_line.set('Line Production')
mach_line.grid(row=1, column=1,padx=5,pady=5, sticky='w')

MLB3 = LB(F51, "Machine Name", 2, 0, 'w')
mach_name = StringVar()
ME3 = ET(F51, mach_name, 2, 1, 'w')
MLB4 = LB(F51, "Machine Detail", 3, 0, 'w')
mach_detail = StringVar()
ME4 = ET(F51, mach_detail, 3, 1, 'w')

# mach_instdate = StringVar()
# ME5 = ET(F51, mach_instdate, 4, 1, 'w')

# machine installation_date
MLB5 = LB(F51, "Machine Install Date", 4, 0, 'w')
mach_instdate = DateEntry(F51, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
mach_instdate.grid(row=4, column=1, padx=5, pady=5, sticky='w')


def add_machine():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO machine VALUES (
	
					:ID,\
					:machine_code,\
					:machine_line,\
					:machine_name,\
					:machine_detail,\
					:machine_installdate
					)""",

				          {'ID':None,
				           'machine_code': mach_code.get(),
				           'machine_line': mach_line.get(),
				           'machine_name': mach_name.get(),
				           'machine_detail': mach_detail.get(),
				           'machine_installdate': mach_instdate.get(),
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
PB1 = BT(F51, 'Add', 'add_machine', 5, 1)


# ------------------TREEVIEW Machine--------------------
def updatemach():
	try:
		with conn:
			c.execute("""SELECT * FROM machine""")
			tvmalist = c.fetchall()
		conn.commit()
		print(tvmalist)
		print('Success')
	except:
		pass

	try:
		x = TVMach.get_children()
		count = len(x)
		for z in range(count):
			TVMach.delete(x[z])

	except:
		pass
	print(tvmalist)

	for it in tvmalist:
		TVMach.insert('','end',values=it[1:])


# Treview
TVFMach = Frame(F52, width=200)
TVFMach.grid(row=8,column=1,pady=20)

TVHMach= ['รหัส','ชื่อไลน์ผลิต','ชื่อเครื่องจักร','รายละเอียด','วันที่ติดตั้ง']
TVHMaW = [(80,80),(200,200),(120,120),(250,250),(80,80)]

# TREEVIEW----------------------

TVMach = ttk.Treeview(TVFMach,columns=TVHMach, show="headings", height=20)
for i,col in enumerate(TVHMach):
	TVMach.heading(col, text=col.title())
	TVMach.column(col,minwidth=TVHMaW[i][0],width=TVHMaW[i][1],anchor=N)

TVMach.pack(fill=BOTH)
addtomach = ttk.Button(TVFMach,text='อัพเดต', style='my.TButton',command=updatemach)

updatemach()

addtomach.pack(padx=5,pady=5)
# -----------------------------Tab5 End-----------------------------

# -----------------------------Tab6-----------------------------
# ------Label and Entry------
PALB1 = LB(F61, "Partlist Code", 0, 0, 'w')
part_code = StringVar()
PAE1 = ET(F61, part_code, 0, 1, 'w')
PALB2 = LB(F61, "Partlist Name", 1, 0, 'w')
part_name = StringVar()
PAE2 = ET(F61, part_name, 1, 1, 'w')
PALB3 = LB(F61, "Partlist Model", 2, 0, 'w')
part_model = StringVar()
PAE3 = ET(F61, part_model, 2, 1, 'w')
PALB4 = LB(F61, "Partlist Price", 3, 0, 'w')
part_price = StringVar()
PAE4 = ET(F61, part_price, 3, 1, 'w')
PALB5 = LB(F61, "Partlist Quantity", 4, 0, 'w')
part_quan = StringVar()
PAE5 = ET(F61, part_quan, 4, 1, 'w')
PALB6 = LB(F61, "Partlist Machine", 5, 0, 'w')
# part_mach = StringVar()
# PAE6 = ET(F61, part_mach, 5, 1, 'w')
part_mach = ttk.Combobox(F61, values = mach, font=('TH Sarabun New', 15))
part_mach.set('Machine')
part_mach.grid(row=5, column=1,padx=5,pady=5, sticky='w')

PALB7 = LB(F61, "Partlist Supplier", 6, 0, 'w')
part_supp = StringVar()
PAE7 = ET(F61, part_supp, 6, 1, 'w')


def add_partlist():
	def confirm():
		try:
			with conn:
				c.execute("""INSERT INTO partlist VALUES (
	
					:ID,\
					:partlist_code,\
					:partlist_name,\
					:partlist_model,\
					:partlist_price,\
					:partlist_quantity,\
					:partlist_machine,\
					:partlist_supplier
					)""",

				          {'ID':None,
				           'partlist_code': part_code.get(),
				           'partlist_name': part_name.get(),
				           'partlist_model': part_model.get(),
				           'partlist_price': int(part_price.get()),
				           'partlist_quantity': int(part_quan.get()),
				           'partlist_machine': part_mach.get(),
				           'partlist_supplier': part_supp.get()
				           }
				          )
			conn.commit()
			print('Success')
		except:
			pass

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ", "ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()


# ------Button------
BB1 = BT(F61, 'Add', 'add_partlist', 7, 1)


# ------------------TREEVIEW Partlist--------------------
def updatepartlst():
	try:
		with conn:
			c.execute("""SELECT * FROM partlist""")
			tvpalist = c.fetchall()
		conn.commit()
		print(tvpalist)
		print('Success')
	except:
		pass

	try:
		x = TVPartlst.get_children()
		count = len(x)
		for z in range(count):
			TVPartlst.delete(x[z])

	except:
		pass
	print(tvpalist)

	for it in tvpalist:
		TVPartlst.insert('','end',values=it[1:])


# Treview
TVFPartlst = Frame(F62, width=200)
TVFPartlst.grid(row=8,column=1,pady=20)

TVHPartlst= ['รหัส','ชื่ออะไหล่','รุ่น','ราคา','จำนวน','เครื่องจักร','ผู้จำหน่าย']
TVHPaW = [(80,80),(200,200),(120,120),(100,100),(80,80),(150,150),(250,250)]

# TREEVIEW----------------------

TVPartlst = ttk.Treeview(TVFPartlst,columns=TVHPartlst, show="headings", height=20)
for i,col in enumerate(TVHPartlst):
	TVPartlst.heading(col, text=col.title())
	TVPartlst.column(col,minwidth=TVHPaW[i][0],width=TVHPaW[i][1],anchor=N)

TVPartlst.pack(fill=BOTH)
addtopartlst = ttk.Button(TVFPartlst,text='อัพเดต', style='my.TButton',command=updatepartlst)
addtopartlst.pack(padx=5,pady=5)

updatepartlst()

def deleteitem(event):
	def delitem():
		
		try:
			ts = TVRecord.selection()
			x = TVRecord.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM record_fix WHERE ID = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updaterecord()


TVRecord.bind('<Double-1>',deleteitem)


##############################################################
def deleteitem2(event):
	def delitem():
		
		try:
			ts = TVPrev.selection()
			x = TVPrev.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM preventive WHERE preventive_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updateprev()


TVPrev.bind('<Double-1>',deleteitem2)

##############################################################

#tvdlist

def deleteitem3(event):
	def delitem():
		
		try:
			ts = TVDep.selection()
			x = TVDep.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM department WHERE dep_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updatedep()


TVDep.bind('<Double-1>',deleteitem3)

##############################################################
#TVLine
def deleteitem4(event):
	def delitem():
		
		try:
			ts = TVLine.selection()
			x = TVLine.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM linepd WHERE linepd_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updateline()


TVLine.bind('<Double-1>',deleteitem4)

##############################################################
#TVMach

def deleteitem5(event):
	def delitem():
		
		try:
			ts = TVMach.selection()
			x = TVMach.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM machine WHERE machine_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updatemach()


TVMach.bind('<Double-1>',deleteitem5)

##############################################################
#TVOff

def deleteitem6(event):
	def delitem():
		
		try:
			ts = TVOff.selection()
			x = TVOff.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM officer WHERE officer_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updateofficer()


TVOff.bind('<Double-1>',deleteitem6)

##############################################################
#TVPartlst
def deleteitem7(event):
	def delitem():
		
		try:
			ts = TVPartlst.selection()
			x = TVPartlst.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM partlist WHERE partlist_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updatepartlst()


TVPartlst.bind('<Double-1>',deleteitem7)

##############################################################
#TVBreak

def deleteitem8(event):
	def delitem():
		
		try:
			ts = TVBreak.selection()
			x = TVBreak.item(ts)
			print(x['values'][0])

			y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

			
			if y == True:
				with conn:
					c.execute("DELETE FROM breakdown WHERE breakdown_code = (:code)",{'code':x['values'][0]})
					conn.commit()
				messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
			else:
				messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
		except:
			messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')
		
	delitem()
	updatebreak()


TVBreak.bind('<Double-1>',deleteitem8)
##############################################################




##############################################################



















##############################################################
# -----------------------------Tab6 End-----------------------------
# gui,listx,listy,width,height,row,column

ydata = [20,30,40,25,45]
count = len(ydata)
xdata = list(range(count))

# BT7 = ttk.Button(F7,text='test').grid(row=0,column=0)

# -----------------TEST GRAPH------------------
X = [0,1,2,3,4,5,6,7]
Y = [100,200,400,300,500,100,300,400]

w, h = 700, 500


def draw_figure(canvas, figure, loc=(0, 0)):

    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)

    # Unfortunately, there's no accessor for the pointer to the native renderer
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)

    return photo


# canvas1 = tk.Canvas(F7, width=w, height=h)
# canvas1.grid(row=0,column=0)

# b1 = ttk.Button(F7, text='Update')
# b1.grid(row=1,column=0, sticky='E')

# fig = mpl.figure.Figure(figsize=(4, 3))
# ax = fig.add_axes([0, 0, 1, 1])

# ax.bar(X, Y)

# countx = len(X)
# dmax = max(X)
# diff = dmax * 0.05
# for i in range(countx):
# 	ax.text(X[i],Y[i]+diff,str(Y[i]),ha='center')

# # Keep this handle alive, or else figure will disappear
# fig_x, fig_y = 10, 10
# fig_photo = draw_figure(canvas1, fig, loc=(fig_x, fig_y))
# fig_w, fig_h = fig_photo.width(), fig_photo.height()

# # Add more elements to the canvas, potentially on top of the figure
# # canvas.create_line(200, 50, fig_x + fig_w / 2, fig_y + fig_h / 2)
# canvas1.create_text(200, 50, text="Total Expense", anchor="s")


GUI.mainloop()

