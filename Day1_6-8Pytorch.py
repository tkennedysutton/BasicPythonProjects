import torch
daily_steps = torch.tensor([9000,8900,6900,8960], dtype=torch.float32) #dtype=torch.float32: This specifies the data type of the tensor.
if daily_steps.numel() % 2 != 0:                    #daily_steps.numel()This is a method that returns the total number of elements in the tensor, and you need to call it with ()
    raise ValueError("Must be even values")
reshaped_tensor = daily_steps.view(2,-1)
print("reshaped tensor:\n",reshaped_tensor)


