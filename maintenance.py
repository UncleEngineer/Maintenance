# pip install reportlab
# pip install tkcalendar


import os
from tkinter import *
#from firebase import firebase
from tkinter import ttk,messagebox
from tkinter.ttk import Notebook
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import sqlite3
import tkinter.font as tkFont
import subprocess
#import report2
#import reportwithdraw
#-------------------pdf report---------------------

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer,Image
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
#Add font
from reportlab.platypus import SimpleDocTemplate, Spacer, Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet

######################STOCK CARD############################

class Stockcard(object):
	""""""
 
	#----------------------------------------------------------------------
	def __init__(self,codename,reorderpoint,spare,use):
		"""Constructor"""
		self.width, self.height = A4
		self.styles = getSampleStyleSheet()
		self.codename = codename
		self.reorderpoint = reorderpoint
		self.spare = spare
		self.use = use
		
 
	#----------------------------------------------------------------------
	def coord(self, x, y, unit=1):
		"""
		http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
		Helper class to help position flowables in Canvas objects
		"""
		x, y = x * unit, self.height -  y * unit
		return x, y
 
	#----------------------------------------------------------------------
	def run(self,filename,data):
		"""
		Run the report
		"""
		self.doc = SimpleDocTemplate(filename,pagesize=A4, rightMargin=30,leftMargin=30, topMargin=50,bottomMargin=18)
		self.story = [Spacer(1, 1*cm)]
		self.createLineItems(data)
 
		self.doc.build(self.story, onFirstPage=self.createDocument)
		print ("finished!")
 
	#----------------------------------------------------------------------
	def createDocument(self, canvas, doc):
		"""
		Create the document
		"""
		pdfmetrics.registerFont(TTFont('nomalFont', 'THSarabunNew.ttf'))
		pdfmetrics.registerFont(TTFont('boldFont', 'THSarabunNew Bold.ttf'))

		#Title page A4 size 595 x 842 pixel 72ppi
		 #office name
		office_name = "ใบสต๊อคการ์ด"
		canvas.setFont("boldFont", 18)
		canvas.drawCentredString(297.5,820, office_name)
		
		 #report type
		report_type = "รายการ:  {}                 การใช้งาน: {}".format(self.spare, self.use)
		canvas.setFont("nomalFont", 15)
		canvas.drawString(35,765, report_type)

		#top
		ptext = "รหัสวัสดุ    {}".format(self.codename)
		canvas.setFont("nomalFont",13)
		canvas.drawString(420,810,ptext)
		ptext = "จุดสั่งซื้อ     {}".format(self.reorderpoint)
		canvas.setFont("nomalFont",13)
		canvas.drawString(420,790,ptext)

		#line
		canvas.setLineWidth(.3)
		canvas.line(455,823,550,823)
		canvas.line(455,803,550,803)
		canvas.line(455,783,550,783)

		canvas.line(455,823,455,783)
		canvas.line(550,823,550,783)
		
	#----------------------------------------------------------------------
	def createLineItems(self,datatext):
		"""
		Create the line items
		"""
		pdfmetrics.registerFont(TTFont('nomalFont', 'THSarabunNew.ttf'))
		pdfmetrics.registerFont(TTFont('boldFont', 'THSarabunNew Bold.ttf'))
		stylesheet = getSampleStyleSheet()

		# container for the "Flowable" objects
		#elements = []
		styles=getSampleStyleSheet()
		styleN = styles["Normal"]
		styleT = styles["Title"]


		# Header of Table
		CH1 = Paragraph("<font size=12 name='boldFont'>วันที่</font>", styleT)
		CH2 = Paragraph("<font size=12 name='boldFont'>รายการรับ-จ่ายของ</font>", styleT)
		CH3 = Paragraph("<font size=12 name='boldFont'>ลงชื่อ</font>", styleT)

		CH4 = Paragraph("<font size=12 name='boldFont'>ยกมา</font>", styleT)
		CH5 = Paragraph("<font size=12 name='boldFont'>รับเพิ่ม</font>", styleT)
		CH6 = Paragraph("<font size=12 name='boldFont'>ใช้ไป/ชำรุด</font>", styleT)
		CH7 = Paragraph("<font size=12 name='boldFont'>คงเหลือ</font>", styleT)
		CH8 = Paragraph("<font size=12 name='boldFont'>ผู้รับ / ผู้จ่าย</font>", styleT)
		CH9 = Paragraph("<font size=12 name='boldFont'>ผู้เบิก</font>", styleT)
		CH10 = Paragraph("<font size=12 name='boldFont'>ผจก.</font>", styleT)

		CH11 = Paragraph("<font size=12 name='boldFont'>จำนวน</font>", styleT)
		CH12 = Paragraph("<font size=12 name='boldFont'>ราคา</font>", styleT)
		CH13 = Paragraph("<font size=12 name='boldFont'>จำนวน</font>", styleT)
		CH14 = Paragraph("<font size=10 name='boldFont'>No.ใบแจ้งซ่อม</font>", styleT)
		
		data = [[CH1,CH2,' ',' ',' ',' ',' ',CH3,' ',' '],
				[' ',CH4,CH5,' ',CH6,' ',CH7,CH8,CH9,CH10],
				[' ',' ',CH11,CH12,CH13,CH14,' ',' ',' ',' ']]

		# Data of Table
		textlist = datatext

		count = len(textlist)

		for i in range(count):
			t1 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][0]),styleN)
			t2 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][1]),styleN)
			t3 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][2]),styleN)
			t4 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][3]),styleN)
			t5 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][4]),styleN)
			t6 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][5]),styleN)
			t7 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][6]),styleN)
			t8 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][7]),styleN)
			t9 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][8]),styleN)
			t10 = Paragraph("<font name='nomalFont'>{}</font>".format(textlist[i][9]),styleN)
		
			data.append([t1,t2,t3,t4,t5,t6,t7,t8,t9,t10])
			
		#line of table
		lineoftable = 40
		count2 = len(data)
		countf = lineoftable - count2
		
		for i in range(countf):
			blank = ['','','','','','','','','','']

			if count < lineoftable:
				data.append(blank)
			else:
				pass
		 #reporttest A4 MAX len 18.3 cm
		tableThatSplitsOverPages = Table(data, [2 * cm, 1.5 * cm, 1.5 * cm, 1.5 * cm, 1.3 * cm, 2 * cm, 1.9 * cm, 2.2 * cm, 2.2 * cm,2.2 * cm], repeatRows=1,rowHeights=18)

		tableThatSplitsOverPages.hAlign = 'LEFT'

		style2 = TableStyle([  ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
								('VALIGN',(0,0),(0,-1),'MIDDLE'),
							   ('ALIGN',(0,0),(-1,-1),'CENTER'),
							   ('VALIGN',(0,0),(-1,-1),'MIDDLE'), 
							   ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
							   ('BOX', (0,0), (-1,-1), 1, colors.black),
							   ('SPAN',(0,0),(0,2)),
							   ('SPAN',(1,0),(6,0)),
							   ('SPAN',(7,0),(9,0)),
							   
							   ('SPAN',(1,1),(1,2)),
							   ('SPAN',(2,1),(3,1)),
							   ('SPAN',(4,1),(5,1)),
							   ('SPAN',(6,1),(6,2)),
							   ('SPAN',(7,1),(7,2)),
							   ('SPAN',(8,1),(8,2)),
							   ('SPAN',(9,1),(9,2)),
							   ])

		tableThatSplitsOverPages.setStyle(style2)
 
		self.story.append(tableThatSplitsOverPages)




 ########################################################################
