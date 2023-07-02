# Django-School
Django-School is a web-based application built using the Django framework to automate school processes. It provides features for managing teachers, students, classes, and other related entities.

## Installation
To install and run the Django-School project, follow these steps:

1. Clone the project repository from GitHub:
   
   ```
   git clone https://github.com/VastaGit/Django-School
   ```
2. Navigate to the project directory:
  
   ```
   cd Django-School
   ```

3. Create a virtual environment to isolate the project dependencies:
  
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:

    On Windows:
  
   ```
   venv\Scripts\activate
   ```

    On macOS and Linux:
   
   ```
   source venv/bin/activate
   ```

5. Install the project dependencies:
  
   ```
   pip install -r requirements.txt
   ```

6. Create a PostgreSQL database for the project.

7. Configure the database settings in the settings.py file located in the School directory

   ```
       DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_database_name',
            'USER': 'your_database_username',
            'PASSWORD': 'your_database_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
   ```

8. Apply the database migrations to create the necessary tables:

   ```
    python manage.py makemigrations
    python manage.py migrate
   ```

9. Start the development server:
    
   ```
    python manage.py runserver
   ```

10. Access the Django-School application in your web browser at http://localhost:8000.

## Features

Django-School provides the following features:

- [x] Registration of teachers through the website.
- [x] Teacher authentication with phone number and password.
- [x] CRUD operations for managing students.
- [x] Email notifications sent to students upon creation.
- [x] Search functionality to find students by their names.
- [x] Mass email sending to selected students.
- [x] PostgreSQL database as the backend.

## Usage

### Teacher Registration

1. Access the registration page by navigating to http://localhost:8000/register.

2. Fill in the required fields, including subject, phone number, and password.

3. Click the "Register" button to create a new teacher account.

![image](https://github.com/VastaGit/Django-School/assets/88315984/be746cf2-8130-4c3a-a5d9-13f97391e63d)

### Teacher Login
1. Access the login page by navigating to http://localhost:8000/login.

2. Enter the phone number and password of the teacher account.

3. Click the "Login" button to authenticate and access the teacher dashboard.

![image](https://github.com/VastaGit/Django-School/assets/88315984/2ad61284-0038-4c1f-93ff-0bbd6cdd35cd)

### Managing Students
1. After logging in as a teacher, you can perform CRUD operations on students.

2. Navigate to the appropriate section of the website to view, add, edit, or delete students.

![image](https://github.com/VastaGit/Django-School/assets/88315984/eba4c399-5781-4a12-bc63-47f85ddeda4e)

### Email Notifications
1. Upon creating a student, an email notification is automatically sent to the student's email address.

2. Teachers can also send mass emails to selected students by using the admin actions which provides email form.
   
![image](https://github.com/VastaGit/Django-School/assets/88315984/b6677022-e1ed-49c7-aa0d-e0278742d37d)

![image](https://github.com/VastaGit/Django-School/assets/88315984/847f67ac-d3c8-4fe4-b0bf-a3ce73f114eb)

3. To enable email sending, ensure that the email password is set in the secret_key.py file. The file is not pushed to the Git repository for security reasons. The gmail password could be found in your Google settings, if not, you can create it immediately there:

 - Go to your Google Account and choose Security on the left panel.
 - On the Signing in to Google tab, select App Passwords.
 
   If you don’t see this option, it might mean that:

   - Two-step verification is not set up for your Google account.
   - Two-step verification is set up for security keys only.
   - Your account is used through work, school, or another organization.
   - You’ve turned on Advanced Protection for your account.
   
 - Click on Select app and pick the app you’re using. 
 - Click Select device and choose the device you’re using.
 - Click on Generate.
 - Follow the instructions to enter the App Password.
 - Click on Done.
   
### Contributions
Contributions to the Django-School project are welcome. If you encounter any issues or have suggestions for improvement, please create a new issue on the project's GitHub repository.

### Additional Notes
1. The virtual environment (myworld) directory has been added to the git repository, make sure to delete it after git clone.

2. The secret_key.py file, which contains sensitive information, has been excluded from version control.
