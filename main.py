#%%
import DataReader
import pandas as pd
import numpy as np
import apriori
import generateRule
import datetime
import apriori_byTree
import fpTree

#%%
def ibm_Apiori_bruteForce(min_support,min_confidence):
    path_ibm = './dataset/IBM-Quest-Data-Generator.exe/ttt.data.txt'
    member_group = DataReader.readDataIBM(path_ibm)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T
    L1 = apriori.createL1(result_df_T,min_support)
    for i in range(len(L1)):
        if str(L1[0][i])=='None':
            L1 = L1.drop([i],axis = 0)
    L1 = L1.reset_index(drop=True)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        Lnn = apriori.cal_support_and_generate_L( apriori.generate_cand_itemset(Ln),result_df,min_support )
        Ln = Lnn
        Ls.append(Ln)

    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)
#%%
def kaggle_Apiori_hashtree(min_support,min_confidence):
    path_kaggle = './dataset/BreadBasket_DMS.csv'
    member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)
    
    for i in range(len(L1)):
        if str(L1[0][i])=='None':
            L1 = L1.drop([i],axis = 0)
    L1 = L1.reset_index(drop=True)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        C = apriori.generate_cand_itemset(Ln)
        # print(C)
        Lnn = apriori_byTree.generate_L_kaggle( C , member_group , min_support )
        Ln = Lnn
        if len(Ln)==0:
            break
        Ls.append(Ln)

    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)


#%%
def ibm_Apiori_hashtree(min_support,min_confidence):
    path_ibm = './dataset/IBM-Quest-Data-Generator.exe/ttt.data.txt'
    member_group = DataReader.readDataIBM(path_ibm)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T
    L1 = apriori.createL1(result_df_T,min_support)
    for i in range(len(L1)):
        if str(L1[0][i])=='None':
            L1 = L1.drop([i],axis = 0)
    L1 = L1.reset_index(drop=True)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        C = apriori.generate_cand_itemset(Ln)
        # print(C)
        Lnn = apriori_byTree.generate_L( C , member_group , min_support )
        Ln = Lnn
        Ls.append(Ln)
    
    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)


#%%
def kaggle_Apiori_bruteForce(min_support,min_confidence):
    path_kaggle = './dataset/BreadBasket_DMS.csv'
    member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        Lnn = apriori.cal_support_and_generate_L( apriori.generate_cand_itemset(Ln),result_df,min_support )
        Ln = Lnn
        Ls.append(Ln)
 
    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)

#%%
def ibm_fptree(min_support,min_confidence):
    path_ibm = './dataset/IBM-Quest-Data-Generator.exe/ttt.data.txt'
    member_group = DataReader.readDataIBM(path_ibm)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T
    L1 = apriori.createL1(result_df_T,min_support)
    for i in range(len(L1)):
        if str(L1[0][i])=='None':
            L1 = L1.drop([i],axis = 0)
    L1 = L1.reset_index(drop=True)

    
    l1_sort = L1.sort_values(['count'],ascending=False)
    l1_sort = l1_sort.reset_index(drop=True)
   
    # member_group = (np.array(result_df)).tolist()
    
    new_member_group=[]
    for i in range(len(member_group)):
        member=[]
        for j in range(len(l1_sort)):
            if l1_sort[0][j] in member_group[i]:
                member.append(l1_sort[0][j])
        new_member_group.append(member)


    # 建立FP tree
    fp_tree_root = fpTree.createTree(new_member_group)

    # fp growth
    freq_pats = fpTree.fpGrowth(l1_sort,fp_tree_root,min_support)

    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(len(freq_pats)):
        if (freq_pats[i].val in freq_itemset) == False:
            freq_itemset.append(freq_pats[i].val)
            freq_itemset_count.append(freq_pats[i].count)
            
    
    df_itemset = pd.DataFrame(freq_itemset)
    df_itemset_count = pd.DataFrame(freq_itemset_count,columns=['count'])
    df_ans = pd.concat([df_itemset_count,df_itemset],axis=1)
    print('freq itemsets:')
    print(df_ans)

    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)

