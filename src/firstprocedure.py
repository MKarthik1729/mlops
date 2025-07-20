import pandas as pd
import os








def firstprocedure(a,b,c):
    return a+b+c



if __name__ == "__main__":
    # print(firstprocedure(1,2))
    # read the csv file
    df = pd.read_csv("data/values.csv")
    print(df)
    # add a column to the csv file
    # df["sum"] = df["a"] + df["b"]
    disturbance = 100
    data = firstprocedure(df["val1"],df["val2"],disturbance)
    print(data)

    # create a csv file with the sum of the values
    # df["sum"] = data
    total={"sum":[data[0]]}
    df = pd.DataFrame(total)
    df.to_csv("data/first_procedure_output.csv",index=False)

    # create a csv file with the sum of the values

    # save the csv file
    





