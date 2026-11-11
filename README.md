# Tanh Activation Function Visualisation

## 1. Project Overview

This project develops an interactive web application to visualise the **Hyperbolic Tangent (Tanh) Activation Function** using Python and Streamlit.

The application allows users to adjust input values through an interactive slider and observe how the Tanh function transforms the input into an output between -1 and 1.

The graph and calculated output update automatically whenever the selected input value changes, providing an interactive way to understand the behaviour of the Tanh activation function in artificial neural networks.

## 2. Project Objectives

- To understand the concept and behaviour of the Tanh activation function.
- To visualise the relationship between input and output values.
- To demonstrate how Tanh transforms input values into a range between -1 and 1.
- To develop an interactive web application using Python and Streamlit.
- To provide a clear visual learning experience for understanding activation functions in neural networks.

## 3. Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Develop the interactive web application |
| NumPy | Generate input values and calculate Tanh outputs |
| Matplotlib | Create and display the Tanh graph |
| GitHub | Source code management and project documentation |
| Streamlit Community Cloud | Deploy the application online |

## 4. Tanh Activation Function

The Hyperbolic Tangent (Tanh) activation function is commonly used in artificial neural networks and deep learning.

Its mathematical formula is:

\[
f(x)=\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}
\]

The Tanh function transforms real-valued inputs into outputs between -1 and 1.

### Function Behaviour

- **Negative input:** The output approaches -1.
- **Zero input:** The output equals 0.
- **Positive input:** The output approaches 1.

### Example Outputs

| Input (x) | Tanh Output |
|---:|---:|
| -5 | -0.9999 |
| -2 | -0.9640 |
| 0 | 0.0000 |
| 1 | 0.7616 |
| 2 | 0.9640 |
| 5 | 0.9999 |

## 5. Application Features

### 5.1 Interactive Input Slider

Users can select an input value ranging from -6 to 6 using the Streamlit slider.

### 5.2 Dynamic Graph Visualisation

The application displays the Tanh activation curve using Matplotlib. The graph updates automatically whenever the selected input value changes.

### 5.3 Selected Input Indicator

A red point highlights the selected input value and its corresponding output on the graph.

### 5.4 Real-Time Output Display

The application calculates and displays the Tanh output based on the selected input value.

### 5.5 Clear and User-Friendly Interface

The application provides a clear title, graph labels, legend, grid, input slider, and output display to improve readability and user interaction.

## 6. Application Screenshot

The following screenshot shows the developed Tanh Activation Function web application.

![Tanh Activation Function Application](images/tanh_app.png)

**Figure 1: Tanh Activation Function Web Application**

### Screenshot Interpretation

Based on the displayed application:

- Selected input value: **1.00**
- Calculated Tanh output: **0.7616**
- The red point highlights the selected input and its corresponding output on the graph.
- The output demonstrates how the Tanh function transforms an input of 1 into approximately 0.7616.

The graph shows an S-shaped curve that approaches -1 for negative inputs and 1 for positive inputs, with the curve passing through zero.

## 7. Project Structure

The Tanh application is developed as an independent Python web application.

```text
Tanh-activation-function/
│
├── SD24024_LAB4_tanh_app.py
├── requirements.txt
├── README.md
│
└── images/
    └── tanh_app.png
```

| File | Description |
|---|---|
| `SD24024_LAB4_tanh_app.py` | Main Python script containing the Tanh calculation, Streamlit interface, and graph visualisation |
| `requirements.txt` | Lists the required Python libraries |
| `README.md` | Project documentation and setup instructions |
| `images/tanh_app.png` | Screenshot of the Tanh application |

The Tanh application is maintained in its own Python file, separate from the ReLU and Sigmoid applications. This independent structure makes the application easier to understand, execute, maintain, and update.

## 8. Installation and Setup

Follow the instructions below to run the application locally.

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/gabrielladorrie/Tanh-activation-function.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Tanh-activation-function
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit Application

```bash
streamlit run SD24024_LAB4_tanh_app.py
```

After running the command, Streamlit will open the application in your default web browser.

## 9. Requirements

The application requires the following Python libraries:

```text
streamlit
numpy
matplotlib
```

These dependencies are listed in the `requirements.txt` file to make installation easier and ensure the application can be reproduced in another environment.

## 10. Deployment

The application is deployed using **Streamlit Community Cloud**, allowing users to access the application through a web browser without installing Python locally.

### Deployment Steps

1. Upload the project files to the GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Connect your GitHub account.
4. Select the Tanh Activation Function repository.
5. Set `SD24024_LAB4_tanh_app.py` as the main application file.
6. Click Deploy.
7. Test the deployed application to ensure the slider, graph, and output display work correctly.

**Live Streamlit Application:**

https://tanh-activation-function-7wjrhksvc6vrsaetyvv7yw.streamlit.app/

**GitHub Repository:**

https://github.com/gabrielladorrie/Tanh-activation-function

## 11. Learning Outcomes

Through this project, users can understand:

- The mathematical concept of the Tanh activation function.
- How negative input values produce outputs closer to -1.
- How positive input values produce outputs closer to 1.
- Why the Tanh function is zero-centred.
- How activation functions introduce non-linearity into neural networks.
- How Python libraries such as Streamlit, NumPy, and Matplotlib can be combined to create interactive visualisations.

## 12. Conclusion

The Tanh Activation Function application demonstrates how the Hyperbolic Tangent function transforms input values into outputs between -1 and 1 through an interactive visualisation.

By using Streamlit, users can adjust input values and immediately observe the corresponding changes in the graph and calculated output.

The application provides an effective visual learning experience for understanding the behaviour and application of the Tanh activation function in artificial neural networks.

## 13. GitHub Repository Topics

Suggested repository topics:

`python` `streamlit` `tanh` `hyperbolic-tangent` `activation-function` `neural-networks` `deep-learning` `machine-learning` `data-visualisation`
