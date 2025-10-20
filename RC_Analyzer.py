import streamlit as st
import numpy as np
import sympy as smp
import matplotlib.pyplot as plt
import datetime as dt

st.title("RC CIRCUIT ANALYZER")
st.markdown("---")
st.subheader("Objectives :")
st.write("""
Build an interactive RC circuit analysis and visualization tool using Streamlit that :
- Symbolically solves the voltage and current equations,
- Numerically computes and plots results,
- Allows user input via Streamlit widgets,
- Displays results and errors clearly.
""")
st.markdown("---")

st.subheader("INPUT SECTION")
col1,col2,col3 = st.columns(3)
with col1 :
    resistance = st.number_input("Enter value of resistance : ")
    st.caption("Enter value in ohms")
with col2:
    capacitance = st.number_input("Enter value of capacticance : ")
    st.caption("Enter value in Farad")
with col3 :
    supply_voltage = st.number_input("Enter value of supply voltage : ")
    st.caption("Enter value in Volts")

col1,col2 = st.columns(2)
with col1:
    simulation_time = st.number_input("Enter simulation time : ")
    st.caption("Enter time in seconds")
with col2:
    sampling_rate = st.number_input("Enter sample rate : ")
    st.caption("Enter number of points ")
st.markdown("---")

st.subheader("THEORY SECTION")
t,R,C,Vo = smp.symbols("t R C Vo")
Vc = smp.Function("Vc")(t)
charging_eqn = smp.Eq(Vc,Vo*(1-smp.exp(-t/(R*C))))
st.write("The Charging equation of capacitor is given as :")
st.latex(smp.latex(charging_eqn))
st.write("The Discharging equation of capacitor is given as :")
discharging_eqn = smp.Eq(Vc,Vo*smp.exp(-t/(R*C)))
st.latex(smp.latex(discharging_eqn))
st.write(f"Time constant of the system : RC = {resistance*capacitance} seconds")
st.markdown("---")

st.subheader("SIMULATION SECTION")
st.write(f"Experiment Date : {dt.datetime.now().date()}")
st.write(f"Experiment Time : {dt.datetime.now().time()}")
st.markdown("---")

c1,c2,c3 = st.columns(3)
with c1:
    st.write(f"Resistance : {resistance} ohm")
with c2:
    st.write(f"Capacitance : {capacitance} Farad")
with c3:
    st.write(f"Supply Voltage : {supply_voltage} Volts")

c1,c2,c3 = st.columns(3)
with c1:
    st.write(f"Simulation Time : {simulation_time} secs")
with c2:
    st.write(f"Sample Rate : {sampling_rate}")
st.markdown("---")


time_values = np.linspace(0,int(simulation_time),int(sampling_rate))
charging_function = smp.lambdify((t),charging_eqn.rhs.subs([(R,resistance),
                                        (C,capacitance),(Vo,supply_voltage)]))
discharging_function = smp.lambdify((t),discharging_eqn.rhs.subs([(R,resistance),
                                        (C,capacitance),(Vo,supply_voltage)]))
charging_voltage = charging_function(time_values)
discharging_voltage = discharging_function(time_values)

fig,axs = plt.subplots(1,2)
fig.suptitle("RC CHARGING DISCHARGING NATURE")
axs[0].plot(time_values,charging_voltage,ls = "--",
            color = "red",label = "Charging Nature")
axs[0].grid(True)
axs[0].set_title("CHARGING CURVE")
axs[0].set_xlabel("TIME VALUE")
axs[0].set_ylabel("VOLTAGE VALUE")
axs[0].legend()

axs[1].plot(time_values,discharging_voltage,"k--",
            label = "Discharging nature")
axs[1].grid(True)
axs[1].set_title("DISCHARGING CURVE")
axs[1].set_xlabel("TIME VALUE")
axs[1].set_ylabel("VOLTAGE VALUE")
axs[1].legend()

plt.tight_layout()
st.pyplot(fig)
st.markdown("---")


fig,axs = plt.subplots()
axs.plot(time_values,charging_voltage,label = "CHARGING")
axs.plot(time_values,discharging_voltage,label="DISCHARGING")
axs.set_title("COMBINED VOLTAGE NATURE")
axs.legend()
axs.grid(True)
axs.set_xlabel("TIME VALUES")
axs.set_ylabel("VOLTAGE VALUES")
plt.tight_layout()
st.pyplot(fig)

st.markdown("---")

st.subheader("CONCLUSION")
st.write("""
This project combined theory and code to simulate an RC circuit interactively.
It revised all major Python libraries through real-world application.
A perfect step toward becoming a software-based electrical engineer.
         """)
st.markdown("---")

st.caption("~ By Samrat Malla ")
st.markdown("---")














