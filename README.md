# tutorsession
This is the source code to an API that manages tutor sessions in a school's tutoring lab.
# File Structure
- The  `school` folder is actually a virtual environment that contains an installed version of `python`, `django` and all other dependencies.
- The `school\schoolManager` folder is the django project folder, it contains the project settings file `settings.py` and the `urls.py` that contains the url routes.
- The `school\institution` folder houses the files for the __institution__ app. Here the `models.py` file contains the model classes for each entity. The `serializers.py` file, defines how the data should be serialized, in this case, the JSON format. The `views.py` file contains the class based views that handles CRUD operations for each entity. The `urls.py` file binds the routes/__endpoints__ to its respective view class.
# Running the Project
1. Download or clone the repository to your local machine.
2. In your terminal navigate to the location of the school folder. This should look something like `root@jowzaiah:/mnt/c/downloads/tutorsession/school$` for __(Mac & Linux)__. 
On windows it should look something like `C:\Users\jowzaiah\tutorsession\school>`
3. Run the `source bin/activate` command to activate the virtual environment if you are on __(Mac & Linux)__. On __(Windows)__, the command would be `scripts\activate`. If this is successfully done, the terminals command prompt would be modified to start with `(school)`. For example it would look similar to `(school)root@jowzaiah:/mnt/c/downloads/tutorsession/school$` on __(Mac & Linux)__ and 
`(school)C:\Users\jowzaiah\tutorsession\school>` on __Windows__.
4. Now an admin account has to be created. To do this run the command `python manage.py createsuperuser`. This will then prompt you to input your username, email and password.
5. To spin up the web server, the command `python manage.py runserver`. This will start a webserver running at the loopback address on port 8000. This would be `localhost:8000`, or when resolved to an IP address, `127.0.0.1:8000`. Look [here](https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver) for a guide to run the server on a different address and port.
6. Now to log into the django admin console in a browser, the address for that is the host address followed by `/admin`. Say, for example a server is running at `127.0.0.1:8000`, then the address to the admin console would be `127.0.0.1:8000/admin`. Here the username and password created in step __4__ is used to log in.
7. The next step involves creating a token for the superuser account so that you will be able to carry out requests to the "Detail" endpoints. This is done by clicking the "Add" button in the admin portal under "Tokens", and then selecting the account to create the token for. When the token is created, it can be used to make requests by passing it in the authorization request header.
8. Now you can create, read, update, and delete instances of each entity either in the admin console, or by making HTTP requests to any of the desired endpoints, or actually visiting each endpoint in a browser.
9. To stop the server from running hit `Ctrl + C` on your keyboard.
10. You can exit the virtual environment by running the command `deactivate`.

# Making Requests
To make a request, tools like Postman, curl, and httpie can be used. The django restframework's webpages hosted on each of the "List" endpoints can be used as well. The most recent version of this API utilzes token based authentication so a token has to be created for the user in the admin console, and used when making requests to all "Detail" endpoints. Reffer to step __7__ above.

# Note:
- The tutor, student, and instructor model classes all extend the user model class. Also they each posess a one to one realtionship with the user model class. This means that when creating any instances of these entities, a user has to be created first and then that existing user object is used to create an instance of any of these entities.
- There is currently no form of Permissions enabled. That means, any user (student, instructor, admin, tutor) with a valid token can create and modify any instances of all the entities (tutor,books,instructors,). This is in the process of being implemented.
