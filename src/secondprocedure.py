import pandas as pd


def secondprocedure(a,b):
    return a*b


if __name__ == "__main__":
    # read the csv file
    df = pd.read_csv("data1/first_procedure_output.csv")
    print(df)
    # add a column to the csv file
    print(df["sum"][0])
    adder = 5
    multiplier = 20 + adder
    data = secondprocedure(df["sum"][0],multiplier)
    print(data)
    # save the csv file
    total={"multiplied":[data]}
    df = pd.DataFrame(total)
    df.to_csv("data1/second_procedure_output.csv",index=False)
