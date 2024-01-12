
##Assignment 2 concept of continue and break

raw_data = [1,2,3,4,200,300,400,500,234,"918",00,0,"88", "abcd",420,32]
for clean_data in raw_data:
    if isinstance(clean_data, int):
        print(clean_data)
    elif clean_data.isdigit():
        print("String value detected")
        continue
    else:
        print(f"opps! {clean_data} is not valid digit")
        break

