
# EireBnb

## Author

Ameen Noor

## Introduction
EireBnb, where you can find awesome places to stay in Ireland. Our website is tailored for users looking to explore Ireland and find the perfect stay for their unique preferences.
With EireBnb, users can easily browse through a variety of accommodations, each offering its own unique charm and amenities. Our website is designed to provide detailed information about each accommodation, helping you make an informed decision. Whether you're a solo traveler, a couple on a romantic getaway, or a family seeking adventure, EireBnb is your trusted companion in discovering and reserving accommodations that suit your needs.


![Am I Responsive](https://github.com/AmeenNoor/eire-bnb/blob/main/media/responsive/am-i-responsive.png)

Click [here](https://eire-bnb-01c201f35540.herokuapp.com/) to visit the website.

## Table of Contents

- [EireBnb](#eirebnb)
  - [Author](#author)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [Agile Process](#agile-process)
    - [Project Goals](#project-goals)
    - [Initial User Stories](#initial-user-stories)
    - [Agile Methodology](#agile-methodology)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Database Choice](#database-choice)
    - [Data Models](#data-models)
      - [Accommodation Data Model](#accommodation-data-model)
      - [Booking Data Model](#booking-data-model)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Frameworks, Tools, Libraries and Programs Used](#frameworks-tools-libraries-and-programs-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Compatibility and Responsive Testing](#compatibility-and-responsive-testing)
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


## Agile Process
### Project Goals
EireBnb, was developed with the following goals:

1. **Provide Accommodation Information:**
   - Let people check out and learn about different places to stay in Ireland.
   - They can see details like descriptions, prices, and what's available.

2. **Manage Bookings Easily:**
   - Help users book the places they like.
   - If someone signs up, they can easily see and change their bookings.

3. **Keep the Site Updated:**
   - Give site admins the tools to add new accommodations, update info, or remove old records.
   - Make sure everything on the site stays accurate and helpful.

4. **Make It Easy for Everyone:**
   - Design the website so it's easy for anyone to use.
   - Whether you're just looking or you're a member, it should be simple to find what you need.

5. **Keep Things Safe and Private:**
   - Make sure all user info is safe and secure.
   - If someone signs up, their personal details are kept private and secure.

### Initial User Stories

1. As a Site User I can browse through a list of accommodations so that I can explore various options

2. As a Site User I can view detailed information about each accommodation, including descriptions, images, and amenities

3. As a Site User I can book an available accommodation for specified dates

4. As a Site User I can view my booking history so that I can track past and upcoming reservations

5. As a Site User/ Admin I can cancel booking so that I can adjust plans

6. As a Site User I can update or modify existing booking details so that I can change dates or accommodations

7. As a Site User I can register for an account so that I can access booking features

8. As a Site User I can log in and out of my account so that I can ensure secure access

9. As a Site Admin I can view, add, edit, or remove accommodations so that I can manage and update accommodations

### Agile Methodology

An Agile methodology was employed in the creation of this application, ensuring a flexible and iterative approach to development. GitHub Projects was utilized to manage and track user stories, allowing for the prioritization and implementation of features based on their significance to the app's functionality and user experience. Three distinct categories, "Must Have", "Could I have" and "Should Have," were established to indicate the level of importance for each user story.

![Agile1](https://github.com/AmeenNoor/eire-bnb/blob/main/media/agile_process/agile-image1.png)

![Agile2](https://github.com/AmeenNoor/eire-bnb/blob/main/media/agile_process/agile-image2.png)

## User Experience (UX)

### Target Audience

EireBnb is for everyone who loves exploring Ireland! Families, couples, solo travelers, and business folks, no matter your age, we've got cozy places for you. If you like booking online and care about the environment, EireBnb is your go-to. Whether you're a tech fan, a local looking for new spots, or just love unique stays, we've made it easy for you to find the perfect place in Ireland.

### Design Choices
- #### Colors
   The website's color scheme uses soft and warm tones that make people feel calm and relaxed. There is also a bright color that adds excitement and passion to the design. White is used for the background and text, making everything look clean and simple, plus a deep blue color with a hint of purple, which looks nice. The colors were picked to make the website look good, go well together.
   
  ![colors](https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/design/colors.png)
  
- #### Typography
  The 'Rye' font was chosen for the logo part to give a nice appearance and clear visual. 'Nanum Myeongjo' was selected for its readability, ensuring clear body text.
  

### Wireframes
- #### Desktop

<img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/desktop-accommodations-page.png" alt="Desktop 1" width="270px" height="270px"> <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/desktop-home-page.png" alt="Desktop 2" width="270px" height="270px"> 
- #### Tablet

  <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/tablet-home-page.png" alt="Tablet 1" width="250"> &nbsp; <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/tablet-accommodations-page.png" alt="Tablet 2" width="250"> &nbsp; 
- #### Mobile

  <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/mobile-home-page.png" alt="Mobile 1" width="200"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://github.com/AmeenNoor/eire-bnb/blob/main/media/ux/wireframes/mobile-accommodations-page.png" alt="Mobile 2" width="200"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;


## Information Architecture
### Entity Relationship Diagram

![Entity Relationship Diagram](https://github.com/AmeenNoor/eire-bnb/blob/main/media/information_architecture/entity-relationship-diagram.png)

### Database Choice
PostgreSQL was chosen as the database for its relational data structure. This choice aligns with the project's needs, where accommodations and bookings involve complex relationships. Additionally, deploying on Heroku. Choosing PostgreSQL on Heroku was a smart move because it helps us have a reliable and scalable database.

### Data Models
#### Accommodation Data Model
**Accommodation Model:**
The Accommodation model represents different types of places available for booking.

**Fields:**

- **id** (Primary Key, Integer): Unique identifier for each accommodation.
- **name** (String): Name of the accommodation.
- **description** (Text): Description of the accommodation.
- **address** (String): Address of the accommodation.
- **city** (String): City where the accommodation is located.
- **country** (String): Country where the accommodation is located.
- **price_per_night** (Decimal): Cost per night for the accommodation.
- **capacity** (Integer): Maximum number of guests the accommodation can accommodate.
- **accommodation_type** (String): Type of accommodation (e.g., Flat, Room, Apartment).
- **accommodation_image** (Cloudinary Image): Image of the accommodation.

**Validation:**

- **name:** Required, minimum 1 character, maximum 100 characters.
- **price:** Required, decimal format.

**CRUD Operations:**

- **Create:** Accommodations are created when a user adds a new place for booking.
- **Read:** Accommodations are read when users browse available places, view details, or make bookings.
- **Update:** Accommodations are updated when a user modifies details like price, capacity, or accommodation type.

#### Booking Data Model
**Booking Model:**
The Booking model represents reservations made by users for specific accommodations.

**Fields:**

- **id** (Primary Key, Integer): Unique identifier for each booking.
- **first_name** (String): First name of the person making the booking.
- **last_name** (String): Last name of the person making the booking.
- **phone_number** (String): Phone number of the person making the booking.
- **email** (Email): Email of the person making the booking.
- **check_in_date** (Date): Date when the guests will check-in.
- **check_out_date** (Date): Date when the guests will check-out.
- **booking_date** (DateTime): Date and time when the booking was made.
- **user** (Foreign Key to User): Reference to the user making the booking.
- **accommodation** (Foreign Key to Accommodation): Reference to the booked accommodation.

**Validation:**

- **first_name, last_name:** Required, minimum 1 character, maximum 50 characters.
- **phone_number:** Required, string format.
- **email:** Required, valid email format.
- **number_of_guests:** Required, integer format.
- **check_in_date, check_out_date:** Required, date format.

**CRUD Operations:**

- **Create:** Bookings are created when a user reserves an accommodation.
- **Read:** Bookings are read when users view their booking history or details of a specific booking.
- **Update:** Bookings can be updated if the user wants to modify the check-in/out dates or the number of guests.
- **Delete:** Bookings can be canceled, resulting in a deletion of the booking record.


## Features
### Implemented Features

1. Responsive Design: The website is designed to be responsive, adapting to different screen sizes and providing an optimal viewing experience on various devices, from desktops to mobile devices.
   
2. Navigation: The header includes navigation links for easy access to different sections of the website. The navigation is designed to be user-friendly and visually appealing.
   
3. Accommodation Listings: The main content area displays a list of accommodations, each represented as a card. Accommodations include an image, name, price, and city for quick reference. Users can click on "More Details" to view additional information about each accommodation.

4. Booking Functionality: Users have the option to book accommodations directly from the listing by clicking on the "Book" button. The website likely includes functionality to handle booking requests, capturing user details, and managing reservations.

5. Accommodation Detail Page: There is a dedicated page for detailed information about a specific accommodation, including a larger image and additional details. The layout is designed to provide a comprehensive view of the accommodation details.
   
6. Dropdown Navigation: The header includes a dropdown navigation feature, enhancing the user experience by organizing related links under a single dropdown button.

7. 404 and 500 Error Pages: Custom 404 and 500 error pages have been implemented to gracefully handle situations where users encounter page-not-found or server errors.

### Future Features

1. User Reviews and Ratings: Allow users to leave reviews and ratings for accommodations they have booked.
   
2. Advanced Search and Filtering: Allow users to filter accommodations based on specific criteria such as price range, amenities, and location.

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

8. [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/):
   Bootstrap was utilized for the styling and layout of the website.

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

- 1. **CSS:**
    Validation testing was performed using Jigsaw to ensure code quality. Here is the validation testing results:
    
    ![CSS Test](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/css/css-test.png)  
    
- 2. **Python**
    Validation testing was performed using CI's PEP8 tool to ensure code quality. Here are the validation testing results for each file:
**accommodation app:**
1. #### admin.py

![Admin](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/python/admin.png)  

1. #### apps.py
  
![Apps](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/python/apps.png)  

1. #### models.py

![Models](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/python/models.png)  

1. #### urls.py

![Urls](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/python/urls.png)  

1. #### views.py

![Views](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/validation_testing/python/views.png)

### Compatibility and Responsive Testing
The website was tested on various browsers and devices to ensure compatibility and optimal user experience. The testing process yielded successful results for most browsers and devices. See table and screenshots below:

<div align="center">

| Device                    | Browser         | OS       | Screen Width | Status |
| ------------------------- | --------------- | -------- | ------------ | ------ |
| dev tools: iPhone SE      | Chrome          | iOS      | 375 x 667    | ✔      |
| dev tools: iPhone 12      | Chrome          | iOS      | 390 x 844    | ✔      |
| dev tools: iPad Air       | Chrome          | iOS      | 820 x 1180   | ✔      |
| dev tools: Galaxy S8      | Chrome          | Android  | 362 x 740    | ✔      |
| real computer: Toshiba    | Microsoft Edge  | Windows 10 | 1366 x 768  | ✔      |
| real computer: Toshiba    | Firefox         | Ubuntu 22.04 | 1920 x 1080 | ✔      |
| real computer: MacBook Pro 13" | Safari    | iOS      | 1920 x 1080  |  ✔     |
| real mobile phone: iPhone 7 Plus | Safari    | iOS      | 1920 x 1080  |  ✔     |

</div>

### Manual Testing
View manual testing results [here!](https://docs.google.com/spreadsheets/d/1ZbcYyAvHtrs21mm9MX5rQsxUZEM0ATxkRj6NU_ZPbKE/edit#gid=0)

![Manual Testing Image](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/manual_testing/manual-testing.png)

### Fixing Bugs
- #### Validation Bug
  **Python**
  1. **urls.py**:
  Indentation issues in the 'urls.py' file have been fixed.

  ![Urls Fixed](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/fixing_bugs/python/urls-fixed.png)

  2. **views.py**:
  Indentation issues in the 'views.py' file have been fixed.

  ![Views Fixed](https://github.com/AmeenNoor/eire-bnb/blob/main/media/testing/fixing_bugs/python/views-fixed.png)

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

1. The GitHub repository was created using the "Code Institute template." You can find the template at: [Code Institute Template](https://github.com/Code-Institute-Org/ci-full-template).

2. The carousel/slideshow code in use has been adapted by [W3Schools](https://www.w3schools.com/bootstrap5/tryit.asp?filename=trybs_carousel2).

### Content

1. The content in the accommodation description has been adapted and rephrased from [daft](https://www.daft.ie/)
   
### Media

1. The responsive image is generated using the [Am I Responsive](https://ui.dev/amiresponsive) tool.
   
2. The color scheme image is sourced from [Coolors](https://coolors.co/).

3. The social media icons are sourced from [FontAwesome](https://fontawesome.com/).

4. The fonts 'Rye' and 'Nanum Myeongjo' are sourced from [Google Fonts](https://fonts.google.com/).
   
5. Accommodation images are sourced from [Unsplash](https://unsplash.com/)
   
### Mentor
Huge thanks to my mentor "Malia Havlicek" for her support and guidance.
