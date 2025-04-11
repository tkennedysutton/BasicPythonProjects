# Define a class called Calculator
class Calculator:
    """A simple calculator to perform arithmetic operations with error handling."""
    def __init__(self):
            pass
    
   
# Create an instance (object) of the Calculator class
calc = Calculator()

import torch

class TensorOperationError(Exception):
    """Custom exception for handling invalid tensor operations."""
    pass  # 'pass' means we don't add anything new here, just create a named exception
  

# Define a new class called SimpleTensorProcessor
# This class inherits (extends) from Calculator, so it has all its methods too!
class SimpleTensorProcessor(Calculator):
    """
    Extends the Calculator class to process and manipulate tensors using PyTorch.
    Useful for tasks like analyzing pupil data or ML tasks involving tensor math.
    """

    # Constructor method to initialize the class
    def __init__(self):
        # Use 'super()' to call the parent class (Calculator) initializer
        super().__init__()

    # Define a method to multiply a tensor by a scalar value
    def multiply_tensor(self, tensor, scalar):
        try:
            # First, check if the input is a valid PyTorch tensor
            if not isinstance(tensor, torch.Tensor):
                # If not, raise our custom exception
                raise TensorOperationError("Input is not a valid PyTorch tensor.")
            # Perform tensor multiplication
            result = tensor * scalar
        except Exception as e:
            # Catch any unexpected exceptions and print an error message
            print(f"Error during tensor multiplication: {e}")
            return None  # Return None to indicate the operation failed
        return result  # Return the result if successful

    # Define a method to safely divide two tensors
    def safe_divide_tensors(self, tensor_a, tensor_b):
        try:
            # Check if both inputs are tensors
            if not isinstance(tensor_a, torch.Tensor) or not isinstance(tensor_b, torch.Tensor):
                raise TensorOperationError("Both inputs must be PyTorch tensors.")
            # Check if tensor_b contains any zero values to avoid division by zero
            if torch.any(tensor_b == 0):
                raise TensorOperationError("Division by zero encountered in tensor_b.")
            # Perform element-wise tensor division
            result = tensor_a / tensor_b
        except TensorOperationError as te:
            # Handle our custom tensor errors
            print(f"Custom tensor error: {te}")
            return None
        except Exception as e:
            # Catch any other unexpected exceptions
            print(f"An unexpected error occurred during tensor division: {e}")
            return None
        return result  # Return the result if successful


# Now, let's create an instance (object) of our new processor class
processor = SimpleTensorProcessor()

# Create two example tensors using PyTorch
tensor1 = torch.tensor([10.0, 20.0, 30.0])  # Tensor with some values
tensor2 = torch.tensor([2.0, 5.0, 0.0])     # Tensor with a zero to test division safety

# Test the multiply_tensor method
print("Tensor Multiplication by 2:", processor.multiply_tensor(tensor1, 2))

# Test the safe_divide_tensors method (expecting an error because tensor2 contains zero)
print("Safe Tensor Division:", processor.safe_divide_tensors(tensor1, tensor2))
