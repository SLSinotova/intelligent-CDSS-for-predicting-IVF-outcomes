from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
import pandas as pd

class HTMLDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(HTMLDelegate, self).__init__(parent)
        self.doc = QtGui.QTextDocument(self)

    def paint(self, painter, option, index):
        painter.save()
        options = QtWidgets.QStyleOptionViewItem(option)
        self.initStyleOption(options, index)
        self.doc.setHtml(options.text)
        options.text = ""
        style = QtWidgets.QApplication.style() if options.widget is None \
            else options.widget.style()
        style.drawControl(QtWidgets.QStyle.CE_ItemViewItem, options, painter)

        ctx = QtGui.QAbstractTextDocumentLayout.PaintContext()
        if option.state & QtWidgets.QStyle.State_Selected:
            ctx.palette.setColor(QtGui.QPalette.Text, option.palette.color(
                QtGui.QPalette.Active, QtGui.QPalette.HighlightedText))
        else:
            ctx.palette.setColor(QtGui.QPalette.Text, option.palette.color(
                QtGui.QPalette.Active, QtGui.QPalette.Text))
        textRect = style.subElementRect(QtWidgets.QStyle.SE_ItemViewItemText, options, None)
        if index.column() != 0:
            textRect.adjust(5, 0, 0, 0)
        constant = 4
        margin = (option.rect.height() - options.fontMetrics.height()) // 2
        margin = margin - constant
        textRect.setTop(textRect.top() + margin)

        painter.translate(textRect.topLeft())
        painter.setClipRect(textRect.translated(-textRect.topLeft()))
        self.doc.documentLayout().draw(painter, ctx)
        painter.restore()

    def sizeHint(self, option, index):
        return QtCore.QSize(self.doc.idealWidth(), self.doc.size().height())

       
