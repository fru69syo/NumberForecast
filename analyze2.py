import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

#【MAX_CONTINUE】同じ数字が何回連続で出るか
def getMaxContinue(data):

    data_arr = [0] * 43
    rows = data[1:]
    max_arr = [0] * 43
    temp_max_count = [1] * 43
    match = False
    max_continue = 0
    count = 0
    max_count = [0]*10
    temp_arr = []
    temp_arr2 = []

    #print(max_arr)

    for r in range(len(rows)-1):
        arr = rows[r][2:8]
        next_arr = rows[r+1][2:8]
        #print(arr,next_arr)
        for i in range(len(arr)):
            for j in range(len(next_arr)):
                if arr[i] == next_arr[j]:
                    #print('match:',arr[i],arr,next_arr)
                    data_arr[next_arr[j]-1] += 1
                    match = True
                    match_count = 0
                    temp_arr.append(next_arr[j])
        while match:
            count += 1
            try:
                next_arr = rows[r+count][2:8]
            except:
                break

            #print('next:',r+count,temp_arr, next_arr)
            for i in range(len(next_arr)):
                for j in range(len(temp_arr)):
                    if next_arr[i] == temp_arr[j]:
                        #print('match:', next_arr,temp_arr[j])
                        data_arr[next_arr[i] - 1] += 1
                        match_count += 1
                        temp_max_count[temp_arr[j]-1] += 1
                        if(max_arr[temp_arr[j]-1] < temp_max_count[temp_arr[j]-1]):
                            max_arr[temp_arr[j]-1] = temp_max_count[temp_arr[j] - 1]
                        temp_arr2.append(temp_arr[j])

            if match_count > 0:
                temp_arr = temp_arr2
                temp_arr2 = []
                match_count = 0
            else:
                if max_continue < count:
                    max_continue = count;
                max_count[count-1] += 1
                count = 0
                match_count = 0
                temp_max_count = [1] * 43
                match = False
                temp_arr = []
                temp_arr2 = []

    print('最大連続数:',max_continue) #max_arr(max)で出せるが念のため
    print('2回以上連続した回数:',data_arr)
    print('数字別最大連続回数 :',max_arr)
    print('連続数総計',max_count)


# 【NEIGHBOR_NUM】隣り合う数字
def getNeighborNum(data):

    data_arr = [0] * 43
    rows = data

    data_arr = [0] * 43
    neighbor_arr = [] # 隣り合う数字のセットを格納する？
    neighbor_count = [0] * 6 # 隣り合う数の位置統計
    neighbor_max_count = [0] * 6 # 最大隣接数
    refer_arr = [0] * 6 # 隣り合う数の位置
    temp_arr = []

    count = 1

    for row in rows:

        arr = row[2:8]
        for i in range(5):
            num1 = arr[i]
            num2 = arr[i + 1]

            if (num2 - num1 == 1):
                #neighbor_arr.append([num1, num2])
                count += 1
                refer_arr[i] = 1
                refer_arr[i + 1] = 1
            else:
                if (count > 1):
                    neighbor_max_count[count-1] += 1
                count = 1


        for j in range(6):
            if (refer_arr[j] == 1):
                #print(arr[j] * refer_arr[j]-1)
                data_arr[arr[j] * refer_arr[j] - 1] += 1
                neighbor_count[j] += 1
                temp_arr.append(arr[j] * refer_arr[j])

        if len(temp_arr) > 0:
            neighbor_arr.append(temp_arr)
        temp_arr = []
        refer_arr = [0]*6

    # for n in neighbor_arr:
    #     data_arr[n[0]-1] += 1
    #     data_arr[n[1]-1] += 1

    print('隣接する数字が存在した回数:',len(neighbor_arr))
    print('隣接最大数総計:',neighbor_max_count)
    print('位置別隣接数字登場回数:',neighbor_count)
    print('隣接数字:',neighbor_arr)
    print('数字別隣接回数:',data_arr)






# 【MAX_INTERVAL】最大間隔

def getMaXInterval(data):

    data_arr = [0] * 43 #数字別最大間隔
    max_arr = [0] * 43
    mean_interval_arr = [0]*43
    median_interval_arr = [0]*43

    # 数字毎
    interval_arr = [[] for i in range(43)]
    max_interval_arr = [0]*43
    rows = data
    max_interval =0

    for row in rows:

        data_arr = list(map(lambda x: x + 1, data_arr))
        arr = row[2:8]

        for i in range(len(arr)):
            if(max_interval_arr[arr[i]-1] < data_arr[arr[i]-1]):
                max_interval_arr[arr[i] - 1] = data_arr[arr[i]-1]

            #print(data_arr[arr[i]-1]-1)
            interval_arr[arr[i]-1].append(data_arr[arr[i]-1]-1)
            data_arr[arr[i] - 1] = 0
            if (max_interval < max(data_arr)):
                max_interval = max(data_arr)


    for i in range(len(interval_arr)):
        if(len(interval_arr[i])==0):
            interval_arr[i].append(max_interval)

        mean_interval_arr[i] = round(sum(interval_arr[i])/len(interval_arr[i]),1)
        median_interval_arr[i] = statistics.median(interval_arr[i])


    print('直近間隔:',data_arr)
    print('最大間隔:',max_interval)
    print('数字別最大間隔値:',max_interval_arr)
    print('平均値:',mean_interval_arr)
    print('中央値:',median_interval_arr)
#
# 【NUM_CORRELATION】
# data_arr = [[0] * XX] * XX
#
# for row in rows:
#
#     arr = row
#     for i in range(6):
#         for j in range(i + 1, 6):
#             data_arr[row[i]][row[j]] = +1
#             data_arr[row[j]][row[i]] = +1
#
#
# 【NEIGHBOR_NUM】
# data_arr = [0] * XX
# neighbor_arr = [] // 隣り合う数字のセットを格納する？
# neighbor_count = [0] * 6 // 隣り合う数の位置統計
# neighbor_max_count = [0] * 6 // 最大隣接数
# refer_arr = [0] * 6 // 隣り合う数の位置
#
# count = 1
#
# for row in rows:
#
#     arr = row
#     for i in range(5):
#         num1 = arr[i]
#         num2 = arr[i + 1]
#
#         if (num2 - num1 = 1):
#             neighbor_arr.append([num1, num2])
#             count += 1
#             refer_arr[i] = 1
#             refer_arr[i + 1] = 1
#         else:
#             if (count > 1):
#                 neighbor_max_count[count] += 1
#             count = 1
#
#     for j in range(5)
#         if (refer_arr[j] = 1):
#             data_arr[arr[i] * refer_arr[i] - 1] += 1
#             neighbor_count[j] += 1
#

# データの読み込み
df = pd.read_csv('loto6_data.csv', encoding='shift_jis')

# SepalLength列をndarrayに変換
data = np.array(df.tail(100))
print(data)
getMaxContinue(data)
getNeighborNum(data)
getMaXInterval(data)


