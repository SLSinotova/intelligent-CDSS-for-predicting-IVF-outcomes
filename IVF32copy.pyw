from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication
import pandas as pd
import models
import result_in_listWidget as res
import features_from_radioButtons as ffrB


Form, _ = uic.loadUiType("GUI2 all.ui")

class Ui (QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui,self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.count)
        self.pushButton_2.clicked.connect(self.count2)
        self.pushButton_5.clicked.connect(self.count3)
        self.pushButton_4.clicked.connect(self.count4)
        
        delegate = ffrB.HTMLDelegate(self.listWidget)
        self.listWidget.setItemDelegate(delegate)
        self.listWidget_2.setItemDelegate(delegate)
        self.listWidget_5.setItemDelegate(delegate)
        self.listWidget_4.setItemDelegate(delegate)
        
    
    def count(self): 

        data_all = pd.DataFrame(index=[0],columns=range(0,104))
        
        data = ffrB.features_b1(self,data_all)
        
        data[data.columns[49]]=1  
        
        predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
        
        predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
        predict_gt =  models.loaded_model_gt.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49]]])
        predict_pp =  models.loaded_model_pp.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49]]])
        predict_gsd =  models.loaded_model_gsd.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,47,49]]])
        
        data[data.columns[50]]=predict_icn
        data[data.columns[51]]=predict_gt
        data[data.columns[52]]=predict_pp
        data[data.columns[53]]=predict_gsd
        
        predict_nov =  models.loaded_model_nov.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,47,48,8,49,50,53]]])
        predict_prpo =  models.loaded_model_prpo.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,49,50,53]]])
    
        data[data.columns[54]]=predict_prpo    
            
        predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
        predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
        predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
        predict_break =  models.loaded_model_break.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,47,48,8,49,51,52,54,50,53]]])
        predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
        predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

        data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
        data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
        data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
        data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
        data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
        
        predict_group12 =  models.loaded_model_group12.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59]]])
        predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
        predict_group5 =  models.loaded_model_group5.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,47,48,8,49,50,51,53,55,56,57,58,59]]])
           
      
        self.listWidget.clear()
        pregnancy='вероятность наступления беременности: '+str(round(predictpr[0,1]*100))+'%'
        self.listWidget.addItem(pregnancy)
        self.listWidget.addItem('<b>при одноплодной беременности:</b>')
        
        num = res.result_in_listWidget(self.listWidget,predictpr,
                                 predict_icn,predict_gt,predict_pp,predict_gsd,predict_nov,predict_prpo,
                                 predict_break,predict_pret,predict_term,
                                 predict_plan,predict_emer,predict_vag,
                                 predict_group12,predict_group34,predict_group5)

        if ((num == 2) or (num == 3)):
            predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
            predict_c00_d48 =  models.loaded_model_c00_d48.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53]]])    
            predict_d50_d89 =  models.loaded_model_d50_d89.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53]]])
            predict_e00_e90 =  models.loaded_model_e00_e90.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53]]])
            predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
            predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
            predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
            predict_i00_i99 =  models.loaded_model_i00_i99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53]]])
            predict_j00_j99 =  models.loaded_model_j00_j99.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53]]])
            predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
            predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
            predict_m00_m99 =  models.loaded_model_m00_m99.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48]]])
            predict_n00_n99 =  models.loaded_model_n00_n99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53]]])
            predict_p00_p96 =  models.loaded_model_p00_p96.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53]]])
            predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
         
        
            res.diagnosis_result(self.listWidget,predict_a00_b99,predict_c00_d48,predict_d50_d89,
                      predict_e00_e90,predict_g00_g99,predict_h00_h59,
                      predict_h60_h95,predict_i00_i99,predict_j00_j99,predict_k00_k93,
                      predict_l00_l99,predict_m00_m99,predict_n00_n99,predict_p00_p96,predict_q00_q99)

        data[data.columns[49]]=2
        self.listWidget.addItem('<b>при многоплодной беременности:</b>')
        predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
        
        predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
        predict_gt =  models.loaded_model_gt.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49]]])
        predict_pp =  models.loaded_model_pp.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49]]])
        predict_gsd =  models.loaded_model_gsd.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,47,49]]])
        
        data[data.columns[50]]=predict_icn
        data[data.columns[51]]=predict_gt
        data[data.columns[52]]=predict_pp
        data[data.columns[53]]=predict_gsd
        
        predict_nov =  models.loaded_model_nov.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,47,48,8,49,50,53]]])
        predict_prpo =  models.loaded_model_prpo.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,49,50,53]]])
            
        data[data.columns[54]]=predict_prpo    
            
        predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
        predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
        predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
        predict_break =  models.loaded_model_break.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,47,48,8,49,51,52,54,50,53]]])
        predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
        predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

        data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
        data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
        data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
        data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
        data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
        
        predict_group12 =  models.loaded_model_group12.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59]]])
        predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
        predict_group5 =  models.loaded_model_group5.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,47,48,8,49,50,51,53,55,56,57,58,59]]])
        

        num = res.result_in_listWidget(self.listWidget,predictpr,
                                         predict_icn,predict_gt,predict_pp,predict_gsd,predict_nov,predict_prpo,
                                         predict_break,predict_pret,predict_term,
                                         predict_plan,predict_emer,predict_vag,
                                         predict_group12,predict_group34,predict_group5)

        if ((num == 2) or (num ==3)):
            predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
            predict_c00_d48 =  models.loaded_model_c00_d48.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53]]])    
            predict_d50_d89 =  models.loaded_model_d50_d89.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53]]])
            predict_e00_e90 =  models.loaded_model_e00_e90.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53]]])
            predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
            predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
            predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
            predict_i00_i99 =  models.loaded_model_i00_i99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53]]])
            predict_j00_j99 =  models.loaded_model_j00_j99.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53]]])
            predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
            predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
            predict_m00_m99 =  models.loaded_model_m00_m99.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48]]])
            predict_n00_n99 =  models.loaded_model_n00_n99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53]]])
            predict_p00_p96 =  models.loaded_model_p00_p96.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53]]])
            predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
         
        
            res.diagnosis_result(self.listWidget,predict_a00_b99,predict_c00_d48,predict_d50_d89,
                          predict_e00_e90,predict_g00_g99,predict_h00_h59,
                          predict_h60_h95,predict_i00_i99,predict_j00_j99,predict_k00_k93,
                          predict_l00_l99,predict_m00_m99,predict_n00_n99,predict_p00_p96,predict_q00_q99) 
       
        return data
