#messing with try and except
import torch

class TensorMismatchError(Exception):  # Custom exception class
    pass  # Create a named exception for tensor length mismatch

def tensor_lengths(tensor_a, tensor_b):
    try:
        # Check if both inputs are PyTorch tensors
        if not isinstance(tensor_a, torch.Tensor) or not isinstance(tensor_b, torch.Tensor):
            raise TypeError("Both inputs must be tensors.")
        
        # Check if tensor lengths match
        if tensor_a.size(0) != tensor_b.size(0):
            raise TensorMismatchError("Tensors don't match.")
        
        # Perform tensor multiplication and return the result
        result = tensor_a * tensor_b
        return result  # Return the result directly
        
    except TensorMismatchError as e:  # Handle specific tensor mismatch error
        print(f"Custom error: {e}")
        return None  # Return None if tensor lengths don't match

    except Exception as e:  # Handle any other unexpected errors
        print(f"Custom error: {e}")
        return None  # Return None for any other exception

# Example tensors
tensor1 = torch.tensor([1, 2, 3])
tensor2 = torch.tensor([4, 5, 6])

tensor3 = torch.tensor([1, 2])
tensor4 = torch.tensor([4, 5, 6])

# Test case where tensors match in length
result = tensor_lengths(tensor1, tensor2)
if result is not None:
    print("Tensor multiplication result (matching lengths):", result)  # Expected output: tensor([4, 10, 18])

# Test case where tensors don't match in length
result = tensor_lengths(tensor3, tensor4)
if result is None:
    print("Tensor multiplication result (mismatched lengths): Error")  # Expected output: Error

# Dynamically test check lengths
import torch

class TensorMismatchError(Exception):  # Custom exception class
    pass  # Create a named exception for tensor length mismatch

def tensor_lengths(tensor_a, tensor_b):
    try:
        # Check if both inputs are PyTorch tensors
        if not isinstance(tensor_a, torch.Tensor) or not isinstance(tensor_b, torch.Tensor):
            raise TypeError("Both inputs must be tensors.")
        
        # Check if tensor lengths match
        if tensor_a.size(0) != tensor_b.size(0):
            raise TensorMismatchError("Tensors don't match in length.")
        
        # If lengths match, perform multiplication
        result = tensor_a * tensor_b
        return result  # Return the result directly if no error
        
    except TensorMismatchError as e:  # Handle specific tensor mismatch error
        print(f"Custom error: {e}")
        return None  # Return None if tensor lengths don't match

    except Exception as e:  # Handle any other unexpected errors
        print(f"Custom error: {e}")
        return None  # Return None for any other exception

# Example tensors
tensor1 = torch.tensor([1, 2, 3])  # Matching tensor
tensor2 = torch.tensor([4, 5, 6])  # Matching tensor

tensor3 = torch.tensor([1, 2])     # Mismatched tensor (too short)
tensor4 = torch.tensor([4, 5, 6])  # Mismatched tensor (too long)

# Test case where tensors match in length
result = tensor_lengths(tensor1, tensor2)
if result is not None:
    print("Tensor multiplication result (matching lengths):", result)  # Expected output: tensor([4, 10, 18])

# Test case where tensors don't match in length
result = tensor_lengths(tensor3, tensor4)
if result is None:
    print("Tensor multiplication result (mismatched lengths): Error")  # Expected output: Error
