from abc import ABC, abstractmethod
import math as m
import numpy as np
import matplotlib.pyplot as plt
import random as r
import datetime as d
from datetime import timedelta 

class Electrical_Component(ABC):
    def __init__(self):
        pass

    def calculate_reactance(self):
        pass

class Resistor(Electrical_Component):
    def __init__(self,resistance):
        super().__init__()
        self.resistance = resistance

    def calculate_reactance(self):
        self.reactance = self.resistance

class Inductor(Electrical_Component):
    def __init__(self,inductance):
        self.inductance = inductance

    def calculate_reactance(self,angular_frequency):
        self.reactance = round(angular_frequency * self.inductance,3)

class Capacitor(Electrical_Component):
    def __init__(self,capacitance):
        self.capacitance = capacitance

    def calculate_reactance(self,angular_frequency):
        self.reactance = round(1/(angular_frequency * self.capacitance),3)

class Net_component():
    def __init__(self,impedence):
        self.impedence = impedence

    def calculate_voltage_values(self,max_voltage):
        self.max_voltage = max_voltage
        self.rms_voltage = round(self.max_voltage / m.sqrt(2),3)
        self.mean_voltage = round((2/m.pi)*self.max_voltage,3)

    def calculate_current_values(self,max_current):
        self.max_current = max_current
        self.rms_current = round(self.max_current / m.sqrt(2),3)
        self.mean_current = round((2/m.pi)*self.max_current,3)
    
    def calculate_power_values(self,phase):
        self.active_power = self.rms_current * self.rms_voltage * m.cos(m.radians(phase))
        self.reactive_power = self.rms_current * self.rms_voltage * m.sin(m.radians(phase))
        self.apparent_power = self.rms_current * self.rms_voltage 

def plotting_function_RLC(time_array,current_array,voltage_array,max_current,rms_current,
                      mean_current,max_voltage,rms_voltage,mean_voltage):
    
    fig,axs = plt.subplots(1,2)
    fig.suptitle("... CURRENT AND VOLTAGE ...",fontsize = 20)

    axs[0].set_title("CURRENT")
    axs[0].plot(time_array,current_array)
    axs[0].grid(True)
    axs[0].set_xlabel("TIME in 's'")
    axs[0].set_ylabel("CURRENT VALUE IN 'A'")
    axs[0].axhline(max_current,label = "MAX",color = "r",ls = "--")
    axs[0].axhline(rms_current,label = "RMS",color = "b",ls = "--")
    axs[0].axhline(mean_current,label = "MEAN",color = "g",ls = "--")
    axs[0].legend(loc="lower right")


    axs[1].set_title("VOLTAGE")
    axs[1].plot(time_array,voltage_array)
    axs[1].grid(True)
    axs[1].set_xlabel("TIME in 's'")
    axs[1].set_ylabel("VOLTAGE VALUE IN 'V'")
    axs[1].axhline(max_voltage,label = "MAX",color = "r",ls = "--")
    axs[1].axhline(rms_voltage,label = "RMS",color = "b",ls = "--")
    axs[1].axhline(mean_voltage,label = "MEAN",color = "g",ls = "--")
    axs[1].legend(loc="lower right")

    
    plt.tight_layout()
    plt.show()


def Summary_Table_RLC(Period,Ang_freq,v_rms,v_max,v_mean,i_rms,
                   i_max,i_mean,resistance,capacitance,inductance,
                   active_power,reactive_power,apparent_power,phase) :
    print(f"\n+--------------------------------+")
    print(f"| {' SUMMARY TABLE ':<30} |")
    print(f"+--------------------------------+")
    print(f"| Time Period (sec) : {round(Period,3):<10} |")
    print(f"+--------------------------------+")
    print(f"| Ang.Freq (rad/sec) : {round(Ang_freq,2):<9} |")
    print(f"+--------------------------------+")
    print(f"| Resistance (ohm) : {round(resistance,3):<11} |")
    print(f"+--------------------------------+")
    print(f"| Capacitance (F) : {round(capacitance,3):<12} |")
    print(f"+--------------------------------+")
    print(f"| Inductance (H) : {round(inductance,3):<13} |")
    print(f"+--------------------------------+")
    print(f"|{' PHASE { deg }':<17}: {round(phase,3):<13}|")
    print(f"+--------------------------------+")
    
    print("\n")
    
    
    print(f"+--------------------------------+")
    print(f"| {' CALCULATED VALUES : ':<30} |")
    print(f"+--------------------------------+")
    print(f"|{' QUANTITIES':<17}|{' VALUES':<14}|")
    print(f"+--------------------------------+")
    print(f"|{' V.RMS { V }':<17}| {round(v_rms,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' V.MAX { V }':<17}| {round(v_max,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' V.MEAN { V }':<17}| {round(v_mean,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.RMS { Amp }':<17}| {round(i_rms,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.MAX { Amp }':<17}| {round(i_max,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.MEAN { Amp }':<17}| {round(i_mean,3):<13}|")
    print(f"+--------------------------------+") 
    
    print("\n")
    print(f"+--------------------------------+")
    print(f"| {' POWER VALUES : ':<30} |")
    print(f"+--------------------------------+")
    print(f"|{' QUANTITIES':<17}|{' VALUES':<14}|")
    print(f"+--------------------------------+")
    print(f"|{' ACTIVE { W }':<17}| {round(active_power,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' REACTIVE { VAr }':<17}| {round(reactive_power,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' APPARENT { VA }':<17}| {round(apparent_power,3):<13}|")
    print(f"+--------------------------------+")

