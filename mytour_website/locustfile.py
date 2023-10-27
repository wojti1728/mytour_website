from locust import HttpUser, TaskSet, task, between
import json


class MyUser(HttpUser):
    wait_time = between(2, 5)  # setting random number between 2 and 5 seconds

    # start necessary function (we are starting with log in)
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
        response = self.client.post(
            "/users/login_user",
            data=login_data,
        )
        if response.status_code == 200:
            print("Log in success!")
        else:
            print("Log in failed!")

    @task
    def create_tour(self):

        # Create a new Tour
        tour_data = {
            'title': 'New Tour',
            'description': 'Tour description',
            'start_date': '2023-01-01',
            'end_date': '2023-01-10',
            'price': 1000,
            'tour_plan': 'Tour plan details',
            'accommodation': 1032,
            'administrator': 2,
            'places': [8, 5],
            'things_list': [1, 2],
            'transports': [1, 3]
        }
        response = self.client.post("/create_tour/", data=tour_data)
        if response.status_code == 200:
            print("Created a new tour successfully!")
        else:
            print("Create a new tour failed!")

    @task
    def create_accommodation(self):

        accommodation_data = {
            "name": "New Accommodation",
            "description": "Description of the new accommodation",
            "price": 10
        }

        response = self.client.post(
            "/add_accommodation",
            data=accommodation_data,
        )

        if response.status_code == 200:
            print("Create a new accommodation")
        else:
            print("Createa a new accommodation failed")

    @task
    def login_and_browse(self):
        # Simulate logging in
        response = self.client.get("/admin/login/?next=/admin/")
        csrftoken = response.cookies['csrftoken']
        self.client.headers.update({'X-CSRFToken': csrftoken})
        response = self.client.post(
            "/admin/login/?next=/admin/",
            {"username": "admin", "password": "student"},
        )

        if response.status_code == 200:
            self.client.get("/admin/")
            print("get into admin")

    @task
    def view_tour_list(self):
        self.client.get("/list_tours")

    @task
    def view_place_list(self):
        self.client.get("/list_places")

    @task
    def view_my_tours(self):
        self.client.get("/my_tours")

    @task
    def view_one_place(self):
        self.client.get("/show_place/2")

    @task
    def view_one_tour(self):
        self.client.get("/show_tour/2392")

    @task(2)
    def view_calendar_main_page(self):
        self.client.get("/")

    @task
    def download_tour_pdf(self):
        self.client.get("/tour_pdf")
