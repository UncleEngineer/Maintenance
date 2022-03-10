import os
from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import Notebook
from tkcalendar import Calendar, DateEntry
from datetime import datetime
import sqlite3
import tkinter.font as tkFont


#-----------------REPORT-------------------
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
import subprocess

class Report17(object):
    def __init__ (self):
        self.width, self.height = A4

    def run(self, pdfname, data, data_tool):
        #crete main canvas
        self.c = canvas.Canvas(pdfname, pagesize=A4)

        #call
        self.drawText(data, data_tool)
        self.drawTable()

        #save canvas to pdf
        self.c.save()
        print("create " + pdfname)
#--------------------------------------------------------------------------------------------------------------------------
    def drawText(self, data, data_tool):
        #inifont
        pdfmetrics.registerFont(TTFont('nomalFont', 'THSarabunNew.ttf'))
        pdfmetrics.registerFont(TTFont('boldFont', 'THSarabunNew Bold.ttf'))
        styles=getSampleStyleSheet()
        styleN = styles["Normal"]
        styleT = styles["Title"]

        #top
        ptext = Paragraph("<font size=20 name='boldFont'>Uncle Engineer</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 280 *mm)
        ptext = Paragraph("<font size=18 name='boldFont'>Uncle Engineer</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 272 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>ใบส่งงานซ่อม</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 265 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>วันที่ " + data[0] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -78 *mm, 255 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>ตามใบแจ้งซ่อมที่ " + data[1] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c,70 *mm, 255 *mm)

        #อุปกรณ์ส่งซ่อม
        ptext = Paragraph("<font size=16 name='boldFont'>หมวดอุปกรณ์ส่งซ่อม</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 247 *mm)
        ptext = Paragraph("<font size=14 name='boldFont'>ชื่ออุปกรณ์/รหัสอุปกรณ์</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -50 *mm, 240 *mm)
        ptext = Paragraph("<font size=14 name='boldFont'>ลักษณะงานซ่อม</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 50 *mm, 240 *mm)

        s_line = 233
        for i in range(len(data_tool)):
            ptext = Paragraph("<font size=14 name='nomalFont'>" + data_tool[i][0] +"</font>", styleT)
            ptext.wrapOn(self.c, self.width, self.height)
            ptext.drawOn(self.c, -50 *mm, s_line *mm)
            ptext = Paragraph("<font size=14 name='nomalFont'>" + data_tool[i][1] +"</font>", styleT)
            ptext.wrapOn(self.c, self.width, self.height)
            ptext.drawOn(self.c, 50 *mm, s_line *mm)
            s_line -= 7

        #หมวดดำเนินการ
        ptext = Paragraph("<font size=16 name='boldFont'>หมวดดำเนินการ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 198 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>ผู้ส่งซ่อม : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 187 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[2] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -35 *mm, 187 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>( " + data[3] + " )</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -35 *mm, 180 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>อนุมัติโดย : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 25 *mm, 187 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[4] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 65 *mm, 187 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>( " + data[5] + " )</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 65 *mm, 180 *mm)

        #หมวดผู้รับมอบ
        ptext = Paragraph("<font size=16 name='boldFont'>หมวดผู้รับมอบ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 0 *mm, 170 *mm)
        
        ptext = Paragraph("<font size=16 name='boldFont'>ผู้รับซ่อม : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 161 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[6] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -10 *mm, 161 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>ที่อยู่/เบอร์โทร :</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 154 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[7] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -10 *mm, 154 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>กำหนดการแล้วเสร็จ :</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 147 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[8] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -10 *mm, 147 *mm)

        #ตรวจสอบงานซ่อม
        ptext = Paragraph("<font size=16 name='boldFont'>ตรวจสอบงานซ่อม : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -75 *mm, 133 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>[" + data[9][0] + "] ยอมรับ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, -35 *mm, 126 *mm)
        ptext = Paragraph("<font size=16 name='boldFont'>[" + data[9][1] + "] ไม่ยอมรับ</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 35 *mm, 126 *mm)

        ptext = Paragraph("<font size=16 name='boldFont'>ประเมินงานโดย : </font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 25 *mm, 115 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>" + data[10] + "</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 65 *mm, 115 *mm)
        ptext = Paragraph("<font size=16 name='nomalFont'>( " + data[11] + " )</font>", styleT)
        ptext.wrapOn(self.c, self.width, self.height)
        ptext.drawOn(self.c, 65 *mm, 108 *mm)
#--------------------------------------------------------------------------------------------------------------------------
    def drawTable(self):
        # 1 line = 20
    
        #หมวดอุปกรณ์ส่งซ่อม
        self.c.line(30,720,560,720)
        self.c.line(30,700,560,700)

        self.c.line(30,680,560,680)
        self.c.line(30,660,560,660)
        self.c.line(30,640,560,640)
        self.c.line(30,620,560,620)
        self.c.line(30,600,560,600)
        self.c.line(30,580,560,580)
        self.c.line(295,700,295,580)

        #หมวดดำเนินการ
        self.c.line(30,560,560,560)
        self.c.line(30,500,560,500)
        self.c.line(295,560,295,500)



        #หมวดผู้รับมอบ
        self.c.line(30,480,560,480)
        self.c.line(30,400,560,400)

        #อตรวจงานซ่อม
        self.c.line(30,260,560,260)

        #เส้นหน้าหลัง
        self.c.line(30,720,30,260)
        self.c.line(560,720,560,260)
#--------------------------------------------------------------------------------------------------------------------------
#############################################################################

def gen_report17():

	try:
		ts = TVOutsource.selection()
		x = TVOutsource.item(ts)
		wd_code4export = x['values'][2]
		by_code = x['values'][3]
		print(wd_code4export,by_code)
	except:
		wd_code4export = '0'

	with conn:
		c.execute("SELECT * FROM outsource WHERE sf_doc_no = ? AND sf_sender = ?",([wd_code4export,by_code]))
		vfilter = c.fetchall()
		print(vfilter)

	if vfilter[0][10] == 'ยอมรับ':
		yy = ['/',' ']
	else:
		yy = [' ','/']

	try:
		data = [vfilter[0][1],vfilter[0][2],vfilter[0][3],vfilter[0][4],vfilter[0][5],vfilter[0][6],vfilter[0][7],vfilter[0][8],vfilter[0][9],yy,vfilter[0][11],vfilter[0][12]]

	except:
		data = ['dd/mm/yyyy','xxx/xx','นาย ผู้ส่งซ่อม','dd/mm/yyyy','นางสาว อนุมัติโดย','dd/mm/yyyy','นายช่างรับซ่อม','08-0000-0000/ชื่อร้าน','dd/mm/yyyy',['/',' '],'นาย ประเมินงาน โดย','dd/mm/yyyy']
	
	
	try:
		partlist0 = vfilter[0][-1].split(',')
		data_tool = []
		print("PARTLIST 0: ",partlist0)
		for i in partlist0:
			data2 = i.split('-')
			data_tool.append(data2)
		print("ALLPARTLISTSEND",data_tool)
	except:

		data_tool = [['เพลา','ซ่อม'],['แบริ่ง','เปลี่ยน'],['ล้อ','ปะ'],['สายพาน','เปลี่ยน']]

	dt1 = datetime.now().strftime('%Y-%m-%d %H%M%S')
	reportname = 'Outsource-'+dt1+'.pdf'

	Report17().run(reportname, data, data_tool)
	messagebox.showinfo('Report Exporting',reportname + ' was Exported')
	subprocess.Popen(reportname,shell=True)



########################################################################
class Report(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = A4
        self.styles = getSampleStyleSheet()
        
 
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
        office_name = "Uncle Engineer"
        canvas.setFont("boldFont", 18)
        canvas.drawCentredString(297.5,820, office_name)
        office_name = "Uncle Engineer"
        canvas.setFont("boldFont", 18)
        canvas.drawCentredString(297.5,805, office_name)
        
         #report type
        report_type = "บันทึกการแจ้งซ่อม/Mainternance request record"
        canvas.setFont("nomalFont", 15)
        canvas.drawCentredString(297.5,785, report_type)

        #top
        ptext = "Monthly/ประจำเดือน...................................."
        canvas.setFont("nomalFont",13)
        canvas.drawString(400,765,ptext)
        
         #bot
        ptext = "Review by : ........................................."
        canvas.setFont("boldFont", 14)
        canvas.drawString(355,105, ptext)
        ptext = "(Engneering Manager)"
        canvas.setFont("boldFont", 14)
        canvas.drawString(410,90, ptext)
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
        CH1 = Paragraph("<font size=8 name='boldFont'>Item รายการ</font>", styleT)
        CH2 = Paragraph("<font size=8 name='boldFont'>Requrst No. หมายเลข แจ้งซ่อม</font>", styleT)
        CH3 = Paragraph("<font size=8 name='boldFont'>Discription รายละเอียด</font>", styleT)
        CH4 = Paragraph("<font size=8 name='boldFont'>Break down งานด่วน</font>", styleT)
        CH5 = Paragraph("<font size=8 name='boldFont'>Repair work order งาน ซ่อม</font>", styleT)
        CH6 = Paragraph("<font size=8 name='boldFont'>Requestor แจ้งโดย</font>", styleT)
        CH7 = Paragraph("<font size=8 name='boldFont'>Maintenance by ซ่อมโดย</font>", styleT)
        CH8 = Paragraph("<font size=8 name='boldFont'>Remark หมายเหตุ</font>", styleT)
        
        data = [[CH1,CH2,CH3,CH4,CH5,CH6,CH7,CH8]]

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
        
            data.append([t1,t2,t3,t4,t5,t6,t7,t8])
            
        #line of table
        lineoftable = 30
        count2 = len(data)
        countf = lineoftable - count2
        
        for i in range(countf):
            blank = ['','','','','','','']

            if count < lineoftable:
                data.append(blank)
            else:
                pass
         #reporttest A4 MAX len 18.3 cm
        tableThatSplitsOverPages = Table(data, [1.5 * cm, 1.72 * cm, 6 * cm, 1.3 * cm, 1.8 * cm, 1.7 * cm, 2 * cm,2.78 * cm], repeatRows=1)

        tableThatSplitsOverPages.hAlign = 'LEFT'

        style2 = TableStyle([  ('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                                ('VALIGN',(0,0),(0,-1),'MIDDLE'),
                               ('ALIGN',(0,0),(-1,-1),'CENTER'),
                               ('VALIGN',(0,0),(-1,-1),'MIDDLE'), 
                               ('INNERGRID', (0,0), (-1,-1), 1, colors.black),
                               ('BOX', (0,0), (-1,-1), 1, colors.black)
                               ])

        tableThatSplitsOverPages.setStyle(style2)
 
        self.story.append(tableThatSplitsOverPages)

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
		B.grid(row=self.rw, column=self.cl,padx=5,pady=5,ipadx=5,ipady=5)


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
		L = ttk.Label(self.gui,text=self.text,font=('TH Sarabun New',15))
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
#------------------------------------------

dbname = 'DB-Maintenance.db'
conn = sqlite3.connect(dbname)
c = conn.cursor()

sparepart_id = []

# c.execute(""" CREATE TABLE IF NOT EXISTS sparepart_list (

# 				ID INTEGER PRIMARY KEY AUTOINCREMENT,
# 				sp_code text,
# 				sp_type text,
# 				sp_cat text,
# 				sp_name text,
# 				sp_model text,
# 				sp_price real,
# 				sp_quantity integer,
# 				sp_lastpur text,
# 				sp_reorder integer,
# 				sp_by text,
# 				sp_supp text

# 	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS bd_request (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				bd_mtcode text,
				bd_request text,
				bd_section text,
				bd_type text,
				bd_date text,
				bd_mc text,
				bd_mc_code text,
				bd_workdesc text,
				bd_workdetail text,
				bd_engineer text,
				bd_datereceive text,
				bd_break text,
				bd_inspection text,
				bd_sparepart text,
				bd_verify text,
				bd_remark text
				
	      )	""")

c.execute("""CREATE TABLE IF NOT EXISTS sparepart_list (
			ID INTEGER PRIMARY KEY AUTOINCREMENT ,
			 sp_code text,
			 sp_name text,
			 sp_Unit text,
			 sp_quantity integer,
			 sp_price real,
			 sp_reorder integer,
			 sp_suplier text
			
			)""")

c.execute(""" CREATE TABLE IF NOT EXISTS outsource (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				sf_date text,
				sf_doc_no text,
				sf_sender text,
				sf_send_date text,
				sf_verify text,
				sf_verify_date text,
				sf_reciever text,
				sf_recieve_address text,
				sf_finish_date text,
				sf_checkk text,
				sf_checkby text,
				sf_check_date text,
				sf_partlist text
				
				
	      )	""")

c.execute(""" CREATE TABLE IF NOT EXISTS purchase_request (

				ID INTEGER PRIMARY KEY AUTOINCREMENT,
				pr_department text,
				pr_req_date text,
				pr_user text,
				pr_verify text,
				pr_verify_date text,
				pr_requestor text,
				pr_req_date2 text		
				
	      )	""")



def expxl():
	pass

t = Report()

def reportpdf():

	with conn:
		c.execute("""SELECT bd_mtcode,bd_workdesc,bd_break,bd_break,bd_request,bd_engineer,bd_remark FROM bd_request""")
		bd_list = c.fetchall()
	conn.commit()
	print('Success')
	print(bd_list)

	datatopdf = []

	for j,i in enumerate(bd_list):
		
		if i[2] == 'Yes':
			bd = '/'
			rw = ''
		else:
			bd = ''
			rw = '/'
		reportdata = [str(j+1),i[0],i[1],bd,rw,i[4],i[5],i[6]]
		datatopdf.append(reportdata)

    #sparepart = [['1','001/61','ตรวจเช็ค Heater','/',' ','พี่ lop','เอนก',' '],['1','001/61','ตรวจเช็ค Heater','/',' ','พี่ lop','เอนก',' ']]
    

    
	dt1 = datetime.now().strftime('%Y-%m-%d %H%M%S')
	reportname = 'Breakdown-'+dt1+'.pdf'
	t.run(reportname,datatopdf)
	messagebox.showinfo('Report Exporting',reportname + ' was Exported')



def insert_MR():

	with conn:
		c.execute("""SELECT count(DISTINCT ID) from bd_request""")
		countcode = c.fetchall()
		print("COUNT in Table",countcode)

	
	if countcode[0][0] >= 10 and countcode[0][0] <100:
		wd_generatecode = 'BD00' + str(countcode[0][0]+1)
	elif countcode[0][0] >= 100 and countcode[0][0] <1000:
		wd_generatecode = 'BD0' + str(countcode[0][0]+1)
	else:
		wd_generatecode = 'BD000' + str(countcode[0][0]+1)
		#codestate = 0

	

	print(wd_generatecode)
	
	bd_codeshow.set('Request No.: ' + wd_generatecode)

	bd_mtcode = wd_generatecode
	abd_request = bd_request.get()
	abd_section = bd_section.get()
	abd_type = bd_type.get()
	abd_date = bd_date.get()

	abd_mc = bd_mc.get()
	abd_mc_code = bd_mc_code.get()

	abd_workdesc = T1.get("1.0",'end-1c')
	abd_workdetail = T2.get("1.0",'end-1c')

	abd_engineer = bd_engineer.get()
	abd_datereceive = bd_datereceive.get()
	abd_break = bd_break.get()

	abd_inspection = T11.get("1.0",'end-1c')

	

	abd_verify = bd_verify.get()
	abd_remark = bd_remark.get("1.0",'end-1c')

	textinsert = ''
	cc = len(sparepart_id)
	x = 1
	for i in sparepart_id:
		if x < cc:
			textinsert += i + ','
			x += 1
		else:
			textinsert += i
			x += 1

	abd_sparepart = textinsert

	print(textinsert)

	c.execute(""" INSERT INTO bd_request VALUES (

				:ID,\
				:bd_mtcode,\
				:bd_request,\
				:bd_section,\
				:bd_type,\
				:bd_date,\
				:bd_mc,\
				:bd_mc_code,\
				:bd_workdesc,\
				:bd_workdetail,\
				:bd_engineer,\
				:bd_datereceive,\
				:bd_break,\
				:bd_inspection,\
				:bd_sparepart,\
				:bd_verify,\
				:bd_remark
				
	      )	""",
	      { 
	      		'ID':None,
				'bd_mtcode':bd_mtcode,
				'bd_request':abd_request,
				'bd_section':abd_section,
				'bd_type':abd_type,
				'bd_date':abd_date,
				'bd_mc':abd_mc,
				'bd_mc_code':abd_mc_code,
				'bd_workdesc':abd_workdesc,
				'bd_workdetail':abd_workdetail,
				'bd_engineer':abd_engineer,
				'bd_datereceive':abd_datereceive,
				'bd_break':abd_break,
				'bd_inspection':abd_inspection,
				'bd_sparepart':abd_sparepart,
				'bd_verify':abd_verify,
				'bd_remark':abd_remark
	      }
	      )
	conn.commit()
	try:
		x = sparelist4.get_children()
		count = len(x)
		for z in range(count):
			sparelist4.delete(x[z])
			
	except:
		pass



#CLEAR ALL IN TREEVIEW: tree.delete(*tree.get_children())
def clearlist():
	try:
		x = sparelist4.get_children()
		count = len(x)
		for z in range(count):
			sparelist4.delete(x[z])
			
	except:
		pass
	global sparepart_id
	sparepart_id = []	

GUI = Tk()
GUI.title('Uncle Engineer')
GUI.state('zoomed')
GUI.geometry('600x600+30+30')

def add_sparepart(event=None):

	
	

	def db_add_sp(event=None):

		with conn:
			c.execute("""INSERT INTO sparepart_list VALUES (
				:ID,\
				:sp_code,\
				:sp_name,\
				:sp_Unit,\
				:sp_quantity,\
				:sp_price,\
				:sp_reorder,\
				:sp_suplier\
				)""",
				{'ID':None,
				'sp_code':sp_code.get(),
				 'sp_name':sp_title.get(),
				 'sp_Unit':sp_unit.get(),
				 'sp_quantity':int(sp_quantity.get()),
				 'sp_price':float(sp_price.get()),
				 'sp_reorder':int(sp_reorder.get()),
				 'sp_suplier':sp_supplier.get()}
				)
		conn.commit()
		print('Success')
		messagebox.showinfo("ยืนยันการทำรายการ", "บันทึกรายการเรียบร้อยแล้ว")

	GUI_SP = Toplevel()
	GUI_SP.geometry('300x450+300+50')
	#------------Variables-------------
	sp_code = StringVar()
	sp_title = StringVar()
	sp_unit = StringVar()
	sp_quantity = StringVar()
	sp_price = StringVar()
	sp_reorder = StringVar()
	sp_supplier = StringVar()

	

	LT1 = ['Code','S/P Title','Unit','Quantity','Price','Reorder Point','Supplier']

	for i,j in enumerate(LT1):
		L1 = ttk.Label(GUI_SP, text=j)
		L1.grid(row=i, column=0,pady=5,padx=5,sticky='nw')


	SPE1 = ttk.Entry(GUI_SP, textvariable=sp_code, font=('TH Sarabun New',15))
	SPE1.grid(row=0, column=1, padx=5, pady=5)

	SPE2 = ttk.Entry(GUI_SP, textvariable=sp_title, font=('TH Sarabun New',15))
	SPE2.grid(row=1, column=1, padx=5, pady=5)

	SPE3 = ttk.Entry(GUI_SP, textvariable=sp_unit, font=('TH Sarabun New',15))
	SPE3.grid(row=2, column=1, padx=5, pady=5)

	SPE4 = ttk.Entry(GUI_SP, textvariable=sp_quantity, font=('TH Sarabun New',15))
	SPE4.grid(row=3, column=1, padx=5, pady=5)

	SPE5 = ttk.Entry(GUI_SP, textvariable=sp_price, font=('TH Sarabun New',15))
	SPE5.grid(row=4, column=1, padx=5, pady=5)

	SPE6 = ttk.Entry(GUI_SP, textvariable=sp_reorder, font=('TH Sarabun New',15))
	SPE6.grid(row=5, column=1, padx=5, pady=5)

	SPE7 = ttk.Entry(GUI_SP, textvariable=sp_supplier, font=('TH Sarabun New',15))
	SPE7.grid(row=6, column=1, padx=5, pady=5)

	SPB1 = ttk.Button(GUI_SP, text='Add Sparepart', command=db_add_sp)
	SPB1.grid(row=7, column=1, padx=5, pady=5)



	GUI_SP.mainloop()



menubar = Menu(GUI)
#----------------Menu File > Export to Excel > Exit---------
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label='Export to PDF', command=reportpdf)
filemenu.add_separator()
filemenu.add_command(label='Upload to Server', command=expxl)
filemenu.add_command(label='Exit', command=GUI.quit)

menubar.add_cascade(label='File', menu=filemenu)

#----------------Sparepart----------------------
sparepartmenu = Menu(menubar, tearoff=0)
sparepartmenu.add_command(label='Add Spare Part', command=add_sparepart, accelerator="Ctrl+O")
sparepartmenu.add_command(label='View Spare Part', command=expxl, accelerator="Ctrl+P")
menubar.add_cascade(label='Spare Part', menu=sparepartmenu)
GUI.config(menu=menubar)
#-----------------------------------------------
#-------------Font Config for Notebook------------
f = tkFont.Font(family='TH Sarabun New', size=15)
s = ttk.Style()
s.configure('.', font=f)
#-------------Font Config for Notebook------------

wd_state = StringVar()
wd_state.set('0')

def tab():
	global Tab
	global F0
	global F1
	global F2
	global F3
	global F4
	global F5
	Tab = Notebook(GUI, height=950)
	F0 = Frame(Tab, width=200, height=950)
	F1 = Frame(Tab, width=200, height=950)
	F2 = Frame(Tab, width=200, height=950)
	F3 = Frame(Tab, width=200, height=950)
	F4 = Frame(Tab, width=200, height=950)
	F5 = Frame(Tab, width=200, height=950)
	#font=('TH Sarabun New',20)
	Tab.add(F0, text='Maintenance Record')
	Tab.add(F1, text='Breakdown List')
	Tab.add(F2, text='Outsource')
	Tab.add(F3, text='Material/Sparepart PR')
	Tab.add(F4, text='Summary')
	Tab.add(F5, text='Setting')
	Tab.pack(fill=BOTH, padx=10, pady=10)
tab()

# ------------SUB TAB-------------
# ------------Sub Tab 02--------------
TabF2 = Notebook(F2, height=950)

F21 = Frame(TabF2, width=200, height=950)
F22 = Frame(TabF2, width=200, height=950)

TabF2.add(F21, text='บันทึกรายการ ใบส่งงานซ่อม')
TabF2.add(F22, text='รายงาน ใบส่งงานซ่อม')
TabF2.pack(fill=BOTH, padx=10, pady=10)



# ------------Sub Tab 03--------------
TabF3 = Notebook(F3, height=900)

F31 = Frame(TabF3, width=200, height=900)
F32 = Frame(TabF3, width=200, height=900)

TabF3.add(F31, text='บันทึกรายการ ใบขอซื้อ Purchase Request')
TabF3.add(F32, text='รายงาน ใบขอซื้อ Purchase Request')
TabF3.pack(fill=BOTH, padx=10, pady=10)


# --------------------Function-----------------------
###########################


listpartoutsource = []

def picksparepartbd():
	# Treeview
	global spbdlist
	with conn:
			c.execute("SELECT bd_sparepart FROM bd_request WHERE bd_mtcode = ?",([sf_doc_no.get()]))
			spbdlist = c.fetchall()
			print(spbdlist)

	listtosparesend = []

	for i in spbdlist[0]:
		listpart = i.split(',')
		print(listpart)
		for j in listpart:
			with conn:
				c.execute("SELECT sp_name FROM sparepart_list WHERE sp_code = ?",([j]))
				beforetolist = []
				beforetolist.append(j)
				zz = c.fetchall()[0][0]
				beforetolist.append(zz)
				print(beforetolist)
				
				listtosparesend.append(beforetolist)




	#print(listtosparesend)


	def insertbdpart(event):
		ts = treeview5.selection()
		x = treeview5.item(ts)
		bdnumber = x['values'][0]
		bdname = x['values'][1]
		print(bdnumber)
		
		listtoinsert = [bdnumber,bdname]

		sf_sparelist1.insert('','end',values=listtoinsert)
		listpartoutsource.append(listtoinsert)


		
		

	

	GUI_DOC = Toplevel()
	GUI_DOC.title('ค้นหาอุปกรณ์')
	GUI_DOC.geometry('400x400+400+100')
	# GUI.bind('<Escape>',out)

	doc_header = ['เลขที่ใบแจ้งซ่อม', 'รายการ']
	doc_header_width = [(60,60),(200,200)]


	FDOCTop1 = Frame(GUI_DOC)

	global treeview5
	treeview5 = ttk.Treeview(FDOCTop1,columns=doc_header, show="headings", height=20)



	for i,col in enumerate(doc_header):
		treeview5.heading(col, text=col.title())
		#treeview5.column(col,minwidth=doc_header_width[i][0],width=doc_header_width[i][1])

	treeview5.pack(fill=BOTH,expand=1)

	for h in listtosparesend:
		treeview5.insert('','end',values=h)

	#updatebd_list_search()
	treeview5.bind("<Double-1>",insertbdpart)

	style = ttk.Style()
	style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
	style.configure("Treeview", font=('TH Sarabun New', 15))


	FDOCTop1.pack()
	GUI_DOC.mainloop()


###########################
def add_sf_sparepart():


	global itemsend
	itemsend = []

	def add_sp_fix():
		#sf_sparelist1
		itemtolist = [sf_name.get(),sf_detail.get()]
		sf_sparelist1.insert('','end',values=itemtolist)

		count = len(itemsend)
		itemsend.append(itemtolist)
		print(itemsend)



	GUI_SF = Toplevel()
	GUI_SF.geometry('250x300+300+50')
	#------------Variables-------------
	sf_code = StringVar()
	sf_name = StringVar()
	sf_detail = StringVar()



	# LT1 = ['ลำดับ','รายการ','จำนวน']
	# LT2 = ['ชื่ออุปกรณ์/รหัสอุปกรณ์','ลักษณะงานซ่อม']
	#
	# for i,j in enumerate(LT2):
	# 	L2 = ttk.Label(GUI_SF, text=j)
	# 	L2.grid(row=i, column=0,pady=5,padx=5,sticky='nw')
	SFLBT1 = LB(GUI_SF,'ชื่ออุปกรณ์/รหัสอุปกรณ์',0,0,'n')

	# SFE1 = ttk.Entry(GUI_SF, textvariable=sf_code, font=('TH Sarabun New',15))
	# SFE1.grid(row=0, column=1, padx=5, pady=5)

	SFE2 = ttk.Entry(GUI_SF, textvariable=sf_name, font=('TH Sarabun New',15))
	SFE2.grid(row=1, column=0, padx=5, pady=5)

	SFLBT2 = LB(GUI_SF,'ลักษณะงานซ่อม',2,0,'n')

	SFE3 = ttk.Entry(GUI_SF, textvariable=sf_detail, font=('TH Sarabun New',15))
	SFE3.grid(row=3, column=0, padx=5, pady=5)

	

	#SFB1 = BT(GUI_SF, 'เพิ่มอุปกรณ์ที่ซ่อม', 'add_sp_fix', 4, 0)
	SFB2 = ttk.Button(GUI_SF, text='เพิ่มอุปกรณ์ที่ซ่อม', command=add_sp_fix).grid(row=4, column=0, padx=5, pady=5)


	GUI_SF.mainloop()





def clear_pr_sparepart():
	tree.delete(*tree.get_children())

def updatebd_list_search():

	with conn:
		c.execute("""SELECT bd_mtcode,bd_workdesc FROM bd_request""")
		sp_list = c.fetchall()
	conn.commit()
	print('Success')
	print(sp_list)

	try:
		x = treeview3.get_children()
		count = len(x)
		for z in range(count):
			treeview3.delete(x[z])
			
	except:
		pass


	for it in sp_list:
		treeview3.insert('','end',values=it)

def pick_sf_doc_no():
	# Treeview

	def setbdnumber(event):
		ts = treeview3.selection()
		x = treeview3.item(ts)
		bdnumber = x['values'][0]
		print(bdnumber)
		sf_doc_no.set(bdnumber)
		GUI_DOC.withdraw()

	GUI_DOC = Toplevel()
	GUI_DOC.title('ค้นหาอุปกรณ์')
	GUI_DOC.geometry('400x400+400+100')
	# GUI.bind('<Escape>',out)

	doc_header = ['เลขที่ใบแจ้งซ่อม', 'รายการ']
	doc_header_width = [(60,60),(200,200)]


	FDOCTop1 = Frame(GUI_DOC)

	global treeview3
	treeview3 = ttk.Treeview(FDOCTop1,columns=doc_header, show="headings", height=20)



	for i,col in enumerate(doc_header):
		treeview3.heading(col, text=col.title())
		#treeview3.column(col,minwidth=doc_header_width[i][0],width=doc_header_width[i][1])

	treeview3.pack(fill=BOTH,expand=1)
	updatebd_list_search()
	treeview3.bind("<Double-1>",setbdnumber)

	style = ttk.Style()
	style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
	style.configure("Treeview", font=('TH Sarabun New', 15))


	FDOCTop1.pack()
	GUI_DOC.mainloop()

# def picksparepartbd():
# 	# Treeview

# 	def setbdnumber(event):
# 		ts = treeview3.selection()
# 		x = treeview3.item(ts)
# 		bdnumber = x['values'][0]
# 		print(bdnumber)
# 		sf_doc_no.set(bdnumber)
# 		GUI_DOC.withdraw()

# 	GUI_DOC = Toplevel()
# 	GUI_DOC.title('ค้นหาอุปกรณ์')
# 	GUI_DOC.geometry('400x400+400+100')
# 	# GUI.bind('<Escape>',out)

# 	doc_header = ['เลขที่ใบแจ้งซ่อม', 'รายการ']
# 	doc_header_width = [(60,60),(200,200)]


# 	FDOCTop1 = Frame(GUI_DOC)

# 	global treeview3
# 	treeview3 = ttk.Treeview(FDOCTop1,columns=doc_header, show="headings", height=20)



# 	for i,col in enumerate(doc_header):
# 		treeview3.heading(col, text=col.title())
# 		#treeview3.column(col,minwidth=doc_header_width[i][0],width=doc_header_width[i][1])

# 	treeview3.pack(fill=BOTH,expand=1)
# 	updatebd_list_search()
# 	treeview3.bind("<Double-1>",setbdnumber)

# 	style = ttk.Style()
# 	style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
# 	style.configure("Treeview", font=('TH Sarabun New', 15))


# 	FDOCTop1.pack()
# 	GUI_DOC.mainloop()


def pick_pr_sparepart():
	# Treeview

	GUI_PRS = Toplevel()
	GUI_PRS.title('ค้นหาอุปกรณ์')
	GUI_PRS.geometry('750x500+400+100')
	# GUI.bind('<Escape>',out)

	prs_header = ['Code', 'Sparepart Name','Unit','Quantity','Price','Reorderpoint','Supplier']
	prs_header_width = [(60,60),(200,200),(50,50),(70,70),(70,70),(120,120),(200,200)]


	FPRSTop1 = Frame(GUI_PRS)

	global treeview4
	treeview4 = ttk.Treeview(FPRSTop1,columns=prs_header, show="headings", height=20)



	for i,col in enumerate(prs_header):
		treeview4.heading(col, text=col.title())
		treeview4.column(col,minwidth=prs_header_width[i][0],width=prs_header_width[i][1])

	treeview4.pack(fill=BOTH,expand=1)
	# treeview1.bind("<Double-1>",hello)



	'''
	"Treeview"
	"Treeview.Heading"
	"Treeview.Row"
	"Treeview.Cell"
	"Treeview.Item"

	'''
	style = ttk.Style()
	style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
	style.configure("Treeview", font=('TH Sarabun New', 15))


	FPRSTop1.pack()
	GUI_PRS.mainloop()


def clear_sf_sparepart():
	itemsend = []
	sf_sparelist1.delete(*sf_sparelist1.get_children())
	print(itemsend)



# -------------Tab 00--------------------------------------------
#---------LABEL FRAME 01 -------------------
LBF1 = LabelFrame(F0,text='For Requestor' ,font=('TH Sarabun New',15))
LBF1.grid(row=0, column=0,padx=5,pady=5, sticky='NW')

LBF1_text = ['Requestor','Sector','Breakdown Type','Date','Machine Name','Machine No.']

for i,j in enumerate(LBF1_text):
	LBF1_L1 = ttk.Label(LBF1,text=j,font=('TH Sarabun New',15), width=18)
	LBF1_L1.grid(row=i,column=0,pady=5,padx=5,sticky='nw')

#------------VARIABLE----------------------

def updatebd_list():

	with conn:
		c.execute("""SELECT bd_mtcode,bd_date,bd_workdesc,bd_break,bd_break,bd_request,bd_engineer,bd_remark FROM bd_request""")
		sp_list = c.fetchall()
	conn.commit()
	print('Success')
	print(sp_list)



bd_mtcode = StringVar()
bd_request = StringVar() #0
bd_section = StringVar() #1

bd_mc_code = StringVar()

bd_workdesc = StringVar()
bd_workdetail = StringVar()

bd_engineer = StringVar()

bd_verify = StringVar()
bd_remark = StringVar()

combofont=('TH Sarabun New', '15')
GUI.option_add('*TCombobox*Listbox.font', combofont)

LBF1_E1 = ttk.Entry(LBF1, textvariable=bd_request, font=('TH Sarabun New',15),width=22)
LBF1_E1.grid(row=0, column=1, padx=5, pady=5, sticky='w')

LBF1_E2 = ttk.Entry(LBF1, textvariable=bd_section, font=('TH Sarabun New',15),width=22)
LBF1_E2.grid(row=1, column=1, padx=5, pady=5, sticky='w')

pet_select = ['Breakdown','Repair Work Order']
bd_type = ttk.Combobox(LBF1, values = pet_select, font=('TH Sarabun New', 15))
bd_type.set('Breakdown')
bd_type.grid(row=2, column=1,padx=5,pady=5, sticky='w')

bd_date = DateEntry(LBF1, width=18, backgroud='blue', foreground='white',
	borderwidth=2, font=('TH, Sarabun New',12))
bd_date.grid(row=3, column=1, padx=5, pady=5, sticky='w')

#---------------MACHINE SELECT--------------------

pet_select = ['PET1','PET2','PET3','PET4','PET5','PET6','PET7']
bd_mc = ttk.Combobox(LBF1, values = pet_select, font=('TH Sarabun New', 15))
bd_mc.set('PET1')
bd_mc.grid(row=4, column=1,padx=5,pady=5, sticky='w')

pet_select2 = ['ชุดอบวัตถุดิบ','เครื่องดูดเกล็ด 1','เครื่องดูดเกล็ด 2','ชุดหัวสกรู',
				'อ่างน้ำ','ชุดดูดความชื้น','ชุด Take up 1','ตู้อบ 1','ลุด Take up 2',
				'ตู้อบ 2','ชุด Take up 3','Emboss 1','Emboss 2','ตู้อบ 3',
				'ชุดเข้าม้วน 1','ชุดเข้าม้วน 2']

bd_mc_code = ttk.Combobox(LBF1, values = pet_select2, font=('TH Sarabun New', 15))
bd_mc_code.set('ชุดอบวัตถุดิบ')
bd_mc_code.grid(row=5, column=1,padx=5,pady=8, sticky='w')

LBF2 = LabelFrame(F0, text='Work Detail', font=('TH Sarabun New',15))
LBF2.grid(row=0, column=1,padx=5,pady=5, sticky='N')

TL1 = ttk.Label(LBF2, text='Work Main Description').grid(row=0,column=1,padx=5,pady=5,sticky='NW')
T1 = Text(LBF2, height=4.4, width=35,font=('TH Sarabun New',14))
T1.grid(row=0,column=2,padx=5,pady=5)
#T1.bind('<F2>',lambda event=None: C1.focus())
#dbd_bd_detail = T1.get("1.0",'end-1c')
TL2 = ttk.Label(LBF2, text='Work Detail Description').grid(row=1,column=1,padx=5,pady=5,sticky='NW')
T2 = Text(LBF2, height=4.5, width=35,font=('TH Sarabun New',14))
T2.grid(row=1,column=2,padx=5,pady=5)

#FOR Maintenance Sector

LBF3 = LabelFrame(F0, text='For Maintenance', font=('TH Sarabun New',15))
LBF3.grid(row=1, column=0,padx=5,pady=5, sticky='N')

LBF3_L1 = ttk.Label(LBF3, text='Engineer').grid(row=0,column=0,padx=5,pady=5,sticky='NW')
LBF3_E1 = Entry(LBF3, textvariable=bd_engineer, font=('TH Sarabun New',15),width=22)
LBF3_E1.grid(row=0, column=1, padx=5, pady=5, sticky='NW')

LBF3_L1 = ttk.Label(LBF3, text='Date').grid(row=1,column=0,padx=5,pady=5,sticky='NW')
bd_datereceive = DateEntry(LBF3, width=18, backgroud='blue', foreground='white',
	borderwidth=2, font=('TH, Sarabun New',12))
bd_datereceive.grid(row=1, column=1, padx=5, pady=5, sticky='w')

#---------------MACHINE SELECT--------------------
LBF3_L1 = ttk.Label(LBF3, text='Downtime Required',width=18).grid(row=2,column=0,padx=5,pady=5,sticky='NW')
pet_select2 = ['Yes','No']
bd_break = ttk.Combobox(LBF3, values = pet_select2, font=('TH Sarabun New', 15))
bd_break.set('Yes')
bd_break.grid(row=2, column=1,padx=5,pady=5, sticky='w')



TL11 = ttk.Label(LBF3, text='Inspection \nand Correction').grid(row=3,column=0,padx=5,pady=5,sticky='NW')
T11 = Text(LBF3, height=4, width=25,font=('TH Sarabun New',14))
T11.grid(row=3,column=1,padx=5,pady=15)
#T1.bind('<F2>',lambda event=None: C1.focus())
#dbd_bd_detail = T1.get("1.0",'end-1c')
LBF4 = Frame(F0)
LBF4.grid(row=1, column=1,padx=5,pady=17, sticky='NW',columnspan=2)


#Treeview

def updatewithdraw():
	pass



def popupsearchid():
	# Treeview

	def out(event=None):
		GUI_ID.withdraw()

	def hello(event=None):
		ts = treeview1.selection()
		print(ts)
		text1 = treeview1.item(ts,'values')
		#print("Hello world", text1[0]) # select code
		#print("Hello world", text1[1]) # select value in list
		#print(text1)
		print(text1)
		#print(text1[4])
		calc = (int(quan.get())*float(text1[4]))
		#print(calc)
		#print(type(calc))
		datatolist = (text1[0],text1[1],int(quan.get()),text1[5],calc)

		sparepart_id.append(text1[0])
		sparelist4.insert('','end',values=datatolist)
		#GUI_ID.withdraw()
		print(sparepart_id)

	GUI_ID = Toplevel()
	GUI_ID.title('Search ID')
	GUI_ID.geometry('750x500+400+100')
	GUI.bind('<Escape>',out)

	car_header = ['Code', 'Sparepart Name','Unit','Quantity','Price','Reorderpoint','Supplier']
	sparelist_width6 = [(60,60),(200,200),(50,50),(70,70),(70,70),(120,120),(200,200)]


	FS1 = Frame(GUI_ID)

	global treeview1
	treeview1 = ttk.Treeview(FS1,columns=car_header, show="headings", height=20)



	for i,col in enumerate(car_header):
		treeview1.heading(col, text=col.title())
		treeview1.column(col,minwidth=sparelist_width6[i][0],width=sparelist_width6[i][1])

	treeview1.pack(fill=BOTH,expand=1)
	treeview1.bind("<Double-1>",hello)

	

	'''
	"Treeview"
	"Treeview.Heading"
	"Treeview.Row"
	"Treeview.Cell"
	"Treeview.Item"

	'''
	style = ttk.Style()
	style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
	style.configure("Treeview", font=('TH Sarabun New', 15))

	with conn:
		c.execute("SELECT * FROM sparepart_list")
		cus_fet = c.fetchall()
		print(cus_fet)

	# customer_list = [
	# ('B101', 'Bearing 6002-2Z/C3') ,
	# ('B102', 'Bearing 6205-2Z') ,
	# ('B103', 'Bearing 6206-2RS1') ,
	# ('B104', 'Bearing 6207ZZCM/5K') ,
	# ('B105', 'Bearing 6202CM') ,
	# ('B106', 'Bearing 6212CM') ,
	
	
	# ]

	for it in cus_fet:
		print(it)
		
		treeview1.insert('','end',values=it[1:])

	FS1.pack()

	quan = StringVar()
	

	l01 = ttk.Label(GUI_ID, text='Quantity')
	l01.pack(padx=5,pady=5)

	e01 = ttk.Entry(GUI_ID,textvariable=quan)
	e01.pack(padx=5,pady=5)

	
	e01.focus()
	quan.set(1)

	GUI_ID.mainloop()



style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))

# sparepartheader4= ['Requestor', 'Section','Work Type','Date','Machine Name', 'Machine no.','Work Main Description', 'Work Detail','Engineer','Date','Dwontime Required','Inspection','Verify','Rewiif']
# sparelist_width4 = [(80,80),(70,70),(70,70),(70,70),(80,80),(80,80),(80,80),(80,80),(70,70),(70,70),(80,80),(80,80),(80,80),(80,80)]

sparepartheader4= ['Code', 'Partlist','Quantity','Price','total']
sparelist_width4 = [(60,60),(150,150),(70,70),(70,70),(70,70)]

sparelist4 = ttk.Treeview(LBF4,columns=sparepartheader4, show="headings", height=10)

for i,col in enumerate(sparepartheader4):
	sparelist4.heading(col, text=col.title())
	sparelist4.column(col,minwidth=sparelist_width4[i][0],width=sparelist_width4[i][1])

sparelist4.grid(row=0,column=0,padx=5,pady=5,columnspan=2)

WDB2 = ttk.Button(LBF4,text='Add Sparepart...', style='my.TButton',command=popupsearchid)
WDB2.grid(row=1,column=0,padx=5,pady=5,sticky='W')

#clearlist()
WDB3 = ttk.Button(LBF4,text='Clear', style='my.TButton',command=clearlist)
WDB3.grid(row=1,column=0,padx=5,pady=5,sticky='E')


LBF5 = LabelFrame(F0,text='Verify after Job Completed', font=('TH Sarabun New', 15))
LBF5.grid(row=0, column=2,padx=5,pady=17, sticky='N',columnspan=3)


LBF5_L1 = ttk.Label(LBF5, text='Job Completed').grid(row=0,column=0,padx=5,pady=5,sticky='NW')
# LBF5_E1 = Entry(LBF5, textvariable=bd_engineer, font=('TH Sarabun New',15),width=22)
# LBF5_E1.grid(row=0, column=1, padx=5, pady=5, sticky='NW')

pet_select2 = ['Permanent','Temporary Repair']
bd_verify = ttk.Combobox(LBF5, values = pet_select2, font=('TH Sarabun New', 15))
bd_verify.set('Permanent')
bd_verify.grid(row=0, column=1,padx=5,pady=5, sticky='w')


LB5_TL11 = ttk.Label(LBF5, text='Remark').grid(row=1,column=0,padx=5,pady=5,sticky='NW')
bd_remark = Text(LBF5, height=4, width=25,font=('TH Sarabun New',14))
bd_remark.grid(row=1,column=1,padx=5,pady=15)

bd_codeshow = StringVar()

bd_mtcode_show = ttk.Label(LBF5, textvariable=bd_codeshow)
bd_mtcode_show.grid(row=2,column=0,padx=5,pady=5,sticky='w')

WDB2 = ttk.Button(LBF5,text='Submit Form', style='my.TButton',command=insert_MR)
WDB2.grid(row=2,column=1,padx=5,pady=5)


# -------------Tab 01--------------------------------------------
#------------------View Part Section-------------------------


def updatebd_list():

	with conn:
		c.execute("""SELECT bd_mtcode,bd_date,bd_workdesc,bd_break,bd_break,bd_request,bd_engineer,bd_remark FROM bd_request""")
		sp_list = c.fetchall()
	conn.commit()
	print('Success')
	print(sp_list)

	try:
		x = sparelist5.get_children()
		count = len(x)
		for z in range(count):
			sparelist5.delete(x[z])
			
	except:
		pass


	for it in sp_list:
		sparelist5.insert('','end',values=it)


sparepartheader5= ['Request No','Date', 'Description','Breakdown','Repair Work','Requestor','Maintenance by','Remark']
sparelist_width5 = [(80,80),(80,80),(200,200),(60,60),(80,80),(80,80),(90,90),(120,120)]

sparelist5 = ttk.Treeview(F1,columns=sparepartheader5, show="headings", height=10)

for i,col in enumerate(sparepartheader5):
	sparelist5.heading(col, text=col.title())
	sparelist5.column(col,minwidth=sparelist_width5[i][0],width=sparelist_width5[i][1])

sparelist5.pack(fill=X,padx=5,pady=5)

WDB2 = ttk.Button(F1,text='Update Breakdown List', style='my.TButton',command=updatebd_list)
WDB2.pack(padx=5,pady=5)

# -------------Tab 02--------------------------------------------
def add_outsource(event=None):



	def confirm():

		text_sf_partlist = ""

		for i in itemsend:
			text_sf_partlist += i[0] + '-' + i[1] + ','

		print(text_sf_partlist)

		

		try:
			if sf_check.get() == 1:
				sf_checkk = "ยอมรับ"
			else:
				sf_checkk = "ไม่ยอมรับ"

			print(sf_checkk)
			with conn:
				c.execute("""INSERT INTO outsource VALUES (
	
					:ID,\
					:sf_date,\
					:sf_doc_no,\
					:sf_sender,\
					:sf_send_date,\
					:sf_verify,\
					:sf_verify_date,\
					:sf_reciever,\
					:sf_recieve_address,\
					:sf_finish_date,\
					:sf_checkk,\
					:sf_checkby,\
					:sf_check_date,\
					:sf_partlist
					)""",

				          {'ID':None,
				           'sf_date': sf_date.get(),
				           'sf_doc_no': sf_doc_no.get(),
				           'sf_sender': sf_sender.get(),
				           'sf_send_date': sf_send_date.get(),
				           'sf_verify': sf_verify.get(),
				           'sf_verify_date': sf_verify_date.get(),
				           'sf_reciever': sf_reciever.get(),
				           'sf_recieve_address':sf_recieve_address.get(),
				           'sf_finish_date':sf_finish_date.get(),
				           'sf_checkk':sf_checkk,
				           'sf_checkby':sf_checkby.get(),
				           'sf_check_date':sf_check_date.get(),
				           'sf_partlist':text_sf_partlist[:-1]
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

def clear_outsource():
	pass






SFLBF1 = LabelFrame(F21, text='หมวดดำเนินการ', font=('TH Sarabun New', 15))
SFLBF1.grid(row=0, column=0, padx=5, pady=5, sticky='NW')

SFLBF2 = LabelFrame(F21, text='หมวดผู้รับมอบ', font=('TH Sarabun New', 15))
SFLBF2.place(x=650,y=15)

SFLBF3 = LabelFrame(F21, text='ตรวจสอบงานซ่อม', font=('TH Sarabun New', 15))
SFLBF3.place(x=650,y=200)

SFLB21 = LB(SFLBF1, "วันที่ยื่นคำร้อง", 0, 0, 'w')
sf_date = DateEntry(SFLBF1, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
sf_date.grid(row=0, column=1, padx=5, pady=5, sticky='w')

SFLB22 = LB(SFLBF1,"ใบแจ้งซ่อมเลขที่",1,0,'w')
sf_doc_no = StringVar()
SFET22 = ET(SFLBF1,sf_doc_no,1,1,'w')
# SFBT22 = BT(SFLBF1,'ค้นหา','sf_search_doc_no',1,2)
SFBT22 = ttk.Button(SFLBF1,text='ค้นหา',command=pick_sf_doc_no)
SFBT22.place(x=300,y=45)

SFLB23 = LB(SFLBF1,"อุปกรณ์ที่ส่งซ่อม",2,0,'w')
SFBT23 = BT(SFLBF1,'...','add_sf_sparepart',2,1)
SFBT24 = BT(SFLBF1,'ล้างรายการ','clear_sf_sparepart',2,2)

# ------------------TREEVIEW SF Sparepart--------------------
style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))

sf_sparelist_header1= ['ชื่ออุปกรณ์ / รหัสอุปกรณ์', 'ลักษณะงานซ่อม']
sf_sparelist_width1 = [(250,250),(250,250)]

sf_sparelist1 = ttk.Treeview(SFLBF1,columns=sf_sparelist_header1, show="headings", height=5)

for i,col in enumerate(sf_sparelist_header1):
	sf_sparelist1.heading(col, text=col.title())
	sf_sparelist1.column(col,minwidth=sf_sparelist_width1[i][0],width=sf_sparelist_width1[i][1])

sf_sparelist1.grid(row=3,column=1,padx=5,pady=5, columnspan=5)
# sf_sparelist1.place(x=300,y=300)
# ---------------------------------------------------
SFLB25 = LB(SFLBF1,"ผู้ส่งซ่อม",4,0,'w')
sf_sender = StringVar()
SFET25 = ET(SFLBF1,sf_sender,4,1,'w')

SFLB26 = LB(SFLBF1,"อนุมัติโดย",4,2,'e')
sf_verify = StringVar()
SFET26 = ET(SFLBF1,sf_verify,4,3,'w')

SFLB27 = LB(SFLBF1, "วันที่ส่งซ่อม", 5, 0, 'w')
sf_send_date = DateEntry(SFLBF1, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
sf_send_date.grid(row=5, column=1, padx=5, pady=5, sticky='w')

SFLB28 = LB(SFLBF1, "วันที่อนุมัติ", 5, 2, 'e')
sf_verify_date = DateEntry(SFLBF1, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
sf_verify_date.grid(row=5, column=3, padx=5, pady=5, sticky='w')

SFLB29 = LB(SFLBF2,"ผู้รับซ่อม",0,0,'w')
sf_reciever = StringVar()
SFET29 = ET(SFLBF2,sf_reciever,0,1,'w')

SFLB30 = LB(SFLBF2,"ที่อยู่ / เบอร์โทรศัพท์",1,0,'w')
sf_recieve_address = StringVar()
SFET30 = ttk.Entry(SFLBF2,textvariable=sf_recieve_address,width=40,font=('TH Sarabun New',15))
SFET30.grid(row=1, column=1, padx=5, pady=5, sticky='w')

SFLB31 = LB(SFLBF2, "กำหนดแล้วเสร็จ", 2, 0, 'w')
sf_finish_date = DateEntry(SFLBF2, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
sf_finish_date.grid(row=2, column=1, padx=5, pady=5, sticky='w')

sf_check = IntVar()
sf_check1 = Radiobutton(SFLBF3, text = "ยอมรับ", variable=sf_check, value=1, font=('TH Sarabun New', 15))
sf_check1.grid(row=0, column=0,padx=5,pady=5, sticky='w')
sf_check2 = Radiobutton(SFLBF3, text = "ไม่ยอมรับ", variable=sf_check, value=2, font=('TH Sarabun New', 15))
sf_check2.grid(row=0, column=1,padx=5,pady=5, sticky='w')
sf_checkk = 0

SFLB32 = LB(SFLBF3,"ประเมินงานโดย",1,0,'w')
sf_checkby = StringVar()
SFET32 = ET(SFLBF3,sf_checkby,1,1,'w')

SFLB33 = LB(SFLBF3, "วันที่", 2, 0, 'w')
sf_check_date = DateEntry(SFLBF3, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
sf_check_date.grid(row=2, column=1, padx=5, pady=5, sticky='w')

SFB31 = BT(SFLBF3, 'บันทึกข้อมูล', 'add_outsource', 2, 4)
SFB32 = BT(SFLBF3, 'เคลียร์', 'clear_outsource', 2, 5)
# ------------------TREEVIEW Outsource--------------------
def print_outsource():
	pass

def updateoutsource():
	try:
		with conn:
			c.execute("""SELECT * FROM outsource""")
			outsourcelist = c.fetchall()
		conn.commit()
		print(outsourcelist)
		print('Success')
	except:
		pass

	try:
		x = TVOutsource.get_children()
		count = len(x)
		for z in range(count):
			TVOutsource.delete(x[z])

	except:
		pass
	print(outsourcelist)

	for it in outsourcelist:
		TVOutsource.insert('','end',values=it[0:])
# Treview

TVFOutsource = Frame(F22, width=200)
TVFOutsource.grid(row=8,column=1,pady=20)

TVHOutsource = ['ลำดับ','วันที่','ใบแจ้งซ่อมเลขที่','ผู้ส่งซ่อม','วันที่ส่งซ่อม','อนุมัติโดย','วันที่อนุมัติ','ผู้รับซ่อม','ที่อยู่/เบอร์โทร','กำหนดแล้วเสร็จ','ตรวจสอบงานซ่อม','ประเมินงานโดย','วันที่ประเมินงาน']

TVHOUT = [(50,50),(80,80),(100,100),(100,100),(100,100),(100,100),(100,100),(100,100),(100,100),(120,120),(120,120),(120,120),(100,100)]

# TREEVIEW----------------------


TVOutsource = ttk.Treeview(TVFOutsource,columns=TVHOutsource, show="headings", height=20)

for i,col in enumerate(TVHOutsource):
	TVOutsource.heading(col, text=col.title())
	TVOutsource.column(col,minwidth=TVHOUT[i][0],width=TVHOUT[i][1],anchor=N)

TVOutsource.pack(fill=BOTH)
update_outsource = ttk.Button(TVFOutsource,text='อัพเดต', style='my.TButton',command=updateoutsource)
update_outsource.pack(padx=5,pady=5)
print_outsource = ttk.Button(TVFOutsource,text='ออกรายงานใบส่งงานซ่อม', style='my.TButton',command=gen_report17)
print_outsource.pack(padx=5,pady=5)


# -------------Tab 03--------------------------------------------
def add_pr(event=None):
	def confirm():
		try:

			with conn:
				c.execute("""INSERT INTO purchase_request VALUES (
	
					:ID,\
					:pr_department,\
					:pr_req_date,\
					:pr_user,\
					:pr_verify,\
					:pr_verify_date,\
					:pr_requestor,\
					:pr_req_date2
					
					)""",

				          {'ID':None,
				           'pr_department': pr_department.get(),
				           'pr_req_date': pr_req_date.get(),
				           'pr_user': pr_user.get(),
				           'pr_verify': pr_verify.get(),
				           'pr_verify_date': pr_verify_date.get(),
				           'pr_requestor': pr_requestor.get(),
				           'pr_req_date2': pr_req_date2.get()
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

def clear__pr():
	pass

LB31 = LB(F31,"แผนก",0,0,'w')
pr_department = ['Maintenance','Production']
ET31 = CB(F31,pr_department,0,1,'w')

LB32 = LB(F31, "วันที่ยื่นคำร้อง", 1, 0, 'w')
pr_req_date = DateEntry(F31, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
pr_req_date.grid(row=1, column=1, padx=5, pady=5, sticky='w')

LB33 = LB(F31,"ผู้ใช้งาน",2,0,'w')
pr_user = StringVar()
ET33 = ET(F31,pr_user,2,1,'w')

# LB34 = LB(F31,"เลือกรายการ",3,0,'w')
# BT34 = BT(F31,'...','pick_sparepart',3,1)
#
# BT35 = BT(F31,'ล้างรายการ','clear_pr_sparepart',3,2)

LB34 = ttk.Label(F31,text="เลือกรายการ")
LB34.place(x=400, y=80)
BT34 = ttk.Button(F31,text="...",command="pick_pr_sparepart")
BT34.place(x=500, y=80)
BT35 = ttk.Button(F31,text="ล้างรายการ",command="clear_pr_sparepart")
BT35.place(x=650, y=80)

# ------------------TREEVIEW PR Sparepart--------------------
style = ttk.Style()
style.configure("Treeview.Heading", font=('TH Sarabun New', 15, 'bold'))
style.configure("Treeview", font=('TH Sarabun New', 15))

pr_sparelist_header1= ['จำนวน', 'รายการ','กำหนดใช้ของ','ประเภทการใช้งาน']
pr_sparelist_width1 = [(60,60),(250,250),(100,100),(250,250)]

pr_sparelist1 = ttk.Treeview(F31,columns=pr_sparelist_header1, show="headings", height=10)

for i,col in enumerate(pr_sparelist_header1):
	pr_sparelist1.heading(col, text=col.title())
	pr_sparelist1.column(col,minwidth=pr_sparelist_width1[i][0],width=pr_sparelist_width1[i][1])

pr_sparelist1.grid(row=4,column=1,padx=5,pady=5, columnspan=5)
# ---------------------------------------------------

LB36 = LB(F31,"ผู้อนุมัติ",5,0,'w')
pr_verify = StringVar()
ET36 = ET(F31,pr_verify,5,1,'w')

LB37 = LB(F31,"ผู้ยื่นคำร้อง",5,2,'e')
pr_requestor = StringVar()
ET37 = ET(F31,pr_requestor,5,3,'w')

LB38 = LB(F31, "วันที่อนุมัติ", 6, 0, 'w')
pr_verify_date = DateEntry(F31, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
pr_verify_date.grid(row=6, column=1, padx=5, pady=5, sticky='w')

LB39 = LB(F31, "วันที่ยื่นคำร้อง", 6, 2, 'e')
pr_req_date2 = DateEntry(F31, width=18, backgroud='blue', foreground='white',borderwidth=2, font=('TH, Sarabun New',12))
pr_req_date2.grid(row=6, column=3, padx=5, pady=5, sticky='w')

# LBFPR1 = LabelFrame(F31, text='', font=('TH Sarabun New', 15))
# # LBFPR1.grid(row=0, column=0, padx=5, pady=5, sticky='NW')
# LBFPR1.place(x=150,y=550)

BT40 = ttk.Button(F31,text="บันทึกข้อมูล",command="add_pr")
BT40.place(x=150, y=480)
BT41 = ttk.Button(F31,text="เคลียร์",command="clear_pr")
BT41.place(x=350, y=480)

# ------------------TREEVIEW Outsource--------------------
def print_pr():
	pass

def updatepr():
	try:
		with conn:
			c.execute("""SELECT * FROM purchase_request""")
			prlist = c.fetchall()
		conn.commit()
		print(prlist)
		print('Success')
	except:
		pass

	try:
		x = TVPRequest.get_children()
		count = len(x)
		for z in range(count):
			TVPRequest.delete(x[z])

	except:
		pass
	print(prlist)

	for it in prlist:
		TVPRequest.insert('','end',values=it[0:])
# Treview

TVFPRequest = Frame(F32, width=200)
TVFPRequest.grid(row=8,column=1,pady=20)

TVHPRequest = ['ลำดับ','แผนก','วันที่ยื่นคำร้อง','ผู้ใช้งาน','ผู้อนุมัติ','วันที่อนุมัติ','ผู้ยื่นคำร้อง','วันที่ยื่นคำร้อง']

TVHPR = [(80,80),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120),(120,120)]

# TREEVIEW----------------------


TVPRequest = ttk.Treeview(TVFPRequest,columns=TVHPRequest, show="headings", height=20)

for i,col in enumerate(TVHPRequest):
	TVPRequest.heading(col, text=col.title())
	TVPRequest.column(col,minwidth=TVHPR[i][0],width=TVHPR[i][1],anchor=N)

TVPRequest.pack(fill=BOTH)
update_pr = ttk.Button(TVFPRequest,text='อัพเดต', style='my.TButton',command=updatepr)
update_pr.pack(padx=5,pady=5)
print_pr = ttk.Button(TVFPRequest,text='ออกรายงานPR', style='my.TButton',command=print_pr)
print_pr.pack(padx=5,pady=5)





GUI.mainloop()