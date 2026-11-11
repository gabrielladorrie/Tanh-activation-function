
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Page title
st.title("Tanh Activation Function")
st.write("Visualisation of the Hyperbolic Tangent (Tanh) activation function.")

# Generate input values
xgrid = np.linspace(-6, 6, 400)

# Activation function
def act_curve(name, x):
    if name == "tanh":
        return np.tanh(x)
    return x

# User input
input_value = st.slider("Select input value (x)", -6.0, 6.0, 1.0)

# Calculate output
ygrid = act_curve("tanh", xgrid)
output = act_curve("tanh", input_value)

# Plot graph
fig, ax = plt.subplots(figsize=(6, 4))

ax.plot(xgrid, ygrid, label="Tanh")
ax.scatter(input_value, output, color="red", label="Selected input")

ax.set_title("Tanh Activation Function")
ax.set_xlabel("Input (x)")
ax.set_ylabel("Output f(x)")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# Display output
st.write("### Output")
st.metric("Tanh Output", f"{output:.4f}")