class Report(object):
	""""""
 
	#----------------------------------------------------------------------
	def __init__(self,date='2018-05-02'):
		"""Constructor"""
		self.width, self.height = A4
		self.styles = getSampleStyleSheet()
		self.datefromsql = date
		
 
	#----------------------------------------------------------------------
	def coord(self, x, y, unit=1):
		"""
		http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
		Helper class to help position flowables in Canvas objects
		"""
		x, y = x * unit, self.height -  y * unit
		return x, y
 
	#----------------------------------------------------------------------
	def run(self,filename,data):
		"""
		Run the report
		"""
		self.doc = SimpleDocTemplate(filename,pagesize=A4, rightMargin=30,leftMargin=30, topMargin=50,bottomMargin=18)
		self.story = [Spacer(1, 1*cm)]
		self.createLineItems(data)
 
		self.doc.build(self.story, onFirstPage=self.createDocument)
		print ("finished!")
 
	#----------------------------------------------------------------------
	def createDocument(self, canvas, doc):
		"""
		Create the document
		"""
		pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))

		self.c = canvas
		normal = self.styles["Title"]
 
		header_text = "<font name='chsFont'><b>Uncle Engineer</b></font>"
		p = Paragraph(header_text, normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(0, 12, mm))
 
		ptext = """<font name='chsFont'>ใบเบิกจ่ายวัสดุ</font>"""
 
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(0, 20, mm))
 
		ptext = """<font name='chsFont'>ลงชื่อผู้ขอเบิก.........................................</font>"""
		
		normal.fontSize = 12
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(-65, 110, mm))

		ptext = """<font name='chsFont'>หัวหน้าแผนก/ผู้จัดการฝ่าย.............................................</font>"""
		
		normal.fontSize = 12
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(60, 110, mm))

		ptext = """<font name='chsFont'>F01-WI01-QP-PD-10</font>"""
		
		normal.fontSize = 12
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(80, 115, mm))

		ptext = """<font name='chsFont'>{}</font>""".format(self.datefromsql)
		
		normal.fontSize = 12
		p = Paragraph(ptext, style=normal)
		p.wrapOn(self.c, self.width, self.height)
		p.drawOn(self.c, *self.coord(80, 30, mm))
	#----------------------------------------------------------------------
	def createLineItems(self,datatext):
		"""
		Create the line items
		"""
		pdfmetrics.registerFont(TTFont('chsFont', 'THSarabunNew.ttf'))
		stylesheet = getSampleStyleSheet()

		# container for the "Flowable" objects
		elements = []
		styles=getSampleStyleSheet()
		styleN = styles["Normal"]
		styleT = styles["Title"]


		style_center = ParagraphStyle(name='right', parent=styles['Normal'], fontName='chsFont',
						fontSize=13, alignment=TA_CENTER)
		# styleN.fontSize = 15
		# styleN.alignment=TA_JUSTIFY

		TH15 = ParagraphStyle(name='TH12', fontName='chsFont', fontSize=15, alignment=TA_JUSTIFY)



		a = Image("logo.png")  
		a.drawHeight = 3*cm
		a.drawWidth = 3*cm

		# Header of Table
		CH1 = Paragraph("<font size=13 name='chsFont'>ชนิดวัสดุ(ระบุลักษณะให้ชัดเจน)</font>", styleT)
		CH2 = Paragraph("<font size=13 name='chsFont'>จำนวน</font>", styleT)
		CH3 = Paragraph("<font size=13 name='chsFont'>วัตถุประสงค์การใช้งาน</font>", styleT)
		CH4 = Paragraph("<font size=13 name='chsFont'>ระบุหน่วยให้ชัดเจน</font>", styleT)



		
		data = [[CH1,CH2,CH3],['',CH4,'']]
		#data = [[CH1,CH2,CH3,a,CH5,CH6,CH7]]


		# Data of Table
		textlist = datatext
		#[['1','','/','แผ่นเจียร์ยาว 4 นิ้ว'],[2,'/','','ลวดเชื่อม']]

		count = len(textlist)

		for i in range(count):
			t1 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][0]),styleN)
			t2 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][1]),styleN)
			t3 = Paragraph("<font name='chsFont'>{}</font>".format(textlist[i][2]),styleN)
			
			data.append([t1,t2,t3])

		lineoftable = 9
		count2 = len(data)
		countf = lineoftable - count2

		for i in range(countf):
			blank = ['-','','']

			if count < lineoftable:
				data.append(blank)
			else:
				pass
 
		tableThatSplitsOverPages = Table(data, [6 * cm, 3 * cm, 9 * cm], repeatRows=1)

		tableThatSplitsOverPages.hAlign = 'RIGHT'

		tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
							   ('VALIGN',(0,0),(-1,-1),'TOP'),
							   ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
							   ('BOX',(0,0),(-1,-1),1,colors.black),
							   ('BOX',(0,0),(0,-1),1,colors.black)])

		style2 = TableStyle([  ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
								('SPAN',(0,0),(0,1)),
								('SPAN',(2,0),(2,1)),
								('VALIGN',(0,0),(0,-1),'TOP'),
							   ('ALIGN',(0,0),(-1,-1),'CENTER'),
							   ('VALIGN',(0,0),(-1,-1),'TOP'), 
							   ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
							   ('BOX', (0,0), (-1,-1), 1, colors.black),
							   ])
		# ('SPAN') is a combine (0,0),(1,1) column x=0 to x=1 y=0 to y=1 is row 0 to row 1
		# tblStyle.add('BACKGROUND',(0,0),(1,0),colors.white)
		# tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)

		tableThatSplitsOverPages.setStyle(style2)
 
		self.story.append(tableThatSplitsOverPages)
		# -------------------END OF REPORT---------------------------




def focusquantity(event=None):
	SE2.focus()

class Spinbox(ttk.Widget):
	def __init__(self, master, **kw):
		ttk.Widget.__init__(self, master, 'ttk::spinbox', kw)

