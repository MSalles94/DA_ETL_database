class pdf_printer():
    def __init__(self,path='teste.pdf',
                 main_header='THIS IS THE HEADER',
                 sub_header='SUB HEADER',
                 footer='THIS IS THE FOOTER') -> None:
        self.head_foot=[main_header,sub_header,footer]
        
        from reportlab.platypus import SimpleDocTemplate
        self.doc=SimpleDocTemplate(path)
        self.story=[]
        self.__create_styles()

    def __create_styles(self):
        from reportlab.lib import colors
        from reportlab.platypus import TableStyle
        from reportlab.lib.styles import getSampleStyleSheet
        #table styles
        
        tab_green = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.green),  # Cor de fundo para o cabeçalho
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Cor do texto do cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Cor de fundo para o conteúdo da tabela
        ('GRID',(0,0),(-1,-1),1,colors.black)
    ])
        tab_red = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.red),  # Cor de fundo para o cabeçalho
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Cor do texto do cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.lightcoral),  # Cor de fundo para o conteúdo da tabela
        ('GRID',(0,0),(-1,-1),1,colors.black)
    ])
        self.style_table={
            'green':tab_green,
            'red':tab_red
        }

        #paragraph styles
        styles=getSampleStyleSheet()
        # Obtendo estilos de exemplo
        # Criando um novo estilo baseado no estilo 'Normal'
        title = styles['Normal']
        title.textColor = colors.black  # Cor do texto
        title.fontName = 'Helvetica-Bold'
        title.borderColor = '#000000'  # Cor da borda
        title.borderWidth = 1  # Largura da borda
        title.borderPadding = (5, 5, 5, 5) 
        title.backColor=colors.lightgrey
       
       
        self.style_paragraph={
            'title1':title
        }
        pass

    def insert_paragraph(self,text='teste',style=''):
        from reportlab.platypus import  Paragraph
        if style=='':
            paragraph1 = Paragraph(text)
        else:
            style=self.style_paragraph[style]
            paragraph1 = Paragraph(text,style=style)
        self.story.append(paragraph1)

    def insert_spacer(self,size=0.5):
        from reportlab.platypus import Spacer
        from reportlab.lib.units import inch
        self.story.append(Spacer(width=inch*size,height=inch*size))

    def insert_table(self,dataframe,style='green'):
        style=self.style_table[style]
        from reportlab.platypus import Table
        data = [dataframe.columns.values.tolist()] + dataframe.values.tolist()
        new_table=Table(data,style=style)
        self.story.append(new_table)

    def save_document(self,path='./teste.pdf'):
        path=path
        self.doc.build(self.story,onFirstPage=self.page_head_foot, onLaterPages=self.page_head_foot)

    def page_head_foot(self,canvas,doc):
        from reportlab.lib.units import mm
        page_num = canvas.getPageNumber()
        pg_numb = "Page #%s" % page_num
        canvas.drawRightString(200*mm, 20*mm, pg_numb) #page number
        canvas.drawRightString(25*mm, 0*mm, self.head_foot[0]) #Main header
        canvas.drawRightString(250*mm, 0*mm, self.head_foot[1]) #Main header
        canvas.drawRightString(500*mm, 0*mm, self.head_foot[2]) #Main header
        pass

    def jump_page(self):
        from reportlab.platypus import  PageBreak
        self.story.append(PageBreak())
        
import numpy as np
import pandas
data = np.random.randint(1, 100, size=(5, 5)).tolist()
data=pandas.DataFrame(data,columns=['A','B','C','D','E'])


report_pdf=pdf_printer()
report_pdf.insert_paragraph(text='TITLE OF THE REPORT',style='title1')
report_pdf.insert_spacer()
report_pdf.insert_paragraph()
report_pdf.insert_table(dataframe=data)
report_pdf.jump_page()
report_pdf.insert_table(dataframe=data)

report_pdf.save_document(path='')
