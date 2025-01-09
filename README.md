
# EthioSphere: Social Media API

## Project Description
The EthioSphere Social Media API is a backend application designed for a social media platform. It provides essential functionality for users to create, manage, and interact with posts, follow other users, comment, and engage with posts through likes and dislikes. Built using Django Rest Framework (DRF), this API ensures rapid development and robust data management. It is designed to deploy on platforms like Heroku or PythonAnywhere.

## Core Features and Functionality

### User Management
- Create, retrieve, update, and delete user profiles.
- User authentication and authorization.

### Post Management
- Create, retrieve, update, and delete posts.
- Posts are linked to specific users via user IDs.

### Following System
- Follow/unfollow other users.
- Maintain a relationship between users for the follow feature.

### Commenting
- Users can comment on posts.
- Retrieve all comments for a specific post.
- Update and delete comments by the author.

### Likes/Dislikes
- Users can like or dislike posts.
- Track the count of likes and dislikes for each post.

### Personalized Feed
- Retrieve a feed of posts from followed users, ordered by creation time (newest first).

## API Endpoints

### User Endpoints
- `POST /api/users/`: Create a new user.
- `GET /api/users/<user_id>/`: Retrieve user details.
- `PUT /api/users/<user_id>/`: Update user details.
- `DELETE /api/users/<user_id>/`: Delete a user.

### Post Endpoints
- `POST /api/posts/`: Create a new post.
- `GET /api/posts/<post_id>/`: Retrieve a post by ID.
- `PUT /api/posts/<post_id>/`: Update a post.
- `DELETE /api/posts/<post_id>/`: Delete a post.
- `GET /api/posts/`: Retrieve all posts (supports pagination).

### Follow System Endpoints
- `POST /api/users/<user_id>/follow/`: Follow a user.
- `DELETE /api/users/<user_id>/follow/`: Unfollow a user.

### Feed Endpoints
- `GET /api/feed/`: Retrieve the feed of posts from followed users.

### Comment Endpoints
- `POST /api/posts/<post_id>/comments/`: Create a new comment on a post.
- `GET /api/posts/<post_id>/comments/`: Retrieve all comments for a post.
- `PUT /api/comments/<comment_id>/`: Update a comment.
- `DELETE /api/comments/<comment_id>/`: Delete a comment.

### Like/Dislike Endpoints
- `POST /api/posts/<post_id>/like/`: Like a post.
- `POST /api/posts/<post_id>/dislike/`: Dislike a post.
- `DELETE /api/posts/<post_id>/like/`: Remove a like from a post.
- `DELETE /api/posts/<post_id>/dislike/`: Remove a dislike from a post.

## Tools and Libraries

### Framework and Libraries
- Django Rest Framework (DRF)
- Django ORM

### Database
- SQLite (for local development).

### Hosting and Deployment
- PythonAnywhere

### Other Tools
- Git for version control.
- Postman for API testing and documentation.

## Installation Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Requirements

### requirements.txt
```plaintext
Django>=4.2
Django-REST-framework>=3.14
mysqlclient>=2.1.1
psycopg2-binary>=2.9.6
python-dotenv>=1.0.0


### **Setup Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install django

   ```

4. **Run the Server**
   ```bash
   python manage.py runserver
   ```
   Open your browser and go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## **Project Structure**
```
social_media_api/
├── core/              # Main app for API features
├── socialmedia/       # Django project settings
├── manage.py          # Django management script
├── .gitignore         # Ignored files for Git
└── README.md          # Project documentation
```

---

## **Contributing**
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

