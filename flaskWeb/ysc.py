#coding=utf-8

import pandas as pd
import numpy as np
import math

def init():
    path = r"C:\Users\shilzhan\mygithub\mem\flaskWeb\ysc.xlsx"
    df1 = pd.read_excel(path,sheet_name=[0,1,2])
    df2 = pd.read_excel(path,sheet_name=[3,4,5,6])
    df3 = pd.read_excel(path,sheet_name=[7,8,9])
    df4 = pd.read_excel(path,sheet_name=[10,11,12,13,14,15])
    return df1,df2,df3,df4
def cal(S):
    df1,df2,df3,df4 = init()
    df1[0]['参数值'] = df1[0]['参数'].apply(lambda x:int(x[2:4]))
    df1[1]['参数值'] = df1[1]['参数'].apply(lambda x:int(''.join([i for i in x if i.isdigit()])))
    df1[2]['参数值'] = df1[2].apply(lambda x:int(x['参数'][2:3]) if x['备注']==1 else int(x['参数'][0:2]) ,axis=1)
    rs1 = []
    df1[0]['数量'] = S*0.6/df1[0]['参数值']
    df1[0]['数量'] = df1[0]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df1[0]['总价'] = df1[0]['数量'] * df1[0]['价格（万元）'] 
    df1[0]['总能力'] = df1[0]['数量'] * df1[0]['参数值']
    rs1.append(df1[0][(df1[0]['总价'] >= S*0.6*0.75) & (df1[0]['总价'] <= S*0.6*1.25)])
    rs1[0]['得分'] = rs1[0]['总价'].apply(lambda x:5 if x<=S*0.6 else 5.0- ((x-S*0.6)/(S*0.6) * 4)*5.0)
    df1[1]['数量'] = (S/8)/df1[1]['参数值']
    df1[1]['数量'] = df1[1]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df1[1]['总价'] = df1[1]['数量'] * df1[1]['价格（万元）'] 
    df1[1]['总能力'] = df1[1]['数量'] * df1[1]['参数值']
    rs1.append(df1[1][(df1[1]['总价'] >= S*0.7*0.75) & (df1[1]['总价'] <= S*0.7*1.25)])
    rs1[1]['得分'] = rs1[1]['总价'].apply(lambda x:10 if x<=S*0.7 else 10.0- ((x-S*0.7)/(S*0.7) * 4)*10.0)
    df1[2]['数量'] = (S/8)/df1[2]['参数值']
    df1[2]['数量'] = df1[2]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df1[2]['总价'] = df1[2]['数量'] * df1[2]['价格（万元）'] 
    df1[2]['总能力'] = df1[2]['数量'] * df1[2]['参数值']
    templist = df1[2][:9]['总价'].tolist()
    df1[2]['合价'] =  df1[2][9:]['总价'].apply(lambda x:[x+i for i in templist])
    df1[2]['ind'] = df1[2].index.tolist()
    def cal_point(x,base,ind):
        rs = []
        c = 0

        for i in x:
            if i >= base*0.75 and i <=base*1.25:
                if i <= base:
                    rs.append((5,ind,c))
                else:
                    t = (5.0- ((i-base)/(base) * 4)*5.0)
                    rs.append((t,ind,c))
            else:
                rs.append((0,ind,c))
            c+=1
        return rs
    temp_rs = sorted(df1[2][9:].apply(lambda x:cal_point(x['合价'],S*0.15,x['ind']),axis=1).agg(sum),key=lambda x:x[0],reverse=True)
    newd = pd.DataFrame(columns=['装置','参数','材质','总价','数量','总能力','得分','厂家'])
    c = 0
    for i in temp_rs:
        if temp_rs[0][0] - i[0] <=0.5:        
            canshu = df1[2].loc[i[2]]['参数'] + ' + '+df1[2].loc[i[1]]['参数']
            caizhi = df1[2].loc[i[2]]['材质'] + ' + '+df1[2].loc[i[1]]['材质']
            zongjia = df1[2].loc[i[2]]['总价'] + df1[2].loc[i[1]]['总价']
            shuliang = df1[2].loc[i[2]]['数量'] + df1[2].loc[i[1]]['数量']
            nengli = df1[2].loc[i[2]]['总能力'] + df1[2].loc[i[1]]['总能力']
            defen = i[0]
            changjia = df1[2].loc[i[2]]['厂家'] + ' + '+df1[2].loc[i[1]]['厂家']
            newd.loc[c] = ['沥液箱+输送泵',canshu,caizhi,zongjia,shuliang,nengli,defen,changjia]
            c+=1
    rs1.append(newd)

    df2[3]['参数值'] = df2[3]['参数'].apply(lambda x:float(x[:-3]))
    df2[4]['参数值'] = df2[4]['参数'].apply(lambda x:int(x[:-3]))
    df2[5]['参数值'] = df2[5]['参数'].apply(lambda x:int(x[:-3]))
    df2[6]['参数值'] = df2[6]['参数'].apply(lambda x:int(x[:-3]))
    df2[5].columns = df2[5].columns.str.replace('Unnamed: 5','备注')
    rs2= []
    df2[3]['数量'] = (S/8)/df2[3]['参数值']
    df2[3]['数量'] = df2[3]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df2[3]['总价'] = df2[3]['数量'] * df2[3]['价格（万元）'] 
    df2[3]['总能力'] = df2[3]['数量'] * df2[3]['参数值']
    rs2.append(df2[3][(df2[3]['总价'] >= S*0.9*0.75) & (df2[3]['总价'] <= S*0.9*1.25)])
    rs2[0]['得分'] = rs2[0]['总价'].apply(lambda x:10 if x<=S*0.9 else 10.0- ((x-S*0.9)/(S*0.9) * 4)*10.0)


    df2[4]['数量'] = (S/8)/df2[4]['参数值']
    df2[4]['数量'] = df2[4]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df2[4]['总价'] = df2[4]['数量'] * df2[4]['价格（万元）'] 
    df2[4]['总能力'] = df2[4]['数量'] * df2[4]['参数值']
    rs2.append(df2[4][(df2[4]['总价'] >= S*0.3*0.75) & (df2[4]['总价'] <= S*0.3*1.25)])
    rs2[1]['得分'] = rs2[1]['总价'].apply(lambda x:5 if x<=S*0.3 else 5- ((x-S*0.3)/(S*0.3) * 4)*5.0)

    df2[5]['数量'] = (S/8)/df2[5]['参数值']
    df2[5]['数量'] = df2[5]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df2[5]['总价'] = df2[5]['数量'] * df2[5]['价格（万元）'] 
    df2[5]['总能力'] = df2[5]['数量'] * df2[5]['参数值']
    tempdf25 = df2[5][df2[5]['备注']==1]
    plusva = np.min(df2[5][df2[5]['备注']==2]['总价'])
    rs2.append(tempdf25[(tempdf25['总价'] + plusva >= S*1.15*0.75) & (tempdf25['总价'] + plusva<= S*1.15*1.25)])
    rs2[2]['得分'] = rs2[2]['总价'].apply(lambda x:10 if x+plusva<=S*1.15 else 10- ((x+plusva-S*1.15)/(S*1.15) * 4)*10.0)
    rs2[2].loc[24] = df2[5].loc[24]

    df2[6]['数量'] = (S/8)/df2[6]['参数值']
    df2[6]['数量'] = df2[6]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df2[6]['总价'] = df2[6]['数量'] * df2[6]['价格（万元）'] 
    df2[6]['总能力'] = df2[6]['数量'] * df2[6]['参数值']
    rs2.append(df2[6])

    df3[7]['参数值'] = df3[7]['参数'].apply(lambda x:float(x[:2]))
    df3[8]['参数值'] = df3[8]['参数'].apply(lambda x:int(x[:-3]))
    df3[9]['参数值'] = df3[9]['参数'].apply(lambda x:int(x[:-3]))
    rs3= []
    df3[7]['数量'] = (S/8)/df3[7]['参数值']
    df3[7]['数量'] = df3[7]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df3[7]['总价'] = df3[7]['数量'] * df3[7]['价格（万元）'] 
    df3[7]['总能力'] = df3[7]['数量'] * df3[7]['参数值']
    rs3.append(df3[7][(df3[7]['总价'] >= S*0.2*0.75) & (df3[7]['总价'] <= S*0.2*1.25)])
    rs3[0]['得分'] = rs3[0]['总价'].apply(lambda x:10 if x<=S*0.2 else 10.0- ((x-S*0.2)/(S*0.2) * 4)*10.0)

    df3[8]['数量'] = (S/8)/df3[8]['参数值']
    df3[8]['数量'] = df3[8]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df3[8]['总价'] = df3[8]['数量'] * df3[8]['价格（万元）'] 
    df3[8]['总能力'] = df3[8]['数量'] * df3[8]['参数值']
    rs3.append(df3[8][(df3[8]['总价'] >= S*0.2*0.75) & (df3[8]['总价'] <= S*0.2*1.25)])
    rs3[1]['得分'] = rs3[1]['总价'].apply(lambda x:10 if x<=S*0.2 else 10.0- ((x-S*0.2)/(S*0.2) * 4)*10.0)

    df3[9]['数量'] = (S/40)/df3[9]['参数值']
    df3[9]['数量'] = df3[9]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df3[9]['总价'] = df3[9]['数量'] * df3[9]['价格（万元）'] 
    df3[9]['总能力'] = df3[9]['数量'] * df3[9]['参数值']
    rs3.append(df3[9][(df3[9]['总价'] >= S*0.1*0.75) & (df3[9]['总价'] <= S*0.1*1.25)])
    rs3[2]['得分'] = rs3[2]['总价'].apply(lambda x:5 if x<=S*0.1 else 5- ((x-S*0.1)/(S*0.1) * 4)*5.0)
    df4[10]['参数值'] = df4[10]['参数'].apply(lambda x:float(x[:2]))
    df4[11]['参数值'] = df4[11]['参数'].apply(lambda x:int(x[:-4]))
    df4[12]['参数值'] = df4[12]['参数'].apply(lambda x:int(x[0]))
    df4[13]['参数值'] = df4[13]['参数'].apply(lambda x:int(x[:2]))
    df4[14]['参数值'] = df4[14]['参数'].apply(lambda x:int(x[:2]))
    df4[14].columns = df4[14].columns.str.replace('Unnamed: 5','备注')
    df4[15]['参数值'] = df4[15]['参数'].apply(lambda x:int(x[:-3]))
    df4[11].columns = df4[11].columns.str.replace('Unnamed: 5','备注')
    rs4= []
    df4[10]['数量'] = (S/5)/df4[10]['参数值']
    df4[10]['数量'] = df4[10]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[10]['总价'] = df4[10]['数量'] * df4[10]['价格（万元）'] 
    df4[10]['总能力'] = df4[10]['数量'] * df4[10]['参数值']
    rs4.append(df4[10][(df4[10]['总价'] >= S*0.5*0.75) & (df4[10]['总价'] <= S*0.5*1.25)])
    rs4[0]['得分'] = rs4[0]['总价'].apply(lambda x:5 if x<=S*0.5 else 5.0- ((x-S*0.5)/(S*0.5) * 4)*5.0)


    df4[11]['数量'] = (S/8)/df4[11]['参数值']
    df4[11]['数量'] = df4[11]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[11]['总价'] = df4[11]['数量'] * df4[11]['价格（万元）'] 
    df4[11]['总能力'] = df4[11]['数量'] * df4[11]['参数值']
    tempdf411 = df4[11][df4[11]['备注']==1]
    plusva = np.min(df4[11][df4[11]['备注']==2]['总价'])
    rs4.append(tempdf411[(tempdf411['总价'] + plusva >= S*0.75) & (tempdf411['总价'] + plusva <= S*1.25)])
    rs4[1]['得分'] = rs4[1]['总价'].apply(lambda x:10 if x+plusva<=S else 10- ((x+plusva-S)/(S) * 4)*10.0)
    rs4[1].loc[rs4[1].index.max()+1] = df4[11].loc[df4[11]['备注']==2].iloc[0]

    df4[12]['数量'] = (S/20)/df4[12]['参数值']
    df4[12]['数量'] = df4[12]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[12]['总价'] = df4[12]['数量'] * df4[12]['价格（万元）'] 
    df4[12]['总能力'] = df4[12]['数量'] * df4[12]['参数值']
    para = 0.15
    rs4.append(df4[12][(df4[12]['总价'] >= S*para*0.75) & (df4[12]['总价'] <= S*para*1.25)])
    rs4[2]['得分'] = rs4[2]['总价'].apply(lambda x:3 if x<=S*para else 3.0- ((x-S*para)/(S*para) * 4)*3.0)

    df4[13]['数量'] = (S/8)/df4[13]['参数值']
    df4[13]['数量'] = df4[13]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[13]['总价'] = df4[13]['数量'] * df4[13]['价格（万元）'] 
    df4[13]['总能力'] = df4[13]['数量'] * df4[13]['参数值']
    para = 0.02
    rs4.append(df4[13][(df4[13]['总价'] >= S*para*0.75) & (df4[13]['总价'] <= S*para*1.25)])
    rs4[3]['得分'] = rs4[3]['总价'].apply(lambda x:2 if x<=S*para else 2.0- ((x-S*para)/(S*para) * 4)*2.0)

    df4[14]['数量'] = (S/2)/df4[14]['参数值']
    df4[14]['数量'] = df4[14]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[14]['总价'] = df4[14]['数量'] * df4[14]['价格（万元）'] 
    df4[14]['总能力'] = df4[14]['数量'] * df4[14]['参数值']
    tempdf414 = df4[14][df4[14]['备注']==1]
    plusva = np.min(df4[14][df4[14]['备注']==2]['总价'])
    rs4.append(tempdf414[(tempdf414['总价'] + plusva >= S*0.5*0.75) & (tempdf414['总价'] + plusva <= S*0.5*1.25)])
    rs4[4]['得分'] = rs4[4]['总价'].apply(lambda x:5 if x+plusva<=S*0.5 else 5- ((x+plusva-S*0.5)/(S*0.5) * 4)*5.0)
    rs4[4].loc[rs4[4].index.max()+1] = df4[14].loc[df4[14]['备注']==2].iloc[0]

    df4[15]['数量'] = (S/8)/df4[15]['参数值']
    df4[15]['数量'] = df4[15]['数量'].apply(lambda x:math.ceil(x) if not pd.isna(x) else x)
    df4[15]['总价'] = df4[15]['数量'] * df4[15]['价格（万元）'] 
    df4[15]['总能力'] = df4[15]['数量'] * df4[15]['参数值']
    rs4.append(df4[15][(df4[15]['总价'] >= S*0.5*0.75) & (df4[15]['总价'] <= S*0.5*1.25)])
    rs4[5]['得分'] = rs4[5]['总价'].apply(lambda x:5 if x<=S*0.5 else 5.0- ((x-S*0.5)/(S*0.5) * 4)*5.0)
    return rs1+rs2+rs3+rs4

def calresult(S):
    return pd.concat(cal(S))
# print(pd.concat(cal(210))[['装置','材质','厂家','参数','数量','总能力','总价','得分']])