def Summary_Table_single(Type,Period,Ang_freq,v_rms,v_max,v_mean,i_rms,
                   i_max,i_mean,value,
                   active_power,reactive_power,apparent_power,phase) :
    print(f"\n+--------------------------------+")
    print(f"| {' SUMMARY TABLE ':<30} |")
    print(f"+--------------------------------+")
    print(f"| Time Period (sec) : {round(Period,3):<10} |")
    print(f"+--------------------------------+")
    print(f"| Ang.Freq (rad/sec) : {round(Ang_freq,2):<9} |")
    print(f"+--------------------------------+")
    print(f"| Passive element : {Type:<12} |")
    
    if Type == "Resistor":
    
        print(f"+--------------------------------+")
        print(f"| Resistance (ohm) : {value:<12}|")
        print(f"+--------------------------------+")
    
    elif Type == "Capacitor":
    
        print(f"+--------------------------------+")
        print(f"| Capacitance (F) : {value:<13}|")
        print(f"+--------------------------------+")
        
    elif Type == "Inductor" :
        
        print(f"+--------------------------------+")
        print(f"| Inductance (H) : {value:<14}|")
        print(f"+--------------------------------+")

    print(f"|{' PHASE { deg }':<17}: {round(phase,3):<13}|")
    print(f"+--------------------------------+")
    
    print("\n")
    
    
    print(f"+--------------------------------+")
    print(f"| {' CALCULATED VALUES : ':<30} |")
    print(f"+--------------------------------+")
    print(f"|{' QUANTITIES':<17}|{' VALUES':<14}|")
    print(f"+--------------------------------+")
    print(f"|{' V.RMS { V }':<17}| {round(v_rms,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' V.MAX { V }':<17}| {round(v_max,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' V.MEAN { V }':<17}| {round(v_mean,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.RMS { Amp }':<17}| {round(i_rms,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.MAX { Amp }':<17}| {round(i_max,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' I.MEAN { Amp }':<17}| {round(i_mean,3):<13}|")
    print(f"+--------------------------------+") 
    
    print("\n")
    print(f"+--------------------------------+")
    print(f"| {' POWER VALUES : ':<30} |")
    print(f"+--------------------------------+")
    print(f"|{' QUANTITIES':<17}|{' VALUES':<14}|")
    print(f"+--------------------------------+")
    print(f"|{' ACTIVE { W }':<17}| {round(active_power,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' REACTIVE { VAr }':<17}| {round(reactive_power,3):<13}|")
    print(f"+--------------------------------+")
    print(f"|{' APPARENT { VA }':<17}| {round(apparent_power,3):<13}|")
    print(f"+--------------------------------+")



print("\n--- WELCOME TO SINEWAVE SYMPHONY WAVE SIMULATION ---\n")
print("DEAR USER, ENTER THE GIVEN DATA : \n")