def reportpdf():

	# data = [['1',' ','/','แผ่นเจียร์บาง 4 นิ้ว AC60','12.84/แผ่น','5/7/60','150'],
	# 		['2',' ','/','แผ่นเจียร์บาง 5 นิ้ว AC60','15.89/แผ่น','6/7/60','550'],
	# 		['3',' ','/','แผ่นเจียร์บาง 6 นิ้ว AC60','17.85/แผ่น','8/7/60','250']
	# ]
	try:
		ts = sparelist4.selection()
		x = sparelist4.item(ts)
		wd_code4export = x['values'][0]
		print(wd_code4export)
	except:
		wd_code4export = 'WD0001'

	datatopdf = []

	with conn:
		c.execute("""SELECT * FROM wd_list1 WHERE wd_id = (:id)""",{'id':wd_code4export})
		wd_list = c.fetchall()
	conn.commit()
	print(wd_list)
	
	for i in wd_list:
		reportdata = [i[4]+"-"+i[5],str(i[6]),i[9]]
		dateofreport = i[2]
		datatopdf.append(reportdata)
	

	print(wd_list)
	print('Success')

	data = [['น้ำยาหม้อน้ำ','2','ใช้เติมหม้อต้มน้ำสกิมบล็อก'],
			['เทปพันสายไฟ','3','ใช้พันสายไฟเครื่องตีน้ำ'],
			['น้ำยา sonax','2','ใช้ฉีดสนิมโซ่เครน']
	]

	
	

	t = Report(dateofreport)
	dt1 = datetime.now().strftime('%Y-%m-%d %H%M%S')
	reportname = 'Withdraw-'+dt1+'.pdf'
	t.run(reportname,datatopdf)
	messagebox.showinfo('Report Exporting',reportname + ' was Exported')



def reportpdfoffice():
	
	try:
		ts = sparelist4.selection()
		x = sparelist4.item(ts)
		wd_code4export = x['values'][0]
		print(wd_code4export)
	except:
		wd_code4export = 'WD0001'

	datatopdf = []

	with conn:
		c.execute("""SELECT * FROM wd_list1 WHERE wd_id = (:id)""",{'id':wd_code4export})
		wd_list = c.fetchall()
	conn.commit()
	print(wd_list)



def createFolder(directory):
	try:
		if not os.path.exists(directory):
			os.makedirs(directory)
	except OSError:
		print('Error: Creating Directory. ' + directory)

# createFolder('./test/')
# createFolder('./test/b/c/d')




global conn
global c

