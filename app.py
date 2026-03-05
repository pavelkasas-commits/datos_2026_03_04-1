import pendulum

data_str = input("iveskit da (yyyy-mm-dd ): ")
data = pendulum.from_format(data_str, "YYYY-MM-DD")
delta = data.diff(pendulum.today())

print(f"Praejo dienu : {delta.in_days()}")

