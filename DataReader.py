import pandas as pd
import numpy as np

def readDataIBM(path):
    # path = 'D:/Alia/Downloads/109-1/資料探勘/HW1/IBM-Quest-Data-Generator.exe/ttt.data.txt'
    f = open(path,mode = 'r')
    words = f.readlines()
    
    #將txt檔轉為list*3
    tid=[]
    cid=[]
    item_id=[]
    for w in words:
        t=str(int(w[:10].strip(' ')  ))
        c=str(int(w[10:21].strip(' ')))
        i=str(int(w[21:32].strip(' ')))
        tid.append(t)
        cid.append(c)
        item_id.append(i)
    
    #list-->dataframe
    t_df = pd.DataFrame (tid,columns=['tid'])
    c_df = pd.DataFrame (cid,columns=['cid'])
    i_df = pd.DataFrame (item_id,columns=['item_id'])
    
    df = pd.concat([t_df,c_df,i_df], axis=1)
    # print(df)
    
    # 將每個組合分開
    member=[]
    member_group=[]
    # group_id=[]
    for i in range(len(df)):
        if i==0:
            # member.append(df['tid'][i])
            member.append(df['item_id'][i])
        elif df['tid'][i]==df['tid'][i-1]:
            member.append((df['item_id'][i]))
        else:
            member_group.append(list(member))
            # group_id.append(df['t_id'][i-1])
            member=[]
            # member.append(df['tid'][i])
            member.append(df['item_id'][i])
    member_group.append(list(member))
    # result_df = pd.DataFrame(member_group)
    # print(result_df)
    # result_df_T=result_df.T
    # result_df_T
    # return result_df_T
    print(type(member_group))
    return member_group


def readDataKaggle(path):
    #讀檔
    # path = 'D:/Alia/Downloads/109-1/資料探勘/HW1/BreadBasket_DMS.csv'
    df = pd.read_csv(path)
    
    df=df.drop(['Date'],axis=1)
    df=df.drop(['Time'],axis=1)
    # df
    
    member=[]
    member_group=[]
    # group_id=[]
    for i in range(len(df)):
        if i==0:
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
        elif df['Transaction'][i]==df['Transaction'][i-1]:
            member.append(df['Item'][i])
        else:
            member_group.append(list(member))
            # group_id.append(df['t_id'][i-1])
            member=[]
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
    member_group.append(list(member))
    # result_df = pd.DataFrame(member_group)
    # # print(result_df)
    # result_df_T=result_df.T
    
    
    # for i in range(len(result_df_T)):
    #     for j in range(len(result_df)):
    #         if str(result_df_T[j][i])=='None':
    #             result_df_T[j][i]=np.nan
    
    # return result_df_T
    print(type(member_group))
    return member_group
