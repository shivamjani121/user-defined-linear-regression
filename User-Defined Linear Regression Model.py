#program to make user define linear regression
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from sklearn.metrics import mean_squared_error,r2_score
import numpy as np
#To import dataset
#Dataset
def load_data():
    #fetching the information from the data set to the dataframe(df) using pandas
    global df
    f=input("Enter the file path or file name:")
    df = pd.read_csv(f)
    return df
def show():
    #Using Head comand to print the data in the top 5 ROW 
    pd.set_option('display.max_columns', None)
    print(df.head())
def eda():
    #To find the null values in the set 
    print("Null values")
    print(df.isnull().sum())
def clean():
    #Deleting the null vale from the dataset
    global df
    df.dropna(inplace=True)
    print("Null values removed")
def select():
    #Selecting the dependend and independent variable to train the model
    global X,y,I,A,D
    print(df.head(1))
    D=input("Enter the dependent variable:")
    A=int(input("No of column you want to enter for independent"))
    if A==1:
        I=[input("Enter the independent variable:")]
    else:
        I = input("Enter the independent variable(s), separated by comma: ").split(",")
    X  = df[I]
    y  = df[D]
    print("Independent variables:", I)
    print("Dependent variable:", D)
def split():
    #Spliting the data to train the model into 80:20 ratio Train:Test
    global X_train, X_test, y_train, y_test
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)
def train():
    #To train the model 
    global model
    model = LinearRegression()
    model.fit(X_train,y_train)
def pred():
    #to predict the random prediction
    global y_pred
    y_pred = model.predict(X_test)
    print("Random Predicted Values:",y_pred)
def prediction_check():
    #To take input from the use for specific predicted 
    global y_pred
    values = []
    print("--- Prediction Check ---")
    if A==1:
        # Simple Linear Regression
        value = float(input(f"Enter value for {I[0]}: "))
        values = [[value]]
        y_pred = model.predict(values)
        print("Predicted value",D,":", y_pred)

    else:
        for i in range(len(I)):
            value = float(input(f"Enter value for {I[i]}: "))
            values.append(value)
        X_new = [values]
        y_pred = model.predict(X_new)
        print("Predicted value:", y_pred[0])

def plot():
    print("Random prediction for ploting the graph")
    y_pred_plot = model.predict(X_test)
    if len(I) == 1:
        T=input("Enter the title for graph")
        YL=input("Enter the Y label for graph")
        XL=input("Enter the X label for graph")
        # Simple Linear Regression
        plt.scatter(
            X_test,
            y_test,
            label="Actual"
        )

        plt.plot(
            X_test,
            y_pred_plot,
            label="Regression Line"
        )

        plt.xlabel(XL)
        plt.ylabel(YL)
        plt.title(T)

    else:
        # Multiple Linear Regression
        T=input("Enter the title for graph")
        YL=input("Enter the Y label for graph")
        XL=input("Enter the X label for graph")
        plt.scatter(
            y_test,
            y_pred_plot,
            label="Actual "
        )

        minimum = min(
            y_test.min(),
            y_pred_plot.min()
        )

        maximum = max(
            y_test.max(),
            y_pred_plot.max()
        )

        plt.plot(
            [minimum, maximum],
            [minimum, maximum],
            label="Prediction (Best Fit Line)"
        )
        plt.xlabel(XL)
        plt.ylabel(YL)
        plt.title(T)
    plt.legend()
    plt.grid()
    plt.show()

def eval():
    #matrix for the evalution 
    print('MSE (Mean Square Error):',mean_squared_error(y_test,y_pred))
    print('RMSE(Root Mean Square Error):',np.sqrt(mean_squared_error(y_test,y_pred)))
    print('R2Score(root 2 score):',r2_score(y_test,y_pred))

#calling the function according to the requirement
while True:
    print("WELCOME TO THE AUTONOMOUS LINEAR REGRESSION MODEL")
    print("MADE BY Shivam Singh Jani")
    print("What do you want to do?")
    print("1 for dataset input")
    print("2 for Exit")
    n1=int(input("Enter your choice"))
    if n1==1:
        load_data()
        print("The dataset is ready now.")
        print("1 to show 5 row of data ")
        print("2 for exit")
        n2=int(input("What you want to perform "))
        if n2==1:
            show()
            print("Now What you want to do ")
            print("1 for checking any null values")
            print("2 for exit")
            n3=int(input("Enter your choice"))
            if n3==1:
                eda()
                print("Now What you want to do ")
                print("1 for drop null values")
                print("2 for exit")
                n4=int(input("Enter your choice"))
                if n4==1:
                    clean()
                    print("1 for selecting columns ")
                    print("2 for exit")
                    n5=int(input("Enter your choice"))
                    if n5==1:
                        select()
                        split()
                        train()
                        print("What you want to predict")
                        print("1 for random prediction")
                        print("2 for specific prediction")
                        print("3 for exit")
                        n6=int(input("Enter your choice"))
                        if n6==1:
                            pred()
                            a=input("do you want to plot the graph also Y/N")
                            if a=="Y" or a=="y":
                                plot()
                                a=input("do you also want evaluation matrix Y/N")
                                if a=="Y" or a=="y":
                                   eval()
                                else:
                                    break 
                            else:
                                break
                        elif n6==2:
                            prediction_check()
                            a=input("do you What to plot the graph also Y/N")
                            if a=="Y" or a=="y":
                                pred()
                                plot()
                                a=input("do you also What evaluation matrix Y/N")
                                if a=="Y" or a=="y":
                                    eval()
                                else:
                                    break 

                        elif n6==3:
                            break
                        else:
                            print("enter a correct choice")
                    elif n5==2:
                        break
                    else:
                        print("enter a correct choice")
                elif n4==2:
                    break
                else:
                    print("enter a correct choice")
            elif n3==2:
                break
            else:
                print("enter a correct choice")

        elif n2==2:
            break
        else:
            print("enter a correct choice")
    elif n1==2:
        break
    else:
        print("enter a correct choice")