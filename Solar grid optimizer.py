# Power Plant Optimizer

import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc
from abc import ABC, abstractmethod
import datetime as d
import os


def clear_screen():
    os.system("cls")

class Plant_Optimizer_Structure(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def cost_function(self):
        pass

class Plant_Optimizer(Plant_Optimizer_Structure):
    def __init__(self,total_demand,solar_panel_cost,
                 energy_solar,battery_cost,energy_battery):
        self.total_demand = total_demand
        self.solar_panel_cost = solar_panel_cost
        self.energy_solar = energy_solar
        self.energy_battery = energy_battery
        self.battery_cost = battery_cost

    def cost_function(self,variable):
        x,y = variable
        self.cost_equation = (x*self.solar_panel_cost) + (y*self.battery_cost)
        return self.cost_equation
    
    def energy_function(self,variable):
        x,y = variable
        self.energy_equation = ((x*self.energy_solar) +
                                 (y*self.energy_battery) - 
                                self.total_demand)
        return self.energy_equation
    
    def optimizing_function(self,guess):
        limit = ([1,None],[1,None])
        constraint = {"type":"eq","fun":self.energy_function}
        self.min_value = sc.minimize(fun = self.cost_function,
                            bounds = limit,constraints=constraint,
                            x0=guess).x

    
    def display_optimized_reasult(self):
        clear_screen()
        print("\n--- OPTIMIZING DATA ---")
        print("\n--- DISPLAYING REASULT ---\n")
        current_time = d.datetime.now()
        print("Optimization date :",current_time.date())
        print("Optimization time :",current_time.time())
        print()
        print("TOTAL ENERGY DEMAND :",self.total_demand,"KWH")
        print(f"\n+--------------+--------------+")
        print(f"| {'APPARATUS':12} | {'QUANTITY':12} |")
        print(f"+--------------+--------------+")
        print(f"| {'SOLAR PANELS':12} | {np.round(self.min_value[0],0):12} |")
        print(f"+--------------+--------------+")
        print(f"| {'BATTERIES':12} | {np.round(self.min_value[1],0):12} |")
        print(f"+--------------+--------------+\n")        

clear_screen()

print("\n--- WELCOME TO SOLAR ENERGY PLANT MANAGER ---")
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

    if choice == 1:
        clear_screen()
        print("\n--- ENTERING SYSTEM ---")
        total_energy_demand = int(input("\nEnter total energy demand in KWH : "))
        solar_energy = int(input("Enter energy produced by 1 solar panel : "))
        battery_energy = int(input("Enter energy stored by 1 battery : "))
        solar_cost = int(input("Enter Cost of 1 solar panel in NPR : "))
        battery_cost = int(input("Enter Cost of 1 battery in NPR : "))

        optimizer_object = Plant_Optimizer(total_demand=total_energy_demand,
                                        solar_panel_cost=solar_cost,
                                        battery_cost=battery_cost,
                                        energy_solar=solar_energy,
                                        energy_battery=battery_energy)

        guess = np.random.randint(10,50,size = 2)
        optimizer_object.optimizing_function(guess)

        while True :

            print(f"\n+----------------------+--------------+")
            print(f"| {'CHOICE':20} | {'OPTION':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'OPTIMIZE DATA':20} | {'1':12} |")
            print(f"+----------------------+--------------+")
            print(f"| {'RETURN MENU':20} | {'2':12} |")
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
                optimizer_object.display_optimized_reasult()
            
            if choice == 2:
                clear_screen()
                break

    if choice == 2:
        print("\n--- EXITING SYSTEM ---")
        print("--- THANK YOU ---\n")
        exit()

    








    