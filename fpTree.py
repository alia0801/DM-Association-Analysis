from itertools import combinations

class treeNode:
    def __init__(self, val):
        # 初始化節點
        self.val = val
        self.count = 1
        self.child = None
        self.parent = None
        self.next = None

    def insertNext(self, val):
        if self.next == None:
            self.next = treeNode(val)
            self.next.parent = self.parent
        # 若旁邊已經有結點，使用遞迴找到最後一個結點並新增
        else:
            self.next.insertNext(val)
    
    def insertChild(self, val):
        if self.child == None:
            self.child = treeNode(val)
            self.child.parent = self
        #若child已經存在，則再往旁邊新增一個child
        else:
            self.child.insertNext(val)
    
    def findAllChild(self):
        childs=[]
        myFirstChild = self.child
        now_child=myFirstChild
        while now_child != None:
            childs.append(now_child.val)
            now_child = now_child.next

        return childs

    def findAllNext(self):
        nexts=[]
        now_next = self
        while now_next != None:
            nexts.append(now_next.val)
            now_next = now_next.next

        return nexts

    def findAllParents(self):
        parents=[]
        temp = self
        while temp.parent != None:
            temp = temp.parent
            parents.append(temp.val)

        return parents

    def findCertenChild(self, key):
        myFirstChild = self.child
        now_child=myFirstChild
        ans = None
        while now_child != None:
            if now_child.val == key:
                ans = now_child
                break
            else:
                now_child = now_child.next
        return ans
    
    def findCertenNext(self, key):
        now_next = self
        ans = None
        while now_next != None:
            if now_next.val == key:
                ans = now_next
                break
            else:
                now_next = now_next.next
        return ans

    def walkEntiredTree(self):
        node = self
        childs = node.findAllChild()
        # print(self.val, childs)
        for i in range(len(childs)):
            temp = node.findCertenChild(childs[i])
            if temp != None:
                # node = temp
                temp.walkEntiredTree()

    def walkEntiredFindItem(self, key):
        ans=[]
        node = self
        childs = node.findAllChild()
        # print(self.val, childs)
        for i in range(len(childs)):
            temp = node.findCertenChild(childs[i])
            if temp != None:
                if temp.val == key:
                    # print(temp.val)
                    ans.append(temp)
                    # a1=temp
                a = temp.walkEntiredFindItem(key)
                if len(a)>0:
                    for j in range(len(a)):
                        ans.append(a[j])
        return ans



class patterns:
    def __init__(self, val, count):
        self.val = val
        self.count = count



def createTree(new_member_group):
    fp_tree_root = treeNode('ROOT')
    for i in range(len(new_member_group)):
        if len(new_member_group)>0:
            node = fp_tree_root
            for j in range(len(new_member_group[i])):
                inserTarget = new_member_group[i][j]
                temp = node #暫存目前的node 以免下一個沒找到而消失
                node = node.findCertenChild(inserTarget)
                if node == None: #沒找到這一個
                    temp.insertChild(inserTarget)
                    node = temp.findCertenChild(inserTarget)
                else: #有找到 count+1
                    node.count += 1
    return fp_tree_root

# FP growth
def fpGrowth(l1_sort,fp_tree_root,min_support):
    
    items=[]
    cond_pat_bases=[]
    for i in range(1,len(l1_sort)):
    # for i in range(1,5):
        cond_pats = []
        item = l1_sort[0][i]
        nodes = fp_tree_root.walkEntiredFindItem(item)
    
        for j in range(len(nodes)):
            node=nodes[j]
            item_arr=node.findAllParents()
            item_arr.reverse()
            item_arr.pop(0)
            cond_pat = patterns(item_arr,node.count)
            cond_pats.append(cond_pat)
    
        items.append(item)
        cond_pat_bases.append(cond_pats)

    

    cond_fp_trees=[]
    for i in range(len(cond_pat_bases)):
        print(items[i])
        cond_fp_pat=[]
    
        cond_pats = cond_pat_bases[i]
        
        if len(cond_pats)>1:
            lens_arr=[]
            # print('\nitems')
            for j in range(len(cond_pats)):
                # print(cond_pats[j].val,cond_pats[j].count)
                lens_arr.append(len(cond_pats[j].val))
                # if cond_pats[j].count >= min_support and len(cond_pats[j].val)>0:
                    # cond_fp_pat.append(cond_pats[j])
                
            temp_len=min(lens_arr)
            while temp_len<10000:
                
                index=lens_arr.index(temp_len)
                temp_set = cond_pats[index]
                # print()
                # print('in while',temp_set.val,temp_set.count)
    
                # if temp_set.count >= min_support and len(temp_set.val)>0:
                #     cond_fp_pat.append(temp_set)
                #     lens_arr[index]=10000     
                #     temp_len=min(lens_arr) 
                #     continue
                # else:
    
                used = [False]*len(cond_pats)
                used[index] = True
                sets=[]
                for j in range(temp_len):#此list的每一個元素
                    for k in range(len(cond_pats)):#去其他list找
                        if lens_arr[k] == 10000:
                            continue
                        if temp_set.val[j] in cond_pats[k].val :
                            used[k]=True
                            # sets.append(temp_set.val[j])
                        # if (temp_set.val[j] in cond_pats[k].val) and ((temp_set.val[j] in sets) == False):
                            if (temp_set.val[j] in sets) == False:
                                sets.append(temp_set.val[j])
                            
                # print(used)
                sets_count=0
                for j in range(len(cond_pats)):
                    if used[j]:
                        sets_count += cond_pats[j].count
                # print(sets,sets_count)
                # print('ans',sets,sets_count)
                if len(sets)>0 and sets_count>=min_support:
                    print('ans',sets,sets_count)
                    cond_fp_pat.append(patterns(sets,sets_count))
    
                lens_arr[index]=10000     
                temp_len=min(lens_arr)       
                        
        elif len(cond_pats)==1:
            if cond_pats[0].count >= min_support and len(cond_pats[0].val)>0:
                cond_fp_pat.append(cond_pats[0])
        #     else:
        #         cond_fp_pat.append(None)
        # else:
        #     cond_fp_pat.append(None)
        
        # if ((cond_fp_pat in cond_fp_trees) == False) or cond_fp_pat==[]:
        cond_fp_trees.append(cond_fp_pat)
    
    
    
    cond_fp_trees_n=[]
    for i in range(len(cond_fp_trees)):
        for j in range(len(cond_fp_trees[i])):
            pats = cond_fp_trees[i][j]
            # print(pats.val,pats.count)
            if (items[i] in pats.val) == False:
                (pats.val).append(items[i])
            cond_fp_trees_n.append(pats)
            print(pats.val,pats.count)
        
    
    
    freq_pats=[]
    for i in range(len(cond_fp_trees_n)):
        # print("yyy",cond_fp_trees_n[i].val,cond_fp_trees_n[i].count)
        # code=[]
        # for j in range(len(cond_fp_trees_n[i].val)):
        #     code.append( (cond_fp_trees_n[i].val)[j] )
        for j in range(2,len(cond_fp_trees_n[i].val)):
            comb_code = list(combinations(cond_fp_trees_n[i].val,j))
            for k in range(len(comb_code)):
                # print(list(comb_code[k]))
                arr = sorted(list(comb_code[k]))
                pat = patterns(arr,cond_fp_trees_n[i].count)
                freq_pats.append(pat)
                # print(pat.val,pat.count)
    
        pat = patterns(sorted(cond_fp_trees_n[i].val),cond_fp_trees_n[i].count)
        if (pat in freq_pats) ==False:
            freq_pats.append(pat)

    return freq_pats