def features_b1(window,data):  
    
    for i in range (0,104):
        data[data.columns[i]]=0
        
  # анамнез
    if (window.radioButton_3.isChecked()==True):
        data[data.columns[1]]=1  
    if (window.radioButton_9.isChecked()==True):
        data[data.columns[2]]=1
    if (window.radioButton_13.isChecked()==True):
        data[data.columns[3]]=1
    if (window.radioButton_36.isChecked()==True):
        data[data.columns[4]]=1      
    if (window.radioButton_17.isChecked()==True):
        data[data.columns[5]]=1
    if (window.radioButton_11.isChecked()==True):
        data[data.columns[6]]=1
    if (window.radioButton_15.isChecked()==True):
        data[data.columns[7]]=1
    if (window.radioButton_49.isChecked()==True):
        data[data.columns[8]]=1    
    if (window.radioButton_7.isChecked()==True):
        data[data.columns[9]]=1    
    if ((window.radioButton_7.isChecked()==False) and(window.radioButton_3.isChecked()==False)and(window.radioButton_9.isChecked()==False)and(window.radioButton_13.isChecked()==False)and(window.radioButton_36.isChecked()==False)and(window.radioButton_17.isChecked()==False)and(window.radioButton_11.isChecked()==False)and(window.radioButton_15.isChecked()==False)and(window.radioButton_49.isChecked()==False)):
        data[data.columns[10]]=1   
    ## все подряд
    if (window.radioButton_92.isChecked()==True):
        data[data.columns[11]]=1
    if (window.radioButton_72.isChecked()==True):
        data[data.columns[12]]=1
    if (window.radioButton_68.isChecked()==True):
        data[data.columns[13]]=1
    if (window.radioButton_70.isChecked()==True):
        data[data.columns[14]]=1
    if (window.radioButton_76.isChecked()==True):
        data[data.columns[15]]=1    
    if (window.radioButton_86.isChecked()==True):
        data[data.columns[16]]=1
    if (window.radioButton_74.isChecked()==True):
        data[data.columns[17]]=1 
    if (window.radioButton_78.isChecked()==True):
        data[data.columns[18]]=1
    if (window.radioButton_80.isChecked()==True):
        data[data.columns[19]]=1
    if (window.radioButton_82.isChecked()==True):
        data[data.columns[20]]=1     
    if (window.radioButton_84.isChecked()==True):
        data[data.columns[21]]=1 
    ## операции    
    if (window.radioButton_25.isChecked()==True):
        data[data.columns[22]]=1
    if (window.radioButton_29.isChecked()==True):
        data[data.columns[23]]=1
    if (window.radioButton_23.isChecked()==True):
        data[data.columns[24]]=1    
    if (window.radioButton_21.isChecked()==True):
        data[data.columns[25]]=1
    if (window.radioButton_19.isChecked()==True) or (window.radioButton_7.isChecked()==True):
        data[data.columns[26]]=1
    if (window.radioButton_27.isChecked()==True):
        data[data.columns[27]]=1
    if (window.radioButton_29.isChecked()==False)and(window.radioButton_25.isChecked()==False)and(window.radioButton_23.isChecked()==False)and(window.radioButton_21.isChecked()==False)and(window.radioButton_19.isChecked()==False)and(window.radioButton_7.isChecked()==False)and(window.radioButton_27.isChecked()==False):
        data[data.columns[28]]=1     
    ## женские болезни 
    if (window.radioButton_60.isChecked()==True):
        data[data.columns[29]]=1
    ## возраст 
    if (window.radioButton_33.isChecked()==True):
        data[data.columns[30]]=1
    if (window.radioButton_34.isChecked()==True):
        data[data.columns[31]]=1    
    if (window.radioButton_31.isChecked()==True):
        data[data.columns[32]]=1    
    if (window.radioButton_32.isChecked()==True):
        data[data.columns[33]]=1   
    if (window.radioButton_35.isChecked()==True):
        data[data.columns[34]]=1         
    ## ИМТ
    if (window.radioButton_41.isChecked()==True):
        data[data.columns[35]]=1
    if (window.radioButton_42.isChecked()==True):
        data[data.columns[36]]=1
    if (window.radioButton_43.isChecked()==True):
        data[data.columns[37]]=1  
    ## заболевания  
    if (window.radioButton_56.isChecked()==True):
        data[data.columns[39]]=1    
    if (window.radioButton_90.isChecked()==True):
        data[data.columns[40]]=1    
    if (window.radioButton_64.isChecked()==True):
        data[data.columns[41]]=1   
    if (window.radioButton_62.isChecked()==True):
        data[data.columns[42]]=1
    if (window.radioButton_56.isChecked()==False)and(window.radioButton_90.isChecked()==False)and(window.radioButton_64.isChecked()==False)and(window.radioButton_62.isChecked()==False):
        data[data.columns[38]]=1
    if (window.radioButton_101.isChecked()==True):
        data[data.columns[38]]=0
    ## номер попытки    
    if (window.radioButton_45.isChecked()==True):
        data[data.columns[43]]=1    
    if (window.radioButton_46.isChecked()==True):
        data[data.columns[44]]=1     
    if (window.radioButton_47.isChecked()==True):
        data[data.columns[45]]=1    
    if (window.radioButton_48.isChecked()==True):
        data[data.columns[46]]=1   
    ## программа    
    if (window.radioButton_53.isChecked()==True):
        data[data.columns[47]]=1    
    if (window.radioButton_54.isChecked()==True):
        data[data.columns[48]]=1 

    return data  

