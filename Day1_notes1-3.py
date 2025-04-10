#Variables
name = "Tristan"                        #string
Steaks_eaten = 9                      #int - whole number
time_to_run_to_coffee_machine = 6.234   #float - can have decimals
Currently_has_coffee = False            #bool - true or false values
weather = "Sunny"

# Variables for ML world
# String: used for labels, file paths, or column names
dataset_name = "CIFAR-10"  # name of a dataset

# Integer: counts, indices, epochs
batch_size = 32  # number of samples processed at once

# Float: values with decimals — common in ML for loss, accuracy, etc.
learning_rate = 0.001  # controls step size during training

# Boolean: True/False conditions — used in flags or conditional logic
use_gpu = True  # whether to use CUDA if available


#If Statements
if weather == "Sunny":            # == used to compare values in python
    print("Go for a coffee outside","It will require you",time_to_run_to_coffee_machine,"to get to the coffee machine") #can have multiple things printed
elif weather == "rainy":
    print("have your coffee inside","It will require you",time_to_run_to_coffee_machine,"to get to the coffee machine")
else:
    print("eat some steaks, you have currently eaten", Steaks_eaten,"steaks")

#in ML world
accuracy = 0.72

if accuracy > 0.9:
    print("Excellent model!")
elif accuracy > 0.75:
    print("Pretty good.")
else:
    print("Needs improvement.")

#additional ML world if statements
if use_gpu:
    print("Running model on GPU")  # runs this if use_gpu is True
else:
    print("Running model on CPU")  # fallback if use_gpu is False

accuracy = 0.85

if accuracy >= 0.90:
    print("Excellent performance")
elif accuracy >= 0.75:
    print("Good performance")
else:
    print("Needs improvement")

# Loops
#Tristan looping through coffee shops that have a coffee machine
areas = ["Rico's Coffee","paz coffee","columbian supreme coffee"]       #creates a list of coffee shops
for area in areas:                                                      #This is a for loop, which is used to iterate over each item in the areas list
    print(f"Tristan explores for a decent coffee shop {area}")          #this prints a message for each area in the list, the f before the string so python substitues the value of area inside the {}

energy = 5                                                              #variable
while energy > 0:                                                       #This is a while loop. The loop will continue to run as long as the condition energy > 0 is true.
    print(f"Energy left: {energy}")
    energy -= 1     
    if energy < 2:
        print("Energy running low")                                                    #This is a shorthand for energy = energy - 1, which decreases the energy by 1 each time the loop runs.
print("energy depleted")
#ML context
loss = 1.0  # Initialize loss (variable) with a value of 1.0

while loss > 0.1:  # Continue the loop as long as loss is greater than 0.1
    print(f"Loss: {loss}")  # Print the current value of loss
    loss *= 0.5  # Multiply loss by 0.5, reducing its value by half - *= operator is used to multiply variable by a factor (0.5 here)
    if loss <0.5:
        print("getting worse")
