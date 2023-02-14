import pandas as pd

def main():
    data = pd.read_csv("squirrel_data.csv")
    # counts = data['Primary Fur Color'].value_counts() #need index_col = 0
    grey_squirrels_count = len(data[data['Primary Fur Color'] == "Gray"])
    cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
    black_squirrels_count = len(data[data['Primary Fur Color'] == "Black"])

    data_dict = {
        'fur_colour': ['gray', 'cinnamon', 'black'],
        'count': [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
    }

    counts = pd.DataFrame(data_dict)
    counts.to_csv("fur_colour_count.csv")

if __name__ == "__main__":
    main()