from itertools import combinations

def generateRule(freq_itemset,freq_itemset_count,L1,min_conf):
    
    for i in range(len(freq_itemset)):
        now_itemset = freq_itemset[i]
        for j in range(1,len(now_itemset)):
            subsets = list(combinations(now_itemset,j))
            for l in range(len(subsets)):
                subset1 = list(subsets[l])
                if len(subset1)==1:
                    if (subset1[0] in list(L1[0])):
                        index = list(L1[0]).index(subset1[0])
                        set1_sup = L1['count'][index]
                    else:
                        set1_sup = 0
                else:
                    if (subset1 in freq_itemset):
                        index = freq_itemset.index(subset1)
                        set1_sup = freq_itemset_count[index]
                    else:
                        set1_sup = 0
    
                subset2 = []
                for k in range(len(now_itemset)):
                    if (now_itemset[k] in subset1) == False:
                        subset2.append(now_itemset[k])
                support = freq_itemset_count[i]
                confidence = support / set1_sup
                if confidence >=min_conf:
                    print('rule:',subset1,'-->',subset2)
                    print('support:',support,'confidence:',confidence,'\n')

