TRADE_DATA = """MSFT|400
IBM|1000
AAPL|500
AAPL|600
NFLX|1000
AMZN|700
GOGL|300
"""


def solution(TRADE_DATA, top):
    TRADE_DATA_dic = {}
    TRADE_DATA_dic_sorted = [] 
    for line in TRADE_DATA.split("\n"):
        if not line: 
            break
        # print(line)
        line_arr = line.split("|")
        # print(line_arr)
        try: 
            # print(line_arr[0])
            # print(line_arr[1])
            pass
        except:
            print("error")
        if not line_arr[0] in TRADE_DATA_dic:
            TRADE_DATA_dic[line_arr[0]] = int(line_arr[1])
        else: 
            TRADE_DATA_dic[line_arr[0]] += int(line_arr[1])
        
       
        # print(TRADE_DATA_dic_sorted)
     # ... sort the value 
    print(TRADE_DATA_dic)
    TRADE_DATA_dic_sorted = sorted(TRADE_DATA_dic.items(), key=lambda x:x[1], reverse=True)
    print(TRADE_DATA_dic_sorted[0:top])

solution(TRADE_DATA, 3)