##------------------------------------------------------------------------------------------
##--------этап 2--------------------------------------------------------------------------

    def count2(self): 
        
        data_all = Ui.count(self)
        
        data = ffrB.features_b2(self,data_all)

        predictfoln =  models.loaded_model_foln.predict(data[data.columns[[1,2,3,4,5,6,11,12,13,14,15,16,60,18,19,20,21,22,23,24,25,26,27,28,29,61,62,30,31,33,34,80,37,38,41,63,42,64,65,43,44,45,46,66,67,68,69,70,72,74,75,76,77,78,79,8]]])
        predictend =  models.loaded_model_end.predict(data[data.columns[[2,7,10,12,15,16,18,19,20,21,22,24,25,26,29,30,31,32,33,35,36,38,41,42,43,44,45,68,70,71,72,73,74,77,79,8]]])
        predictoocq =  models.loaded_model_oocq.predict(data[data.columns[[1,2,3,5,7,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,67,68,70,71,72,73,74,77,78,79,8]]])
       
        self.listWidget_2.clear()
        if (self.radioButton_53.isChecked()==False):
            self.listWidget_2.addItem('предусмотрена только для программы ЭКО')
        
        else: 
            if (self.radioButton_155.isChecked()==True):
                foln='ожидаемое количество фолликул: 2'
            else:
                foln='ожидаемое количество фолликул: '+str(int(predictfoln))
            self.listWidget_2.addItem(foln)
            if (predictend==1):
                                            end='толщина эндометрия 8-15 мм'
            else:  
                                            end='толщина эндометрия менее 8 мм'                              
            self.listWidget_2.addItem(end)

            if (predictoocq==1):
                                            ooc='хорошее качество ооцитов'
            else:  
                                            ooc='плохое качество ооцитов'                            
            self.listWidget_2.addItem(ooc)
        
            data[data.columns[80]]=int(predictfoln)
            data[data.columns[81]]=predictend
            data[data.columns[82]]=predictoocq       
        
            data[data.columns[49]]=1  
            predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
        
            predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
            predict_gt =  models.loaded_model_gt.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49]]])
            predict_pp =  models.loaded_model_pp.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49]]])
            predict_gsd2 =  models.loaded_model_gsd2.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,70,71,72,74,77,79,49]]])
        
            data[data.columns[50]]=predict_icn
            data[data.columns[51]]=predict_gt
            data[data.columns[52]]=predict_pp
            data[data.columns[53]]=predict_gsd2
        
            predict_nov2 =  models.loaded_model_nov2.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,71,72,74,77,8,49,50,53,82]]])
            predict_prpo =  models.loaded_model_prpo.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,49,50,53]]])
    
            data[data.columns[54]]=predict_prpo    
            
            predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            predict_break2 =  models.loaded_model_break2.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,81,82,51,52,54,50,53]]])
            predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

            data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
        
            predict_group122 =  models.loaded_model_group122.predict_proba(data[data.columns[[7,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,71,72,74,77,79,49,50,53,55,56,57,58,59,81,82]]])
            predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
            predict_group52 =  models.loaded_model_group52.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,67,71,72,77,79,8,49,50,51,53,55,56,57,58,59,81,82]]])
        
        
            pregnancy='вероятность наступления беременности: '+str(round(predictpr[0,1]*100))+'%'
            self.listWidget_2.addItem(pregnancy)
            self.listWidget_2.addItem('<b>при одноплодной беременности:</b>')

            num = res.result_in_listWidget(self.listWidget_2,predictpr,
                                     predict_icn,predict_gt,predict_pp,predict_gsd2,predict_nov2,predict_prpo,
                                     predict_break2,predict_pret,predict_term,
                                     predict_plan,predict_emer,predict_vag,
                                     predict_group122,predict_group34,predict_group52)

            if ((num == 2) or (num ==3)):
                predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                predict_c00_d48_2 =  models.loaded_model_c00_d48_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53,72,73,77,79]]])    
                predict_d50_d89_2 =  models.loaded_model_d50_d89_2.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53,71,73]]])
                predict_e00_e90_2 =  models.loaded_model_e00_e90_2.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,74,77,79]]])
                predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
                predict_i00_i99_2 =  models.loaded_model_i00_i99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53,72,73,74,77,79,81]]])
                predict_j00_j99_2 =  models.loaded_model_j00_j99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,77]]])
                predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
                predict_m00_m99 =  models.loaded_model_m00_m99.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48]]])
                predict_n00_n99_2 =  models.loaded_model_n00_n99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53,72,73,77]]])
                predict_p00_p96_2 =  models.loaded_model_p00_p96_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,72,74]]])
                predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
         
                res.diagnosis_result(self.listWidget_2,predict_a00_b99,predict_c00_d48_2,predict_d50_d89_2,
                 predict_e00_e90_2,predict_g00_g99,predict_h00_h59,
                 predict_h60_h95,predict_i00_i99_2,predict_j00_j99_2,predict_k00_k93,
                 predict_l00_l99,predict_m00_m99,predict_n00_n99_2,predict_p00_p96_2,predict_q00_q99) 

                data[data.columns[49]]=2 
                self.listWidget_2.addItem('<b>при многоплодной беременности:</b>')
                predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
            
                predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
                predict_gt =  models.loaded_model_gt.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49]]])
                predict_pp =  models.loaded_model_pp.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49]]])
                predict_gsd2 =  models.loaded_model_gsd2.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,70,71,72,74,77,79,49]]])
            
                data[data.columns[50]]=predict_icn
                data[data.columns[51]]=predict_gt
                data[data.columns[52]]=predict_pp
                data[data.columns[53]]=predict_gsd2
            
                predict_nov2 =  models.loaded_model_nov2.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,71,72,74,77,8,49,50,53,82]]])
                predict_prpo =  models.loaded_model_prpo.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,49,50,53]]])
        
                data[data.columns[54]]=predict_prpo    
                
                predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
                predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
                predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
                predict_break2 =  models.loaded_model_break2.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,81,82,51,52,54,50,53]]])
                predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
                predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
    
                data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
                data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
                data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
                data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
                data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
            
                predict_group122 =  models.loaded_model_group122.predict_proba(data[data.columns[[7,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,71,72,74,77,79,49,50,53,55,56,57,58,59,81,82]]])
                predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
                predict_group52 =  models.loaded_model_group52.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,67,71,72,77,79,8,49,50,51,53,55,56,57,58,59,81,82]]])
            
                num = res.result_in_listWidget(self.listWidget_2,predictpr,
                                         predict_icn,predict_gt,predict_pp,predict_gsd2,predict_nov2,predict_prpo,
                                         predict_break2,predict_pret,predict_term,
                                         predict_plan,predict_emer,predict_vag,
                                         predict_group122,predict_group34,predict_group52)
    
                if ((num == 2) or (num ==3)):
                    predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                    predict_c00_d48_2 =  models.loaded_model_c00_d48_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53,72,73,77,79]]])    
                    predict_d50_d89_2 =  models.loaded_model_d50_d89_2.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53,71,73]]])
                    predict_e00_e90_2 =  models.loaded_model_e00_e90_2.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,74,77,79]]])
                    predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                    predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                    predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
                    predict_i00_i99_2 =  models.loaded_model_i00_i99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53,72,73,74,77,79,81]]])
                    predict_j00_j99_2 =  models.loaded_model_j00_j99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,77]]])
                    predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                    predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
                    predict_m00_m99 =  models.loaded_model_m00_m99.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48]]])
                    predict_n00_n99_2 =  models.loaded_model_n00_n99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53,72,73,77]]])
                    predict_p00_p96_2 =  models.loaded_model_p00_p96_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,72,74]]])
                    predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
             
                    res.diagnosis_result(self.listWidget_2,predict_a00_b99,predict_c00_d48_2,predict_d50_d89_2,
                     predict_e00_e90_2,predict_g00_g99,predict_h00_h59,
                     predict_h60_h95,predict_i00_i99_2,predict_j00_j99_2,predict_k00_k93,
                     predict_l00_l99,predict_m00_m99,predict_n00_n99_2,predict_p00_p96_2,predict_q00_q99) 
         
        return data
