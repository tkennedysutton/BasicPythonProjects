from pptx import Presentation

# Create a presentation object
presentation = Presentation()

# Set slide size to widescreen (16:9) using preset values in the pptx library
# 13 inches width and 7.5 inches height in inches
width_inch = 13  # Width for 16:9
height_inch = 7.5  # Height for 16:9
EMU_conversion = 914400  # 1 inch = 914400 EMUs

# Convert inches to EMUs and ensure values are integers
presentation.slide_width = int(width_inch * EMU_conversion)  # Convert to EMUs and make sure it's an integer
presentation.slide_height = int(height_inch * EMU_conversion)  # Convert to EMUs and make sure it's an integer

# Gather information to fill slides
include_title_slide = input("Do you want a title slide? (yes/no): ").strip().lower()
if include_title_slide == "yes":
    presentation_title = input("Enter the overall title for your presentation (Eg. Welcome to My Quiz): ")
    num_slides = int(input("How many content slides do you want?:\n"))  # No +1 here; title slide is separate
else:
    num_slides = int(input("How many content slides do you want?"))

# Create a dictionary to store input user data from terminal
slides_content = {}

# Initialize loop to collect user input data
for i in range(1, num_slides + 1):  # Loop through number of slides user wants to create
    slide_key = f"slide {i}"  # Create a key for each slide
    print(f"\n ---{slide_key}---")  # Displays which slide is being worked on
    slide_title = input("Enter title slide for this slide:\n")  # Ask user for the title on the slide

    numbers = []  # Initialize empty list to gather input from user for each question
    while True:  # Start loop to gather input for questions until user writes 'done'
        question = input("Write your question (or leave blank and press enter if done):\n")  # Gather question input
        if question == "":  # If user leaves blank
            break  # Loop ends
        numbers.append(question)  # Add question to the list

    # Store the slide's title and questions in the dictionary
    slides_content[slide_key] = {
        "Title": slide_title,
        "Questions": numbers  # Fixed from "Question" to "Questions"
    }

# Create the title slide (if requested)
if include_title_slide == "yes":
    title_layout_slide = presentation.slide_layouts[0]  # Title slide layout
    title_slide = presentation.slides.add_slide(title_layout_slide)
    title_slide.shapes.title.text = presentation_title

# Create Question slide(s)
question_slide_layout = presentation.slide_layouts[1]  # Title and Content Layout

for slide_data in slides_content.values():
    slide = presentation.slides.add_slide(question_slide_layout)  # Add a content slide
    slide.shapes.title.text = slide_data["Title"]  # Set slide title

    content = slide.placeholders[1]  # Access content placeholder

    if slide_data["Questions"]:  # If there are questions, add them
        content.text = slide_data["Questions"][0]  # Add the first question directly

        # Add the rest of the questions as numbered paragraphs
        for question in slide_data["Questions"][1:]:
            paragraph = content.text_frame.add_paragraph()
            paragraph.text = question
            paragraph.level = 0  # Main bullet level

        # Set numbering style
        for paragraph in content.text_frame.paragraphs:
            paragraph.level = 0  # Top-level bullet
            paragraph.numbered = True  # Set numbering

# Save the presentation
presentation.save("Quiz_Presentation.pptx")
print("Presentation saved as 'Quiz_Presentation.pptx'")
