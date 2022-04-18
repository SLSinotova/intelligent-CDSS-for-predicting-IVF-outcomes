def result_in_listWidget(listWidget,predictpr,
                         predict_icn,predict_gt,predict_pp,predict_gsd,predict_nov,predict_prpo,
                         predict_break,predict_pret,predict_term,
                         predict_plan,predict_emer,predict_vag,
                         predict_group12,predict_group34,predict_group5):

        if (predict_icn==1):
                                            end='истмико-цервикальная недостаточность'
                                            listWidget.addItem(end)
        if (predict_gt==1):
                                            end='гипертензивные расстройства'
                                            listWidget.addItem(end)
        if (predict_pp==1):
                                            end='предлежание плаценты'
                                            listWidget.addItem(end)
        if (predict_gsd==1):
                                            end='гестационный сахарный диабет'
                                            listWidget.addItem(end)       
        if (predict_nov==1):
                                            end='нарушения количества околоплодных вод'
                                            listWidget.addItem(end)  
        if (predict_prpo==1):
                                            end='преждевременный разрыв плодных оболочек'
                                            listWidget.addItem(end)              
        if (predict_icn==0)and(predict_gt==0)and(predict_pp==0)and(predict_gsd==0)and(predict_nov==0)and(predict_prpo==0):  
                                            end='физиологическое течение беременности'                              
                                            listWidget.addItem(end)
        
        max = 0
        num = 0
        summ = 0
        for prediction in [predict_break[0,1],predict_pret[0,1],predict_term[0,1]]:
            summ = summ+1
            if (prediction > max):
                max = prediction
                num = summ   
  
        if (num == 1): listWidget.addItem('прерывание')    
        elif (num == 2): listWidget.addItem('преждевременные роды')    
        elif (num == 3): listWidget.addItem('срочные роды')  
        
        if (num != 1):
            max1 = 0
            num1 = 0
            summ1 = 0
            for prediction in [predict_plan[0,1],predict_emer[0,1],predict_vag[0,1]]:
                summ1 = summ1+1
                if (prediction > max1):
                    max1 = prediction
                    num1 = summ1   
       
            if (num1 == 1): listWidget.addItem('плановое кс')       
            elif (num1 == 2): listWidget.addItem('экстренное кс')
            elif (num1 == 3): listWidget.addItem('самостоятельные роды')  
        
            max = 0
            num = 0
            summ = 0
            for prediction in [predict_group12[0,1],predict_group34[0,1],predict_group5[0,1]]:
                summ = summ+1
                if (prediction > max):
                    max = prediction
                    num = summ   
        
            if (num == 1): listWidget.addItem('группа здоровья ребенка: 1, 2')    
            elif (num == 2): listWidget.addItem('группа здоровья ребенка: 3, 4')    
            elif (num == 3): listWidget.addItem('группа здоровья ребенка: 5')  

            return num

def diagnosis_result(listWidget,predict_a00_b99,predict_c00_d48,predict_d50_d89,
                     predict_e00_e90,predict_g00_g99,predict_h00_h59,
                     predict_h60_h95,predict_i00_i99,predict_j00_j99,predict_k00_k93,
                     predict_l00_l99,predict_m00_m99,predict_n00_n99,predict_p00_p96,predict_q00_q99):
    a00_b99 = ''
    c00_d48 = ''
    d50_d89 = ''
    e00_e90 = ''
    g00_g99 = ''
    h00_h59 = ''
    h60_h95 = ''
    i00_i99 = ''
    j00_j99 = ''
    k00_k93 = ''
    l00_l99 = ''
    m00_m99 = ''
    n00_n99 = ''
    p00_p96 = ''
    q00_q99 = ''
    if (predict_a00_b99 ==1): a00_b99 = 'A00-B99,'
    if (predict_c00_d48 ==1): c00_d48 = 'C00-D48,'
    if (predict_d50_d89 ==1): d50_d89 = 'D50-D89,'
    if (predict_e00_e90 ==1): e00_e90 = 'E00-E90,'
    if (predict_g00_g99 ==1): g00_g99 = 'G00-G99,'
    if (predict_h00_h59 ==1): h00_h59 = 'H00-H59,'
    if (predict_h60_h95 ==1): h60_h95 = 'H60-H95,'
    if (predict_i00_i99 ==1): i00_i99 = 'I00-I99,'
    if (predict_j00_j99 ==1): j00_j99 = 'J00-J99,'
    if (predict_k00_k93 ==1): k00_k93 = 'K00-K93,'
    if (predict_l00_l99 ==1): l00_l99 = 'L00-L99,'
    if (predict_m00_m99 ==1): m00_m99 = 'M00-M99,'
    if (predict_n00_n99 ==1): n00_n99 = 'N00-N99,'
    if (predict_p00_p96 ==1): p00_p96 = 'P00-P96,'
    if (predict_q00_q99 ==1): q00_q99 = 'Q00-Q99,'

    rez_diagnoz = '('+a00_b99 + c00_d48 + d50_d89 + e00_e90 + g00_g99 + h00_h59 + h60_h95 + i00_i99 + j00_j99 + k00_k93 + l00_l99 + m00_m99 + n00_n99 + p00_p96 + q00_q99 +')'
    if (rez_diagnoz !='()'): 
        if (len(rez_diagnoz) > 42):
            listWidget.addItem(rez_diagnoz[0:41])  
            rez_diagnoz2 = rez_diagnoz[41:len(rez_diagnoz)]
            rez_diagnoz2 = rez_diagnoz2[0:-2] +')'
            listWidget.addItem(rez_diagnoz2) 
        else:
            rez_diagnoz = rez_diagnoz[0:-2] +')'
            listWidget.addItem(rez_diagnoz) 