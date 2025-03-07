# TechForing Backend Task

## API Documentation
[Postman API Docs](https://documenter.getpostman.com/view/20333890/2sAYdoDS6H)

### Postman Collection & Environment Files
You can import the following files into Postman:
1. **TechForing API.postman_collection.json** – Contains API endpoints.
2. **TechForing.postman_environment.json** – Contains environment variables.

---

## Setup Instructions
### 1. Create a Virtual Environment
```sh
python -m venv venv
```
### 2. Activate Virtual Environment
#### Windows:
```sh
venv\Scripts\activate
```
#### macOS/Linux:
```sh
source venv/bin/activate
```

### 3. Install Required Packages
```sh
pip install -r requirements.txt
```

### 4. Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser
```sh
python manage.py createsuperuser
```

---

## API Usage Guide
### 1. Authentication APIs
- **Register**: Takes `email`, `password`, `username`, `first_name`, and `last_name` as the request body.
  - Validates uniqueness and password format.
  - Returns a response upon successful account creation.
- **Login**: Accepts `email` and `password` as input.
  - Authenticates the user and returns a JWT token along with user details.
- **User Management**:
  - **Retrieve, Update, and Delete** user details using JWT authentication (Bearer Token).
  - Modifiable fields: `first_name`, `last_name`, `email`, `username`.
- **Change Password**: Available via a dedicated password change API.

### 2. Project APIs
- Implemented using Django ModelViewSet with custom logic to reduce code duplication.
- Provides efficient API creation with minimal development time.
- Refer to the [Postman Documentation](https://documenter.getpostman.com/view/20333890/2sAYdoDS6H) for valid request body details.

---

## Notes
- **JWT Authentication** is used for securing API endpoints.
- Follow the Postman documentation for detailed request/response formats.
- Ensure environment variables are correctly set before making API requests.

