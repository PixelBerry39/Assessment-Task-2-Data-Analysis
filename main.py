import pandas as pd
import matplotlib.pyplot as plt

quit = False

original_df = pd.read_csv('Deaths in NSW 2012-2022.csv')


deathsnsw_df = pd.read_csv('Deaths in NSW 2012-2022.csv')

deathsnsw_df = deathsnsw_df[deathsnsw_df['Standardised death rate'].str.contains('np')==False]
deathsnsw_df['Estimated resident population'] = deathsnsw_df['Estimated resident population'].str.replace(',', '')
deathsnsw_df['Standardised death rate'] = deathsnsw_df['Standardised death rate'].astype(float)
deathsnsw_df['Estimated resident population'] = deathsnsw_df['Estimated resident population'].astype(float)
deathsnsw_df['Death Percentage'] = (deathsnsw_df['Standardised death rate'] / deathsnsw_df['Estimated resident population']) * 100
print(deathsnsw_df)


def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(deathsnsw_df)

def showCharts():
    deathsnsw_df.plot(
                    kind='bar',
                    x='Estimated resident population',
                    y='Standardised death rate',
                    color='blue',
                    alpha=0.3,
                    title='Population\'s effect on death rate')
    plt.show()

def showMean():
    mean_death_rate = deathsnsw_df['Standardised death rate'].mean()
    print(f"The mean death rate is {mean_death_rate}")

    deathsnsw_df.plot(
        kind='bar',
        x='Estimated resident population',
        y='Standardised death rate', 
        color='blue',
        alpha=0.3,
        title=f'Mean Death Rate: {mean_death_rate}'
        )
    plt.show()

def calculateDeathPercentage():
    print(deathsnsw_df[['Location', 'Estimated resident population', 'Standardised death rate', 'Death Percentage']])

def showExtremes():
    highest = deathsnsw_df.loc[deathsnsw_df['Death Percentage'].idxmax()]
    lowest = deathsnsw_df.loc[deathsnsw_df['Death Percentage'].idxmin()]
    print(f"Suburb with the highest death percentage:\n{highest}\n")
    print(f"Suburb with the lowest death percentage:\n{lowest}")

def userOptions():
    global quit

    print("""Welcome to the Death Rate Data Extraordinaire! :D
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the death rate
    4 - Show the mean death rate
    5 - Calculate death percentage by suburb
    6 - Show highest and lowest death rates
    7 - Quit Program
        """)
    

    choice = int(input('Enter Selection: '))

    if choice == 1:
        showOriginalData()
    elif choice == 2:
        showUpdatedData()
    elif choice == 3:
        showCharts()
    elif choice == 4: 
        showMean()
    elif choice == 5:
        calculateDeathPercentage()
    elif choice == 6:
        showExtremes()
    elif choice == 7:
        quit = True
    else:
        print('A number between 1 and 7, come on!')


    #print('Enter a number, it is not that hard.')

while not quit:
    userOptions()