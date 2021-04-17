#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram


# Our first simple quantum circuit
So to build our first circuit, we need to encode the input, perform some operation and then obtain an output/ measurement. All of these need to be done by obeying the postulates of quantum mechanics (operators, observables, evolution, collapse etc)
# In[3]:


#We start by creating a circuit with 6 qubits and 6 outputs
no = 6  #no is the number of qubits
no_q = no
no_b = no
qc_output = QuantumCircuit(no_q,no_b)


# In[5]:


# We use the operation Measure to extract the outputs of those 6 qubits that we considered.

for j in range(no):
    qc_output.measure(j,j)


# In[6]:


#To visualize it, we invoke the draw command
qc_output.draw()

If we run the circuit several times and plot the results in a histogram, we will observe that the result for each qubit is always a 0. This is because we haven't performed any operation or calculation yet, by default qubits are always initialized to give a 0. 

# In[7]:


sim = Aer.get_backend('qasm_simulator')  # qasm simulator is one of the many simulators
qobj = assemble(qc_output)  # we are turning the circuit into an object so that the backend can run it
result = sim.run(qobj).result()  # the exp is run and we obtain the result in the variable result
# counts is a dictionary containing the number of times each result appeared

counts = result.get_counts()
# we now display it on a histogram

plot_histogram(counts)


# In[12]:


qc_encode = QuantumCircuit(no)
qc_encode.x(3)
qc_encode.draw()


# In[13]:


qc = qc_encode + qc_output
qc.draw()


# In[14]:


qobj = assemble(qc)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)


# In[17]:


qc_cnot = QuantumCircuit(5)
qc_cnot.cx(0,1)
qc_cnot.draw()


# In[20]:


qc = QuantumCircuit(2,2)
qc.x(0)
qc.cx(0,1)
qc.measure(0,0)
qc.measure(1,1)
qc.draw()


# In[21]:


import qiskit
qiskit.__qiskit_version__


# In[22]:


from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi


# In[23]:


from qiskit_textbook.widgets import plot_bloch_vector_spherical
coords = [pi/2,0,1] # [Theta, Phi, Radius]
plot_bloch_vector_spherical(coords) # Bloch Vector with spherical coordinates


# In[25]:


qc = QuantumCircuit(1)
qc.x(0)
qc.draw()


# In[27]:


# Create the X-measurement function:
def x_measurement(qc, qubit, cbit):
    """Measure 'qubit' in the X-basis, and store the result in 'cbit'"""
    qc.h(qubit)
    qc.measure(qubit, cbit)
    return qc

initial_state = [1/sqrt(2), -1/sqrt(2)]
# Initialise our qubit and measure it
qc = QuantumCircuit(1,1)
qc.initialize(initial_state, 0)
x_measurement(qc, 0, 0)  # measure qubit 0 to classical bit 0
qc.draw()


# In[28]:


qasmsim = Aer.get_backend('qasm_simulator')  # Tell Qiskit how to simulate our circuit
qobj = assemble(qc)  # Assemble circuit into a Qobj that can be run
counts = qasmsim.run(qobj).result().get_counts()  # Do the simulation, returning the state vector
plot_histogram(counts)  # Display the output state vector


# In[ ]:




