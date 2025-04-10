#Task: Create two PyTorch tensors and perform element-wise addition and multiplication
import torch
a = torch.tensor([23,45,34,56,78,55,44,33,45,78,98,98,99,3,5,6,7,6,78,24])
b = torch.tensor([12,23,23,31,45,46,54,34,3,23,21,43,23,45,65,43,34,34,56,34])
def c(a,b):
    return a+b
add = c(a,b)
def d(a,b):
    return a*b
dd = d(a,b)
print("sum of tensors",add)
print("tensor ab multiplication=\n",dd)

reshaped_output = dd.reshape([5,-1])
print("Reshaped a*b:\n",reshaped_output)
reshaped_output2 = add.reshape([5,-1])
print("Reshaped a+b:\n",reshaped_output2)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"using device: {device}")
reshaped_output.to(device)
reshaped_output2.to(device)
def alpha(reshaped_output,reshaped_output2):
    return reshaped_output * reshaped_output2
sigma = alpha(reshaped_output,reshaped_output2)
print(sigma)