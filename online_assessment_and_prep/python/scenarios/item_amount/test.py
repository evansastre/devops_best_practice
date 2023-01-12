
#    example:
#     UserID      ItemID      Amount
#     100         1           67
#     100         1           34
#     101         2           2
#     100         3           100
#     102         1           88
#     100         2           12
#     102         3           67
#     101         3           886

#  第一列玩家UserID, 第二列游戏道具ID, 第三列获取的道具数量, 求出
# 每位玩家 对应的 每种道具的 总数量


#UserID      ItemID      Amount
f="test.csv"
def solution(f):
    import pandas as pd
    df = pd.read_csv(f)
    df.sort_values(by=["UserID", "ItemID"], inplace=True, ascending=True, ignore_index=True)
    # print(df)
    print(df.groupby(["UserID", "ItemID"])["Amount"].sum())

solution(f)