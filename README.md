# 資料探勘
## 關聯法則

## 檔案架構
```
.
+-- include
|   +-- FPTree.hpp
|   +-- HashTree.hpp
|   +-- IntList.hpp
+-- lib
|   +-- libCArray.so
|   +-- libFPTree.so
|   +-- libHashTree.so
+-- data
|   +-- Test.csv
|   +-- IBM_data.txt
|   +-- BreadBasket_DMS.csv
+-- CArray
|   +-- CAarry.cpp
|   +-- IntList.cpp
+-- HashTree
|   +-- HashTree.cpp
+-- FPTree
|   +-- FPTree.cpp
+-- Makefile
+-- ArrayConvert.py
+-- Apriori.py
+-- CountMethod.py
+-- DataReader.py
+-- main.py
```
- `include/FPTree.hpp`: FP-Growth物件prototype宣告
- `include/HashTree.hpp`: Hash Tree物件prototype宣告
- `include/IntList.hpp`: IntList物件prototype宣告，用來接收python傳送之list資料結構，其物件內主要為陣列用來儲存list的各個元素，並儲存list長度
- `lib/`: 編譯完之.so檔(library)，當python程式運行時將會引入這些library
- `data/Test.csv`: 本次實驗輸入資料，為驗證本程式與Weka輸出結果一致之測試使用
- `data/IBM_data.txt`: 本次實驗輸入資料，是由IBM Quest Synthetic Data Generator產生之資料
- `data/BreadBasket_DMS.csv`: 本次實驗輸入資料，是由Kaggle平台上公開提供之資料
- `CArray/CAarry.cpp`: CArray物件實作，並建立python調用介面
- `CArray/IntList.cpp`: IntList物件實作
- `HashTree/HashTree.cpp`: Hash Tree物件實作，並建立python調用介面
- `FPTree/FPTree.cpp`: FP-Growth物件實作，並建立python調用介面
- `Makefile`: 自動編譯C++ source code產生library並放置在，lib/目錄底下
- `ArrayConvert.py`: 整合python list與C++ IntList物件轉換介面
- `Apriori.py`: 建立Apriori物件，整合brute force、hash tree及FP-Growth方法，並能輸出frequent itemset
- `CountMethod.py`: 實作brute force方法及調用libHashTree.so建構hash tree方法
- `DataReader.py`: 實作讀取輸入檔案介面
- `main.py`: 主程式

##程式執行
- 以kaggle資料集，使用hashtree實作apiori方法為例，並設定minimum support為 300 instance、minimum confidence為0.5

- 輸出 :  (包含frequent itemset , rules, 執行時間)

## 簡要說明
- 使用python實作Apiori暴力法、Apiori使用hash tree搜尋support值以及使用FP-Growth方法直接找出frequent itemset，並且由frequent itemset生成關聯規則。
- 暴力法為逐筆transaction循序搜尋下去，如果比對candidate成功便會將其support值加一，這是裡面最緩慢的方法。
- Hash tree，其實作的hash function為h(x) = x % 5，其中x為itemset當中所有數字相加，若item為英文字串，則將字串中所有字母轉為ascii代碼後加總。每個節點都可以有5棵子樹，因此搜尋candidate時便可以透過hash function的配對排除其他不必要的搜尋。
- FP-Growth，為三種方法裡面最為迅速的方法，不論minimum support設定多低，都有不錯的表現，迅速地找出Frequent itemset。

## 驗證
# 驗證輸出規則正確
- 由於在大量數據的association rules並不會依照固定順序排列，再比對上有些難度，所以就採用上課投影片比較簡單的transaction，限制minimum support為0.4（2 instance）、minimum confidence為0.5，使用Weka產生association rules，再比對這次作業程式輸出的association rules，確認結果一致。
  |  TID  | Items |
  | :---: | :---: |
  |   1   |  ABC  |
  |   2   |  ABCD |
  |   3   |  BCE  |
  |   4   |  ACDE |
  |   5   |  DE   |

- Weka輸出結果

- 本程式輸出結果

# 驗證3種方法產出frequent itemset之結果相同
- 由於從frequent itemset產出關連規則是使用相同函式(於驗證1已驗證過)，且規則數量較多在比對上有困難，因此只比對frequent itemset是否相同。  
使用ibm資料集，限制minimum support的instance為5，確認3種方法所產出之frequent itemset相同。



## Comparison
- Find frequent itemset
  - IBM data (./data/IBM\_data.txt)
  
    | Condition                                  |       |
    | ---                                        | :---: |
    | Number of items                            |  9969 |
    | Number of transactions                     |  984  |


  - Execution time
    - Minimum support: 2

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force | 10 m 22.637 s |
    |  Hash Tree  |  2 m 32.743 s |
    |  FP-Growth  |  0 m 31.521 s |
  
    - Minimum support: 3

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force |  0 m 47.572 s |
    |  Hash Tree  |  0 m 41.402 s |
    |  FP-Growth  |  0 m  0.450 s |

    - Minimum support: 4

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force |  0 m  2.966 s |
    |  Hash Tree  |  0 m 19.487 s |
    |  FP-Growth  |  0 m  0.064 s |
  ---
  - Kaggle data (./data/BreadBasket\_DMS.csv)
  
    | Condition                                  |       |
    | ---                                        | :---: |
    | Number of items                            | 21294 |
    | Number of transactions                     |  9684 |


  - Execution time
    - Minimum support: 2

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force |  0 m 14.451 s |
    |  Hash Tree  |  0 m  3.875 s |
    |  FP-Growth  |  0 m  0.197 s |
  
    - Minimum support: 3

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force |  0 m  8.521 s |
    |  Hash Tree  |  0 m  1.486 s |
    |  FP-Growth  |  0 m  0.183 s |

    - Minimum support: 4

    |   Method    |      Time     |
    | ---         | ---           |
    | Brute Force |  0 m  6.061 s |
    |  Hash Tree  |  0 m  0.893 s |
    |  FP-Growth  |  0 m  0.174 s |

## Conclusion
- 本實驗是以IBM Quest Synthetic Data Generator所產生的資料及Kaggle上開放的dataset來作程式運行效能的評估。
- 由Coding的過程中，能感受到python與C\+\+程式的效率差異，尤其是在樹狀資料結構，C\+\+能夠更精準明確地使用指標來操作樹走訪，對於記憶體資源使用也比較能控制，因此實作出來的效率遠高於python的效率，經過實際比較，一樣是單純建構hash tree，python執行所需時間約為C\+\+之5倍，因此本程式在運算複雜的地方，都會改用C\+\+來實作，以達成最好的效果。

  ![IBM\_generator\_cmp](img/IBM_generator_cmp.png)
  > IBM Quest Synthetic Data Generator
  
  ![kaggle\_dataset](img/kaggle_dataset.png)
  > Kaggle dataset (Bread Basket)

- 隨著minimum support的下降，可以見到程式運行時間會越來越大幅度成長，尤其是brute force方法最為明顯，也因此brute force雖然coding想法容易，但只要資料量大或是minimum support低的狀況下，並不是一個好的做法。反觀FP-Growth，因為是使用全部的transaction來建構FP tree，因此對於低minimum support的環境下影響不大，比較下來也是這之中最好的做法。

## Authors
[Yu-Tong Shen](https://github.com/yutongshen/)
