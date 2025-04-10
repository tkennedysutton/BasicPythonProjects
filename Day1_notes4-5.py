#Function: A function is a reusable block of code that can perform a specific task, and you can call it whenever needed in your program.
def coffee_bean_quality(flavour_level,strength):    #function definition - has two parameters - these are placeholders that hold values when calling the function
    return flavour_level*strength                   #function body - calculates the quality of the bean         
print(coffee_bean_quality(2,4))                     #calling the function - passing 3 for flavor_level and 2 for cone_thickness
#Arguments and Parameters. In Python, not all functions need to return a value. Functions can perform actions like printing, modifying global variables, or even interacting with files, databases, or other systems. 
def greet(name):  # 'name' is the parameter
    print(f"Hello, {name}!")
greet("Tristan")  # "Tristan" is the argument   
# ML world 
def compute_accuracy(preds, labels):
    if len(preds) != len(labels):       #preds is the parameter for the predicted values (e.g., the output of a machine learning model), labels is the parameter for the true labels (e.g., the actual correct answers for a given dataset).
        raise ValueError("Length of predictions does not match length of labels")
    
    correct = 0                             # variable to count number of correct predictions, set 0 as none counted yet
    for p, l in zip(preds, labels):         #loop where: “For each pair of prediction and label, assign the first one to p and the second one to l.”
        if p == l:                          #where p is equal to l ie 1 from [1,0,1] corresponds with [1,1,1] on two itterances, so correct (variable) increases by 1 twice
            correct += 1
    return correct / len(labels)            #function body - do this calculation

print(compute_accuracy([1, 0, 1,1,1,0], [1, 1, 1,0,1,1]))  # passing [1,0,1] for preds, [1,1,1] for labels (these are lists, but look same shape as tensors)
#Because the zip() function automatically stops at the shortest list. It just quietly ignores any extra elements in the longer list.

#List, tuples. dictionaries
#List: Tristan's daily routine
daily_routine = ["make coffee","stretch","fingerboard","clean teeth","wash face"] #list goes into [] - List: A list is mutable, meaning you can modify its elements after creation (add, remove, or change items

#Tuples: Tristan's favourite clmbing gym location
Best_climbing_gym = (53.46451191950969, -2.3205421213377657) #tuple is in brackets - Tuple: A tuple is immutable, meaning once it's created, you cannot modify its elements. You can't change, add, or remove elements from a tuple

#dictionaries
Tristan_stats = {
    "strength level":7,
    "Climbing ability":5,
    "Plant growing competency":6,
    "Coffee addiction":10
    }
if  Tristan_stats["strength level"] >8:
    print("Tristan's strength level:", Tristan_stats["strength level"])
else:
    print("too weak")
#ML context
# List: Pupil feature values (e.g., scores in different subjects)
features = [0.85, 0.76, 0.92]

# Tuple: Fixed input dimensions for images of pupil assignments (channels, height, width)
input_shape = (3, 64, 64)

# Dictionary: Metrics from a model evaluating pupil performance
metrics = {"accuracy": 0.88, "loss": 0.25}
print("Model Accuracy:", metrics["accuracy"])