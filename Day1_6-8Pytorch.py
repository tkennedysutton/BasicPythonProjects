# tensors
import torch
daily_steps = torch.tensor([9000,8900,6900,8960], dtype=torch.float32) #dtype=torch.float32: This specifies the data type of the tensor.
if daily_steps.numel() % 2 != 0:                    #daily_steps.numel()This is a method that returns the total number of elements in the tensor, and you need to call it with ()
    raise ValueError("Must be even values")         #this raises an error if the tensor is not even
reshaped_tensor = daily_steps.view(2,-1)            #this is to reshape the tensor so it is 2x2
print("reshaped tensor:\n",reshaped_tensor)         #\n leaves a space between: and the tensor

#Element-wise Operations - perform arithmetic on each individual element in a tensor or array
import torch
# Define tensors representing personal daily metrics
coffee_cups = torch.tensor([2,4,8,2])
steaks_eaten = torch.tensor([2,1,6,2])
# Calculate a "fuel" metric: quality coffee and steak together boost energy for the day
def daily_fuel(coffee_cups,steaks_eaten):       #these define the function
    return coffee_cups*steaks_eaten             
fuel = daily_fuel(coffee_cups, steaks_eaten)  #this calls the function
print("daily fuel\n",fuel)               #this prints the calculation, it happens under the surface


#ML context
import torch
# Define two tensors for a model-related computation (e.g., adjustment of pupil scores)
a = torch.tensor([48,37,36,39,36,37])
b = torch.tensor([3,5,6,3,5,3])
def x(a,b):
    return a+b
def y(a,b):
    return a-b
xx = x(a,b)
yy = y(a,b)
print(f"xx= {xx}")
print(f"yy= {yy}")

import torch
import torch

# Check if CUDA is available and set the device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Define tensors and move them to the selected device (GPU if available)
a = torch.tensor([48,37,36,39,36,37]).to(device)
b = torch.tensor([3,5,6,3,5,3]).to(device)

# Define the functions
def x(a, b):
    return a + b

def y(a, b):
    return a - b

# Perform the operations
xx = x(a, b)
yy = y(a, b)

# Print the results, ensuring it's on the right device
print(f"xx= {xx}")
print(f"yy= {yy}")
