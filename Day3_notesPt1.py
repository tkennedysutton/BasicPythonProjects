# Import the library
from pptx import Presentation  # Importing the pptx library to work with PowerPoint presentations

# Step 1: Initialize the Presentation
presentation = Presentation()  # Create a new presentation object

# Step 2: Gather user input for presentation details
presentation_title = input("Enter the overall title for your presentation: ")  # Ask user for the title of the presentation from the terminal
num_slides = int(input("How many content slides would you like to create? "))  # Ask how many slides they want, again from the terminal

# Step 3: Store slide details in a structured dictionary
slides_content = {}  # Initialize an empty dictionary to store slide details

for i in range(1, num_slides + 1):  # Loop through the number of slides user wants to create
    slide_key = f"Slide {i}"  # Create a key for each slide (e.g., Slide 1, Slide 2)
    print(f"\n--- {slide_key} ---")  # Display which slide is being worked on
    slide_title = input("Enter the title for this slide: ")  # Ask user for the slide's title

    bullets = []  # Initialize an empty list to store bullet points for the slide
    while True:  # Start a loop to gather bullet points until user types 'done'
        bullet_point = input("Enter a bullet point (or type 'done' to finish): ")  # Ask for bullet point
        if bullet_point.lower() == 'done':  # If user types 'done', stop gathering bullet points
            break
        elif bullet_point.strip() == '':  # If bullet point is empty, prompt for valid input
            print("Please enter a valid bullet point.")
            continue  # Continue asking for a valid bullet point
        bullets.append(bullet_point)  # Add bullet point to the list

    # Store the slide's title and bullet points in the dictionary
    slides_content[slide_key] = {
        "title": slide_title,
        "bullets": bullets
    }

# Step 4: Create title slide
title_slide_layout = presentation.slide_layouts[0]  # Title Slide Layout (first layout option)
title_slide = presentation.slides.add_slide(title_slide_layout)  # Add a slide with this layout
title_slide.shapes.title.text = presentation_title  # Set the title of the slide to the user-defined title
title_slide.placeholders[1].text = "Generated with python-pptx"  # Add a subtitle with text

# Step 5: Generate content slides
bullet_slide_layout = presentation.slide_layouts[1]  # Title and Content Layout (second layout option)

for slide_data in slides_content.values():  # Loop through each slide's data
    slide = presentation.slides.add_slide(bullet_slide_layout)  # Add a slide with the bullet point layout
    slide.shapes.title.text = slide_data["title"]  # Set the slide's title based on user input

    content = slide.placeholders[1]  # Access the placeholder for content (where bullet points go)
    for bullet in slide_data["bullets"]:  # Loop through the bullet points for the current slide
        content.text += f'\n{bullet}'  # Add each bullet point to the content, separated by new lines

# Step 6: Save the presentation
file_name = input("\nEnter a name for your PowerPoint file (without extension): ")  # Ask user for the filename
presentation.save(f"{file_name}.pptx")  # Save the presentation as a .pptx file with the user-specified name

print(f"\n✅ Presentation '{file_name}.pptx' has been created successfully!")  # Notify user that the presentation is ready
