# Placement Management System

Welcome to the **Placement Management System** repository! This project is designed to streamline and manage the placement activities of educational institutions, providing a user-friendly interface for students, placement officers, and recruiters.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Contact](#contact)

## About the Project

The Placement Management System is a web-based application that automates the entire placement process, making it efficient and easy to manage. From student registration to company interactions and placement drives, everything is handled seamlessly within this system.

## Features

- **Student Module**: Students can register, update their profiles, and apply for placements.
- **Company Module**: Companies can post job openings and view student applications.
- **Admin Module**: Administrators can manage users, jobs, and placement drives.
- **Chatbots**:Real time Communication and query solving using Chatbots.
- **Responsive Design**: Accessible on various devices, thanks to Bootstrap.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Django
- **Database**: SQL (SQLite/PostgreSQL/MySQL)

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

Ensure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/placement-management-system.git
    ```

2. Navigate to the project directory:
    ```sh
    cd placement-management-system
    ```

3. Create a virtual environment:
    ```sh
    python -m venv env
    ```

4. Activate the virtual environment:

    On Windows:
    ```sh
    .\env\Scripts\activate
    ```

    On macOS/Linux:
    ```sh
    source env/bin/activate
    ```

5. Install backend dependencies:
    ```sh
    pip install -r requirements.txt
    ```

6. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

7. Create a superuser for accessing the admin panel:
    ```sh
    python manage.py createsuperuser
    ```

8. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000`.
2. Log in using the superuser credentials to access the admin panel.
3. Students and companies can register and log in to manage their respective profiles and activities.

## Screenshots

*Website view for visitors.*
![Screenshot 2024-05-29 173449](https://github.com/Abhidongre/Placement-management-system/assets/113405820/eacc7254-7b5a-45ed-904e-425259c8a0f1)
![Screenshot 2024-05-29 173549](https://github.com/Abhidongre/Placement-management-system/assets/113405820/748fb1ba-f48e-440c-a9d8-56faab5dde11)
![Screenshot 2024-05-29 173614](https://github.com/Abhidongre/Placement-management-system/assets/113405820/17b69e9b-e643-496e-bffe-4054b9a24e10)

*Student profile management interface.*
![Screenshot 2024-05-29 173721](https://github.com/Abhidongre/Placement-management-system/assets/113405820/31d1064f-e545-4d4f-9eca-9f669de61f81)
![Screenshot 2024-05-29 173815](https://github.com/Abhidongre/Placement-management-system/assets/113405820/6a3c5c21-4b8c-4eaf-8b9d-4fa47e192124)

\
*Interface for companies to post job openings.*
![Screenshot 2024-05-29 173925](https://github.com/Abhidongre/Placement-management-system/assets/113405820/137f9ea9-939e-4c9e-9ca3-05fbd5ba5205)
![Screenshot 2024-05-29 173944](https://github.com/Abhidongre/Placement-management-system/assets/113405820/127f89dd-e8f0-4a4d-a526-b53d8bd7d639)


## Contact

Project Link: [https://github.com/Abhidongre/placement-management-system](https://github.com/Abhidongre/placement-management-system)

For any queries or feedback, please reach out to:
- **Your Name** - [abhidongre2004@gmail.com](mailto:abhidongre2004@gmail.com)
- **GitHub**: [https://github.com/Abhidongre](https://github.com/Abhidongre)
