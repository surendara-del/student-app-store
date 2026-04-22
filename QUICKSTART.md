# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### On Linux/macOS

```bash
# 1. Navigate to the project directory
cd student-app-store

# 2. Run the startup script
chmod +x run.sh
./run.sh

# 3. Open your browser and visit:
# http://localhost:5000
```

### On Windows

```batch
# 1. Navigate to the project directory
cd student-app-store

# 2. Run the startup batch file
run.bat

# 3. Open your browser and visit:
# http://localhost:5000
```

## Manual Setup (If Scripts Don't Work)

### Step 1: Create Virtual Environment
```bash
python -m venv venv

# Activate it:
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python app.py
```

## 📝 First Time Users

1. **Access the App Store**: Open http://localhost:5000 in your browser
2. **Browse Apps**: Click "Browse Apps" to see available applications
3. **Upload Your App**: 
   - Click "Upload App"
   - Fill in app details
   - Upload your app file (.apk, .zip, .ipa, etc.)
   - Click "Upload App"
4. **Rate & Review**: Click on any app to rate it and read reviews
5. **View Statistics**: Check out the "Statistics" page to see trends

## 🎯 Features to Try

### 1. Search & Filter
- Use the search box to find apps by name or developer
- Filter by category
- Sort by latest, most downloaded, or top rated

### 2. Upload an App
- Give your app a unique name
- Add a description
- Choose a category
- Upload your app file
- Your app will appear immediately in the store!

### 3. Rate Apps
- Click "View Details" on any app
- Rate it from 1-5 stars
- Write a review (optional)
- See how the community rates apps

### 4. Check Statistics
- View total apps and downloads
- See top downloaded apps
- Check top rated apps
- Analyze app distribution by category

## 🔧 Troubleshooting

### Port 5000 is Already in Use
Edit `app.py` and change the port:
```python
if __name__ == '__main__':
    app = create_app()
    app.run(port=5001)  # Change to any available port
```

### Dependencies Installation Error
Try updating pip first:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### File Upload Not Working
- Ensure the `uploads` folder exists
- Check that you have write permissions to the uploads folder
- Verify the file is not larger than 100MB

### Database Error
Reset the database:
```bash
rm app_store.db  # Remove existing database
python app.py    # It will recreate on startup
```

## 📚 Sample Data

To populate the app store with sample apps, you can:

1. Upload some test apps manually
2. Or modify `routes/apps.py` to include sample data on first run

## 🌐 Accessing from Other Computers

If you want to access the app from another computer on your network:

1. Find your computer's IP address:
   - Linux/macOS: `ifconfig` (look for inet address)
   - Windows: `ipconfig` (look for IPv4 Address)

2. Update `app.py`:
```python
app.run(host='0.0.0.0', port=5000)
```

3. Access from another computer: `http://YOUR_IP:5000`

## 📖 Documentation

- See `README.md` for detailed documentation
- Check `config.py` for configuration options
- Review `models.py` for database schema

## ✨ Next Steps

- Customize the college name in `templates/index.html`
- Add your college logo
- Configure email notifications
- Set up user authentication

## 💡 Tips

1. Use meaningful app names and descriptions
2. Choose the most appropriate category for your app
3. Add a proper review - it helps others decide
4. Keep app files organized in the uploads folder
5. Regularly check statistics to see what's popular

## 🎓 Educational Use

This app store is perfect for:
- Showcasing student projects
- Learning web development
- Understanding app distribution
- Practicing collaborative development
- Teaching full-stack development

## 🆘 Need Help?

- Check the README.md for more detailed information
- Review the API endpoints in README.md
- Check console output for error messages
- Verify all dependencies are installed

---

**Guided by:** Surendar, Assistant Professor  
**Institution:** Rajalakshmi Engineering College

Happy coding! 🚀