def features_b2(window,data):  
    
    for i in range (60,104):
        data[data.columns[i]]=0
        ## анамнез
    if (window.radioButton_103.isChecked()==True):
        data[data.columns[60]]=1  
    if (window.radioButton_105.isChecked()==True):
        data[data.columns[61]]=1  
    if (window.radioButton_44.isChecked()==True):
        data[data.columns[62]]=1  
    if (window.radioButton_40.isChecked()==True):
        data[data.columns[80]]=1     
    if (window.radioButton_88.isChecked()==True):
        data[data.columns[63]]=1  
    if (window.radioButton_66.isChecked()==True):
        data[data.columns[64]]=1 
    if (window.radioButton_95.isChecked()==True):
        data[data.columns[65]]=1 
    ## претритмент и протокол
    if (window.radioButton_156.isChecked()==True):
        data[data.columns[66]]=1  
    if (window.radioButton_157.isChecked()==True):
        data[data.columns[67]]=1
    if (window.radioButton_158.isChecked()==True):
        data[data.columns[68]]=1
    if (window.radioButton_38.isChecked()==True):
        data[data.columns[69]]=1
    if (window.radioButton_98.isChecked()==True):
        data[data.columns[70]]=1
    if (window.radioButton_39.isChecked()==True):
        data[data.columns[71]]=1    
    if (window.radioButton_94.isChecked()==True):
        data[data.columns[72]]=1
    if (window.radioButton_153.isChecked()==True):
        data[data.columns[73]]=1
    if (window.radioButton_154.isChecked()==True):
        data[data.columns[74]]=1  
    if (window.radioButton_155.isChecked()==True):
        data[data.columns[75]]=1
    if (window.radioButton_159.isChecked()==True):
        data[data.columns[76]]=1
    if (window.radioButton_160.isChecked()==True):
        data[data.columns[77]]=1
    if (window.radioButton_162.isChecked()==True):
        data[data.columns[78]]=1
    if (window.radioButton_161.isChecked()==True):
        data[data.columns[79]]=1
     
    return data  

def features_b3(window,data):  
        
    for i in range (83,104):
        data[data.columns[i]]=0
        
    data[data.columns[83]]=int(window.lineEdit.text())
    
    if (window.radioButton_144.isChecked()==True):
        data[data.columns[84]]=1  
    if (window.radioButton_145.isChecked()==True):
        data[data.columns[85]]=1
    if (window.radioButton_146.isChecked()==True):
        data[data.columns[86]]=1
    if (window.radioButton_147.isChecked()==True):
        data[data.columns[87]]=1
    if (window.radioButton_148.isChecked()==True):
        data[data.columns[88]]=1
    if (window.radioButton_150.isChecked()==True):
        data[data.columns[89]]=1    
    if (window.radioButton_151.isChecked()==True):
        data[data.columns[90]]=1      
    return data

def features_b4(window,data):  
        
    for i in range (92,104):
        data[data.columns[i]]=0
        
       # для ЭКО 
        if (window.radioButton_109.isChecked()==True):
            data[data.columns[92]]=1      
        if (window.radioButton_109.isChecked()==False):
            data[data.columns[92]]=2     
        if (window.radioButton_107.isChecked()==True):
            data[data.columns[93]]=1 
        if ((window.radioButton_125.isChecked()==True) and (window.radioButton_109.isChecked()==True)):
            data[data.columns[94]]=1   
        if ((window.radioButton_125.isChecked()==True) and (window.radioButton_109.isChecked()==False)):
            data[data.columns[94]]=1 
            data[data.columns[95]]=1  
        if (window.radioButton_126.isChecked()==True):
            data[data.columns[94]]=1     
            
       # для Криопереносы 
        if (window.radioButton_175.isChecked()==True):
            data[data.columns[96]]=1      
        if (window.radioButton_176.isChecked()==False):
            data[data.columns[97]]=2     
        if (window.radioButton_178.isChecked()==True):
            data[data.columns[98]]=1 
        if (window.radioButton_179.isChecked()==True):
            data[data.columns[99]]=1 
        if (window.radioButton_111.isChecked()==True):
            data[data.columns[100]]=5  
        if (window.radioButton_181.isChecked()==True):
            data[data.columns[101]]=1     
        if (window.radioButton_182.isChecked()==True):
            data[data.columns[102]]=1 
        if (window.radioButton_184.isChecked()==True):
            data[data.columns[103]]=1     
        if (window.radioButton_109.isChecked()==True):
            data[data.columns[92]]=1      
        if (window.radioButton_109.isChecked()==False):
            data[data.columns[92]]=2    
        if ((window.radioButton_125.isChecked()==True) and (window.radioButton_109.isChecked()==True)):
            data[data.columns[94]]=1   
        if ((window.radioButton_125.isChecked()==True) and (window.radioButton_109.isChecked()==False)):
            data[data.columns[94]]=1 
            data[data.columns[95]]=1  
        if (window.radioButton_126.isChecked()==True):
            data[data.columns[94]]=1           

        return data