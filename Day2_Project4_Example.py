import torch  # PyTorch for tensor operations
import pandas as pd  # Pandas for reading Excel data
import logging  # Logging to keep track of what the script is doing

# === Set up logging ===
logging.basicConfig(
    filename='tensor_normalisation.log',  # All logs will be saved in this file
    level=logging.INFO,  # INFO level logs general successful operations
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format: timestamp - log level - message
)

# === Custom Exceptions ===
# These are "custom errors" we'll use to give more specific feedback if something goes wrong
class IsTensorError(Exception):
    """Raised when input is not a tensor"""
    pass

class ContainsNonNumericalError(Exception):
    """Raised when tensor contains non-numeric values (like NaN or infinity)"""
    pass

class IsDivisionError(Exception):
    """Raised when the tensor has no variation (min == max), which makes normalisation impossible"""
    pass

class Exceed100Error(Exception):
    """Raised when any value in the tensor exceeds 100 — we assume test scores should be max 100"""
    pass

# === Function to normalise a tensor ===
def normalise_tensor(tensor):
    try:
        # Check 1: Ensure input is a PyTorch tensor
        if not isinstance(tensor, torch.Tensor):
            raise IsTensorError("Input is not a tensor")  # If not, raise our custom error

        # Check 2: Ensure all values in the tensor are finite numbers (not NaN or inf)
        if not torch.isfinite(tensor).all():
            raise ContainsNonNumericalError("Tensor contains non-numeric values (inf or NaN)")

        # Check 3: Ensure no value exceeds 100 (logical upper limit for test scores)
        if tensor.max() > 100:
            raise Exceed100Error("Tensor contains value > 100")

        # Check 4: Ensure there is variation in the data (to avoid division by zero in z-score formula)
        if tensor.min() == tensor.max():
            raise IsDivisionError("Tensor only has 1 data point, or all scores equal")

        # === Step 1: Calculate mean and standard deviation ===
        mean_tensor = tensor.mean()  # Calculate the mean of the tensor
        std_dev = tensor.std()  # Calculate standard deviation

        # === Step 2: Apply Z-score normalisation formula ===
        # Formula: (x - mean) / std
        z_scores_tensor = (tensor - mean_tensor) / std_dev

        # Log success
        logging.info("Tensor normalised successfully.")
        return z_scores_tensor  # Return the normalised tensor

    except (IsTensorError, ContainsNonNumericalError, IsDivisionError, Exceed100Error) as e:
        # If any custom error is raised, log it and print it
        logging.error(f"Error during tensor normalisation: {e}")
        print(f"Error: {e}")
        return None  # Return None to signal failure

# === Function to import Excel column and convert to tensor ===
def import_excel_column_to_tensor(file_path, column_name):
    try:
        # Read Excel file into a pandas DataFrame
        df = pd.read_excel(file_path)

        # Extract the desired column, remove missing values, and ensure it's float
        data = df[column_name].dropna().astype(float).values

        # Convert numpy array to PyTorch tensor of float32 type
        tensor = torch.tensor(data, dtype=torch.float32)

        # Log success
        logging.info(f"Data imported from {file_path} and converted to tensor successfully.")
        return tensor

    except Exception as e:
        # If any unexpected error occurs (like wrong file path or column name), log and print it
        logging.error(f"Error importing data: {e}")
        print(f"Error importing data: {e}")
        return None

# === Example Usage ===

# File path to your Excel file containing class test scores
file_path = r'C:\Users\tkennedysutton\Documents\PythonProjects\Example_data.xlsx'


# The column in your Excel file that contains the scores (make sure it matches exactly)
column_name = 'Scores'

# Step 1: Import the data from Excel and convert it to tensor
pupil_scores_tensor = import_excel_column_to_tensor(file_path, column_name)

# Step 2: If import was successful, normalise the tensor
if pupil_scores_tensor is not None:
    z_scores_tensor = normalise_tensor(pupil_scores_tensor)

    # Step 3: If normalisation succeeded, print the result
    if z_scores_tensor is not None:
        print("Normalised tensor:", z_scores_tensor)
