import pandas as pd
import os
from yamlReader import load_params
from dvclive import Live





def firstprocedure(a,b,c):
    return a+b+c



if __name__ == "__main__":
    params = load_params(params_path='params.yaml')
    # print(firstprocedure(1,2))
    # read the csv file
    df = pd.read_csv("data1/values.csv")
    print(df)
    # add a column to the csv file
    # df["sum"] = df["a"] + df["b"]
    disturbance = params["first_procedure"]["disturbance"]
    data = firstprocedure(df["val1"],df["val2"],disturbance)
    print(data)

    # create a csv file with the sum of the values
    # df["sum"] = data
    total={"sum":[data[0]]}
    df = pd.DataFrame(total)
    df.to_csv("data1/first_procedure_output.csv",index=False)
    with Live(save_dvc_exp=True) as live:

        live.log_params(params)
        live.log_metric("sum",data[0])
    # create a csv file with the sum of the values

    # save the csv file
    





