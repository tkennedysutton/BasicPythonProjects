"""Task Overview:
Create a function that performs "Z-Score Normalization" on a tensor. This process will standardize the data (i.e., convert it to a distribution with a mean of 0 and a standard deviation of 1).
"""
import torch

class IsTensorError(Exception):                    # check  tensor is valid
    pass

class ContainsNonNumericalError(Exception):        # check tensor only contains numerical data
    pass                                     

class IsDivisionError(Exception):                  # check if only 1 data point
    pass

class Exceed100Error(Exception):                   # check if scores exceed 100
    pass

def normalise_tensor(tensor):
    try:
        # check if tensor is a tensor
        if not isinstance(tensor, torch.Tensor):    #here I forgot to capitalise Tensor!
            raise IsTensorError("Input is not a tensor")
        # check if tensor contains numerical data
        if not torch.isfinite(tensor).all():
            raise ContainsNonNumericalError("Tensor contains non-numeric values")
        # check if values exceed 100
        max_value = tensor.max()
        if max_value > 100:
            raise Exceed100Error("Tensor contains value > 100")
        # check if only contains 1 value
        min_value = tensor.min()
        if min_value == max_value:
            raise IsDivisionError("Tensor only has 1 data point, or all scores equal")
        # z-value normalisation
        values_intensor = tensor.numel()
        total_sum = tensor.sum()
        mean_tensor = total_sum/values_intensor
        std_dev = tensor.std()
        z_scores_tensor = (tensor - mean_tensor) / (std_dev)
        return z_scores_tensor
    except (IsTensorError, ContainsNonNumericalError, IsDivisionError, Exceed100Error) as e:
        print(f"Error: {e}")
        return None
pupil_scoresA = torch.tensor([34,34,23,45,34,23,43,45,32,34,54],dtype=torch.float32)
z_scores_tensor = normalise_tensor(pupil_scoresA)
if z_scores_tensor is not None:
    print("Normalised tensor:",z_scores_tensor)