#%%
def kaggle_fptree(min_support,min_confidence):
    path_kaggle = './dataset/BreadBasket_DMS.csv'
    member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)

    
    l1_sort = L1.sort_values(['count'],ascending=False)
    l1_sort = l1_sort.reset_index(drop=True)
   
    # member_group = (np.array(result_df)).tolist()
    
    new_member_group=[]
    for i in range(len(member_group)):
        member=[]
        for j in range(len(l1_sort)):
            if l1_sort[0][j] in member_group[i]:
                member.append(l1_sort[0][j])
        new_member_group.append(member)
 

    # 建立FP tree
    fp_tree_root = fpTree.createTree(new_member_group)

    # fp growth
    freq_pats = fpTree.fpGrowth(l1_sort,fp_tree_root,min_support)

    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(len(freq_pats)):
        if (freq_pats[i].val in freq_itemset) == False:
            freq_itemset.append(freq_pats[i].val)
            freq_itemset_count.append(freq_pats[i].count)
            
    
    df_itemset = pd.DataFrame(freq_itemset)
    df_itemset_count = pd.DataFrame(freq_itemset_count,columns=['count'])
    df_ans = pd.concat([df_itemset_count,df_itemset],axis=1)
    print('freq itemsets:')
    print(df_ans)

    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)
#%%

def test_fptree(min_support,min_confidence):
    path = './dataset/Test.csv'
    df = pd.read_csv(path)
    # print(df)
    
    # 將每個組合分開
    member=[]
    member_group=[]
    # group_id=[]
    for i in range(len(df)):
        if i==0:
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
        elif df['TID'][i]==df['TID'][i-1]:
            member.append((df['Item'][i]))
        else:
            member_group.append(list(member))
            # group_id.append(df['t_id'][i-1])
            member=[]
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
    member_group.append(list(member))

    # member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)

    
    l1_sort = L1.sort_values(['count'],ascending=False)
    l1_sort = l1_sort.reset_index(drop=True)
   
    # member_group = (np.array(result_df)).tolist()
    
    new_member_group=[]
    for i in range(len(member_group)):
        member=[]
        for j in range(len(l1_sort)):
            if l1_sort[0][j] in member_group[i]:
                member.append(l1_sort[0][j])
        new_member_group.append(member)
 

    # 建立FP tree
    fp_tree_root = fpTree.createTree(new_member_group)

    # fp growth
    freq_pats = fpTree.fpGrowth(l1_sort,fp_tree_root,min_support)

    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(len(freq_pats)):
        if (freq_pats[i].val in freq_itemset) == False:
            freq_itemset.append(freq_pats[i].val)
            freq_itemset_count.append(freq_pats[i].count)
            
    
    df_itemset = pd.DataFrame(freq_itemset)
    df_itemset_count = pd.DataFrame(freq_itemset_count,columns=['count'])
    df_ans = pd.concat([df_itemset_count,df_itemset],axis=1)
    print('freq itemsets:')
    print(df_ans)

    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)




#%%

def test_Apiori_bruteForce(min_support,min_confidence):
    path = './dataset/Test.csv'
    df = pd.read_csv(path)
    # print(df)
    
    # 將每個組合分開
    member=[]
    member_group=[]
    # group_id=[]
    for i in range(len(df)):
        if i==0:
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
        elif df['TID'][i]==df['TID'][i-1]:
            member.append((df['Item'][i]))
        else:
            member_group.append(list(member))
            # group_id.append(df['t_id'][i-1])
            member=[]
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
    member_group.append(list(member))
    # member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        Lnn = apriori.cal_support_and_generate_L( apriori.generate_cand_itemset(Ln),result_df,min_support )
        Ln = Lnn
        Ls.append(Ln)

    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)

