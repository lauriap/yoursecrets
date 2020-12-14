# Cyber Security Base 2020 project

This project is a course work that is meant to display various cyber security flaws as described in OWASP. The application contains vulnerabilities and they are explored in more detail in a separate essay.

**Installation instruction and information for testing**

Link to repository: https://github.com/lauriap/yoursecrets

Installation instructions:
* In the terminal / bash, navigate to a folder you want to place the project into and type
```
git clone https://github.com/lauriap/yoursecrets
```
* Then, navigate to the src folder than contains manage.py and type
```
python3 manage.py runserver
```
* This sets up a local server at port 8000. Please note that the application can be found under localhost:8000/secflaws. You can test the application with the following logins:

admin - admin@example.com - password

arnold - arnoldisking

rocky - ipunchhard


**Known issues**

* Adding secrets does not work with input containing the character '. This problem could be solved through the use of Django's query tools instead of raw SQL queries. This is not done to demonstrate the original approach's vulnerability to SQL injections.


# List of security issues


1. Security misconfiguration (OWASP #6)
    * Due to an error in the initial .gitignore configuration, yoursecrets/settings.py has been leaked to GitHub. The file contains, among other thing, the secret key for the program. Additionally, the file contains a list of installed apps which could help an attacker to search for known vulnerabilities in these apps as well as the name of the database that is being used. This major problem could easily be avoided by more careful .gitignore configuring. Also, GitHub warned about the leak via e-mail, but it has not been taken into account. Once the problem is discovered, all leaked passwords and other information should be replaced.

2. Injection (OWASP #1)
    * In views.py, the 'addSecret' function has been implemented using SQL queries that utilize user input. This implementation makes it vulnerable to SQL injections. This is a situation in which a user is able to input additional commands into the SQL query to, for example, obtain, manipulate or delete data in or from the database. Instead of an approach that utilizes user input in the queries, a safer version could be used that handles input data in a safe manner. The easiest option would be to use Django's ready-made query tools for this purpose, i.e. create a model object (in this case a Secret object) and storing it directly into the database. 

3. Sensitive data exposure (OWASP #3)
    * The 'details' view in views.py is not configured to block access to other users' secrets. This compromises all users' secrets for leaks by any user that has the ability to sign in. Using the browser's address line a logged in user could access all secrets based on their id. As an example, .../secflaws/1 would return the details of a secret from the database for which id = 1. This would happen regardless of whether the secret belonged to the user trying to access it in this way. With regard to OWASP's list of top 10 application security risks, this flaw would also be considered to fall under broken access control (OWASP #5).

    The simplest way to remedy this problem would be to write a check for the 'details' view based on the authenticated user's id. If the authenticated user's id would not match that of the owner's id in the object trying to be accessed, the view would simply redirect back to the index view. This way, with a a couple of lines of code, we could prevent unauthorized access to other people's data while still allowing users to access their own data.

4. Cross-site scripting (OWASP #7)
    * The application has an unsafe POST operation for adding secrets into the database. The operation does not protection against cross-site request forgery (CSRF), which means that an attacker could potentially create requests from another site to the web application. If the user were to access the source site from which requests were being sent to the target web application while the user was authenticated to the target web application, the user's authentication token could be stolen and used to access their information. The risk of cross-site request forgery could be mitigated with the introduction of CSRF tokens or other CSRF defences that are included in many development frameworks.

5. Broken Authentication (OWASP #2)
    * Admin login information is extremely weak in this example: admin and password. These could be easily discovered using the most basic brute-force methods bombarding the admin login with combinations of common name-password combinations. As the Django framework comes with a fully functional admin interface with the ability of, among other things, manage user data including changing their passwords, breaking into the admin interface would mean that all user data and implicitly also their secrets would all be accessible to the attacker. This risk could be mitigated by using much more robust passwords and changing them frequently.
