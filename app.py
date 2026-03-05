import datetime

data_str = input("iveskit da (yyyy-mm-dd ): ")
data = datetime.datetime.strptime(data_str, "%Y-%m-%d")
delta = datetime.datetime.today() - data
print(f"Praejo dienu : {delta.days}")