#%%
def test_Apiori_hashtree(min_support,min_confidence):
    path = './dataset/Test.csv'
    df = pd.read_csv(path)
    # print(df)
    
    # 將每個組合分開
    member=[]
    member_group=[]
    # group_id=[]
    for i in range(len(df)):
        if i==0:
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
        elif df['TID'][i]==df['TID'][i-1]:
            member.append((df['Item'][i]))
        else:
            member_group.append(list(member))
            # group_id.append(df['t_id'][i-1])
            member=[]
            # member.append(df['tid'][i])
            member.append(df['Item'][i])
    member_group.append(list(member))
    # member_group = DataReader.readDataKaggle(path_kaggle)
    result_df = pd.DataFrame(member_group)
    result_df_T = result_df.T

    L1 = apriori.createL1(result_df_T,min_support)

    for i in range(len(L1)):
        if str(L1[0][i])=='None':
            L1 = L1.drop([i],axis = 0)
    L1 = L1.reset_index(drop=True)

    Ln=L1
    Ls=[]
    Ls.append(L1)
    while len(Ln)>1:
        print(len(Ls))
        C = apriori.generate_cand_itemset(Ln)
        # print(C)
        Lnn = apriori_byTree.generate_L_kaggle( C , member_group , min_support )
        Ln = Lnn
        if len(Ln)==0:
            break
        Ls.append(Ln)

    print('freq itemsets:')
    freq_itemset=[]
    freq_itemset_count=[]
    for i in range(1,len(Ls)):
        temp = (np.array(Ls[i])).tolist()
        for j in range(len(temp)):
            freq_itemset_count.append(temp[j][0])
            freq_itemset.append(list(temp[j][1:]))
            print(temp[j][0],list(temp[j][1:]))

    #生成rules
    generateRule.generateRule(freq_itemset,freq_itemset_count,L1,min_confidence)

#%%
starttime = datetime.datetime.now()
test_Apiori_bruteForce(2,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
#%%
starttime = datetime.datetime.now()
test_Apiori_hashtree(2,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)

#%%
starttime = datetime.datetime.now()
test_fptree(2,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)

#%%
starttime = datetime.datetime.now()
kaggle_Apiori_bruteForce(500,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# 0:58:09.204653 100
# 0:23:10.024551 200
# 0:20:02.641089 300
# 0:05:59.405575 400
# 0:05:58.122872 500
#%%
starttime = datetime.datetime.now()
kaggle_Apiori_hashtree(500,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# 0:00:16.186227 100
# 0:00:14.070713 200
# 0:00:13.300421 300
# 0:00:12.743645 400
# 0:00:12.255837 500
#%%
starttime = datetime.datetime.now()
kaggle_fptree(500,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# 0:00:11.258656 50
# 0:00:09.956878 100
# 0:00:09.643169 150
# 0:00:09.152948 200
# 0:00:08.925191 250
# 0:00:08.382345 300
# 0:00:08.332754 350
# 0:00:08.134953 400
# 0:00:07.955423 450
# 0:00:07.796567 500
#%%
starttime = datetime.datetime.now()
ibm_Apiori_bruteForce(7,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# 3:30:56.213685 4
# 0:12:42.296852 5
# 0:01:42.739456 6
# 0:00:27.748529 7
#%%

starttime = datetime.datetime.now()
ibm_Apiori_hashtree(7,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# >3hr 3
# 0:15:31.734147 4
# 0:00:17.721119 5
# 0:00:13.553411 6
# 0:00:10.749699 7

#%%
starttime = datetime.datetime.now()
ibm_fptree(7,0.5)
endtime = datetime.datetime.now()
print (endtime - starttime)
# 0:01:00.330683 3
# 0:00:15.282360 4
# 0:00:10.475901 5
# 0:00:09.761275 6
# 0:00:09.355027 7




#%%

