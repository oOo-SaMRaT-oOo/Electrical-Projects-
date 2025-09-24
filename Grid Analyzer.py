# Grid Analyzer

import numpy as np
import matplotlib.pyplot as plt
from abc import ABC,abstractmethod
import scipy.spatial as sc
import os

class Grid_Layout(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def Grid_Generator(self):
        pass

class Grid_Practical(Grid_Layout):
    def __init__(self,n_h,n_s):
        self.n_h = n_h
        self.n_s = n_s

    def Grid_Generator(self):
        self.house = np.random.randint(0,100,size = self.n_h*2).reshape(self.n_h,2)
        self.station = np.random.randint(0,100,size = self.n_s *2).reshape(self.n_s,2)

    def Connection_Builder(self):
        indices = sc.KDTree(self.station).query(self.house)[1]
        self.connection_matrix = []
        for i,j in enumerate(indices):
            self.connection_matrix.append([i,j])
        self.connection_matrix = np.array(self.connection_matrix)
        self.house_station_connection = {}
        for i in range(self.n_s):
            self.house_station_connection.update({i:list(indices).count(i)})

    def Outage_Analyzer(self):
        print("\n--- STATION AND HOUSES ---")
        print(f"\n+------------+------------+")
        print(f"| {'STATION':10} | {'HOUSES':10} |")
        print(f"+------------+------------+")
        for key,value in self.house_station_connection.items():
            print(f"| {key:10} | {value:10} |")
            print(f"+------------+------------+")
        print()


    def Grid_Visualizer(self):
        plt.title("--- GRID VISUAL ---",fontsize = 25)
        plt.scatter(self.house[:,0],self.house[:,1],lw=1,
                    label = "House")
        plt.scatter(self.station[:,0],self.station[:,1],lw = 2.5,color ="red",
                    label = "Station")
        indices = sc.KDTree(self.station).query(self.house)[1]
        for i,j in enumerate(indices):
            plt.plot([self.house[i,0],self.station[j,0]],
                     [self.house[i,1],self.station[j,1]],
                     ls = "--",lw = "0.5",color = "gray")
        plt.plot(ls ="--",color ="gray",lw ="0.5",label = "Connection")   
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

def clear_screen():
    os.system("cls")

clear_screen()

print("\n--- WELCOME TO GRID ANALYZER ---")

print("\n--- SELECT YOUR CHOICE ---")

while True :
    print(f"\n+--------------+--------------+")
    print(f"| {'CHOICE':12} | {'OPTION':12} |")
    print(f"+--------------+--------------+")
    print(f"| {'ENTER SYSTEM':12} | {'1':12} |")
    print(f"+--------------+--------------+")
    print(f"| {'EXIT SYSTEM':12} | {'2':12} |")
    print(f"+--------------+--------------+\n")

    while True :
        choice = int(input("Enter choice : "))
        if choice !=1 and choice !=2:
            print("\n--- INVALID CHOICE ---")
            print("--- RE-ENTER ---")
            continue
        break

    if choice == 1 :
        clear_screen()
        print("\n--- ENTERING SYSTEM ---\n")
        n_h = int(input("Enter number of HOUSES : "))
        n_s = int(input("Enter number of STATIONS : "))

        grid_object = Grid_Practical(n_h,n_s)
        grid_object.Grid_Generator()
        grid_object.Connection_Builder()

        while True :

            print(f"\n+----------------------+--------------+")
            print(f"| {'CHOICE':20} | {'OPTION':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'OUTAGE VISUALIZER':20} | {'1':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'GRID VISUALIZER':20} | {'2':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'GO MAIN MENU':20} | {'3':12} |")
            print(f"+----------------------+--------------+\n")

            while True :
                choice = int(input("Enter choice : "))
                if choice !=1 and choice !=2 and choice !=3:
                    print("\n--- INVALID CHOICE ---")
                    print("--- RE-ENTER ---")
                    continue
                break

            if choice == 1:
                clear_screen()
                print("\n--- ENTERING OUTAGE VISUAZLIZER ---\n")
                grid_object.Outage_Analyzer()

            if choice == 2:
                clear_screen()
                print("\n--- ENTERING GRID VISUALIZER ---")
                grid_object.Grid_Visualizer()

            if choice == 3:
                clear_screen()
                break

    if choice == 2:
        clear_screen()
        print("\n--- EXITING SYSTEM ---")
        print("\n--- THANK YOU ---\n")
        exit()






    









