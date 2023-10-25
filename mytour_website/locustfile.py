from locust import HttpUser, TaskSet, task, between
import json


class MyUser(HttpUser):
    wait_time = between(2, 5)  # Random wait time between tasks

    # # The user logs in and saves the CSRF token for subsequent requests.
    # def on_start(self):
    #     response = self.client.get("/admin/login/?next=/admin/")
    #     csrftoken = response.cookies['csrftoken']
    #     self.client.headers.update({'X-CSRFToken': csrftoken})

    # @task
    # def login_and_browse(self):
    #     # Simulate logging in
    #     response = self.client.post(
    #         "/admin/login/?next=/admin/",
    #         {"username": "admin", "password": "student"},
    #     )

    #     # Check if the login was successful
    #     if response.status_code == 200:
    #         self.client.get("/admin/")  # Visit the admin dashboard
    #         print("get into admin")
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get("/users/login_user")
        csrftoken = response.cookies['csrftoken']
        if csrftoken:
            print(f"CSRF Token: {csrftoken}")
        else:
            print("CSRF Token not found in cookies.")
        self.client.headers.update({'X-CSRFToken': csrftoken})

        login_data = {
            "username": "bob",
            "password": "Student123",
        }
        # response = self.client.post(
        #     "/users/login_user",  # Replace with the actual URL for login
        #     data=login_data,
        # )
        response = self.client.get(
            "/users/login_user", auth=('bob', 'Student123'))
        if response.status_code == 200:
            print("success1")
        else:
            print("failed1")

    @task
    def create_place(self):
        # Define the data for creating a new Place (simulating a form submission)
        place_data = {
            "name": "New Place Name",
            "description": "Description of the new place",
            "price": 5
            # Include other fields as needed, e.g., "owner": your_user_id,
        }

        # Send an HTTP POST request to your Django view for adding a new place
        response = self.client.post(
            "/add_accommodation",  # Replace with the actual URL endpoint for adding a new place
            data=place_data,
        )

        # Check if the response status code indicates a successful creation (e.g., 302 for redirect)
        if response.status_code == 200:
            print("success2")
        else:
            print("failed2")

    @task
    def view_tour_list(self):
        self.client.get("/list_tours")

    @task
    def login_and_create_tour(self):
        # Simulate user login
        response = self.client.get("/users/login_user")
        csrftoken = response.cookies['csrftoken']
        if csrftoken:
            print(f"CSRF Token: {csrftoken}")
        else:
            print("CSRF Token not found in cookies.")
        self.client.headers.update({'X-CSRFToken': csrftoken})

        login_data = {
            "username": "bob",
            "password": "Student123",
        }
        # response = self.client.post(
        #     "/users/login_user",  # Replace with the actual URL for login
        #     data=login_data,
        # )
        response = self.client.get(
            "/users/login_user", auth=('bob', 'Student123'))

        # Create a new Tour
        tour_data = {
            'title': 'New Tour',
            'description': 'Tour description',
            'start_date': '2023-01-01',
            'end_date': '2023-01-10',
            'price': 1000,
            'tour_plan': 'Tour plan details',
            'accommodation': 449,  # Replace with the appropriate ID for an existing Accommodation
            'administrator': 2,  # Replace with the appropriate ID for an existing User
            # Replace with the appropriate IDs for existing Places (use a list if there are multiple)
            'places': [8, 5],
            # Replace with the appropriate IDs for existing ThingsList items (use a list if there are multiple)
            'things_list': [1, 2],
            # Replace with the appropriate IDs for existing Transports (use a list if there are multiple)
            'transports': [1, 3]
        }
        response = self.client.post("/create_tour/", data=tour_data)
        if response.status_code == 200:
            print("success3")
        else:
            print("failed3")
