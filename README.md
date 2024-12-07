
# **EthioSphere - Social Media API**

PostFlow is a social media API built with Django that allows users to create, update, and delete posts, follow other users, and interact with content through likes, dislikes, and comments. This project will serve as the backend for a social media platform.

---

## **Features**
- User authentication and profile management.
- Create, update, delete, and retrieve posts.
- Follow/unfollow functionality.
- Like, dislike, and comment on posts.
- View personalized feeds.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python (3.8 or higher)
- pip (Python package manager)
- Git

---

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