##------------------------------------------------------------------------------------------
##--------этап 3--------------------------------------------------------------------------

    def count3(self):   
        
        data_all = Ui.count2(self)
        
        data = ffrB.features_b3(self,data_all)
          
        predict3_6B =  models.loaded_model_3_6B.predict(data[data.columns[[83]]])
        
        self.listWidget_5.clear()
        if (self.radioButton_53.isChecked()==False):
            self.listWidget_5.addItem('не предусмотрено для программы Криопереносы')
        
        else:    
            p3_6B = 'количество клеток на 3 сутки (> 6В):  '+str(int(predict3_6B))
            data[data.columns[91]]=int(predict3_6B)
            predict5_3BB =  models.loaded_model_5_3BB.predict(data[data.columns[[83,91]]])
            predict56_3BB =  models.loaded_model_56_3BB.predict(data[data.columns[[83,91]]])
            predict_BS =  models.loaded_model_BS.predict(data[data.columns[[83,91]]])      
        
            self.listWidget_5.addItem(p3_6B) 
            p5_3BB = 'количество бластоцист на 5 сутки (> 3BB):  '+str(int(predict5_3BB))
            p56_3BB = 'количество бластоцист на 5-6 сутки (> 3BВ):  '+str(int(predict56_3BB))
            p_BS = 'общее количество бластоцист на 5-6 сутки:  '+str(int(predict_BS))
            self.listWidget_5.addItem(p5_3BB) 
            self.listWidget_5.addItem(p56_3BB) 
            self.listWidget_5.addItem(p_BS) 

        return data
