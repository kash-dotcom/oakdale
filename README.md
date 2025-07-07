
# Oakdale Spa
Welcome to the digital home of Oakdale Spa, your sanctuary for relaxation and rejuvenation.
Enter the serene world of Oakdale Spa, our newly created Django-based website. Explore our featured experiences. With our new website, you can book, review, edit, and cancel experiences from the comfort of your own device.


![wesbite](https://res.cloudinary.com/dybts6jei/image/upload/v1742197303/am-i_-responsive_w3lp4t.png)

 [**Visit our website**](https://oakdale-spa-00f9c791dc68.herokuapp.com/)

## About Oakdale Spa 
Oakdale Spa is dedicated to providing exceptional wellness experiences. We offer a range of treatments designed to promote relaxation, revitalise your body, and restore inner balance. Our services include:
* Hot stone massages
* Aromatic steam rooms
* Invigorating saunas
* Infinity pool
* and much, much more!

We prioritise creating a tranquil environment where our guests can escape the stresses of daily life and focus on their well-being.

# User Experience (UX)

Users are welcomed with images that capture the essence of Oakdale Spa: tranquillity, relaxation, and bliss. The simple, elegant design allows for easy navigation across various devices.

## Target Audience

The Oakdale Spa experience is crafted for professionals and individuals seeking an escape from demanding lives, characterized by conflicting deadlines and numerous responsibilities. They value peace and tranquillity, seeking a sanctuary for personal well-being. Frequently, they prioritize the needs of others, making self-care a necessary and cherished reward. They are aspirational and seek to elevate their social, financial, and status.

## First-Time User Experience:

* Visually appealing and calming landing page.
* Clear and concise information about services and philosophy.
* Simple navigation to explore treatments, pricing, and location.
* Clear "BOOK NOW" call-to-action on all pages.
* Easy-to-find contact information linked to WhatsApp and phone.
* Mobile-responsive design for a smooth experience.

## Registered User Experience:

* Easy-to-find location in the footer, linked to Google Maps.
* Ability to communicate via WhatsApp.
* Ability to manage, modify, and delete reservations.
* Access to previous bookings with photos for reference.

## Admin User Experience:

* Ability to add, edit, and delete experiences.
* Publish/unpublish experiences without deleting.
* Secure login.
* Ability to delete user accounts and associated reservations for GDPR compliance.
* Update photos and descriptions via the admin dashboard.

## User Journey

![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1742200491/User_Journey_gkjkmu.png)

# Design

The website's subtle, elegant design features a white background with cream and charcoal grey accents. Green is used to highlight interactive elements. The parallax container showcases relaxing imagery.

![alt Colour Pallet](https://res.cloudinary.com/dybts6jei/image/upload/v1742197974/colormind_macdce.png)

## Typography

Libre Baskerville is used for its elegant and readable aesthetic.

## Mobile First Wirefame
Using the principles of mobile-first, all designs were initially create for mobile and then adapted using Materialize's responsive grids.
![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1742199198/Mobile_first_wireframes_bjcnxa.png)

## Entity Relationship Diagram (ERD)


![Oakdale Spa's ERD](https://res.cloudinary.com/dybts6jei/image/upload/v1742198503/drawSQL-image-export-2025-03-17_zgqacm.png)


# Data Model

* **Login (Sprint 1):** Using Django's Allauth library, this model stores user login credentials, like username and password. It also tracks `created_on` and `updated_on` timestamps, although not used in this project. This allows for potential tracking of user activity for marketing purposes.

* **Guests (Sprint 1):** This model stores guest information, including `guest_id`, `first_name`, `last_name`, `address`, `city`, `postcode`, `phone_number`, `email`, `reason_for_visit`, `created_on`, `updated_on`, and `last_visit` dates. The `guest_id` has a one-to-many relationship with the `Reservation` model, enabling a guest to have multiple reservations. This model is central to enabling [**Please clarify what this model enables. What functionality does it provide?]**

* **Experiences (Sprint 1):** This model stores information about available spa experiences, including `experience_id`, `name`, `description`, `price`, and `image`. Experience coordinators can create and publish new experiences. Experiences have a one-to-many relationship with `Reservations`. One experience can be associated with multiple reservations.

* **Reservations (Sprint 1):** This model is central to all other models and brings together reservation details, including `reservation_id`, `reservation_date`, `experience` (foreign key to `Experiences`), `reservation_price`, `number_of_guests`, and `enhancements`. The `reservation_id` ensures that experiences can only be edited by the correct guest.

* **Payment (Sprint 2):** This model stores payment information, including `payment_id`, `payment_date`, `payment_amount`, `created_on`, and `updated_on`. This will be included in Sprint two.

* **Enhancements (Sprint 2):** This model stores details about available enhancements, including `enhancement_id`, `enhancement_name`, `enhancement_description`, `image`, `enhancement_price`, `quantity`, and `created_on`. These would be used if a guest wanted to make their stay extra special with champagne, chocolates, or flowers.

* **Review (Sprint 2):** This model stores customer reviews, including `review_id`, `review_date`, `review_text`, and `created_on`.

# Agile Project Management

This project utilised agile project management techniques, with Monday.com serving as the primary project management tool.
![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1742209022/Register_models_to_admin_site_-_Admin_Site_gi5wf3.png)

**Monday.com Setup:**

* The project was organised into epics based on user profiles.
* Each task included status, priority, and type attributes.
* Monday.com was integrated with GitHub to link issues, commits, and tasks.
* A Kanban board was used to visualise and manage the workflow, connecting issues to individual tasks.

![alt text](https://res.cloudinary.com/dybts6jei/image/upload/v1742209172/valued-guest-epic_tytrfg.png)

**Sprint Planning:**

* Due to the extensive features, the project was divided into two sprints.
* Sprint 1 focused on delivering the minimum viable product (MVP).
* Sprint 2 aimed to enhance the user experience by adding further features and improvements.


## Security Features

**User Authentication** is used to register guests. This allows for **login decorators** to ensure reservations are changed, deleted, or viewed only by the correct guests. **CSRF Protection** was used to prevent Cross-Site Request Forgery via the APIs.


# Features

* **Welcoming Home Page:**
    * The home page greets guests with a focus on relaxation and unwinding.
    * Parallax images offer a behind-the-scenes glimpse of treatments.

* **Persistent "Book Now" Button:**
    * A "Book Now" button is prominently displayed on every page for easy access.
* **Dynamic Login/Account Options:**

    * The site displays either "Login/Register" or "Account/Logout" based on the user's login status.

* **Consistent Success Messages:**
    * Success messages are consistently displayed in the same location for clear feedback.

![welcome](https://res.cloudinary.com/dybts6jei/image/upload/v1742203736/Screenshot_2025-03-17_090914_lp9znc.png)

* **Informative "About" Page:**
    * Guests can learn about the spa's offerings and philosophy through a dedicated "About" page.

    ![about us](https://res.cloudinary.com/dybts6jei/image/upload/v1742203735/Screenshot_2025-03-17_085605_wqkgcu.png)

* **Experience Cards:**
    * Experiences are showcased in card format with images, providing a visual preview.
    * Cards feature images of countryside views, gym equipment, and massage treatments.
    * Clicking the plus sign reveals more details about each experience.

* **Interactive Price and Booking:**
    * Hovering over the price changes its color, indicating interactivity.
    * Guests can click either the price or the "Book Now" button to access the booking form.

![experiences](https://res.cloudinary.com/dybts6jei/image/upload/v1742203736/Screenshot_2025-03-17_085640_ezqwgs.png)


* **Login/Signup for Non-Members:**
    * Non-members are directed to a login/signup page with imagery that reinforces the spa's peaceful atmosphere.
    * The "Book Now" button on the login/signup page returns users to the experiences homepage.
    * The sign-in form has a link to the signup page.

* **Post-Login Experience:**
    * Upon successful login, users are presented with the experiences and a success message.

    * The user's email address is pre-populated in the booking form.
![date picker for forms](https://res.cloudinary.com/dybts6jei/image/upload/v1742203736/Screenshot_2025-03-17_091224_td6ua9.png)

* **Form Validation:**
    * All form fields are required, and browser-provided hints are displayed for missing fields.
    * Dropdown menus and date pickers prevent database errors.

![editing a reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1742203737/Screenshot_2025-03-17_091724_mk6my5.png)

* **Reservation Confirmation:**
    * A success message confirms the successful creation of a reservation.
![confirmation message](https://res.cloudinary.com/dybts6jei/image/upload/v1742203737/Screenshot_2025-03-17_091436_lslkaf.png)

* **Account Management:**
    * The "Account" section allows users to view past reservations.
    * Users can edit or cancel reservations.
    * The edit function retrieves data, and reminds the user to choose an experience.
    * A success message is shown, with the total price recalculated.
    * Cancellation requires confirmation.
    * A message encourages booking if no reservations exist.

**Accessibility Features:**

* **Alternative Text:**
    * All images include descriptive alternative text for screen readers.
* **High Contrast Design:**
    * The website utilizes a high-contrast design for improved readability.
* **Keyboard Navigation:**
    * Buttons and interactive elements are designed for easy keyboard navigation.
* **Screen Reader Compatibility:**
    * The website's structure and semantic HTML are optimized for screen readers.
* **Clear Focus Indicators:**
    * Interactive elements have clear focus indicators for keyboard users.    ![past reservations](https://res.cloudinary.com/dybts6jei/image/upload/v1742203737/Screenshot_2025-03-17_091724_mk6my5.png)
    

## Future Features

* **Payment Integration:** Enable guests to pay for their reservations online.

* **Enhancements:** Allow guests to add enhancements to their reservations, such as champagne, chocolates, or flowers.

* **Review Approval:** Implement a review approval process to ensure only verified reviews are displayed.

* **User Profiles:** Create user profiles to track reservations and reviews.

* **Email Notifications:** Send email notifications for reservations, cancellations, and reviews.

* **Social Media Integration:** Add social media links for easy sharing of spa experiences.

* **Gift Cards:** Enable guests to purchase gift cards for friends and family.

* **Spa Packages:** Offer spa packages for special occasions, like birthdays, anniversaries, or holidays.

# Testing

Page | Language Test Type| Status | User Action | Expected Results | Outcome
|----|----------|--------|-------------|------------------|---------|
**home.html**|JavaScript|All |	Click the menu|	Open the navigation slider to the left|	Pass|
||Python|Logged-in |-|	Message appears under the header|	Pass
||Python|Logged in|-|	Book Now button	Open the reservation page|	Pass
||Python|Logged out/not registered|	Click **Book Now** button|	Open the reservation page(sign-up/login)|	Pass
||JavaScript|All|Click the + button|Opens the modal with more information|	Pass
||Python|Logged out/not registered |	Click **reserve your peace here**|	Open the reservation page(sign-up/login)|	Pass
||Python|Logged in|	Click **reserve your peace here**|	Open the reservation page	|Pass
||Python|All|Click **price**|	Open the reservation page(sign-up/login)|	Pass
||Python|All|Click **phone number**|	Open the application to make phone calls	|Pass
||Python|All|Click the **email address**|		Opens the application to send an email|	Pass
||Python|All|Click **WhatsApp** logo|	Opens WhatsApp|	Pass
||Python|All|Click **Address**	|	Opens Google maps to Ashleworth	|Pass
||Python|All|Click **Instagram’s** logo|	Opens Instagram	|PassPass
||Python|All|Click **YouTube’s** logo	|Opens YouTube	Opens YouTube	|Pass
||Python|All|Click **Facebook’s** logo|	Opens Facebook|	Pass
||Python|All|Click **X(formerly Twitter)** logo| 	Opens X formerly Twitter|	Pass
|**reservation.html**|Python|	Logged out/not registered|	Click sign up|	Opens signup.html |	Pass
||Python|Registered user|	Click **login**|	Opens login page	|Pass
||Python|Registered user|	Enter first name|	Input name|	Pass
||Python|Registered user|	Enter last name|	Input name|	Pass
||Python|Registered user|	Enter address	|Input email address that must include **@** |Pass
||Python|Registered user|	Enter city	|Input address	|Pass
||Python|Registered user|	Enter postcode	|Input postcode|	Pass
||Python|Registered user|	Enter home number|	Input phone number|	Pass
||JavaScript|Registered user	|Select the number of guests from a dropdown list |	Select the number of guests|	Pass
||JavaScript|Registered user|	Select reservation date from a date picker|	Select reservation date	|Pass
**past_reservations** |Python| Registered user - No reservations|Click **Book Now** button|Opens the experience section of the home page|	Pass
||Python| Registered user - With reservation(s)|Click **Edit** button|User is sent the their reservation to edit|	Pass
||JavaScript| Registered user - With reservation(s)|Click **Cancel** button|A modal window prompts the user to confirm if they want to delete their reservation.|	Pass
|| JavaScript|Registered user - With reservation(s)|Click **No, I'm not** |The model closes|	Pass
|| Python|Registered user - With reservation(s)|Click **Yes, I'm sure** |Message appear at the top of the page **Reservation deleted succesfully!**|	Pass
||Python| Registered user - With reservation(s)|Click **Yes, I'm sure** |User is taken to the pased reservations page and provided with the opportunity to **book now**|	Pass
**NavBar** |Python | Registered user | User clicks the **logout** button|User is sent to the **Logout** page and is prompted if they would like to logout|Pass
||Python|All |Click **Reservations**|User is sent to past_reservations.html|	Pass
||JavaScript | All | Click *burger* icon| Modal opens with **logout** and **reservations**|	Pass

## Validation 
* [JSHint](https://www.jslint.com/) was used to vailidate JavaScript - This passed with no errors
* [CSS Validation Service ](https://jigsaw.w3.org/css-validator/) - Passed with no errors or warnings
* [Markup Validation Service](https://validator.w3.org/) - When viewing the rendered HTML in the browser (with Python code removed) - all pages pass validation
* [Flake8](https://flake8.pycqa.org/en/latest/) - Used as an inline linter - all pages pass **PEP8** vailidation. 

## Known Bugs

|Bug|Description|Planned Fix|
|---|-----------|-----------|
|**Users can select dates in the past** | The reservation form currently allows users to pick and submit dates that have already passed. | Add client-side and server-side validation to restrict date selection to today or future dates|
|**Experience selector**|Regardless of which experience brought the user to the reservation page, they must still select the experience from the dropdown list.|Pre-select the experience in the dropdown based on the user's previous selection or navigation path.|
|**Autofill experience** | When a user edits a reservation, the previously selected experience is not automatically populated in the dropdown. The user must manually re-select the experience. |Ensure the form pre-selects the original experience when editing a reservation.|
|**CSP inline style violation** | Used `unsafe-inline` for the Content Secruity Policy blocks inline styles to circumvent errors | Long term fix would be use hashes or nounces for secure inline style usage | 

## Lighthouse Reports

<details>
<summary>Home Lighthouse Report</summary>
<br>

![Home Page](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/home_lighthouse_zqgqgx.png)

</details>

<details>
<summary>Sign up Lighthouse Report</summary>
<br>

![Sign_up](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/sign_up_lighthouse_nmcfi0.png)

</details>

<details>
<summary>Sign in Lighthouse Report</summary>
<br>

![Sign_in](https://res.cloudinary.com/dybts6jei/image/upload/v1751925794/sign_in_lighthouse_ycnlbo.png)

</details>

<details>
<summary>Sign out Lighthouse Report</summary>
<br>

![Sign out](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/sign_out_lighthouse_br7ipi.png)

</details>

<details>
<summary>Book Reservation Lighthouse Report</summary>
<br>

![Book Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/reservation_lighthouse_olj8fk.png)

</details>

<details>
<summary>Review Reservation Lighthouse Report</summary>
<br>

![Review Reservation](https://res.cloudinary.com/dybts6jei/image/upload/v1751925795/reservation_edit_lighthouse_rjtixz.png)

</details>

# Technologies Used

## Languages

* **HTML5:** The website structure.
* **CSS3:** The website styling.
* **JavaScript:** The Materialize framework.
* **Python:** The Django framework.

## Frameworks, Libraries, and Tools

 **[Materialize](https://materializecss.com/):** 
* **[Django](https://www.djangoproject.com/):** 
* **[Draw SQL](https://drawsql.app/teams/de-pointe/diagrams/spa):**
* **[Canva](https://www.canva.com/):**
* **[Gemini](https://gemini.google.com/)**
* **[VS Code](https://code.visualstudio.com/)**
* **[GitHub](https://github.com/)**
* **[Am I responsive](https://ui.dev/amiresponsive)**
* **[Favicon Generator](https://realfavicongenerator.net/)**
* **[JSHint](https://www.jslint.com/)**
* **[CSS Validation Service ](https://jigsaw.w3.org/css-validator/)**
* **[Colormind](http://colormind.io/)**

# Deployment and Local Development - Oakdale Spa

## Live Deployment

The live deployment of Oakdale Spa can be accessed here: [[Oakdale Spa Live Website ](https://oakdale-spa-00f9c791dc68.herokuapp.com/)]

## Local Development

### How to Fork

1.  Log in (or Sign Up) to GitHub.
2.  Go to the Oakdale Spa repository: [[Oakdale Spa Live Website ](https://oakdale-spa-00f9c791dc68.herokuapp.com/)]
3.  Click the "Fork" button in the top right corner.

### How to Clone

1.  Log in (or Sign Up) to GitHub.
2.  Go to the Oakdale Spa repository: [[Oakdale Spa Live Website ](https://oakdale-spa-00f9c791dc68.herokuapp.com/)]
3.  Click the "Code" button and select your preferred cloning method (HTTPS, SSH, or GitHub CLI). Copy the link.
4.  Open your code editor's terminal and navigate to the directory where you want to clone the repository.
5.  Run the following command in the terminal (replace `[copied link]` with the link you copied in step 3):
    ```bash
    git clone [copied link]
    ```
6.  Set up a virtual environment (optional, but recommended). If you're using a GitPod template, this is usually pre-configured.
7.  Install the required packages from `requirements.txt`:
    ```bash
    pip3 install -r requirements.txt
    ```

### Database

Oakdale Spa uses an Code Institute's PostgreSQL database.

### Cloudinary

Oakdale Spa utilises Cloudinary for image and video management.

1.  Go to [Cloudinary](https://cloudinary.com/).
2.  Choose "Programmable Media" as your primary interest.
3.  Optionally, edit your cloud name.
4.  Copy your API Environment Variable from the Cloudinary Dashboard.
5.  Remove `CLOUDINARY_URL=` from the beginning of the API value.

### Heroku Deployment

1.  Log in to your [Heroku](https://www.heroku.com/) account or create one.
2.  Click "New" -> "Create New App."
3.  Enter a unique application name.
4.  Select your region and click "Create App."
5.  **Environment Setup:**
    * Create an `env.py` file in your project's main directory.
    * Add `DATABASE_URL`, `SECRET_KEY`, and `CLOUDINARY_URL` values to `env.py`.
    * Update `settings.py` to import `env.py` and access the environment variables.
    * Comment out the default database configuration in `settings.py`.
    * Make migrations after saving all files.
    * Add Cloudinary libraries to `INSTALLED_APPS` in `settings.py`.
    * Configure static file settings in `settings.py` (URL, storage, directories, root, media URL, default storage).
    * Link to the templates directory in Heroku by changing the templates directory variable to `TEMPLATES_DIR`.
    * Add your Heroku app URL and `localhost` to `ALLOWED_HOSTS` in `settings.py`.
6.  **Heroku Config Vars:**
    * In Heroku, go to "Settings" -> "Config Vars."
    * Add the following variables:
        * `SECRET_KEY` (Django secret key)
        * `CLOUDINARY_URL` (Cloudinary API key)
        * `PORT` (set to 8000)
        * `DISABLE_COLLECTSTATIC` (set to 1 for initial deployment, remove later)
        * `DATABASE_URL` (database URL)
7.  **Required Files:**
    * Ensure you have `requirements.txt` and `Procfile` in your project root.
8.  **Deployment:**
    * Set `DEBUG = False` in `settings.py`.
    * In Heroku, go to the "Deploy" tab.
    * Connect to your GitHub repository.
    * Enable automatic deploys or manually deploy the branch.
    * Click "Open App" to view the live site.
# References

**Messages**
[How to use Messages Framework](https://codewithstein.com/how-to-use-the-messages-framework-django-tutorial/)

**Choice Field** 
[Choice Field](https://stackoverflow.com/questions/8859504/django-form-dropdown-list-of-numbers)

**Overriding CSS Frameworks** - 
[Jonathan Soma](https://jonathansoma.com/everything/web/overriding-frameworks/)

**Code Institute's Tutorials** [Code Institute](https://codeinstitute.net)

**Error Handling** - [HTTP Cats]([text](https://http.cat/))

**Test Cases** -
[Accelatest](https://accelatest.com/how-to-write-test-cases-for-login-page/)

**User Stories** - [Parabol](https://www.parabol.co/blog/user-story-examples/#user-story-examples-for-online-shopping)

## Media

 [Photo by Ron Lach](https://www.pexels.com/photo/man-and-woman-in-hot-tub-8845113/)

 [Compass Pools](https://www.compass-pools.co.uk/learning-centre/faqs/a-guide-to-designing-and-building-an-infinity-pool-and-how-it-works/)

 [Pexel](https://www.pexels.com/)

[Overlapping Divs](https://stackoverflow.com/questions/2527782/div-on-top-of-div-using-z-index)

## Design
[Colour Picker]([text](https://imagecolorpicker.com/))

**README Responsive Display** [Am I Responsive](https://ui.dev/amiresponsive)



**Inspiration** - 
[Ragdale Hall Spa](https://www.ragdalehall.co.uk/?_ga=2.135503475.33112821.1741430307-1430965657.1741430358)

## Content
The content was created by the developerwith help from Gemini and Copilot. The text was inspired by various spa websites and tailored to the Oakdale Spa brand.

## Acknowledgement
Thank you to those I spoke at [Turkish Baths 1877](https://turkishbaths1877.com/) and the **outstanding** team a Code InsCode Institute. 
