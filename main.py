import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('Deaths in NSW 2012-2022.csv')


deathsnsw_df = pd.read_csv('Deaths in NSW 2012-2022.csv')
deathsnsw_df = deathsnsw_df[deathsnsw_df['Standardised death rate'].str.contains('np')==False]
deathsnsw_df = deathsnsw_df['Standardised death rate'].astype(float)


def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(deathsnsw_df)

def showCharts():
    deathsnsw_df.plot(
                    kind='bar',
                    x='Population',
                    y='Death Rate',
                    color='blue',
                    alpha=0.3,
                    title='Population\'s effect on death rate')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Death Rate Data Extraordinaire! :D
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the death rate
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('A number between 1 and 4, come on!')

    except:
        print('Enter a number, it is not that hard.')

while not quit:
    userOptions()