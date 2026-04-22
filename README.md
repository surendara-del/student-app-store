# Rajalakshmi Engineering College - Student App Store

A comprehensive web application for discovering, uploading, and managing student-developed applications. Built for Rajalakshmi Engineering College to facilitate app sharing among the student community.

**Guided by:** Surendar, Assistant Professor

## Features

### 🎯 Core Features
- **Browse Applications**: Explore apps by category, ratings, and downloads
- **Upload Apps**: Students can upload their applications (APK, ZIP, IPA, EXE, DMG, etc.)
- **Rate & Review**: Community-driven rating system with detailed reviews
- **Search & Filter**: Find apps by name, developer, or category
- **Statistics**: Track trending apps, popular categories, and developer statistics
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices

### 📊 Admin Features
- Category management
- App moderation
- Statistics and analytics
- Developer profiles

### 🔐 Security Features
- File type validation
- Secure file uploads (100MB limit)
- XSS protection
- CSRF protection
- SQL injection prevention via SQLAlchemy ORM
- **Google OAuth 2.0 Authentication** - Secure login with Gmail accounts

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite (with SQLAlchemy ORM)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API**: RESTful API architecture

## Project Structure

```
student-app-store/
├── app.py                 # Main Flask application
├── config.py              # Configuration settings
├── db.py                  # Database initialization
├── models.py              # SQLAlchemy models
├── routes/
│   ├── apps.py           # Apps browsing routes
│   ├── upload.py         # File upload routes
│   └── stats.py          # Statistics routes
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── app.js        # Frontend logic
├── uploads/              # Uploaded files storage
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone or Download the Project

```bash
cd student-app-store
```

### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
# Development mode
python app.py

# Or with Flask CLI
flask run
```

The application will be available at: `http://localhost:5000`

### Step 5: Google OAuth Setup (Required for Login)

1. **Create Google Cloud Project**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one

2. **Enable Google+ API**:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Google+ API" and enable it

3. **Create OAuth 2.0 Credentials**:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth 2.0 Client IDs"
   - Configure OAuth consent screen if prompted
   - Set Application type to "Web application"
   - Add authorized redirect URIs: `http://localhost:5000/auth/google/callback`

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory:

   ```env
   FLASK_ENV=development
   SECRET_KEY=your-secret-key-here
   GOOGLE_CLIENT_ID=your_google_client_id_here
   GOOGLE_CLIENT_SECRET=your_google_client_secret_here
   GOOGLE_REDIRECT_URI=http://localhost:5000/auth/google/callback
   ```

### Step 6: Initialize Database

```bash
python init_sample_data.py
```

### Step 7: Run the Application

```bash
# Development mode
python app.py

# Or with Flask CLI
flask run
```

The application will be available at: `http://localhost:5000`

## 🚀 Deployment to Render

