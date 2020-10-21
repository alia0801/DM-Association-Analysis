
import pandas as pd
import numpy as np
from itertools import combinations

def createL1(result_df_T,min_support):
    
    cand_item_set_1=[]
    counts=[]
    for i in range(len(result_df_T.T)):
        for j in range(len(result_df_T)):
            if str(result_df_T[i][j])=='nan' or str(result_df_T[i][j])=='NONE':
                break
            # elif np.isnan(result_df_T[i][j]):
            #     break
            if result_df_T[i][j] in cand_item_set_1:
                index =  cand_item_set_1.index(result_df_T[i][j])
                counts[index]+=1
            else:
                cand_item_set_1.append(result_df_T[i][j])
                counts.append(1)
    
    df_count = pd.DataFrame(counts,columns=['count'])
    df_id = pd.DataFrame(cand_item_set_1)
    c1 = pd.concat([df_count,df_id],axis=1)

    #將c1-->L1
    # min_support = 5
    item_set = c1
    for i in range(len(item_set)):
        if item_set['count'][i] < min_support:
            item_set = item_set.drop([i],axis=0)
    
    L1 = item_set.reset_index(drop=True)

    return L1

def generate_cand_itemset(L):

    for i in range(len(L)):
        for j in range(len(L.T)-1):
            if str(L[j][i])=='None':
                L[j][i]=np.nan
            else:
                L[j][i] = str(L[j][i])
    # print(L)
    #生成所有可能組合
    code = []
    for i in range(len(L)):
        code.append(i)
    comb_code = list(combinations(code,2))
    
    itemset=[]
    temp = (L.drop(['count'],axis=1)).T #L的set部分
    for i in range(len(comb_code)):
        set0 = list(temp[ comb_code[i][0] ])
        set1 = list(temp[ comb_code[i][1] ])
        count=0
        for j in range(len(set0)):
            if set0[j] in set1:
                count+=1
        if count==(len(set0)-1):#2個set之間僅一成員不同
            cand_set=[]
            for j in range(len(set0)):
                if str(set0[j])!='None':
                    cand_set.append(str(set0[j]))
            # cand_set = set0
            for j in range(len(set1)):
                if (set1[j] in set0)==False and str(set1[j])!='None':
                    cand_set.append(str(set1[j]))
            # print(cand_set)
            cand_set = sorted(cand_set)
            if (cand_set in itemset)==False:
                itemset.append(cand_set)
    # return itemset
    # print(itemset)
    #逐一檢查子集合是否在L內
    record=[]
    for i in range(len(itemset)):
    # for i in range(3):
        subset = list(combinations(itemset[i],len(cand_set)-1))
        # print(subset)
        total_y = True #預設子集合都在L
        for j in range(len(subset)):#每個子集合去L檢查
            y=False #此子集合預設不在L
            for k in range(len(temp.T)):
                if sorted(list(subset[j])) == list(temp[k]):
                    y=True
                    break
                # else:
                #     print(sorted(list(subset[j])),list(temp[k]))
            if y==False:
                total_y = False
        if total_y==False:
            record.append(i)
    #有子集合不在L內的itemset剔除
    ttt = pd.DataFrame(itemset)
    for i in range(len(ttt)):
        if i in record:
            ttt=ttt.drop([i],axis=0)
    # print(record)
    return ((np.array(ttt)).tolist())



#從C計算support值，並將低於min support的刪去以生成L
def cal_support_and_generate_L(C,result_df,min_support):
    # print('hello')
    # print(C)
    counts=[]

    for i in range(len(C)):
        count=0
        for j in range(len(result_df)):
            add=True
            for k in range(len(C[0])):
                # print(C[i][k] in list(result_df_T[j]),C[i][k],list(result_df_T[j]))
                if (C[i][k] in list(result_df.T[j]))==False:
                    # print('123')
                    add=False
                    break
            if add==True:
                count+=1

            # if item_set_3[i][0] in list(result_df_T[j][1:]) and item_set_3[i][1] in list(result_df_T[j][1:]) and item_set_3[i][2] in list(result_df_T[j][1:]):
            #     count+=1
        counts.append(count)
        # print(count)
    
    df_count = pd.DataFrame(counts,columns=['count'])
    df_itemset = pd.DataFrame(C)
    L = pd.concat([df_count,df_itemset],axis=1)
    for i in range(len(L)):
        if L['count'][i] < min_support:
            L = L.drop([i],axis=0)
    return L.reset_index(drop=True)