while True :

    print(f"\n+------------------+------------+")
    print(f"|{' CHOICE':18}|{' NUMBER':12}|")
    print(f"+------------------+------------+")
    print(f"|{' SINGLE " R "  ':18}|{'  1.':12}|")
    print(f"+------------------+------------+")
    print(f"|{' SINGLE " L " ':18}|{'  2.':12}|")
    print(f"+------------------+------------+")
    print(f"|{' SINGLE " C " ':18}|{'  3.':12}|")
    print(f"+------------------+------------+")
    print(f"|{' SERIES " RLC " ':18}|{'  4.':12}|")
    print(f"+------------------+------------+")

    while True:
        choice = int(input("Enter choice : "))
        if choice <1 or choice >4:
            print("--- INVALID CHOICE ---")
            print("--- PLEASE RE-ENTER ---")
            continue
        break
    if choice == 1:
        max_voltage = float(input("\nEnter max voltage (V) : "))
        time_period = float(input("Enter time period (s) : "))

        angular_frequency = round((2*m.pi)/time_period,3)

        resistance = float(input("Enter resistance (ohm) : "))
        r = Resistor(resistance)
        r.calculate_reactance()

        total_impedence = m.sqrt(pow(r.reactance,2))
        max_current = max_voltage/total_impedence

        phase_difference = round(m.degrees(m.atan(0/r.reactance)),3)

        net = Net_component(total_impedence)
        net.calculate_current_values(max_current)
        net.calculate_voltage_values(max_voltage)
        net.calculate_power_values(phase_difference)

        start_time_date = d.datetime.now()

        value_array =[]
        voltage_array = []
        current_array = []
        time_array = np.arange(0,100)

        # here i is inductor so using j

        for j in range(100):
            voltage_array.append(max_voltage*m.sin((angular_frequency*time_array[j])+m.radians(phase_difference)))
            current_array.append(max_current*m.sin((angular_frequency*time_array[j])))


        print("\nEXPERIMENT TYPE : RESPONSE OF SINGLE RESISTIVE CIRCUIT ")
        print("EXPERIMENT DATE : ",start_time_date.date())
        print("EXPERIMENT TIME ",start_time_date.strftime("%I:%M:%S %p"))    

        Summary_Table_single("Resistor",time_period,angular_frequency,net.rms_voltage,net.max_voltage,
                    net.mean_voltage,net.rms_current,net.max_current,net.mean_current,
                    r.reactance,net.active_power,net.reactive_power,
                    net.apparent_power,phase_difference)

        plotting_function_RLC(time_array,current_array,voltage_array,net.max_current,net.rms_current,
                        net.mean_current,net.max_voltage,net.rms_voltage,net.mean_voltage)
        
    if choice == 2:
        max_voltage = float(input("\nEnter max voltage (V) : "))
        time_period = float(input("Enter time period (s) : "))

        angular_frequency = round((2*m.pi)/time_period,3)

        inductance = float(input("Enter inductance (H) : "))
        i = Inductor(inductance)
        i.calculate_reactance(angular_frequency)

        total_impedence = m.sqrt(pow(i.reactance,2))
        max_current = max_voltage/total_impedence

        phase_difference = 90

        net = Net_component(total_impedence)
        net.calculate_current_values(max_current)
        net.calculate_voltage_values(max_voltage)
        net.calculate_power_values(phase_difference)

        start_time_date = d.datetime.now()

        value_array =[]
        voltage_array = []
        current_array = []
        time_array = np.arange(0,100)

        # here i is inductor so using j

        for j in range(100):
            voltage_array.append(max_voltage*m.sin((angular_frequency*time_array[j])+m.radians(phase_difference)))
            current_array.append(max_current*m.sin((angular_frequency*time_array[j])))


        print("\nEXPERIMENT TYPE : RESPONSE OF SINGLE INDUCTIVE CIRCUIT ")
        print("EXPERIMENT DATE : ",start_time_date.date())
        print("EXPERIMENT TIME ",start_time_date.strftime("%I:%M:%S %p"))    

        Summary_Table_single("Inductor",time_period,angular_frequency,net.rms_voltage,net.max_voltage,
                    net.mean_voltage,net.rms_current,net.max_current,net.mean_current,
                    i.reactance,net.active_power,net.reactive_power,
                    net.apparent_power,phase_difference)

        plotting_function_RLC(time_array,current_array,voltage_array,net.max_current,net.rms_current,
                        net.mean_current,net.max_voltage,net.rms_voltage,net.mean_voltage)
    
    if choice == 3:

        max_voltage = float(input("\nEnter max voltage (V) : "))
        time_period = float(input("Enter time period (s) : "))

        angular_frequency = round((2*m.pi)/time_period,3)

        capacitance = float(input("Enter capacitance (F) : "))
        c = Capacitor(capacitance)
        c.calculate_reactance(angular_frequency)

        total_impedence = m.sqrt(pow(-c.reactance,2))
        max_current = max_voltage/total_impedence

        phase_difference = -90

        net = Net_component(total_impedence)
        net.calculate_current_values(max_current)
        net.calculate_voltage_values(max_voltage)
        net.calculate_power_values(phase_difference)

        start_time_date = d.datetime.now()

        value_array =[]
        voltage_array = []
        current_array = []
        time_array = np.arange(0,100)

        # here i is inductor so using j

        for j in range(100):
            voltage_array.append(max_voltage*m.sin((angular_frequency*time_array[j])+m.radians(phase_difference)))
            current_array.append(max_current*m.sin((angular_frequency*time_array[j])))


        print("\nEXPERIMENT TYPE : RESPONSE OF SINGLE CAPACITIVE CIRCUIT ")
        print("EXPERIMENT DATE : ",start_time_date.date())
        print("EXPERIMENT TIME ",start_time_date.strftime("%I:%M:%S %p"))    

        Summary_Table_single("Capacitor",time_period,angular_frequency,net.rms_voltage,net.max_voltage,
                    net.mean_voltage,net.rms_current,net.max_current,net.mean_current,
                    c.reactance,net.active_power,net.reactive_power,
                    net.apparent_power,phase_difference)

        plotting_function_RLC(time_array,current_array,voltage_array,net.max_current,net.rms_current,
                        net.mean_current,net.max_voltage,net.rms_voltage,net.mean_voltage)
        

    if choice == 4 :
        max_voltage = float(input("\nEnter max voltage (V) : "))
        time_period = float(input("Enter time period (s) : "))

        angular_frequency = round((2*m.pi)/time_period,3)

        resistance = float(input("Enter resistance (ohm) : "))
        r = Resistor(resistance)

        inductance = float(input("Enter inductance (H) : "))
        i = Inductor(inductance)

        capacitance = float(input("Enter capacitance (C) : "))
        c = Capacitor(capacitance)

        r.calculate_reactance()
        i.calculate_reactance(angular_frequency)
        c.calculate_reactance(angular_frequency)

        total_impedence = m.sqrt(pow(r.reactance,2)+pow(i.reactance-c.reactance,2))
        max_current = max_voltage/total_impedence

        phase_difference = round(m.degrees(m.atan((i.reactance-c.reactance)/r.reactance)),3)

        net = Net_component(total_impedence)
        net.calculate_current_values(max_current)
        net.calculate_voltage_values(max_voltage)
        net.calculate_power_values(phase_difference)

        start_time_date = d.datetime.now()

        value_array =[]
        voltage_array = []
        current_array = []
        time_array = np.arange(0,100)

        # here i is inductor so using j

        for j in range(100):
            voltage_array.append(max_voltage*m.sin((angular_frequency*time_array[j])+m.radians(phase_difference)))
            current_array.append(max_current*m.sin((angular_frequency*time_array[j])))


        print("\nEXPERIMENT TYPE : RESPONSE OF SERIES 'RLC' CIRCUIT ")
        print("EXPERIMENT DATE : ",start_time_date.date())
        print("EXPERIMENT TIME ",start_time_date.strftime("%I:%M:%S %p"))    

        Summary_Table_RLC(time_period,angular_frequency,net.rms_voltage,net.max_voltage,
                    net.mean_voltage,net.rms_current,net.max_current,net.mean_current,
                    r.reactance,c.reactance,i.reactance,net.active_power,net.reactive_power,
                    net.apparent_power,phase_difference)

        plotting_function_RLC(time_array,current_array,voltage_array,net.max_current,net.rms_current,
                        net.mean_current,net.max_voltage,net.rms_voltage,net.mean_voltage)


    print("\n--- DEAR USER, ENTER YOUR CHOICE ---")
    print(f"\n+------------+----------+")
    print(f"|{' Options':12}|{' Choice':10}|")
    print(f"+------------+----------+")
    print(f"|{' RE-START':12}|{'  1.':10}|")
    print(f"+------------+----------+")
    print(f"|{' EXIT':12}|{'  2.':10}|")
    print(f"+------------+----------+\n")

    while True :
        choice = int(input("Enter your choice : "))
        if choice !=1 and choice !=2:
            print("--- INVALID CHOICE ---")
            print("--- PLEASE RE-ENTER ---")
            continue
        break

    if choice == 2:
        print("--- THANK YOU USER ---")
        print("... EXITING ...")
        print("<3 :) <3")
        print()
        exit()

    print()


                         
                    