##------------------------------------------------------------------------------------------
##--------этап 4--------------------------------------------------------------------------

    def count4(self):  
        
        data_all = Ui.count3(self)

        data = ffrB.features_b4(self,data_all)
        
        if ((self.radioButton_53.isChecked()==True) and (int(self.lineEdit.text()) !=0)):
            self.listWidget_4.clear()
            self.listWidget_4.addItem('<b>программа ЭКО:</b>')

            data[data.columns[49]]=1  
            predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
        
            predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
            predict_gt3 =  models.loaded_model_gt3.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49,87,89,90]]])
            predict_pp3 =  models.loaded_model_pp3.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49,82,89,94]]])
            predict_gsd2 =  models.loaded_model_gsd2.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,70,71,72,74,77,79,49]]])
        
            data[data.columns[50]]=predict_icn
            data[data.columns[51]]=predict_gt3
            data[data.columns[52]]=predict_pp3
            data[data.columns[53]]=predict_gsd2
        
            predict_nov3 =  models.loaded_model_nov3.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,71,72,74,77,8,49,50,53,82,84]]])
            predict_prpo3 =  models.loaded_model_prpo3.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,8,49,50,53,87]]])
    
            data[data.columns[54]]=predict_prpo3    
            
            predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            predict_break3 =  models.loaded_model_break3.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,81,82,51,52,54,50,53]]])
            predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

            data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
    
            predict_group123 =  models.loaded_model_group123.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59,81,82,84,88,92]]])
            predict_group34 = models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
            predict_group53 =  models.loaded_model_group53.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,67,71,72,77,79,8,49,50,51,53,55,56,57,58,59,60,81,82,84,85]]])
    
    
            pregnancy='вероятность наступления беременности: '+str(round(predictpr[0,1]*100))+'%'
            self.listWidget_4.addItem(pregnancy)
            self.listWidget_4.addItem('<b>при одноплодной беременности:</b>')
            
            num = res.result_in_listWidget(self.listWidget_4,predictpr,
                                    predict_icn,predict_gt3,predict_pp3,predict_gsd2,predict_nov3,predict_prpo3,
                                    predict_break3,predict_pret,predict_term,
                                    predict_plan,predict_emer,predict_vag,
                                    predict_group123,predict_group34,predict_group53)
           
            if ((num == 2) or (num ==3)):
                predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                predict_c00_d48_eco =  models.loaded_model_c00_d48_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53,72,73,77,79,83,85,90]]])    
                predict_d50_d89_eco =  models.loaded_model_d50_d89_eco.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53,71,73,83,87]]])
                predict_e00_e90_eco =  models.loaded_model_e00_e90_eco.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,74,77,79,83,87,89]]])
                predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                predict_h60_h95_eco =  models.loaded_model_h60_h95_eco.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53,72,73,74,79,82,83,84,87,88,89,90]]])
                predict_i00_i99_2 =  models.loaded_model_i00_i99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53,72,73,74,77,79,81]]])
                predict_j00_j99_eco =  models.loaded_model_j00_j99_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,77,83,85,90]]])
                predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
                predict_m00_m99_eco =  models.loaded_model_m00_m99_eco.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48,83,90]]])
                predict_n00_n99_eco =  models.loaded_model_n00_n99_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53,72,73,77,83,84,85,89]]])
                predict_p00_p96_eco =  models.loaded_model_p00_p96_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,72,74,83]]])
                predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
         
    
                res.diagnosis_result(self.listWidget_4,predict_a00_b99,predict_c00_d48_eco,predict_d50_d89_eco,
                 predict_e00_e90_eco,predict_g00_g99,predict_h00_h59,
                 predict_h60_h95_eco,predict_i00_i99_2,predict_j00_j99_eco,predict_k00_k93,
                 predict_l00_l99,predict_m00_m99_eco,predict_n00_n99_eco,predict_p00_p96_eco,predict_q00_q99) 

            data[data.columns[49]]=2  
            predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
            predict_gt3 =  models.loaded_model_gt3.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49,87,89,90]]])
            predict_pp3 =  models.loaded_model_pp3.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49,82,89,94]]])
            predict_gsd2 =  models.loaded_model_gsd2.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,70,71,72,74,77,79,49]]])
            
            data[data.columns[50]]=predict_icn
            data[data.columns[51]]=predict_gt3
            data[data.columns[52]]=predict_pp3
            data[data.columns[53]]=predict_gsd2
        
            predict_nov3 =  models.loaded_model_nov3.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,71,72,74,77,8,49,50,53,82,84]]])
            predict_prpo3 =  models.loaded_model_prpo3.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,8,49,50,53,87]]])
    
            data[data.columns[54]]=predict_prpo3    
            
            predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            predict_break3 =  models.loaded_model_break3.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,81,82,51,52,54,50,53]]])
            predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

            data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
    
            predict_group123 =  models.loaded_model_group123.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59,81,82,84,88,92]]])
            predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
            predict_group53 =  models.loaded_model_group53.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,67,71,72,77,79,8,49,50,51,53,55,56,57,58,59,60,81,82,84,85]]])
    

            self.listWidget_4.addItem('<b>при многоплодной беременности:</b>')

            num = res.result_in_listWidget(self.listWidget_4,predictpr,
                                     predict_icn,predict_gt3,predict_pp3,predict_gsd2,predict_nov3,predict_prpo3,
                                     predict_break3,predict_pret,predict_term,
                                     predict_plan,predict_emer,predict_vag,
                                     predict_group123,predict_group34,predict_group53)

            if ((num == 2) or (num ==3)):
                predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                predict_c00_d48_eco =  models.loaded_model_c00_d48_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53,72,73,77,79,83,85,90]]])    
                predict_d50_d89_eco =  models.loaded_model_d50_d89_eco.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53,71,73,83,87]]])
                predict_e00_e90_eco =  models.loaded_model_e00_e90_eco.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,74,77,79,83,87,89]]])
                predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                predict_h60_h95_eco =  models.loaded_model_h60_h95_eco.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53,72,73,74,79,82,83,84,87,88,89,90]]])
                predict_i00_i99_2 =  models.loaded_model_i00_i99_2.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53,72,73,74,77,79,81]]])
                predict_j00_j99_eco =  models.loaded_model_j00_j99_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,77,83,85,90]]])
                predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                predict_l00_l99 =  models.loaded_model_l00_l99.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53]]])
                predict_m00_m99_eco =  models.loaded_model_m00_m99_eco.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48,83,90]]])
                predict_n00_n99_eco =  models.loaded_model_n00_n99_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53,72,73,77,83,84,85,89]]])
                predict_p00_p96_eco =  models.loaded_model_p00_p96_eco.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,72,74,83]]])
                predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
             
                res.diagnosis_result(self.listWidget_4,predict_a00_b99,predict_c00_d48_eco,predict_d50_d89_eco,
                 predict_e00_e90_eco,predict_g00_g99,predict_h00_h59,
                 predict_h60_h95_eco,predict_i00_i99_2,predict_j00_j99_eco,predict_k00_k93,
                 predict_l00_l99,predict_m00_m99_eco,predict_n00_n99_eco,predict_p00_p96_eco,predict_q00_q99) 
       
            
        elif ((self.radioButton_53.isChecked()==True) and (int(self.lineEdit.text()) ==0)):
            self.listWidget_4.clear()
            self.listWidget_4.addItem('заполните ОПЛОДОТВОРЕНИЕ')  
            

