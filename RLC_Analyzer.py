import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sympy as smp
import streamlit as st
import math as m

def plot_function(x,y,entity):
    fig,axs = plt.subplots()
    fig.suptitle(f"{entity} PLOT")
    axs.plot(x,y,lw=2,ls="--",color ="black")
    axs.grid(True)
    axs.set_xlabel("TIME VALUES")
    axs.set_ylabel(f"{entity} VALUES")
    plt.tight_layout()
    st.pyplot(fig)

st.sidebar.header("RLC Analyzer")
st.sidebar.caption("~ By Samrat Malla")
opt = st.sidebar.radio("SELECT ACTIONS TO PERFORM :",
    options=["RLC ANALYSIS","APP OBJECTIVE","ABOUT APP"])
st.sidebar.markdown("---")
if opt =="RLC ANALYSIS":

    st.markdown("<h1 style = 'text-align : center;'>RLC ANALYZER</h1>",
    unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("INPUT SECTION :")
    st.caption("PROVIDE VALUES IN S.I UNITS ")
    col1,col2,col3 = st.columns(3)
    with col1:
        resistance = st.number_input("Enter Resistance (Ω) : ",min_value=0.0,
                                     value = 20.0)
    with col2:
        inductance = st.number_input("Enter Inductance (H) : ",min_value=0.0,
                                     value = 20.0)
    with col3:
        capacitance = st.number_input("Enter Capacitance (C) : ",min_value=0.0,
                                      value = 35.0)

    voltage = st.slider("Enter Source Voltage (V) : ",0,100,15)
    frequency = st.slider("Enter Source Frequency (Hz) : ",0,100,60)
    st.markdown("---")

    st.subheader("THEORY SECTION :")
    L,R,C,Vo,t = smp.symbols("L R C Vo t",real = True)
    i = smp.Function("i")(t)

    eqn = smp.Eq(L*i.diff(t,2) + R*i.diff(t,1) + i/C,Vo)
    soln = smp.dsolve(eqn,i)
    st.write("RLC series differential equation : ")
    st.latex(smp.latex(eqn))
    st.markdown("---")

    st.write("Exact solution for i(t) : ")
    st.latex(smp.latex(soln))
    st.markdown("---")

    st.subheader("CIRCUIT ANALYSIS : ")
    st.markdown("PROVIDED VALUES : ")
    c1,c2,c3 = st.columns(3)
    with c1:
        st.write("RESISTANCE (R) :",f"{str(resistance)}","Ω")
    with c2:
        st.write("INDUCTANCE (L) :",f"{str(inductance)}","H")
    with c3:
        st.write("CAPACITANCE (C) :",f"{str(capacitance)}","F")
    st.markdown("---")

    st.write("SOLUTION OF CURRENT")

    soln = smp.Eq(soln.lhs,soln.rhs.subs([(R,resistance),(C,capacitance),
                                            (L,inductance),(Vo,voltage)]))
    st.latex(smp.latex(soln))
    st.markdown("---")
    st.write("PROVIDE INITIAL CONDITIONS :")
    st.caption("ENTER VALUE IN S.I UNITS")
    c1,c2  = st.columns(2)
    with c1:
        st.caption("INITIAL CONDITIONS FOR FUNCTIONAL VALUE")
        t1 = st.number_input("ENTER TIME FOR i(t) in sec : ")
        i_t1 = st.number_input("ENTER i(t) VALUE in Amps ")

    with c2:
        st.caption("INITIAL CONDITIONS FOR 1st DERIVATIVE VALUE ")
        t2 = st.number_input("ENTER TIME FOR i'(t) in sec : ")
        i_t2 = st.number_input("ENTER i'(t) VALUE in Amps ")
    st.markdown("---")

    eqn = smp.Eq(eqn.lhs.subs([(R,resistance),(C,capacitance),
    (L,inductance)]),eqn.rhs.subs([(Vo,voltage)]))

    soln = smp.dsolve(eqn,i,ics = {i.subs(t,t1):i_t1,
    i.diff(t,1).subs(t,t2):i_t2})
    st.write("COMPLETE SOLUTION :")
    st.latex(smp.latex(soln))
    st.markdown("---")

    st.subheader("VISUALIZATION SECTION :")
    angular_frequency = 2*m.pi*frequency
    Xl = angular_frequency*inductance
    Xc = 1/(angular_frequency*capacitance)
    impedence = m.sqrt(resistance**2+(Xl-Xc)**2)
    choice = st.radio("ENTER VISUALIZATION OPTIONS ",options = ["CURRENT VS TIME",
    "VOLTAGE VS TIME","None"])
    st.markdown("---")


    if choice!="None":
        st.write("ENTER TIME INTERVAL FOR VISUALIZATION :")
        st.caption("ENTER TIME VALUE IN SECONDS")
        c1,c2 = st.columns(2)
        with c1:
            t1 = st.number_input("ENTER LOWER TIME INTERVAL :",0,1000,0)
        with c2:
            t2 = st.number_input("ENTER UPPER TIME INTERVAL :",0,1000,15)
        st.markdown("---")
        time_array  = np.linspace(t1,t2,1000)
        current_function = smp.lambdify((t),soln.rhs)
        current_values = current_function(time_array)
        V = smp.Function("V")(t)
        voltage_eqn = smp.Eq(V,(soln.rhs)/impedence)
        voltage_function = smp.lambdify((t),voltage_eqn.rhs)
        voltage_values = voltage_function(time_array)

        if choice == "CURRENT VS TIME":
            plot_function(time_array,current_values,"CURRENT")
        
        if choice =="VOLTAGE VS TIME":
            plot_function(time_array,voltage_values,"VOLTAGE")
        
        st.markdown("---")

        fig,axs = plt.subplots(2)
        fig.suptitle("COMPARISON GRAPH")

        axs[0].plot(time_array,current_values,"r--")
        axs[0].set_title("CURRENT PLOT")
        axs[0].grid(True)
        axs[0].set_xlabel("TIME VALUES IN SECONDS")
        axs[0].set_ylabel("CURRENT VALUES IN AMP")

        axs[1].plot(time_array,voltage_values,"k--")
        axs[1].set_title("VOLTAGE PLOT")
        axs[1].grid(True)
        axs[1].set_xlabel("TIME VALUES IN SECONDS")
        axs[1].set_ylabel("VOLTAGE VALUES IN V")

        plt.tight_layout()
        st.pyplot(fig)
        st.markdown("---")

    st.subheader("PARAMETERS ANALYSIS :")
    c1,c2  = st.columns(2)
    with c1:
        st.write("RESISTANCE :\n",resistance,"Ω")
    with c2:
        st.write("CAPACITANCE :\n",capacitance,"F")
    c3,c4 = st.columns(2)
    with c3:
        st.write("INDUCTANCE :\n",inductance,"H")
    with c4:
        st.write("TOTAL IMPEDENCE :\n",np.round(impedence,5),"Ω")
    c1,c2  = st.columns(2)
    with c1:
        st.write("SUPPLY VOLTAGE :\n",voltage,"V")
    with c2:
        st.write("SOURCE FREQUENCY :\n",frequency,"Hz")

    st.markdown("---")

    damping_ratio = (resistance/2)*m.sqrt(capacitance/inductance)
    resonance_frequency = 1/(2*m.pi*m.sqrt(inductance*capacitance) )
    c1,c2 = st.columns(2)
    with c1:
        st.write("DAMPING RATIO (ζ) :",np.round(damping_ratio,5))
    with c2:
        st.write("NATURAL FREQUENCY :",np.round(resonance_frequency,5),"Hz")

    if damping_ratio<1:
        st.write("CONDITION : ζ < 1")
        st.write("SYSTEM STATE : UNDERDAMPED")
    elif damping_ratio==1:
        st.write("CONDITION : ζ = 1")
        st.write("SYSTEM STATE : CRITICALLY DAMPED")
    else:
        st.write("CONDITION : ζ > 1")
        st.write("SYSTEM STATE : OVERDAMPED")
    st.markdown("---")

if opt == "APP OBJECTIVE":
    st.markdown("<h1 style = 'text-align : center;'>APP OBJECTIVE</h1>",
              unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <h2>Develop a Streamlit web application that:</h2><h6>

    -> Accepts R (Resistance), L (Inductance), and C (Capacitance) as inputs.

    -> Symbolically solves the governing differential equation using SymPy.

    -> Numerically simulates the system response using SciPy.

    -> Visualizes both symbolic and numerical results using Matplotlib.

    -> Automatically determines and displays natural frequency, damping ratio, and damping type.

    -> Provides interactive controls (sliders, buttons) through Streamlit for parameter tuning.
</h6>""",
        unsafe_allow_html=True)
    st.markdown("---")

if opt =="ABOUT APP":
    st.markdown("<h1 style = 'text-align : center;'>ABOUT APP</h1>",
                unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <h7>The RLC Analyzer is an interactive Streamlit-based web application
                 designed to analyze and visualize the behavior of series RLC 
                circuits. It allows users to input the resistance (R), inductance
                 (L), capacitance (C), source voltage, and frequency to dynamically
                 study the circuit’s transient and steady-state response. Using the
                 power of SymPy, the app symbolically solves the second-order differential
                 equation governing the RLC circuit and presents the exact mathematical
                 solution for current and voltage. Integrated with NumPy and Matplotlib, 
                it further enables users to visualize how current and voltage vary with 
                time through interactive plots. The app bridges electrical theory with 
                software simulation, helping students and engineers gain a deeper 
                understanding of circuit dynamics, damping effects, and resonance behavior
                 — all within an intuitive, real-time interface.</h7>""",unsafe_allow_html=True)
    st.markdown("---")

st.caption("""
~ The RLC Analyzer is an interactive Python–Streamlit application that bridges electrical
            circuit theory and computational simulation, built using NumPy, Matplotlib,
            SymPy, and SciPy — developed by Samrat Malla""")
st.markdown("---")










        