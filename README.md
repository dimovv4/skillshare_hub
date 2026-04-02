# SkillShare Hub

A modern Django-based learning platform where instructors create courses and students enroll to learn new skills.  
This project includes user authentication, course management, enrollments, dashboards, and a fully responsive dark-themed UI.

---

## 🚀 Features

### 👤 User System
- Register, login, logout
- Instructor or student roles
- Dark-themed modern authentication pages

### 📚 Courses
- Browse all courses
- View course details
- Instructor-owned courses
- Clean, modern course cards

### 📝 Enrollments
- Students can enroll in courses
- Dashboard shows enrolled courses

### 🖥️ Dashboard
- Profile overview
- List of enrolled courses
- Clean dark UI

### 🎨 Dark Theme UI
- Fully custom dark mode styling
- Modern inputs, cards, and layout
- Consistent design across all pages

---

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/yourusername/skillsharehub.git
cd skillsharehub

### 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run migrations
python manage.py migrate

### 5. Start the development server
python manage.py runserver

### Creating a superuser
python manage.py createsuperuser