### крио

        if (self.radioButton_54.isChecked()==True):
            self.listWidget_4.clear()
            self.listWidget_4.addItem('<b>программа Криопереносы:</b>')  
        
            data[data.columns[49]]=1  
            predictpr =  models.loaded_modelpr.predict_proba(data[data.columns[[7,10,11,12,15,16,17,18,19,21,25,26,27,32,36,37,38,41,43,47,48]]])
        
            predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
            predict_gt3crio =  models.loaded_model_gt3crio.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49,96,97,98,99,102,92]]])
            predict_pp3crio =  models.loaded_model_pp3crio.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49,96,99,102,103,92]]])
            predict_gsd =  models.loaded_model_gsd.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,47,49]]])
        
        
            data[data.columns[50]]=predict_icn
            data[data.columns[51]]=predict_gt3crio
            data[data.columns[52]]=predict_pp3crio
            data[data.columns[53]]=predict_gsd
        
            predict_nov3crio =  models.loaded_model_nov3crio.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,47,48,8,49,50,53,98,102,95]]])
            predict_prpo3crio =  models.loaded_model_prpo3crio.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,8,49,50,53,97,98,99,101,102,103,92,95]]])
    
            data[data.columns[54]]=predict_prpo3crio    
            
            predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            predict_break3crio =  models.loaded_model_break3crio.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,96,98,99,100,101,102,103,92,95]]])
            predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

            data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
    
            predict_group12 =  models.loaded_model_group12.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59]]])
            predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
            predict_group53crio =  models.loaded_model_group53crio.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,47,48,8,49,50,51,53,55,56,57,58,96,97,98,99,92]]])
    
    
            pregnancy='вероятность наступления беременности: '+str(round(predictpr[0,1]*100))+'%'
            self.listWidget_4.addItem(pregnancy)
            self.listWidget_4.addItem('<b>при одноплодной беременности:</b>')

            num = res.result_in_listWidget(self.listWidget_4,predictpr,
                                     predict_icn,predict_gt3crio,predict_pp3crio,predict_gsd,predict_nov3crio,predict_prpo3crio,
                                     predict_break3crio,predict_pret,predict_term,
                                     predict_plan,predict_emer,predict_vag,
                                     predict_group12,predict_group34,predict_group53crio)
            
            if ((num == 2) or (num ==3)):
                predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                predict_c00_d48 =  models.loaded_model_c00_d48.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53]]])    
                predict_d50_d89 =  models.loaded_model_d50_d89.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53]]])
                predict_e00_e90_crio =  models.loaded_model_e00_e90_crio.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,96,97,98,99,102,103]]])
                predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
                predict_i00_i99 =  models.loaded_model_i00_i99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53]]])
                predict_j00_j99_crio =  models.loaded_model_j00_j99_crio.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,96,97,98,99,102,103]]])
                predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                predict_l00_l99_crio =  models.loaded_model_l00_l99_crio.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53,103]]])
                predict_m00_m99_crio =  models.loaded_model_m00_m99_crio.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48,97,99,102,103]]])
                predict_n00_n99 =  models.loaded_model_n00_n99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53]]])
                predict_p00_p96_crio =  models.loaded_model_p00_p96_crio.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,96,97,98,99,102]]])
                predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
     
                res.diagnosis_result(self.listWidget_4,predict_a00_b99,predict_c00_d48,predict_d50_d89,
                 predict_e00_e90_crio,predict_g00_g99,predict_h00_h59,
                 predict_h60_h95,predict_i00_i99,predict_j00_j99_crio,predict_k00_k93,
                 predict_l00_l99_crio,predict_m00_m99_crio,predict_n00_n99,predict_p00_p96_crio,predict_q00_q99) 

            data[data.columns[49]]=2  

            predict_icn =  models.loaded_model_icn.predict(data[data.columns[[9,11,20,26,27,31,38,41,43,45,47,8,49]]])
            predict_gt3crio =  models.loaded_model_gt3crio.predict(data[data.columns[[1,9,10,12,15,16,18,20,21,25,29,30,31,32,35,38,39,41,42,43,45,47,48,8,49,96,97,98,99,102,92]]])
            predict_pp3crio =  models.loaded_model_pp3crio.predict(data[data.columns[[1,2,5,7,11,12,13,14,20,22,24,25,27,28,29,30,31,32,33,34,36,37,38,41,43,45,47,48,8,49,96,99,102,103,92]]])
            predict_gsd =  models.loaded_model_gsd.predict(data[data.columns[[10,11,12,15,16,21,25,30,32,35,38,43,47,49]]])
        
        
            data[data.columns[50]]=predict_icn
            data[data.columns[51]]=predict_gt3crio
            data[data.columns[52]]=predict_pp3crio
            data[data.columns[53]]=predict_gsd
        
            predict_nov3crio =  models.loaded_model_nov3crio.predict(data[data.columns[[1,5,10,12,14,15,17,18,24,25,26,28,29,33,34,35,38,41,42,43,44,47,48,8,49,50,53,98,102,95]]])
            predict_prpo3crio =  models.loaded_model_prpo3crio.predict(data[data.columns[[1,3,5,7,9,10,11,12,13,14,15,16,19,20,24,25,26,29,30,31,32,33,34,35,38,41,42,43,44,47,48,8,49,50,53,97,98,99,101,102,103,92,95]]])
    
            data[data.columns[54]]=predict_prpo3crio    
            
            predict_plan =  models.loaded_model_plan.predict_proba(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            predict_emer =  models.loaded_model_emer.predict_proba(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            predict_vag =  models.loaded_model_vag.predict_proba(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            predict_break3crio =  models.loaded_model_break3crio.predict_proba(data[data.columns[[1,2,5,10,11,12,13,15,16,20,21,24,25,28,30,32,33,35,36,37,38,41,43,44,45,46,67,69,71,72,74,77,79,8,49,96,98,99,100,101,102,103,92,95]]])
            predict_pret =  models.loaded_model_pret.predict_proba(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            predict_term =  models.loaded_model_term.predict_proba(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])

            data[data.columns[55]]= models.loaded_model_plan.predict(data[data.columns[[2,3,9,10,12,16,22,25,26,30,47,49,54,50,53]]])
            data[data.columns[56]]= models.loaded_model_emer.predict(data[data.columns[[2,12,24,25,33,37,38,39,41,43,49,50,53]]])
            data[data.columns[57]]= models.loaded_model_vag.predict(data[data.columns[[2,9,15,16,26,27,49,52,50]]])
            data[data.columns[58]]= models.loaded_model_pret.predict(data[data.columns[[1,4,6,7,11,12,16,18,20,21,22,23,24,25,27,28,32,33,34,37,38,40,41,42,46,8,49,54,50,53]]])
            data[data.columns[59]]= models.loaded_model_term.predict(data[data.columns[[1,6,12,16,18,20,21,23,27,28,32,33,34,37,38,40,41,42,43,8,49,51,54,50,53]]])
    
            predict_group12 =  models.loaded_model_group12.predict_proba(data[data.columns[[7,10,12,13,14,17,20,22,25,29,30,31,32,37,38,41,43,44,47,48,49,50,53,55,56,57,58,59]]])
            predict_group34 =  models.loaded_model_group34.predict_proba(data[data.columns[[5,11,12,16,20,22,25,30,47,49,50,53,55,56,57,58,59]]])
            predict_group53crio =  models.loaded_model_group53crio.predict_proba(data[data.columns[[2,5,7,10,11,12,13,15,16,19,20,21,24,25,26,27,28,29,31,32,33,35,36,38,42,43,44,45,47,48,8,49,50,51,53,55,56,57,58,96,97,98,99,92]]])
    

            self.listWidget_4.addItem('<b>при многоплодной беременности:</b>')

            num = res.result_in_listWidget(self.listWidget_4,predictpr,
                                     predict_icn,predict_gt3crio,predict_pp3crio,predict_gsd,predict_nov3crio,predict_prpo3crio,
                                     predict_break3crio,predict_pret,predict_term,
                                     predict_plan,predict_emer,predict_vag,
                                     predict_group12,predict_group34,predict_group53crio)
            
            if ((num == 2) or (num ==3)):
                predict_a00_b99 =  models.loaded_model_a00_b99.predict(data[data.columns[[1,3,5,6,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,49,55,56,57,58,59,50,51,53]]])
                predict_c00_d48 =  models.loaded_model_c00_d48.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,35,36,37,38,39,41,42,65,43,44,45,46,47,48,53]]])    
                predict_d50_d89 =  models.loaded_model_d50_d89.predict(data[data.columns[[1,5,7,11,12,13,15,16,17,19,20,21,22,24,25,26,27,28,29,31,32,33,35,36,37,38,39,40,41,42,43,44,45,47,48,53]]])
                predict_e00_e90_crio =  models.loaded_model_e00_e90_crio.predict(data[data.columns[[1,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,41,42,65,43,44,45,46,47,48,49,53,96,97,98,99,102,103]]])
                predict_g00_g99 =  models.loaded_model_g00_g99.predict(data[data.columns[[12,13,20,25,32,37,41,43,47,49,55]]])
                predict_h00_h59 =  models.loaded_model_h00_h59.predict(data[data.columns[[12,58,59]]])
                predict_h60_h95 =  models.loaded_model_h60_h95.predict(data[data.columns[[1,3,5,7,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,30,31,32,33,34,80,35,36,37,38,39,41,42,65,43,44,45,46,47,48,55,56,57,50,53]]])
                predict_i00_i99 =  models.loaded_model_i00_i99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,17,19,20,21,22,24,25,26,27,28,29,61,62,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,49,55,56,57,58,50,51,53]]])
                predict_j00_j99_crio =  models.loaded_model_j00_j99_crio.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,17,20,21,22,24,25,26,28,30,31,32,33,35,37,38,39,41,42,65,43,44,45,46,47,48,49,56,53,96,97,98,99,102,103]]])
                predict_k00_k93 =  models.loaded_model_k00_k93.predict(data[data.columns[[3,5,12,13,15,16,20,25,27,31,32,33,35,38,41,42,43,47,53]]])
                predict_l00_l99_crio =  models.loaded_model_l00_l99_crio.predict(data[data.columns[[1,5,11,12,13,14,15,16,20,22,24,25,26,27,28,29,30,31,32,33,35,38,41,42,43,48,53,103]]])
                predict_m00_m99_crio =  models.loaded_model_m00_m99_crio.predict(data[data.columns[[1,7,11,12,13,14,15,16,17,20,21,22,24,25,26,27,28,30,31,32,33,35,36,37,38,41,42,43,44,45,47,48,97,99,102,103]]])
                predict_n00_n99 =  models.loaded_model_n00_n99.predict(data[data.columns[[1,3,5,7,9,11,12,13,14,15,16,20,21,22,24,25,26,27,28,29,61,30,31,32,33,35,36,37,38,40,41,42,65,43,44,45,47,48,56,50,53]]])
                predict_p00_p96_crio =  models.loaded_model_p00_p96_crio.predict(data[data.columns[[1,3,5,7,9,11,12,13,15,16,19,20,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,42,43,44,45,46,47,48,53,96,97,98,99,102]]])
                predict_q00_q99 =  models.loaded_model_q00_q99.predict(data[data.columns[[11,12,13,15,16,25,26,28,30,32,37,38,41,43,48]]])
             
                res.diagnosis_result(self.listWidget_4,predict_a00_b99,predict_c00_d48,predict_d50_d89,
                 predict_e00_e90_crio,predict_g00_g99,predict_h00_h59,
                 predict_h60_h95,predict_i00_i99,predict_j00_j99_crio,predict_k00_k93,
                 predict_l00_l99_crio,predict_m00_m99_crio,predict_n00_n99,predict_p00_p96_crio,predict_q00_q99) 
            


if __name__ == '__main__':
    app = QApplication([])      # 1. Instantiate ApplicationContext
    window = Ui()
    window.show()
    app.exec_()  
           
   

