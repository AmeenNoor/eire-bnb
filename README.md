

* Run pip show django-allauth in your terminal. Your output should look like the image below.
The Location value is the information we are interested in.
We need to replace the file path shown in the video ../.pip-modules/lib/python3.7/site-packages with the new file path provided by running the previous command.
The result should looking like the example below, and running it should successfully copy the AllAuth templates.
Example: cp -r /workspace/.pyenv_mirror/user/current/lib/python3.11/site-packages/allauth/templates/* ./templates/allauth/ (edited)
Remember => DISABLE_COLLECTSTATIC (HEROKU)
# EireBnb

## Author

Ameen Noor

## Introduction
EireBnb, where you can find awesome places to stay in Ireland. Our website is tailored for users looking to explore Ireland and find the perfect stay for their unique preferences.
With EireBnb, users can easily browse through a variety of accommodations, each offering its own unique charm and amenities. Our website is designed to provide detailed information about each accommodation, helping you make an informed decision. Whether you're a solo traveler, a couple on a romantic getaway, or a family seeking adventure, EireBnb is your trusted companion in discovering and reserving accommodations that suit your needs.


![Am I Responsive](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/responsive/am-i-responsive.png)

Click [here](https://worldscape-adventure-6f50d85fec22.herokuapp.com/) to visit the website.

## Table of Contents

- [EireBnb](#eirebnb)
  - [Author](#author)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User storis](#user-storis)
    - [Design](#design)
      - [Flow Chart](#flow-chart)
    - [Wireframes](#wireframes)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Data Model/ Classes](#data-model-classes)
    - [Worldscape](#worldscape)
    - [Main Program](#main-program)
    - [Data Flow](#data-flow)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Tools, Libraries and Programs Used](#frameworks-tools-libraries-and-programs-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Manual Testing](#manual-testing)
    - [Fixing Bugs](#fixing-bugs)
  - [Deployment](#deployment)
    - [Local deployment](#local-deployment)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Code](#code)
    - [Content](#content)
    - [Media](#media)
    - [Mentor](#mentor)


## User Experience (UX)

### Target Audience

EireBnb is for everyone who loves exploring Ireland! Families, couples, solo travelers, and business folks, no matter your age, we've got cozy places for you. If you like booking online and care about the environment, EireBnb is your go-to. Whether you're a tech fan, a local looking for new spots, or just love unique stays, we've made it easy for you to find the perfect place in Ireland.

### User storis

1. As a Site User I can browse through a list of accommodations so that I can explore various options

2. As a Site User I can view detailed information about each accommodation, including descriptions, images, and amenities

3. As a Site User I can book an available accommodation for specified dates

4. As a Site User I can view my booking history so that I can track past and upcoming reservations

5. As a Site User/ Admin I can cancel booking so that I can adjust plans
   
6. As a Site User I can update or modify existing booking details so that I can change dates or accommodations

7. As a Site User I can register for an account so that I can access booking features

8. As a Site User I can log in and out of my account so that I can ensure secure access
   
9. As a Site Admin I can view, add, edit, or remove accommodations so that I can manage and update accommodations


### Design
#### Flow Chart


![Flow Chart](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/flowchart/flow-chart.png)


### Wireframes
- #### Desktop

<img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/desktop-accommodations-page.png" alt="Desktop 1" width="270px" height="270px"> <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/desktop-home-page.png" alt="Desktop 2" width="270px" height="270px"> 
- #### Tablet

  <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/tablet-home-page.png" alt="Tablet 1" width="250"> &nbsp; <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/tablet-accommodations-page.png" alt="Tablet 2" width="250"> &nbsp; 
- #### Mobile

  <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/mobile-home-page.png" alt="Mobile 1" width="200"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/mobile-accommodations-page.png" alt="Mobile 2" width="200"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

## Features
### Implemented Features

1. Main Menu Navigation: The main menu provides clear options for the user, including "How to Play," "Play Game," "Game Statistics," and "Exit," ensuring easy navigation and interaction.

![Feature1](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature1.png)

2. Game Instructions ("How to Play"): Users can access game instructions, allowing them to quickly understand the game's rules.

![Feature2](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature2.png)

3. Game Category Selection: Players can choose from three categories - countries, cities, or landmarks 

![Feature3](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature3.png)

4. Interactive Gameplay: During the game, users interact by guessing letters one at a time, with feedback. Correct guesses reveal hidden letters, while incorrect ones deduct lives.

![Feature4](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature4.png)

5. Progress Tracking ("Game Statistics"): The "Game Statistics" option allows users to track their progress effortlessly, displaying the number of games played, games won, and games lost.

![Feature5](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature5.png)

6. Exit Option: Users can exit the game by selecting "Exit" from the main menu.

![Feature6](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature6.png)

8. Colorful Notifications: The game provides interactive feedback and colorful notifications.

![Feature7A](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-a.png)

![Feature7B](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-b.png)

![Feature7C](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-c.png)

![Feature7D](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-d.png)

![Feature7E](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-e.png)

![Feature7F](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/features/feature7-f.png)


### Future Features

1. **High Score Tracking**: Implement a feature to ask the user for their name and record all game statistics in an Excel file, allowing players to view high scores and compete for the top spot.

2. **Difficulty Levels**: Add the option for players to choose between different difficulty levels, such as easy and difficult.

3. **Dynamic Word Generation**: Instead of using a constant list of words, connect to an API for word generation, to ensure every game is an exciting adventure.

## Data Model/ Classes
### Worldscape

The Worldscape class represents a word-guessing game environment, allowing players to guess letters to unveil a secret word, track their progress, and manage their remaining lives.

**Attributes:**

1. **name_list**: A list of names (countries, cities, landmarks) from which the secret name will be randomly selected.

2. **secret_name**: The current secret name that the player needs to guess.

3. **encoded_name**: The secret name encoded with dashes, where each letter is initially hidden.

4. **letters_used**: A list of letters that the player has already guessed.

5. **lives**: The number of remaining lives the player has.

**Functions:**

1. **__init__(self, name_list)**: Constructor method to initialize class attributes.
    - **name_list**: The list of names provided as an argument.
    - **Initializes** secret_name and encoded_named as empty strings.
    - **Initializes** letters_used as an empty list.
    - **Initializes** lives to 8.

2. **generate_secret_name(self)**: Randomly selects a secret name from the provided **name_list**.
    - Returns the generated **secret name**.

4. **encode_name(self)**: Encodes the secret name by replacing its characters with dashes.
    - If the country name contains spaces, spaces are displayed as spaces, and other letters are displayed as dashes.
    - Returns the **encoded name**.

5. **is_letter_valid(self, input_letter)**: Validates whether the given input letter is a single alphabetical character.
    - Returns **True** if the input is valid, **False** otherwise.

6. **is_letter_in_name(self, letter)**: Determines whether a given letter is present in the secret name.
    - Returns **True** if the letter is in the name, **False** otherwise.

7. **add_used_letter(self, letter)**: Takes a letter entered by the user and adds it to the letters_used list.
    - Returns the updated list of **used letters**.

8. **is_letter_used_before(self, letter)**: Checks whether a letter has been previously entered by the user.
    - Returns **True** if the letter has been used before, **False** otherwise.

9. **replace_encoded_name_with_guessed_letter(self, letter)**: Replaces dashes in the encoded name with the correct guessed letter.
    - Returns the updated **encoded name**.

10. **display_output(self, name)**: Displays game information to the user, including the number of remaining lives, the guessed letters and dashes in the secret name, and the list of letters that have been used before.

### Main Program

The main program consists of different functions.

**Functions**:

1. **clear_terminal()**: Clears the terminal screen based on the operating system (Windows or Mac/Linux).

2. **display_statistics()**: Displays statistics related to the user's gameplay, including the number of games played, games won, and games lost.

3. **update_game_statistics(is_won)**: Increments the total games played and either the total games won or the total games lost based on the outcome of the game.

4. **display_how_to_play()**: Provides instructions on how to play the game.

5. **play_game(name_list, name)**: Allowing the player to guess letters and attempt to uncover the secret name.

6. **main()**: Allowing users to navigate through the game menu, select game options, and play the game.

### Data Flow

- The **Worldscape** class handles game-specific data, such as the secret name, lives, and encoded name.

- The **main program** manages user interaction, displays menus, and calls the appropriate functions of the Worldscape class based on user input.

## Technologies Used
### Languages Used

1. HTML
2. CSS
3. Python
   
### Frameworks, Tools, Libraries and Programs Used

1. [Heroku](https://www.heroku.com/):
   Heroku was employed for project deployment.

2. [GitHub](https://github.com/):
   GitHub was utilized to store the project file and folder remotely.

3. [Git](https://git-scm.com/):
   Git was used in the Gitpod terminal to add, commit, and then push the changes to GitHub.

4. [CI's pep8 tool](https://pep8ci.herokuapp.com/):
   CI's pep8 tool was used to ensure the code is valid and follows proper indentation

5. [draw.io](https://app.diagrams.net/):
   draw.io was used to craft the flowchart

6. [Font Awesome](https://fontawesome.com/):
   Font Awesome was used to incorporate social media and contact information icons, including icons for Facebook, Twitter, Youtube, Instagram, email and address.
   
7. [Google Fonts](https://fonts.google.com/):
   Google fonts were used to import 'nanum myeongjo' & 'Rye' fonts into the style.css file which are used on all pages throughout the project.

8. [HTML Validator](https://validator.w3.org/):
   The HTML code of the website was tested using the HTML Validator that provided by The World Wide Web Consortium (W3C).

9. [Jigsaw](https://jigsaw.w3.org/css-validator/):
   The CSS code of the website was tested using Jigsaw that provided by The World Wide Web Consortium (W3C).

10. [Balsamiq](https://balsamiq.com/):
   Balsamiq was used to create the mockup design for the website.

11. [Django](https://www.djangoproject.com/):
    Django was used to develop the backend, handling dynamic pages, URL routing, and database management.
    
12. [Cloudinary](https://cloudinary.com/):
    Cloudinary used to host all images.
    
13. [ElephantSQL](https://www.elephantsql.com/):
    ElephantSQL Was used to host the PostgreSQL database.




## Testing
### Validation Testing

Validation testing was performed using CI's PEP8 tool to ensure code quality. Here are the validation testing results for each file:

1. #### worldscape.py

![Worldscape](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/worldscape-validation-testing.png)  

2. #### names.py
  
![Names List](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-validation-testing.png)  

3. #### run.py

![Main Program](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/run-validation-testing.png)  

### Manual Testing
View manual testing results [here!](https://docs.google.com/spreadsheets/d/1C0XAiSfxOVXIjn1UhXu-7vf35j0WS67IYKl_2fVBWd0/edit#gid=0)

![Manual Testing Image](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/manual-testing.png)

### Fixing Bugs
- #### Validation Bug
  
  1. **worldscape.py**:
  Indentation issues in the 'worldscape.py' file have been fixed.

  ![Worldscape Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/worldscape-fixed.png)

  2. **names.py**:
  Indentation issues in the 'names.py' file have been fixed.

  ![Names Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/names-fixed.png) 
  
  3. **run.py**:
  Indentation issues in the 'run.py' file have been fixed.

  ![Run Fixed](https://github.com/AmeenNoor/worldscape-adventure/blob/main/assets/testing/run-fixed.png)

## Deployment
### Local deployment
To deploy the site using Visual Studio Code, follow these steps:

1. **Clone the Repository:**
    * Open VS Code.
    * Use the command palette and run "Git: Clone".
    * Enter the GitHub repository URL and choose a local directory.
    * Open the cloned project in VS Code.

2. **Install Dependencies:**
    * Navigate to the project directory in the terminal & run the following:
    **pip3 install -r requirements.txt**

3. **Set Environment Variables:**
    * Create a .env file in the project root.
    * Copy the contents of env.py into the .env file.

4. **Apply Migrations:**
    * Run the following commands to apply migrations:
    **python3 manage.py migrate**

5. **Create Superuser :**
    * Create an admin superuser for accessing the Django admin panel:
    **python3 manage.py createsuperuser**

6. **Run the Server:**
    * Start the Django server:
    **python3 manage.py runserver**

### Heroku

To deploy the site on Heroku, follow these steps:

1. Begin by forking the repository: <https://github.com/AmeenNoor/eire-bnb.git>.

2. Log in to Heroku and click "New." Select "Create new app."(see screenshots below):

![Deployment_1](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image1.png)

3. Choose a unique name for your app, select your desired region, and then click "Create app." (see screenshot below):

![Deployment_2](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image2.png)

1. In the app settings, navigate to the "Config Vars" section. Set the environment variables directly on Heroku (see screenshots below):

![Deployment_3](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image3.png)

![Deployment_4](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image4.png)

![Deployment_5](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image5.png)

1. Under the "Buildpacks" section, click "Add buildpacks." Add "python" as buildpacks. Ensure that Python is selected first, followed by Node.js. Save your selections. (see screenshots below):

![Deployment_6](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image6.png)

![Deployment_7](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image7.png)

1. In the "Deploy" section, choose "GitHub/Connect to GitHub" as your deployment method. Search for the project on GitHub and connect it. (see screenshots below):

![Deployment_8](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image8.png)

![Deployment_9](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image9.png)

![Deployment_10](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image10.png)

1. Finally, click "Deploy Branch" to deploy your project. (see screenshot below):

![Deployment_11](https://github.com/AmeenNoor/eire-bnb/blob/main/media/deployment/deployment-image11.png)

## Credits
### Code

1. The GitHub repository was created using the "Code Institute template." You can find the template at: [Code Institute Template](https://github.com/Code-Institute-Org/p3-template).

2. The logic for **clear_terminal()** function was adopted from [How to clear screen in python?](https://www.geeksforgeeks.org/clear-screen-python/).

### Content

1. **List of Countries:** obtained from [Worldometers](https://www.worldometers.info/).

2. **List of Cities:** obtained from [World Maps](https://ontheworldmap.com/all/cities/).

3. **List of Landmarks:** obtained from [Destguides](https://www.destguides.com/famous-landmarks).
   
### Media

3. The responsive image is generated using the [Am I Responsive](https://ui.dev/amiresponsive) tool.


### Mentor
Huge thanks to my mentor "Malia Havlicek" for her support and guidance.
