# Import the matplotlib library
import matplotlib.pyplot as plt

def plot_weather_data(weather_data):
    index = 0
    for data in weather_data:
        # Organize data for plotting
        categories = [data[0][1], data[1][1], data[2][1]] # X - axis labels
        values = [data[0][2], data[1][2], data[2][2]] # Y - axis values
        
        # Create the line graph
        plt.plot(categories, values, marker='o')

        # Add labels and title
        plt.xlabel('Cities')

        if(index == 0):
            plt.ylabel('Temperature')
            plt.title("Temperature Graph")
        elif(index == 1):
            plt.ylabel('Humidity')
            plt.title("Humidity Graph")
        else:
            plt.ylabel('Wind Speed')
            plt.title("Wind Speed Graph")

        # Add a legend
        plt.legend()

        # Show the plot
        plt.show()

        index += 1



