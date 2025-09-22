# Smart Grid Nearest Substation Visualizer 

import numpy as np
import matplotlib.pyplot as plt
import scipy.spatial as sc
from abc import ABC,abstractmethod

class Basic_Grid(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def compute_nearest_station(self):
        pass

    @abstractmethod
    def plot_network(self):
        pass

class Smart_Grid(Basic_Grid):
    def __init__(self,house,station):
        self.house = house 
        self.station = station 

    def compute_nearest_station(self):
        self.indices = sc.KDTree(self.station).query(self.house)[1]
        print("\n--- DISPLAYING HOUSE AND SUB-STATIONS ---")
        print(f"\n+--------------+--------------+")
        print(f"| {'HOUSE-NUM':12} | {'SUB-STATION':12} |")
        print(f"+--------------+--------------+")
        for house,station in enumerate(self.indices):
            print(f"| {house:12} | {station:12} |")
            print(f"+--------------+--------------+")


    def plot_network(self):
        self.indices = sc.KDTree(self.station).query(self.house)[1]
        plt.title("NEAREST SUB-STATION",fontsize = 25)
        plt.scatter(self.house[:,0],self.house[:,1],lw = 0.5,
                    color = "green",label = "House")
        plt.scatter(self.station[:,0],self.station[:,1],lw=5,
                    color = "red",label = "Sub Station")

        for i,j in enumerate(self.indices):
            plt.plot([self.house[i,0],self.station[j,0]],
                     [self.house[i,1],self.station[j,1]],
                     ls = "--",color = "black",lw = 0.5)

        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.show()

    def calculate_cabel_length(self):
        self.indices = sc.KDTree(self.station).query(self.house)[1]
        distance = 0
        for i,j in enumerate(self.indices):
            distance += sc.distance.euclidean(self.house[i],
                    self.station[j])
            
        print("\n--- CABEL LENGTH REQUIRED ---")
        print("Cabel length =",np.round(distance,2),"units")
    
    def plot_convex(self):
        self.indices = sc.ConvexHull(self.house).simplices
        plt.title("CONVEX HULL",fontsize = 25)
        plt.scatter(self.house[:,0],self.house[:,1],lw = 0.5,
                    color = "red",label = "House")
        for index in self.indices:
            plt.plot(self.house[index,0],self.house[index,1],
                     ls = "--",lw = 1,color = "black")

        plt.plot([],[],ls="--",
                 color = "black",label = "Convex Hull")
        plt.legend()
        plt.tight_layout()
        plt.grid()
        plt.show()

print("\n--- WELCOME TO SMART GRID SYSTEM ---")

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

    if choice == 1:
        print("\n--- ENTERING SYSTEM ---")
        n_h = int(input("Enter number of houses : "))
        n_st = int(input("Enter number of sub-stations : "))

        house = np.random.randint(0,50,size = n_h*2).reshape(n_h,2)
        station = np.random.randint(0,50,size = n_st*2).reshape(n_st,2)

        grid_object = Smart_Grid(house,station)


        while True :
            print(f"\n+----------------------+--------------+")
            print(f"| {'OPERATION TO DO':20} | {'CHOICE':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'NEAREST STATION':20} | {'1':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'PLOT HOUSE-STATION':20} | {'2':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'PLOT CONVEX HULL':20} | {'3':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'FIND CABEL LENGTH':20} | {'4':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'GO MAIN MENU':20} | {'5':12} |")
            print(f"+----------------------+--------------+\n")

            while True:
                choice = int(input("Enter choice : "))
                if choice <1 or choice >5:
                    print("\n--- INVALID CHOICE ---")
                    print("--- RE-ENTER ---")
                    continue
                break

            if choice == 1:
                print("\n--- CALCULATING NEAREST STATION ---")
                grid_object.compute_nearest_station()
            
            if choice == 2:
                print("\n--- PLOTTING HOUSE AND STATION ---")
                grid_object.plot_network()

            if choice == 3:
                print("\n--- PLOTTING CONVEX HULL ---")
                grid_object.plot_convex()

            if choice == 4:
                grid_object.calculate_cabel_length()

            if choice == 5:
                break


    if choice == 2:
        print("\n--- THANK YOU ---")
        print("--- EXITING SYSMTEM ---")
        print()
        exit()