dbname = 'DB-Stock.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS sparepart_list (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				sp_code text,
				sp_type text,
				sp_cat text,
				sp_name text,
				sp_model text,
				sp_price real,
				sp_quantity integer,
				sp_lastpur text,
				sp_reorder integer,
				sp_by text,
				sp_supp text,
				sp_for text

		  )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS cat_list (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				cat_prefix text,
				cat_name text,
				cat_desc text
				
		  )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS wd_list (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				wd_id text,
				wd_date text,
				wd_idpartlist text,
				wd_partlist text,
				wd_amount integer,
				wd_price real,
				wd_total real,
				wd_reason text,
				wd_by text,
				wd_approved text
				
		  )	""")


c.execute(""" CREATE TABLE IF NOT EXISTS wd_list1 (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				wd_id text,
				wd_date text,
				wd_idpartlist text,
				wd_partlist text,
				wd_model text,
				wd_amount integer,
				wd_price real,
				wd_total real,
				wd_reason text,
				wd_by text,
				wd_approved text,
				Enobd text,
				Eauthor text,
				ttbefore int
				
		  )	""")
#---------------GUI Part----------------


def SP_count():

	with conn:
		c.execute("""SELECT COUNT(*) FROM sparepart_list """)
		y = c.fetchall()
		print(y)
		messagebox.showinfo('Total Count of Sparepart','Total: {}'.format(y[0][0]))


#-------------------FIREBASE--------------------

def selectdata(ID):
	with conn:
		c.execute("SELECT * FROM wd_list1 WHERE wd_id = ?",([ID]) )
		alldata = c.fetchall()
		
	return alldata

def synctofirebase():
	pass
	

def stockcardnew():

	reportdata = []

	data = selectdata()

	for i in data:
		data2 = [i[2],'-','-',i[7],i[6],i[1],'-',' ',' ',' ']
		reportdata.append(data2)




GUI = Tk()

author = StringVar()

GUI.state('zoomed')
#GUI.attributes('-fullscreen', True)
#w, h = GUI.winfo_screenwidth(), GUI.winfo_screenheight()
#GUI.geometry("%dx%d+0+0" % (w, h))
GUI.geometry('600x600+30+30')
GUI.title('Uncle Engineer - Machine')
GUI.bind('<F1>',focusquantity )

f = tkFont.Font(family='TH Sarabun New', size=15)
s = ttk.Style()
s.configure('.', font=f)

def expxl():
	pass

def updatesparepart():

	with conn:
		c.execute("""SELECT * FROM sparepart_list""")
		sp_list = c.fetchall()
	conn.commit()
	print('Success')

	try:
		x = sparelist.get_children()
		count = len(x)
		for z in range(count):
			sparelist.delete(x[z])
			
	except:
		pass


	for it in sp_list:
		sparelist.insert('','end',values=it[1:])
		


#------------Menu------------
def menu():
	menubar = Menu(GUI)
	#----------------Menu File > Export to Excel > Exit---------
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label='Export to PDF', command=reportpdf)
	filemenu.add_command(label='Export to PDF (office)', command=reportpdfoffice)
	filemenu.add_separator()
	filemenu.add_command(label='Upload to Server', command=synctofirebase)
	filemenu.add_command(label='Exit', command=GUI.quit)

	menubar.add_cascade(label='File', menu=filemenu)
	#----------------Menu File > Export to Excel > Exit---------
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
	up_sparepartmenu.add_command(label='Update Spare Part', command=updatesparepart)
	up_sparepartmenu.add_command(label='Update', command=expxl)
	up_sparepartmenu.add_command(label='Count Spare Part', command=SP_count)
	menubar.add_cascade(label='Update', menu=up_sparepartmenu)

	GUI.config(menu=menubar)
menu()
#------------Tab------------
def tab():
	global Tab
	global F0
	global F1
	global F2
	global F3
	global F4
	global F5
	Tab = Notebook(GUI, height=700)
	F0 = Frame(Tab, width=200, height=500)
	F1 = Frame(Tab, width=200, height=500)
	F2 = Frame(Tab, width=200, height=500)
	F3 = Frame(Tab, width=200, height=500)
	F4 = Frame(Tab, width=200, height=500)
	F5 = Frame(Tab, width=200, height=500)
	#font=('TH Sarabun New',20)
	Tab.add(F0, text='รายการสต็อก')
	Tab.add(F1, text='เบิกจ่ายวัสดุ')
	Tab.add(F2, text='รายการอนุมัติ')
	Tab.add(F3, text='สั่งซื้อวัสดุ/อะไหล่')
	Tab.add(F4, text='เพิ่มวัสดุเข้าระบบ')
	Tab.add(F5, text='รายงานสรุป')
	Tab.pack(fill=BOTH, padx=10, pady=10)
tab()


#F4-------





def SPAD_insert(event=None):
	def confirm():

		with conn:
			c.execute("""INSERT INTO sparepart_list VALUES (

				:ID,\
				:sp_code,\
				:sp_type,\
				:sp_cat,\
				:sp_name,\
				:sp_model,\
				:sp_price,\
				:sp_quantity,\
				:sp_lastpur,\
				:sp_reorder,\
				:sp_by,\
				:sp_supp,\
				:sp_for

				)""",

				{'ID':None,
				'sp_code':sp_code.get(),
				'sp_type':sp_type.get(),
				'sp_cat':sp_cat.get(),
				'sp_name':sp_name.get(),
				'sp_model':sp_model.get(),
				'sp_price':float(sp_price.get()),
				'sp_quantity':int(sp_quantity.get()),
				'sp_lastpur':sp_lastpur.get(),
				'sp_reorder':int(sp_reorder.get()),
				'sp_by':sp_by.get(),
				'sp_supp':sp_supp.get(),
				'sp_for':sp_for.get() }
				)
			conn.commit()

		print('Success')

	def cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ","ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		confirm()
	else:
		cancel()			

SPAD_LBF1 = LabelFrame(F4, text='เพิ่มวัสดุเข้าระบบ' ,font=('TH Sarabun New',15))
SPAD_LBF1.grid(row=0,column=0,padx=5,pady=5)

sp_code = StringVar()
sp_name = StringVar()
sp_model = StringVar()
sp_price = StringVar()
sp_quantity = StringVar()
sp_by = StringVar()
sp_reorder = StringVar()
sp_for = StringVar()

SPAD_text = ['รหัส','ประเภท','หมวด','ชื่ออะไหล่','รุ่น','ราคา','จำนวน','สั่งซื้อล่าสุด','จุดสั่งซื้อ','ผู้รับเข้า','Suplier','การใช้งาน']
SPAD_cat = ['หมวด A','หมวด B','หมวด C','หมวด D','หมวด E','หมวด F','หมวด G','หมวด H','หมวด I','หมวด J','หมวด K']
SPAD_sup = ['Uncle Engineer','Supplier 1','Supplier 2','Supplier 3','Supplier 4','Supplier 5']
SPAD_type = ['อะไหล่','วัสดุสิ้นเปลือง']

for i,j in enumerate(SPAD_text):
	SPAD_L1 = ttk.Label(SPAD_LBF1,text=j,font=('TH Sarabun New',15))
	SPAD_L1.grid(row=i,column=0,pady=5,padx=5,sticky='nw')

SPAD_E1 = ttk.Entry(SPAD_LBF1, textvariable=sp_code, font=('TH Sarabun New',15),width=22)
SPAD_E1.grid(row=0, column=1, padx=5, pady=5, sticky='w')
#Combo box *********
combofont=('TH Sarabun New', '15')
GUI.option_add('*TCombobox*Listbox.font', combofont)

sp_type = ttk.Combobox(SPAD_LBF1, values = SPAD_type, font=('TH Sarabun New', 15))
sp_type.set('อะไหล่')
sp_type.grid(row=1, column=1,padx=5,pady=5, sticky='w')

sp_cat = ttk.Combobox(SPAD_LBF1, values = SPAD_cat, font=('TH Sarabun New', 15))
sp_cat.set('หมวด A')
sp_cat.grid(row=2, column=1,padx=5,pady=5, sticky='w')

SPAD_E3 = ttk.Entry(SPAD_LBF1, textvariable=sp_name, font=('TH Sarabun New',15),width=22)
SPAD_E3.grid(row=3, column=1, padx=5, pady=5, sticky='w')

SPAD_E4 = ttk.Entry(SPAD_LBF1, textvariable=sp_model, font=('TH Sarabun New',15),width=22)
SPAD_E4.grid(row=4, column=1, padx=5, pady=5, sticky='w')

SPAD_E5 = ttk.Entry(SPAD_LBF1, textvariable=sp_price, font=('TH Sarabun New',15),width=22)
SPAD_E5.grid(row=5, column=1, padx=5, pady=5, sticky='w')

SPAD_E6 = ttk.Entry(SPAD_LBF1, textvariable=sp_quantity, font=('TH Sarabun New',15),width=22)
SPAD_E6.grid(row=6, column=1, padx=5, pady=5, sticky='w')

sp_lastpur = DateEntry(SPAD_LBF1, width=18, backgroud='blue', foreground='white',
	borderwidth=2, font=('TH, Sarabun New',12))
sp_lastpur.grid(row=7, column=1, padx=5, pady=5, sticky='w')


SPAD_E8_0 = ttk.Entry(SPAD_LBF1, textvariable=sp_reorder, font=('TH Sarabun New',15),width=22)
SPAD_E8_0.grid(row=8, column=1, padx=5, pady=5, sticky='w')


SPAD_E8 = ttk.Entry(SPAD_LBF1, textvariable=sp_by, font=('TH Sarabun New',15),width=22)
SPAD_E8.grid(row=9, column=1, padx=5, pady=5, sticky='w')

sp_supp = ttk.Combobox(SPAD_LBF1, values = SPAD_sup, font=('TH Sarabun New', 15))
sp_supp.set('Uncle Engineer')
sp_supp.grid(row=10, column=1,padx=5,pady=5, sticky='w')


sp_for_e = ttk.Entry(SPAD_LBF1, textvariable=sp_for, font=('TH Sarabun New', 15),width=22)
sp_for_e.grid(row=11, column=1,padx=5,pady=5, sticky='w')


s = ttk.Style()
s.configure('my.TButton', font=('TH Sarabun New', 15))
SPAD_B1 = ttk.Button(SPAD_LBF1,text='Add', style='my.TButton', command=SPAD_insert)
SPAD_B1.grid(row=12, column=1,padx=5,pady=5, sticky='w')

#-------------Treeview

sparepartheader= ['รหัส', 'ประเภท', 'หมวด','ชื่ออะไหล่/วัสดุ','รุ่น','ราคา','จำนวน','สั่งซื้อล่าสุด','จุดสั่งซื้อ','รับเข้าโดย','Suplier']
sparelist_width = [(20,40),(30,50),(40,50),(50,70),(30,50),(30,50),(30,40),(30,50),(30,40),(30,60),(30,200)]

LB3 = Frame(F0, width=200)
LB3.pack(fill=X)


sparelist = ttk.Treeview(LB3,columns=sparepartheader, show="headings", height=50)
for i,col in enumerate(sparepartheader):
	sparelist.heading(col, text=col.title())
	sparelist.column(col,minwidth=sparelist_width[i][0],width=sparelist_width[i][1])

sparelist.pack(fill=BOTH)
#sparelist2.bind("<Double-1>",deleteitem)
style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))

def stockcard():
	ts = sparelist.selection()
	x = sparelist.item(ts)
	print(x['values'][0])
	messagebox.showinfo('Stockcard','กำลังออกใบสต็อกการ์ด: {}'.format(x['values'][0]))

	reportdata = []

	res = str(x['values'][0])

	print("REALDATATA: ",res)
	


	
	ID = str(x['values'][0])
	with conn:
		c.execute("SELECT * FROM wd_list1 WHERE wd_idpartlist = ?",([ID]))
		Y = c.fetchall()
		print("Raw Data Y: ",Y)
		for i in Y:
			data2 = [i[2],i[-1],'-',i[7],i[6],i[-3],i[-1]-i[6],i[-2],' ',' ']
			reportdata.append(data2)

	print("REPORT DATA: ",reportdata)
	dt1 = datetime.now().strftime('%Y-%m-%d')


	with conn:
		c.execute("SELECT * FROM sparepart_list WHERE sp_code = ?",([ID]))
		Z = c.fetchall()
		print("SPAREPART: ",Z)

	#codename,reorderpoint,spare,use

	t = Stockcard(Z[0][1],Z[0][9],Z[0][4],Z[0][-1])


	reportname = 'Stockcard-'+ str(x['values'][0]) +dt1+'.pdf'
	t.run(reportname,reportdata)
	subprocess.Popen(reportname,shell=True)


def deletesparepart():
	with conn:
		c.execute("SELECT * FROM wd_list1 WHERE wd_idpartlist = ?",([ID]))
		Y = c.fetchall()



rmenu = Menu(GUI,tearoff=0)
rmenu.add_command(label='Delete', command=deletesparepart)
rmenu.add_command(label='Stockcard', command=stockcard)

def popup(event):
	rmenu.post(event.x_root,event.y_root)

sparelist.bind('<Button-3>', popup)

#---------------------------Withdraw------------------



def searchsparepart(event=None):
	setext = '%'+ searchtext.get() + '%'
	type2 = sp_type2.get()
	cat2 = sp_cat2.get()
	with conn:
		c.execute("""SELECT * FROM sparepart_list WHERE sp_type = (:type) and sp_cat = (:cat) and sp_name LIKE (:name)""",{'type':type2,'cat':cat2,'name':setext})
		sp_list = c.fetchall()
	conn.commit()
	print('Success')

	try:
		x = sparelist2.get_children()
		count = len(x)
		for z in range(count):
			sparelist2.delete(x[z])
	except:
		pass


	for it in sp_list:
		
		sparelist2.insert('','end',values=it[1:])



global codestate
codestate = 0

global datatolist

global total_datatolist2
total_datatolist = []
total_datatolist2 = [] #Data for insert into table

wd_state = StringVar()


def addto_withdrawlist():

	def addto_confirm():

		wd_state.set('1')
		
		global codestate

		codestate = 1

		for i in total_datatolist2:
			print(i)
			with conn:
				c.execute("""INSERT INTO wd_list1 VALUES (

					:ID,\
					:wd_id,\
					:wd_date,\
					:wd_idpartlist,\
					:wd_partlist,\
					:wd_model,\
					:wd_amount,\
					:wd_price,\
					:wd_total,\
					:wd_reason,\
					:wd_by,\
					:wd_approved,\
					:Enobd,\
					:Eauthor,\
					:ttbefore

					)""",
					{'ID':i[0],
					'wd_id': i[1],
					'wd_date': i[2],
					'wd_idpartlist': i[3],
					'wd_partlist': i[4],
					'wd_model':i[5],
					'wd_amount': i[6],
					'wd_price': i[7],
					'wd_total': i[8],
					'wd_reason': i[9],
					'wd_by':i[10],
					'wd_approved': i[11],
					'Enobd':i[12],
					'Eauthor':i[13],
					'ttbefore':i[14] })

		conn.commit()
		
		
		
		try:
			x = sparelist3.get_children()
			count = len(x)
			for z in range(count):
				sparelist3.delete(x[z])
				
		except:
			pass



	def addto_cancel():
		pass

	ok = messagebox.askyesno("ยืนยันการทำรายการ","ต้องการบันทึกข้อมูลใช่หรือไม่?")
	if ok == True:
		addto_confirm()

	else:
		addto_cancel()

	global total_datatolist2
	total_datatolist2 = []
	wd_state.set('1')

# global codestate
# codestate = 1
codestr = StringVar()

def countquantity():
	global ttbefore
	try:
		query = """SELECT * FROM sparepart_list WHERE sp_code = {}""".format(codestr.get())
		
		with conn:

			c.execute(query)
			
			totalbefore = c.fetchall()
			conn.commit()
			print("ALL in table (Just Quan)",totalbefore[7])
			#print("TOTAL BEFORE ORDER: ",(totalbefore[0][0]))
			ttbefore = totalbefore[0][0]
	except:
		query = """SELECT * FROM sparepart_list WHERE sp_code = {}""".format(codestr.get())
		
		with conn:

			c.execute(query)
			
			totalbefore = c.fetchall()
			conn.commit()
			print("ALL in table (Just Quan)",totalbefore[7])
		
		
		print('Cant connect sparepart')
		ttbefore = 0

def checkcurrent(code):
	with conn:
		c.execute("SELECT sp_quantity FROM sparepart_list WHERE sp_code = ?",([code]))
		X = c.fetchall()
		print("THIS IS CURRENT: ",X[0][0])
		return X[0][0]


def addto_wdlist():
	
	global codestate

	spq = int(spinquantity.get())
	obj1 = objective.get()
	wdb = withdrawby.get()
	enbod = Enobd.get()
	eauthor = Eauthor.get()
	print(enbod,eauthor)
	dt1 = datetime.now().strftime('%Y-%m-%d')
	approved = 'ผู้จัดการ'
	print(dt1)

	if enbod == '' and eauthor == '':
		messagebox.showwarning('Please Input Data','กรุณากรอกเลขที่ใบแจ้งซ่อม และ ลงชื่อผู้จ่าย')
	else:
		try:
		
			with conn:
				c.execute("""SELECT wd_id from wd_list1""")
				countcode = c.fetchall()
				conn.commit()
			
			print("COUNT in Table",countcode[-1][0])
			nextid = countcode[-1][0]
			wd_generatecode0 = nextid[-4:]

			print(wd_generatecode0)
		except:
			wd_generatecode0 = '0001'
		

		
		
		if wd_state == '1':
			if int(wd_generatecode0) >= 10 and int(wd_generatecode0) <100:
				wd_generatecode = 'WD00' + str(int(wd_generatecode0)+1)
			elif int(wd_generatecode0) >= 100 and int(wd_generatecode0) <1000:
				wd_generatecode = 'WD0' + str(int(wd_generatecode0)+1)
			else:
				wd_generatecode = 'WD000' + str(int(wd_generatecode0)+1)
			#codestate = 0

		else:
			if int(wd_generatecode0) >= 10 and int(wd_generatecode0) <100:
				wd_generatecode = 'WD00' + str(int(wd_generatecode0)+1)
			elif int(wd_generatecode0) >= 100 and int(wd_generatecode0) <1000:
				wd_generatecode = 'WD0' + str(int(wd_generatecode0)+1)
			else:
				wd_generatecode = 'WD000' + str(int(wd_generatecode0)+1)
		
		print(wd_generatecode)
		#wd_generatecode = '000'
		wd_state.set('0')
		#sparepartheader3= ['รหัส','ชื่ออะไหล่/วัสดุ','รุ่น','จำนวน','วัตถุประสงค์ของการใช้งาน','ลงชื่อผู้เบิก','วันที่']
		global datatolist

		global wd_code1

		try:
			ts = sparelist2.selection()
			x = sparelist2.item(ts)
			wd_code1 = x['values'][0]
			codestr.set(wd_code1)
			wd_name1 = x['values'][3]
			wd_model1 = x['values'][4]
			wd_price = x['values'][5]
			print(wd_price)
			datatolist = [wd_code1,wd_name1,wd_model1,spq,obj1,wdb,dt1]
			sparelist3.insert('','end',values=datatolist)
			total_datatolist.append(datatolist)
			print("CODE STR: ",codestr)

		except:
			messagebox.showerror('ข้อมูล','กรุณาเลือกรายการที่ต้องการเบิก')



		
		ttbefore = checkcurrent(str(wd_code1))
		totaldata = [None,wd_generatecode,dt1,wd_code1,wd_name1,wd_model1,spq,wd_price, int(spq)*float(wd_price),obj1,wdb,"ผู้จัดการ",enbod,eauthor,ttbefore]
		print(totaldata)
		total_datatolist2.append(totaldata)
	


sparepartheader2= ['รหัส', 'ประเภท', 'หมวด','ชื่ออะไหล่/วัสดุ','รุ่น','ราคา','จำนวน','สั่งซื้อล่าสุด','จุดสั่งซื้อ','รับเข้าโดย','Suplier','ใช้งาน']
sparelist_width2 = [(20,40),(30,50),(50,120),(50,70),(30,50),(30,50),(30,60),(30,50),(30,70),(30,70),(30,70),(30,70)]

WDF1 = Frame(F1, width=200)
WDF1.pack(fill=X)

WDF2 = LabelFrame(F1, width=200, text='ค้นหา', font=('TH Sarabun New', 15))
WDF2.pack()
WDF2.bind('<F2>',focusquantity )


sparelist2 = ttk.Treeview(WDF1,columns=sparepartheader2, show="headings", height=10)
for i,col in enumerate(sparepartheader2):
	sparelist2.heading(col, text=col.title())
	sparelist2.column(col,minwidth=sparelist_width2[i][0],width=sparelist_width2[i][1])

sparelist2.pack(fill=BOTH)

#--------------Select Type---------------
WDL0 = ttk.Label(WDF2, text='เลือกหมวด').grid(row=0, column=0,padx=5,pady=5, sticky='w')

SPAD_type2 = ['อะไหล่','วัสดุสิ้นเปลือง']
sp_type2 = ttk.Combobox(WDF2, values = SPAD_type2, font=('TH Sarabun New', 15))
sp_type2.set('อะไหล่')
sp_type2.grid(row=0, column=1,padx=5,pady=5, sticky='w')


#--------------Select Catagorie---------------
WDL1 = ttk.Label(WDF2, text='เลือกหมวด').grid(row=0, column=2,padx=5,pady=5, sticky='w')

SPAD_cat2 = ['หมวด A','หมวด B','หมวด C','หมวด D','หมวด E','หมวด F','หมวด G','หมวด H','หมวด I','หมวด J','หมวด K']
sp_cat2 = ttk.Combobox(WDF2, values = SPAD_cat2, font=('TH Sarabun New', 15))
sp_cat2.set('หมวด A')
sp_cat2.grid(row=0, column=3,padx=5,pady=5, sticky='w')

searchtext = StringVar()

SE1 = ttk.Entry(WDF2, textvariable=searchtext, font=('TH Sarabun New', 15))
SE1.grid(row=0, column=4,padx=5,pady=5, sticky='w')
SE1.bind('<Return>', searchsparepart)

searchbutton = ttk.Button(WDF2,text='ค้นหา', style='my.TButton',command=searchsparepart)
searchbutton.grid(row=0, column=5,padx=5,pady=5, sticky='w')


spinquantity = StringVar()
spinquantity.set(1)
withdrawby =StringVar()
objective = StringVar()
withdrawby.set('ลงชื่อผู้เบิก')

WDL2 = ttk.Label(WDF2, text='จำนวน').grid(row=1, column=0,padx=5,pady=5, sticky='w')
SE2 = ttk.Entry(WDF2, textvariable=spinquantity, font=('TH Sarabun New', 15),width=22)
SE2.grid(row=1, column=1,padx=5,pady=5, sticky='w')

WDL3 = ttk.Label(WDF2, text='วัตถุประสงค์ของการใช้งาน').grid(row=1, column=2,padx=5,pady=5, sticky='w')
SE3 = ttk.Entry(WDF2, textvariable=objective, font=('TH Sarabun New', 15),width=22)
SE3.grid(row=1, column=3,padx=5,pady=5, sticky='w')

SE4 = ttk.Entry(WDF2, textvariable=withdrawby, font=('TH Sarabun New', 15))
SE4.grid(row=1, column=4,padx=5,pady=5, sticky='w')

addproduct = ttk.Button(WDF2,text='เพิ่ม', style='my.TButton',command=addto_wdlist)
addproduct.grid(row=1, column=5,padx=5,pady=5, sticky='w')
# sp2 = Spinbox(WDF2,from_=0, to=100,textvariable=spinquantity,font=('TH Sarabun New', 14))
# sp2.grid(row=1, column=4,padx=5,pady=5, sticky='w')


# ----------------------------WITH DRAW LIST-----------------------



WDF3 = Frame(F1, width=200)
WDF3.pack(pady=10)

sparepartheader3= ['รหัส','ชื่ออะไหล่/วัสดุ','รุ่น','จำนวน','วัตถุประสงค์ของการใช้งาน','ลงชื่อผู้เบิก','วันที่']
sparelist_width3 = [(80,80),(200,200),(120,120),(70,70),(250,250),(100,100),(80,80)]


sparelist3 = ttk.Treeview(WDF3,columns=sparepartheader3, show="headings", height=8)
for i,col in enumerate(sparepartheader3):
	sparelist3.heading(col, text=col.title())
	sparelist3.column(col,minwidth=sparelist_width3[i][0],width=sparelist_width3[i][1])

sparelist3.pack(fill=BOTH)

LastButton = Frame(F1)
LastButton.pack()


nobreakdown = ttk.Label(LastButton,text='เลขที่ใบแจ้งซ่อม', font=('TH Sarabun New', 15))
nobreakdown.grid(row=0,column=0,padx=5)

Enobd = StringVar() # ----------------------------
 
Enobreakdown = ttk.Entry(LastButton, textvariable=Enobd, font=('TH Sarabun New', 15))
Enobreakdown.grid(row=0,column=1,padx=5)

nobreakdown = ttk.Label(LastButton,text='ลงชื่อผู้จ่าย', font=('TH Sarabun New', 15))
nobreakdown.grid(row=0,column=2,padx=5)

Eauthor = StringVar() # ----------------------------

Enobreakdown = ttk.Entry(LastButton, textvariable=Eauthor, font=('TH Sarabun New', 15))
Enobreakdown.grid(row=0,column=3,padx=5)

addtowithdraw = ttk.Button(LastButton,text='เพิ่มใบเบิกจ่ายวัสดุ', style='my.TButton',command=addto_withdrawlist)
addtowithdraw.grid(row=0, column=4,padx=5,pady=5)

#----------rightclickmenu for clear everything in list
def clearhistory():
	total_datatolist2 = []
	try:
		x = sparelist3.get_children()
		count = len(x)
		for z in range(count):
			sparelist3.delete(x[z])
			
	except:
		pass



amenu2 = Menu(GUI,tearoff=0)
amenu2.add_command(label='clear', command=clearhistory)


def popup3(event):
	amenu2.post(event.x_root,event.y_root)

sparelist3.bind('<Button-3>', popup3)


#--------------WITHDRAW LIST------------------
#wd_approved = (:app) WHERE wd_id = (:code)"
def updatewithdraw():

	with conn:
		c.execute("""SELECT wd_id,wd_by,SUM(wd_total) AS totalprice,wd_date FROM wd_list1  WHERE wd_approved = 'ผู้จัดการ'  GROUP BY wd_id """)
		sp_list4 = c.fetchall()
	conn.commit()
	print(sp_list4)
	print('Success')

	try:
		x = sparelist4.get_children()
		count = len(x)
		for z in range(count):
			sparelist4.delete(x[z])
			
	except:
		pass
	print(sp_list4)

	for it in sp_list4:
		sparelist4.insert('','end',values=it[:4])

'''
with conn:
		c.execute("UPDATE wd_list1 SET pd_quantity = (pd_quantity - (:qt)) WHERE pd_code = (:code)",{'qt':q,'code':cd})
		conn.commit()
'''
def approvedlist():
	print('Approved')

def stockcard2():
	try:

		ts = sparelist4.selection()
		x = sparelist4.item(ts)
		print(x['values'][0])

		y = messagebox.askyesno('Approved','อนมัติรายการ {} ใช่หรือไม่?'.format(x['values'][0]))
		
		print(y)
		print(type(y))
		
		if y == True:
			with conn:
				c.execute("UPDATE wd_list1 SET wd_approved = (:app) WHERE wd_id = (:code)",{'app':'อนุมัติแล้ว','code':x['values'][0]})
				conn.commit()
			messagebox.showinfo('Success','อนมัติรายการ {} แล้ว'.format(x['values'][0]))

			with conn:
				c.execute("SELECT wd_idpartlist,wd_amount FROM wd_list1 WHERE wd_id = (:code)",{'code':x['values'][0]})
				parts = c.fetchall()

			print(parts)
			print('---------')
			for i in parts:
				print(i[0],i[1])
				
				with conn:
					c.execute("UPDATE sparepart_list SET sp_quantity = sp_quantity - (:amout) WHERE sp_code = (:ID)",{'amout':i[1],'ID':i[0]})
				conn.commit()

		else:
			messagebox.showinfo('Cancel','ยกเลิกการอนุมัติรายการ {}'.format(x['values'][0]))
	except:
		messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการอนุมัติ')

	
def deletewithdraw():
	try:
		ts = sparelist4.selection()
		x = sparelist4.item(ts)
		print(x['values'][0])

		y = messagebox.askyesno('Delete','ลบรายการ {} ใช่หรือไม่?'.format(x['values'][0]))

		
		if y == True:
			with conn:
				c.execute("DELETE FROM wd_list1 WHERE wd_id = (:code)",{'code':x['values'][0]})
				conn.commit()
			messagebox.showinfo('Success','ลบรายการ {} แล้ว'.format(x['values'][0]))
		else:
			messagebox.showinfo('Cancel','ยกเลิกการลบรายการ {}'.format(x['values'][0]))
	except:
		messagebox.showinfo('Cancel','กรุณาเลือกรายการที่ต้องการลบ')






sparepartheader4= ['รหัส', 'ลงชื่อผู้เบิก','ค่าใช้จ่าย','วันที่']
sparelist_width4 = [(80,80),(200,200),(120,120),(120,120)]

WDF2_2 = Frame(F2, width=200)
WDF2_2.pack(fill=X)

WDF2 = LabelFrame(F2, width=200, text='ค้นหา', font=('TH Sarabun New', 15))
WDF2.pack()



sparelist4 = ttk.Treeview(WDF2_2,columns=sparepartheader4, show="headings", height=10)
vsb = ttk.Scrollbar(WDF2_2, orient="vertical", command=sparelist4.yview)
vsb.pack(side=RIGHT,fill=BOTH)

for i,col in enumerate(sparepartheader4):
	sparelist4.heading(col, text=col.title())
	sparelist4.column(col,minwidth=sparelist_width4[i][0],width=sparelist_width4[i][1])

sparelist4.pack(fill=BOTH)

#----------------Right Click Menu--------------
amenu = Menu(GUI,tearoff=0)
amenu.add_command(label='Delete', command=deletewithdraw)
amenu.add_command(label='Approved', command=stockcard2)

def popup2(event):
	amenu.post(event.x_root,event.y_root)

sparelist4.bind('<Button-3>', popup2)
#------------------------------------------------

Confirm_ButtonFrame = Frame(WDF2_2)
Confirm_ButtonFrame.pack()

WDB2 = ttk.Button(Confirm_ButtonFrame,text='อัพเดต', style='my.TButton',command=updatewithdraw)
WDB2.grid(row=0,column=0,padx=5,pady=5)

WDB3 = ttk.Button(Confirm_ButtonFrame,text='อนุมัติรายการ', style='my.TButton',command=stockcard2)
WDB3.grid(row=0,column=1,padx=5,pady=5)


#--------------WITHDRAW APROVED LIST------------------
def updatewithdraw2():

	with conn:
		c.execute("""SELECT wd_id,wd_by,SUM(wd_total)  AS totalprice,wd_date, wd_approved FROM wd_list1  WHERE wd_approved = 'อนุมัติแล้ว' GROUP BY wd_id """)
		sp_list5 = c.fetchall()
	conn.commit()
	print(sp_list5)
	print('Success')

	try:
		x = sparelist5.get_children()
		count = len(x)
		for z in range(count):
			sparelist5.delete(x[z])
			
	except:
		pass
	print(sp_list5)

	for it in sp_list5:
		sparelist5.insert('','end',values=it[:5])



sparepartheader4= ['รหัส', 'ลงชื่อผู้เบิก','ค่าใช้จ่าย','วันที่','อนุมัติแล้ว']
sparelist_width5 = [(80,80),(200,200),(120,120),(120,120),(120,120)]

WDF2_3 = Frame(F2, width=200)
WDF2_3.pack(fill=X)

WDF2 = LabelFrame(F2, width=200, text='ค้นหา', font=('TH Sarabun New', 15))
WDF2.pack()



sparelist5 = ttk.Treeview(WDF2_3,columns=sparepartheader4, show="headings", height=10)
vsb = ttk.Scrollbar(WDF2_3, orient="vertical", command=sparelist5.yview)
vsb.pack(side=RIGHT,fill=BOTH)

for i,col in enumerate(sparepartheader4):
	sparelist5.heading(col, text=col.title())
	sparelist5.column(col,minwidth=sparelist_width5[i][0],width=sparelist_width5[i][1])

sparelist5.pack(fill=BOTH)

WDB2 = ttk.Button(WDF2_3,text='อัพเดตรายการอนุมัติแล้ว', style='my.TButton',command=updatewithdraw2)
WDB2.pack(padx=5,pady=5)


#--------------Reorder Point LIST------------------
def reorderpoint():

	with conn:
		c.execute("""SELECT * FROM sparepart_list  WHERE sp_quantity <= sp_reorder """)
		sp_list6 = c.fetchall()
	conn.commit()
	print("SPLIST for PR",sp_list6)
	print('Success')

	try:
		x = sparelist6.get_children()
		count = len(x)
		for z in range(count):
			sparelist6.delete(x[z])
			
	except:
		pass
	print(sp_list6)

	for it in sp_list6:
		sparelist6.insert('','end',values=it[1:])


sparepartheader5= ['รหัส', 'ประเภท', 'หมวด','ชื่ออะไหล่/วัสดุ','รุ่น','ราคา','จำนวน','สั่งซื้อล่าสุด','จุดสั่งซื้อ','รับเข้าโดย','Suplier']
sparelist_width6 = [(20,40),(30,50),(40,50),(50,70),(30,50),(30,50),(30,40),(30,50),(30,40),(30,60),(30,200)]


WDF2_4 = Frame(F3, width=200)
WDF2_4.pack(fill=X)

WDF3 = LabelFrame(F3, width=200, text='ค้นหา', font=('TH Sarabun New', 15))
WDF3.pack()



sparelist6 = ttk.Treeview(WDF2_4,columns=sparepartheader5, show="headings", height=10)
vsb = ttk.Scrollbar(WDF2_4, orient="vertical", command=sparelist6.yview)
vsb.pack(side=RIGHT,fill=BOTH)

for i,col in enumerate(sparepartheader5):
	sparelist6.heading(col, text=col.title())
	sparelist6.column(col,minwidth=sparelist_width6[i][0],width=sparelist_width6[i][1])

sparelist6.pack(fill=BOTH)

WDB3 = ttk.Button(WDF2_4,text='อัพเดตรายการที่ต้องสั่งซื้อ', style='my.TButton',command=reorderpoint)
WDB3.pack(padx=5,pady=5)
##################################PR####################

global allprlist
allprlist = []

def PRForm():

	

	allprlist.append(len(count_L)+1)
	listtotv = [len(count_L)+1]

	x = 'วัสดุ'
	if x == 'วัสดุ':
		listtotv.append('/')
		listtotv.append(' ')
	else:
		listtotv.append(' ')
		listtotv.append('/')
	listtotv.append(PRname.get())
	listtotv.append(PRprice.get())
	listtotv.append(PRDate.get())
	listtotv.append(PRAmount.get())
	allprlist.append(listtotv)

	PRpartlist.insert('','end',values=allprlist)






PRFrame = Frame(F3)
PRFrame.pack()

PRFrame0= LabelFrame(F3,text='แบบฟอร์มสั่งซื้อที่ออฟฟิส')
PRFrame0.place(x=200,y=400)

PRFrame0= LabelFrame(F3,text='รายการสั่งซื้อ', font=('TH Sarabun New', 15))
PRFrame0.place(x=100,y=300)

PRFrameTreeview= LabelFrame(F3,text='รายการสั่งซื้อ', font=('TH Sarabun New', 15))
PRFrameTreeview.place(x=400,y=300)





LBTEXT = ['ชนิดรายการ','รายการ','ราคา','ซื้อล่าสุด','จำนวนที่สั่ง']

for i,j in enumerate(LBTEXT):
	PRLB1 = ttk.Label(PRFrame0,text=j).grid(row=i,column=0,sticky='w',padx=5,pady=5)

PRType = ['อะไหล่','วัสดุ']
PRType_CB = ttk.Combobox(PRFrame0, values = PRType, font=('TH Sarabun New', 15))
PRType_CB.set('อะไหล่')
PRType_CB.grid(row=0, column=1,padx=5,pady=5, sticky='w')



count_L = []
PRname_L = []
PRprice_L = []
PRAmount_L = []
PRDate_L = []


PRname = StringVar()
PRprice = StringVar()
PRAmount = StringVar()
PRDate =StringVar()

PRE01 = ttk.Entry(PRFrame0,textvariable=PRname, font=('TH Sarabun New', 15),width=22).grid(row=1, column=1,padx=5,pady=5, sticky='w')
PRE02 = ttk.Entry(PRFrame0,textvariable=PRprice, font=('TH Sarabun New', 15),width=22).grid(row=2, column=1,padx=5,pady=5, sticky='w')
PRE0D = ttk.Entry(PRFrame0,textvariable=PRDate, font=('TH Sarabun New', 15),width=22, state='disabled').grid(row=3, column=1,padx=5,pady=5, sticky='w')
PRE03 = ttk.Entry(PRFrame0,textvariable=PRAmount, font=('TH Sarabun New', 15),width=22).grid(row=4, column=1,padx=5,pady=5, sticky='w')
BS = ttk.Button(PRFrame0,text='Add',command=PRForm).grid(row=5, column=1,padx=5,pady=5, sticky='w')


# PRList= LabelFrame(PRFrameTreeview,text='รายการสั่งซื้อ', font=('TH Sarabun New', 15))
# PRList.place(x=200,y=100)

PRConfirmlist = ['ลำดับ','วัสดุ','อุปกรณ์','รายการและเหตุผลการสั่งซื้อ','ราคา','ซื้อล่าสุดเมื่อ','จำนวนที่สั่งห']
PRSize = [(20,80),(30,80),(30,80),(100,280),(50,80),(50,120),(30,120)]
PRpartlist = ttk.Treeview(PRFrameTreeview,columns=PRConfirmlist, show="headings", height=8)
PRpartlist.pack(padx=5,pady=5)


for i,col in enumerate(PRConfirmlist):
	PRpartlist.heading(col, text=col.title())
	PRpartlist.column(col,minwidth=PRSize[i][0],width=PRSize[i][1])



def adddatatolist(event=None):
	ts = sparelist6.selection()
	print(ts)
	text1 = sparelist6.item(ts,'values')
	print(text1)

	PRname.set(text1[3])
	PRprice.set(text1[5])
	PRDate.set(text1[7])
	PRType_CB.set(text1[1])
	

sparelist6.bind("<Double-1>",adddatatolist)

GUI.mainloop()