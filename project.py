import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('apartment.csv', encoding='cp949')

#df.head()

#df.index

#df.columns

#df.values

#df.values[0]

#df.describe()

#df.loc[0][0].split(' ')

def avg_money(): # 검색한 지역의 평균 매매가를 알려주기
    total = 0
    money = 0
    count = 0
    location = input("지역을 입력해주세요. : ")
    for row in range(len(df)):
        for i in df.loc[row][0].split(' '):
            if i == location:
                money = int(df.loc[row][8].replace(',','')) # 매매가격이 str 형식의 9,000형식으로 되어있기 때문에 쉼표를 빼고 int형식으로 바꿔준다.
                total +=money
                count += 1
    total = total//count
    plt.rc('font', family = 'Malgun Gothic') # 한글 입력을 위한 폰트 설정

    plt.scatter(location, total, color = 'skyblue', label = f"{location}지역의 평균 매매가")
    plt.legend()
    plt.show()
    return total, location

def graph_loc(result = [], result_name = [], result_money = [], result_min_money = []): #result : 평균매매가 저장 리스트 , result_name : 검색한 지역들, result_money : 최고가
    total = 0 # 매매가를 저장하는 변수
    money = df.loc[0][8] # 하나의 판매가격을 저장하는 변수
    count = 0  # 평균을 내기위해 갯수를 세는 변수
    info = df.loc[0][0] # 지역의 이름을 나타낸느 변수
    max_money = int(df.loc[0][8].replace(',','')) # 최고가를 저장하는 변수
    min_money = int(df.loc[0][8].replace(',',''))
    for row in range(len(df)):  # df [데이터프레임]의 길이만큼 반복
        if info != df.loc[row][0]: # 첫 이름과 반복변수내의 이름이 같지 않을경우 지역을 변경해주며 현재까지 더했던 total 값을 result에 저장
            total = total//count  #평균을 내기 위해 count로 나눠준다 (정수형으로 나누기 위해 //)
            result.append(total)  
            result_name.append(info.split(' ')[-1])  # 이름이 너무 길어지므로 맨 뒤에 이름만 넣는다
            result_money.append(max_money)
            result_min_money.append(min_money)
            total = 0 #새로운 지역을 조사하므로 초기화
            money = 0
            count = 0
            
            info = df.loc[row][0]
            money = int(df.loc[row][8].replace(',',''))
            total +=money
            count += 1
            max_money = money
            min_money = money
        else:                
            money = int(df.loc[row][8].replace(',',''))

            if max_money < money: #최고가 찾기
                max_money = money
            
            if min_money > money:
                min_money = money 

            total +=money
            count += 1
    
    plt.rc('font', family = 'Malgun Gothic') # 한글 입력을 위한 폰트 설정
    plt.figure( figsize = (14,8)) # 화면 크기 설정
    plt.xticks(rotation=45) #글씨 겹침으로 인해 회전 설정
    plt.style.use("fivethirtyeight") # 스타일 설정

    plt.plot(result_name, result_money, color = 'pink', label = '최고가', marker = 'o') # 최고가를 표시하는 선 그래프
    
    plt.bar(result_name, result, color = 'skyblue', label = '평균 매매가') #평균 매매가를 표시하는 바 그래프
    
    plt.plot(result_name, result_min_money, color = 'orange', label = '최저가', marker = 's', alpha = 0.5)
    plt.legend() # 라벨 표시
    plt.show()   # 그래프 표시
    return result,result_name

#total, location = avg_money()
#print(f"{location}지역의 평균 매매가는 {total}만원 입니다.")

#result, result_name = graph_loc()
def sell_month(sell = [], sell_count = []):
    for row in range(len(df)):
        sell.append(df.loc[row][6])
    
    for i in range(6):
        month = 202101+i
        sell_count.append(sell.count(month))
    month = set(sell)
    month = list(month)
    plt.rc('font', family = 'Malgun Gothic') # 한글 입력을 위한 폰트 설정
    plt.figure( figsize = (12,8), dpi = 80) # 화면 크기 설정

    plt.bar(month, sell_count, color = 'skyblue', label = "월별 매매 횟수")
    plt.legend()
    plt.show()
    return sell_count


s= avg_money()