### Prerequisites
- GitHub account
- Render account (https://render.com)
- Google Cloud Console project with OAuth 2.0 credentials

### Step 1: Prepare for Deployment

1. **Commit your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Student App Store"
   git branch -M main
   git remote add origin https://github.com/yourusername/student-app-store.git
   git push -u origin main
   ```

2. **Set up Google OAuth for Production**:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - In your OAuth 2.0 Client ID settings, add your Render domain to authorized redirect URIs:
     ```
     https://your-app-name.onrender.com/auth/google/callback
     ```

### Step 2: Deploy to Render

1. **Connect your GitHub repository**:
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New" → "Web Service"
   - Connect your GitHub repository

2. **Configure the service**:
   - **Name**: `student-app-store` (or your preferred name)
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`

3. **Set Environment Variables**:
   In Render dashboard, add these environment variables:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secure-random-secret-key
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GOOGLE_REDIRECT_URI=https://your-app-name.onrender.com/auth/google/callback
   ```

4. **Deploy**:
   - Click "Create Web Service"
   - Render will build and deploy your app automatically

### Step 3: Post-Deployment Setup

1. **Update Google OAuth Redirect URI**:
   - After deployment, copy your Render app URL
   - Update the redirect URI in Google Cloud Console to match your Render domain

2. **Initialize Database**:
   - The database will be created automatically on first run
   - Sample admin users will be created

3. **Test the Application**:
   - Visit your Render app URL
   - Try logging in with Google OAuth
   - Upload and browse apps

### Troubleshooting

- **Database Issues**: If you need to reset the database, you may need to redeploy
- **OAuth Errors**: Double-check your Google Cloud Console redirect URIs
- **File Uploads**: Render has ephemeral file storage; uploaded files may be lost on redeploy

## API Endpoints

### Authentication
- `GET /api/auth/google` - Initiate Google OAuth login
- `GET /api/auth/google/callback` - Handle Google OAuth callback
- `POST /api/auth/login` - Traditional login (for backward compatibility)
- `POST /api/auth/logout` - Logout user
- `GET /api/auth/me` - Get current user info

### Apps
- `GET /api/apps/` - Get all apps (with pagination, filtering, sorting)
- `GET /api/apps/categories` - Get available categories
- `GET /api/apps/<id>` - Get app details
- `POST /api/apps/<id>/download` - Record download
- `POST /api/apps/<id>/rate` - Rate an app
- `GET /api/apps/<id>/ratings` - Get app ratings

### Upload
- `POST /api/upload/app` - Upload a new app
- `POST /api/upload/check-name` - Check if app name is available

### Statistics
- `GET /api/stats/overview` - Get overall statistics
- `GET /api/stats/categories` - Get stats by category
- `GET /api/stats/trending` - Get trending apps
- `GET /api/stats/developer/<name>` - Get developer statistics

## Usage Guide

### Browsing Apps
1. Navigate to "Browse Apps" from the main menu
2. Search by app name or developer
3. Filter by category
4. Sort by latest, downloads, rating, or name
5. Click "View Details" to see full app information

### Uploading an App
1. Go to "Upload App" section
2. Fill in app details (name, description, version, category)
3. Enter your name/team name as developer
4. Select your app file (supported formats: APK, ZIP, IPA, EXE, DMG, TAR.GZ, WHL, JAR)
5. Click "Upload App"

### Rating & Reviewing
1. Click on any app to view details
2. Scroll to "Rate This App" section
3. Click stars to set rating (1-5)
4. Optionally write a review
5. Click "Submit Rating"

## Supported File Formats

- Android: `.apk`
- Web: `.zip` (for web apps)
- iOS: `.ipa`
- Windows: `.exe`
- macOS: `.dmg`
- Archives: `.tar.gz`, `.whl`, `.jar`

## Database Models

### App
- id, name, description, version, category
- developer, developer_college
- file_path, file_type, file_size
- downloads, rating, rating_count
- created_at, updated_at

### Rating
- id, app_id, rating (1-5)
- review, created_at

### Statistics
- id, total_apps, total_downloads
- active_users, last_updated

## Features in Detail

### 1. Smart Search
- Search across app names, descriptions, and developer names
- Real-time filtering as you type

### 2. Category Management
- Organize apps by categories (Utility, Games, Education, Productivity, Social, Other)
- Filter apps by selected category

### 3. Sorting Options
- Latest: Recently uploaded apps first
- Most Downloaded: Popular apps first
- Top Rated: Highest rated apps first
- Name: Alphabetical order

### 4. Developer Profile
- View all apps by a developer
- Track developer statistics
- See average ratings across apps

### 5. Statistics Dashboard
- Real-time stats about total apps and downloads
- Top downloaded and top rated apps
- Category-wise distribution
- Trending apps algorithm

## Security Considerations

1. **File Upload Security**
   - File type validation (whitelist only known app formats)
   - File size limit (100MB)
   - Secure filename generation with timestamps
   - Files stored outside web root

2. **Data Protection**
   - SQL injection prevention via ORM
   - XSS protection via HTML escaping
   - CSRF protection (can be enabled)
   - Secure session handling

3. **Production Deployment**
   - Set `SECRET_KEY` in environment
   - Use production-grade database (PostgreSQL recommended)
   - Enable HTTPS
   - Set `DEBUG=False`
   - Use production WSGI server (Gunicorn, uWSGI)

## Deployment

### Using Gunicorn (Recommended)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker

```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## Troubleshooting

### Port Already in Use
```bash
# Use a different port
python app.py --port 5001
```

### Database Issues
```bash
# Reset database (development only)
python -c "from app import create_app; from db import reset_db; reset_db(create_app())"
```

### File Upload Not Working
- Check upload folder permissions
- Verify file size is within 100MB limit
- Ensure file format is supported

## Future Enhancements

- User authentication system
- Admin dashboard
- Payment gateway integration
- App versioning and updates
- Comments on apps
- Social sharing features
- Push notifications
- Advanced analytics
- API documentation (Swagger/OpenAPI)

## Contributing

For contributions, please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is developed for educational purposes at Rajalakshmi Engineering College.

## Contact & Support

**Guided by:** Surendar, Assistant Professor
**Institution:** Rajalakshmi Engineering College

For issues and support, please contact through the institution.

---

**Version:** 1.0.0  
**Last Updated:** 2024
