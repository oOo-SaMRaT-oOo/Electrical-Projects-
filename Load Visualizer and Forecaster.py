# Load Visualizer and Forecaster

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sc
from abc import ABC, abstractmethod
import datetime as d
import os 

def clear_screen():
    os.system("cls")

class Load_Structure(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def plot_load(self):
        pass

    @abstractmethod
    def approx_forcast(self):
        pass

class Load(Load_Structure):
    def __init__(self):
        self.t = []
        self.load = []
    
    def plot_load(self,time_interval,load):
        self.t = time_interval
        self.load = load
        a,b = self.t
        x = np.linspace(a,b,len(self.load))
        y = np.array(self.load)

        self.y_x_L = sc.interp1d(x,y,kind  = "linear",
                        fill_value="extrapolate")
        
        self.y_x_Q = sc.interp1d(x,y,kind  = "quadratic",
                        fill_value="extrapolate")
        
        self.y_x_C = sc.interp1d(x,y,kind  = "cubic",
                        fill_value="extrapolate")
        
        x_dense_value = np.linspace(a,b,100)

        fig,axs = plt.subplots(2,2)
        fig.suptitle("LOAD VISUZLIZATION",fontsize = 25)
        plt.title("LOAD VISUALIZATION",fontsize = 25)
                
        axs[0,0].plot(x,y,
                 ls = "--",color = "red",label = "No Interpolation")
        axs[0,0].set_title("Raw Plot")
        axs[0,0].grid(True)
        axs[0,0].legend()
        axs[0,0].set_xlabel("Time")
        axs[0,0].set_ylabel("Load in KWH")


        axs[0,1].plot(x_dense_value,self.y_x_L(x_dense_value),
                 ls = "--",label = "Linear Interpolation")
        axs[0,1].set_title("Linear Plot")
        axs[0,1].grid(True)
        axs[0,1].legend()
        axs[0,1].set_xlabel("Time")
        axs[0,1].set_ylabel("Load in KWH")


        axs[1,0].plot(x_dense_value,self.y_x_Q(x_dense_value),
                 ls = "--",color = "black",label = "Quadratic Interpolation")
        axs[1,0].set_title("Quadratic Plot")
        axs[1,0].grid(True)
        axs[1,0].legend()
        axs[1,0].set_xlabel("Time")
        axs[1,0].set_ylabel("Load in KWH")


        axs[1,1].plot(x_dense_value,self.y_x_C(x_dense_value),
                 ls = "--",color = "green",label = "Cubic Interpolation")
        axs[1,1].set_title("Cubic Plot")
        axs[1,1].grid(True)
        axs[1,1].legend()
        axs[1,1].set_xlabel("Time")
        axs[1,1].set_ylabel("Load in KWH")


        plt.tight_layout()
        plt.show()
        
    def approx_forcast(self):
        print("\n--- FORECASTING LOAD VARIATION ---")
        time_0_4 = np.random.randint(45,55,4)
        time_4_8 = np.random.randint(55,80,4)
        time_8_12 = np.random.randint(60,80,4)
        time_12_16 = np.random.randint(60,90,4)
        time_16_20 = np.random.randint(90,110,4)
        time_20_24 = np.random.randint(50,70,4)

        time_array = np.arange(1,25,1)
        value_array = np.hstack([time_0_4,time_4_8,time_8_12,
                                 time_12_16,time_16_20,time_20_24])
        
        interpolation_function = sc.interp1d(time_array,value_array,
                                             kind = "cubic")
        
        time_array_dense = np.linspace(1,24,1000)
        x = time_array_dense
        y = interpolation_function(time_array_dense)

        for index, value in enumerate(value_array):
            if value == np.max(value_array):
                plt.axhline(value,ls = "--",
                            color = "red",label = "MAX LOAD",lw = 1)
            
            if value ==np.min(value_array):
                plt.axhline(value,ls = "--",color= "green",
                            label = "MIN LOAD",lw = 1)


        plt.title("TODAY'S FORECAST",fontsize = 25)
        plt.xticks(time_array)
        plt.xlabel("Time")
        plt.ylabel("Load in KWH")
        plt.plot(x,y,label = "Load Variation",lw = 2,ls = "--")
        plt.legend()
        plt.grid(True)
        plt.show()


print("\n--- WELCOME TO LOAD VISUALIZER AND FORECASTER ---")

while True :
    print(f"\n+-----------------+--------------+")
    print(f"| {'CHOICE':15} | {'OPTION':12} |")
    print(f"+-----------------+--------------+")
    print(f"| {'VISUALIZE LOAD':15} | {'1':12} |")
    print(f"+-----------------+--------------+")
    print(f"| {'FORECAST LOAD':15} | {'2':12} |")
    print(f"+-----------------+--------------+")
    print(f"| {'EXIT SYSTEM':15} | {'3':12} |")
    print(f"+-----------------+--------------+\n")

    while True:
        choice = int(input("\nEnter choice : "))
        if choice <1 or choice >3 :
            print("\n--- INVALID CHOICE ---")
            print("--- RE-ENTER ---")
            continue
        break

    load_object = Load()

    if choice == 1:
        clear_screen()

        print("\n--- ENTERING LOAD VISUALIZATION ---")

        current_time = d.datetime.now()
        print("\nCurrent Date :",current_time.date())
        print("Current Time :",current_time.time())

        print(f"\n+--------------+--------------+")
        print(f"| {'TIME GAP':12} | {'OPTION':12} |")
        print(f"+--------------+--------------+")
        print(f"| {'1 to 4':12} | {'1':12} |")
        print(f"+--------------+--------------+")
        print(f"| {'4 to 8':12} | {'2':12} |")
        print(f"+--------------+--------------+") 
        print(f"| {'8 to 12':12} | {'3':12} |")
        print(f"+--------------+--------------+")   
        print(f"| {'12 to 16':12} | {'4':12} |")
        print(f"+--------------+--------------+")   
        print(f"| {'16 to 20':12} | {'5':12} |")
        print(f"+--------------+--------------+")   
        print(f"| {'20 to 24':12} | {'6':12} |")
        print(f"+--------------+--------------+\n")       

        while True:
            choice = int(input("\nEnter time interval : "))
            if choice <1 or choice >6:
                print("\n--- INVALID TIME ---")
                print("--- RE-ENTER ---")
                continue
            break

        hourly_load = list(map(int,input("Enter 4 loads measured hourly in KWH : "
                                         ).split()))

        if choice == 1:
            time = [1,4]

        if choice == 2:
            time = [4,8]

        if choice == 3:
            time = [8,12]

        if choice == 4:
            time = [12,16]

        if choice == 5:
            time = [16,20]

        if choice == 6:
            time = [20,24]

        load_object.plot_load(time,hourly_load)

        
    if choice == 2:
        clear_screen()
        print("\n--- ENTERING FORECASTER ---")
        current_time = d.datetime.now()
        print("\nCurrent Date :",current_time.date())
        print("Current Time :",current_time.time())
        load_object.approx_forcast()

    if choice == 3:
        clear_screen()
        print("\n--- EXITING SYSTEM ---")
        print("--- THANK YOU ---\n")
        exit()

    clear_screen()





