#%%
import DataReader
import pandas as pd
import numpy as np
import apriori
import generateRule
import datetime
from itertools import combinations


#%%
# def ibm_Apiori_bruteForce(min_support):
# min_support = 5
# path_ibm = 'D:/Alia/Downloads/109-1/資料探勘/HW1/IBM-Quest-Data-Generator.exe/ttt.data.txt'
# member_group = DataReader.readDataIBM(path_ibm)
# result_df = pd.DataFrame(member_group)
# result_df_T = result_df.T
# L1 = apriori.createL1(result_df_T,min_support)

#%%


class treeNode:
    def __init__(self, val):
        # 初始化節點
        # temp = list( map(int ,val) )
        self.val = [val]
        self.count = [0]
        self.child_0 = None
        self.child_1 = None
        self.child_2 = None
        self.child_3 = None
        self.child_4 = None
        
        self.parent = None
    
    def insertChild(self, val,temp):
        # temp = sum(list( map(int ,val) ))
        cat = temp %5
        if cat == 0:
            if self.child_0 == None:
                self.child_0 = treeNode(val)
                self.child_0.parent = self
            elif len(self.child_0.val) < 5:
                (self.child_0.val).append(val)
                (self.child_0.count).append(0)
            else:
                self.child_0.insertChild(val,temp//10)

        elif cat == 1:
            if self.child_1 == None:
                self.child_1 = treeNode(val)
                self.child_1.parent = self
            elif len(self.child_1.val) < 5:
                (self.child_1.val).append(val)
                (self.child_1.count).append(0)
            else:
                self.child_1.insertChild(val,temp//10)
        
        elif cat == 2:
            if self.child_2 == None:
                self.child_2 = treeNode(val)
                self.child_2.parent = self
            elif len(self.child_2.val) < 5:
                (self.child_2.val).append(val)
                (self.child_2.count).append(0)
            else:
                self.child_2.insertChild(val,temp//10)

        elif cat == 3:
            if self.child_3 == None:
                self.child_3 = treeNode(val)
                self.child_3.parent = self
            elif len(self.child_3.val) < 5:
                (self.child_3.val).append(val)
                (self.child_3.count).append(0)
            else:
                self.child_3.insertChild(val,temp//10)

        elif cat == 4:
            if self.child_4 == None:
                self.child_4 = treeNode(val)
                self.child_4.parent = self
            elif len(self.child_4.val) < 5:
                (self.child_4.val).append(val)
                (self.child_4.count).append(0)
            else:
                self.child_4.insertChild(val,temp//10)

    def findAllParents(self):
        parents=[]
        temp = self
        while temp.parent != None:
            temp = temp.parent
            parents.append(temp.val)

        return parents

    def findAllChilds(self):
        node = self
        if node != None:
            c0 = node.child_0
            c1 = node.child_1
            c2 = node.child_2
            c3 = node.child_3
            c4 = node.child_4
            print('node is ',node.val)
            if c0 != None:
                print(c0.val)
                c0.findAllChilds()
            if c1 != None:
                print(c1.val)
                c1.findAllChilds()
            if c2 != None:
                print(c2.val)
                c2.findAllChilds()
            if c3 != None:
                print(c3.val)
                c3.findAllChilds()
            if c4 != None:
                print(c4.val)
                c4.findAllChilds()
    
    def findCertainChild(self, val,temp):
        # temp = sum(list( map(int ,val) ))
        
        cat = temp %5
        # print(temp,cat)
        if cat ==0:
            child = self.child_0
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        (child.count)[i] += 1
                        find = True
                        find_num = i
                        break
                if find==True:
                    # print('find it',child,find_num)
                    return child, find_num
                elif temp >=1:
                    # print('conti find')
                    child, find_num = child.findCertainChild(val,temp//10)
                    return child, find_num
                else:
                    # print('no result')
                    return None, 0  
            else:
                # print('child is None')
                return None, 0 
        elif cat ==1:
            child = self.child_1
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        (child.count)[i] += 1
                        find = True
                        find_num = i
                        break
                if find:
                    return child, find_num
                elif temp >=1:
                    child, find_num = child.findCertainChild(val,temp//10)
                    return child, find_num
                else:
                    return None, 0 
            else:
                return None, 0
        elif cat ==2:
            child = self.child_2
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        (child.count)[i] += 1
                        find = True
                        find_num = i
                        break
                if find:
                    return child, find_num
                elif temp >=1:
                    child, find_num = child.findCertainChild(val,temp//10)
                    return child, find_num
                else:
                    return None, 0  
            else:
                return None, 0
        elif cat ==3:
            child = self.child_3
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        (child.count)[i] += 1
                        find = True
                        find_num = i
                        break
                if find:
                    return child, find_num
                elif temp >=1:
                    child, find_num = child.findCertainChild(val,temp//10)
                    return child, find_num
                else:
                    return None, 0 
            else:
                return None, 0
        elif cat == 4:
            child = self.child_4
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        (child.count)[i] += 1
                        find = True
                        find_num = i
                        break
                if find:
                    return child, find_num
                elif temp >=1:
                    child, find_num = child.findCertainChild(val,temp//10)
                    return child, find_num
                else:
                    return None, 0 
            else:
                return None, 0    
    
    def findCertainChildCount(self, val,temp):
        # temp = sum(list( map(int ,val) ))
        
        cat = temp %5
        # print(temp,cat)
        if cat ==0:
            child = self.child_0
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        # print((child.count)[i])
                        find = True
                        ans = (child.count)[i]
                        # return (child.count)[i]
                        # (child.count)[i] += 1
                        # find_num = i
                        # break
                if find==True:
                    return ans
                elif temp >=1:
                    # print('conti find')
                    ans = child.findCertainChildCount(val,temp//10)
                    return ans
                else:
                    # print('no result')
                    return  0
            else:
                # print('child is None')
                return  0
        elif cat ==1:
            child = self.child_1
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        # print((child.count)[i])
                        find = True
                        ans = (child.count)[i]
                        # return (child.count)[i]
                        # (child.count)[i] += 1
                        # find_num = i
                        # break
                if find==True:
                    return ans
                elif temp >=1:
                    # print('conti find')
                    ans = child.findCertainChildCount(val,temp//10)
                    return ans
                else:
                    # print('no result')
                    return  0
            else:
                # print('child is None')
                return  0
        elif cat ==2:
            child = self.child_2
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        # print((child.count)[i])
                        find = True
                        ans = (child.count)[i]
                        # return (child.count)[i]
                        # (child.count)[i] += 1
                        # find_num = i
                        # break
                if find==True:
                    return ans
                elif temp >=1:
                    # print('conti find')
                    ans = child.findCertainChildCount(val,temp//10)
                    return ans
                else:
                    # print('no result')
                    return  0
            else:
                # print('child is None')
                return  0 
        elif cat ==3:
            child = self.child_3
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        # print((child.count)[i])
                        find = True
                        ans = (child.count)[i]
                        # return (child.count)[i]
                        # (child.count)[i] += 1
                        # find_num = i
                        # break
                if find==True:
                    return ans
                elif temp >=1:
                    # print('conti find')
                    ans = child.findCertainChildCount(val,temp//10)
                    return ans
                else:
                    # print('no result')
                    return  0 
            else:
                # print('child is None')
                return  0 
        elif cat == 4:
            child = self.child_4
            if child != None:
                find = False
                for i in range(len(child.val)):
                    if sorted(val) == sorted(child.val[i]):
                        # print(sorted(val), sorted(child.val[i]))
                        # print((child.count)[i])
                        find = True
                        ans = (child.count)[i]
                        # return (child.count)[i]
                        # (child.count)[i] += 1
                        # find_num = i
                        # break
                if find==True:
                    return ans
                elif temp >=1:
                    # print('conti find')
                    ans = child.findCertainChildCount(val,temp//10)
                    return ans
                else:
                    # print('no result')
                    return  0
            else:
                # print('child is None')
                return  0 


#%%
# for i in range(len(L1)):
#     if str(L1[0][i])=='None':
#         L1 = L1.drop([i],axis = 0)
# L1 = L1.reset_index(drop=True)
#%%
# C2 = apriori.generate_cand_itemset(L1)
#%%

def generate_L(C,member_group,min_support):

    root = treeNode('ROOT')
    for i in range(len(C)):
        temp = sum(list( map(int ,C[i]) ))
        root.insertChild(C[i],temp)
    #%%
    # root.findAllChilds()
    
    #%%
    
    for i in range(len(member_group)):
        comb_code = list(combinations(member_group[i],len(C[0])))
        for j in range(len(comb_code)):
            temp = sum(list( map(int ,comb_code[j]) ))
            root.findCertainChild(comb_code[j],temp)
    
    #%%
    counts=[]
    for i in range(len(C)):
        temp = sum(list( map(int ,C[i]) ))
        count = root.findCertainChildCount(C[i],temp)
        # print(count)
        counts.append(count)
    
    
    
    #%%
    df_count = pd.DataFrame(counts,columns=['count'])
    df_itemset = pd.DataFrame(C)
    L = pd.concat([df_count,df_itemset],axis=1)
    for i in range(len(L)):
        if L['count'][i] < min_support:
            L = L.drop([i],axis=0)
    L = L.reset_index(drop=True)
    return L
#%%

# C2 = apriori.generate_cand_itemset(L1)
# L2 = generate_L(C2,member_group,min_support)
# #%%

# C3 = apriori.generate_cand_itemset(L2)
# L3 = generate_L(C3,member_group,min_support)

#%%
# Ln=L1
# Ls=[]
# Ls.append(L1)
# while len(Ln)>1:
#     print(len(Ls))
#     C = apriori.generate_cand_itemset(Ln)
#     # print(C)
#     Lnn = generate_L( C , member_group , min_support )
#     Ln = Lnn
#     Ls.append(Ln)

#%%

# freq_itemset=[]
# freq_itemset_count=[]
# for i in range(1,len(Ls)):
#     temp = (np.array(Ls[i])).tolist()
#     for j in range(len(temp)):
#         freq_itemset_count.append(temp[j][0])
#         freq_itemset.append(list(temp[j][1:]))
#         print(temp[j][0],list(temp[j][1:]))
# #生成rules
# generateRule.generateRule(freq_itemset,freq_itemset_count,L1)

# %%
def generate_L_kaggle(C,member_group,min_support):

    if len(C)>0:


        root = treeNode('ROOT')
        for i in range(len(C)):
            temp = 0
            for j in range(len(C[i])):
                for k in range(len(C[i][j])):
                    temp += ord(C[i][j][k])
            # temp = sum(list( map(int ,C[i]) ))
            root.insertChild(C[i],temp)
        #%%
        # root.findAllChilds()
        
        #%%
        
        for i in range(len(member_group)):
            # print(i,len(member_group[i]),len(C[0]))
            if (len(member_group[i])>len(C[0])):
                
                comb_code = list(combinations(member_group[i],len(C[0])))
                for j in range(len(comb_code)):
                    temp = 0
                    for k in range(len(comb_code[j])):
                        for l in range(len(comb_code[j][k])):
                            temp += ord(comb_code[j][k][l])
                    # temp = sum(list( map(int ,comb_code[j]) ))
                    root.findCertainChild(comb_code[j],temp)
        
        #%%
        counts=[]
        for i in range(len(C)):
            temp = 0
            for j in range(len(C[i])):
                for k in range(len(C[i][j])):
                    temp += ord(C[i][j][k])
            # temp = sum(list( map(int ,C[i]) ))
            count = root.findCertainChildCount(C[i],temp)
            # print(count)
            counts.append(count)
        
        
        
        #%%
        df_count = pd.DataFrame(counts,columns=['count'])
        df_itemset = pd.DataFrame(C)
        L = pd.concat([df_count,df_itemset],axis=1)
        for i in range(len(L)):
            if L['count'][i] < min_support:
                L = L.drop([i],axis=0)
        L = L.reset_index(drop=True)
        return L
    else:
        return pd.DataFrame(columns=['count'])
    
# # %%
# min_support = 300
# path_kaggle = 'D:/Alia/Downloads/109-1/資料探勘/HW1/BreadBasket_DMS.csv'
# member_group = DataReader.readDataKaggle(path_kaggle)
# result_df = pd.DataFrame(member_group)
# result_df_T = result_df.T
# L1 = apriori.createL1(result_df_T,min_support)
# # L1 = apriori.createL1(result_df_T,min_support)
# for i in range(len(L1)):
#     if str(L1[0][i])=='None':
#         L1 = L1.drop([i],axis = 0)
# L1 = L1.reset_index(drop=True)
# #%%
# Ln=L1
# Ls=[]
# Ls.append(L1)
# while len(Ln)>1:
#     print(len(Ls))
#     C = apriori.generate_cand_itemset(Ln)
#     # print(C)
#     Lnn = generate_L_kaggle( C , member_group , min_support )
#     Ln = Lnn
#     if len(Ln)==0:
#         break
#     Ls.append(Ln)
# #%%
# freq_itemset=[]
# freq_itemset_count=[]
# for i in range(1,len(Ls)):
#     temp = (np.array(Ls[i])).tolist()
#     for j in range(len(temp)):
#         freq_itemset_count.append(temp[j][0])
#         freq_itemset.append(list(temp[j][1:]))
#         print(temp[j][0],list(temp[j][1:]))


#%%

# C2 = apriori.generate_cand_itemset(L1)
# L2 = generate_L_kaggle(C2,member_group,min_support)
# #%%

# C3 = apriori.generate_cand_itemset(L2)
# L3 = generate_L_kaggle(C3,member_group,min_support)
# %%
