#Edit of code
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('Deaths in NSW 2012~2022')


Deaths_in_NSW_2012~2022_df = pd.read_csv('data/Deaths in NSW 2012~2022_aud.csv',
                            header=None,
                            names=['Country', 'Local', 'AUD', 'Date'])

#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(Deaths_in_NSW_2012-2022_df)

def showCharts():
    Deaths_in_NSW_2012-2022_df.plot(
                    kind='bar',
                    x='Country',
                    y='AUD',
                    color='blue',
                    alpha=0.3,
                    title='Cost of a Big Mac in AUD')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Big Mac Data Extraordinaire!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the cost of a big mac in AUD
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

   

#----Main program----#
while not quit:
    userOptions()