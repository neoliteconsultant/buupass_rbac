### About
A Django Role based Access Control API.


### Prerequisites
Before running the application, ensure you have installed and configured
the following tools

- Pip v20.0.0 or later
- Python v3.8.0 or later
- Postman v6.7.4 or later


### Installation
1. Navigate to the root directory (buupass_rbac) containing the manage.py file in a command line.

2. Install dependencies

      ```
       $ pip install -r requirements.txt
      ```

3.  Create the migrations (generate the SQL commands).

      ```
       $ python manage.py makemigrations
      ```

 
4. Run the migrate command in a shell to create the database tables automatically.
      ```
       $ python manage.py migrate 
      ``` 
   
   
5. Execute the runserver command in a shell to start the development server.This will enable you to access
   the web application in a browser.

      ```
        $ python manage.py runserver
      ```
   
6. Copy the following url in a browser
   
   http://localhost:8000/
   
   NB: The development server runs on port 8000 by default  

### Running API requests
To execute the API requests, import the Postman collection file(BuuPass RABC.postman_collection.json)
in the Postman app: Click on the file tab and then click import.


### Running tests
In a terminal navigate to the root directory of the project containing the manage.py file, 
then run the following command in a shell:  

    ```
      $ ./manage.py test account.tests
    ```



### Assigning user permissions and roles
Django provides an inbuilt permission system that allows permissions to be assigned specific users.
It also provides a way for assigning roles(groups) to users

#### Create Group/Roles
1. Navigate to the root directory (buupass_rbac) containing the manage.py file in a command line

2. Create a superuser account
    ```
      $ python manage.py createsuperuser --email username@domainame --username myusername
    ```

3. Start the development server and navigate to the admin site in your local web browser (http://127.0.0.1:8000/admin/).

      ```
      $ python manage.py runserver
      ```
4. Login to the site using the credentials for your superuser account.

5. Click the Add button (next to Group) in the home page **AUTHENTICATION AND AUTHORIZATION** 
   section to create a new Group; enter the name of the group, select group permissions,
   and then click the SAVE button.

#### Assign a role to user
1. Navigate to the admin site in your local web browser (http://127.0.0.1:8000/admin/).

2. Click the Accounts link in the home page **ACCOUNTS** 
   section.

3. Select a specific user and scroll to the **groups** section.

4. Assign a group to a user by moving the group from the left column to the right section
   using the arrow button.

5. Click the **SAVE** button.
