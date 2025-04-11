# Pupil data idexing tensors project
# Failed in a tired state - below is an example of overthinking
""""import torch

class IsNotTensorError(Exception): # valid tensor error
    pass

class TensorMismatchError(Exception): # matching tensors error
    pass    

class DivisionByZeroError(Exception): # if min==max error
    pass

class TensorContainsNonNumeric(Exception): # is there non-numerical data in tensor
    pass

def tensor_length(*args):
    try:
        if not isinstance(args,torch.Tensor):
            raise IsNotTensorError("Is not tensor")
        first_size = args.size(0)
        if first_size != args.size(0):
            raise TensorMismatchError("Tensors don't match")
        from functools import reduce
        import operator
        result = reduce(operator.mul,args)

    except IsNotTensorError as e:
        print(f"Error: {e}")
    
    except TensorMismatchError as e:
        print(f"Error: {e}")

def AllEqual_values(numerator: torch.Tensor, *denominators: torch.Tensor) -> torch.Tensor:
    try:
       for tensor in denominators:
            if torch.any(tensor ==0):
                raise DivisionByZeroError("Error: Likeley all scores are same, or none missing data")
            from functools import reduce
            import operator 
            denominator_product = reduce(operator.mul, denominators)
            return numerator / denominator_product
    except DivisionByZeroError as e:
        print(f"Error: {e}")



Test_1=torch.tensor([34,23,34,45,56,5,4,32,34])
Test_2=torch.tensor([35,23,21,34,45,56,67,6,34])
Test_3=torch.tensor([34,34,34,34,34,34,34,54,5])
"""
# Below is a working example:
import torch

# Custom exceptions
class IsNotTensorError(Exception):
    pass

class NonNumericDataError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass

def normalize_tensor(tensor: torch.Tensor) -> torch.Tensor:
    try:
        # 1. Validate input: Check if it's a tensor
        if not isinstance(tensor, torch.Tensor):
            raise IsNotTensorError("Input is not a tensor.")

        # 2. Check for non-numeric data (check for NaN or inf values)
        if not torch.isfinite(tensor).all():
            raise NonNumericDataError("Tensor contains non-numeric values (NaN or Inf).")

        # 3. Check for division by zero (min == max)
        min_value = tensor.min()
        max_value = tensor.max()
        
        if min_value == max_value:
            raise DivisionByZeroError("Tensor values are constant, cannot normalize.")

        # 4. Normalize tensor values between 0 and 1
        normalized_tensor = (tensor - min_value) / (max_value - min_value)

        return normalized_tensor

    except (IsNotTensorError, NonNumericDataError, DivisionByZeroError) as e:
        print(f"Error: {e}")
        return None

# Example usage
tensor = torch.tensor([34,45,56,34,34,455,34], dtype=torch.float32)
normalized_tensor = normalize_tensor(tensor)
if normalized_tensor is not None:
    print("Normalized Tensor:", normalized_tensor)

# Improved for only allowing 100 as highest score eg. can't get more than 100% on a test

import torch

# Custom exceptions
class IsNotTensorError(Exception):
    pass

class NonNumericDataError(Exception):
    pass

class DivisionByZeroError(Exception):
    pass

class MaxScoreExceededError(Exception):
    pass  # New custom exception for exceeding max score

def normalize_tensor(tensor: torch.Tensor) -> torch.Tensor:
    try:
        # 1. Validate input: Check if it's a tensor
        if not isinstance(tensor, torch.Tensor):
            raise IsNotTensorError("Input is not a tensor.")

        # 2. Check for non-numeric data (check for NaN or inf values)
        if not torch.isfinite(tensor).all():
            raise NonNumericDataError("Tensor contains non-numeric values (NaN or Inf).")

        # 3. Check if the maximum score exceeds 100
        max_value = tensor.max()
        if max_value > 100:
            raise MaxScoreExceededError(f"Error: The maximum score exceeds 100. Max value found: {max_value}")

        # 4. Check for division by zero (min == max)
        min_value = tensor.min()
        if min_value == max_value:
            raise DivisionByZeroError("Tensor values are constant, cannot normalize.")

        # 5. Normalize tensor values between 0 and 1
        normalized_tensor = (tensor - min_value) / (max_value - min_value)

        return normalized_tensor

    except (IsNotTensorError, NonNumericDataError, DivisionByZeroError, MaxScoreExceededError) as e:
        print(f"Error: {e}")
        return None

# Example usage
tensor = torch.tensor([34, 45, 56, 34, 34, 455, 34], dtype=torch.float32)
normalized_tensor = normalize_tensor(tensor)
if normalized_tensor is not None:
    print("Normalized Tensor:", normalized_tensor)
