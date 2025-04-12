#Scaffold data below for me to fill in
import torch  # PyTorch for tensor operations
import pandas as pd  # Pandas for reading Excel data
import logging  # Logging for tracking progress and errors

# === Set up logging ===
logging.basicConfig(
    filename="Outlier_Detection.log", #all logs stroed here
    level=logging.INFO,              # INFO level logs general successful operations
    format='%(asctime)s - %(levelname)s - %(message)s'  # Format: timestamp - log level - message
)

# === Custom Exceptions ===
class IsTensorError(Exception):
    """Raised when input is not a tensor"""
    pass

class ContainsNonNumericalError(Exception):
    """Raised when tensor contains non-numeric values (NaN or Inf)"""
    pass

class IsDivisionError(Exception):
    pass

class Exceed100Error(Exception):
    pass

class IQRCalculationError(Exception):
    """Raised when the IQR can't be calculated due to insufficient data"""
    pass

# === Function to import Excel data and convert to tensor ===
def import_excel_column_to_tensor(file_path, column_name):              #error made, forgot the colon! (again)
    """Reads an Excel file, extracts a column, and converts it to a PyTorch tensor, for the specific column, regardless of sheet name"""
    try:
        # Step 1: Read the Excel file with all sheets
        sheets = pd.read_excel(file_path, sheet_name=None)  # Returns a dictionary of DataFrames

        # Step 2: Loop through each sheet and check if the column exists
        for sheet_name, df in sheets.items():
            if column_name in df.columns:  # If the column exists in this sheet
                # Step 3: Extract the column data, drop any NaN values, and convert to float
                data = df[column_name].dropna().astype(float).values
                # Step 4: Convert to a PyTorch tensor
                tensor = torch.tensor(data, dtype=torch.float32)
                
                # Log success
                logging.info(f"Data imported from {file_path} (sheet: {sheet_name}) and converted to tensor successfully")
                return tensor  # Return the tensor once data is found
        # If no column found in any sheet, raise an exception
        raise ValueError(f"Column '{column_name}' not found in any sheet.")
        
    except Exception as e:
        # If any unexpected error occurs, log and print it
        logging.error(f"Error importing data: {e}")
        print(f"Error importing data: {e}")
        return None
        
    
# === Function to detect outliers

def Outlier_detection(tensor):
    # Log error if not a tensor
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
        # Compute Q1 and Q3 (quantiles)
        Q1 = torch.quantile(tensor, 0.25)
        Q3 = torch.quantile(tensor, 0.75)
        # Compute IQR
        IQR = Q3 - Q1
        # Calculate lower and upper bound for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Detect outliers: Values outside the bounds
        outliers = tensor[(tensor < lower_bound) | (tensor > upper_bound)]
    
        return outliers
        
        # Log success 
        if outliers.numel() > 0:
            logging.info(f"Outliers detected in {file_path}")
            print("Outliers detected")
    except (IsTensorError, ConnectionAbortedError, Exceed100Error, IsDivisionError,Exceed100Error) as e:
        logging.error(f"import tensor error:", e)
        print("Error,{e}")    
        return None             #signals failure
    except Exception as e:
        # Catch any general exception
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")
        return None

    
# == file use==
# File path to your Excel file containing class test scores
file_path = r'C:\Users\tkennedysutton\Documents\PythonProjects\Example_data.xlsx'

# The column in your Excel file that contains the scores (make sure it matches exactly)
column_name = 'Scores'

# Step 1: Import the data from Excel and convert it to tensor
pupil_scores_tensor = import_excel_column_to_tensor(file_path, column_name)

# Step 2: If import was successful, compute outliers
if pupil_scores_tensor is not None: 
    Outlier_detection(pupil_scores_tensor)
    print("Outliers detected")
