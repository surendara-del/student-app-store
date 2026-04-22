"""
Sample Data Initialization Script
This script populates the app store with sample data for demonstration
"""

from app import create_app
from db import db
from models import App, Statistics

def init_sample_data():
    """Initialize sample apps in the database"""
    app = create_app('development')
    
    with app.app_context():
        # Check if data already exists
        if App.query.first():
            print("Database already has apps. Skipping sample data initialization.")
            return
        
        # Sample apps data
        sample_apps = [
            {
                'name': 'Study Helper Pro',
                'description': 'A comprehensive study tool with notes, flashcards, and exam preparation features.',
                'version': '2.1.0',
                'category': 'Education',
                'developer': 'Arjun Kumar',
                'file_type': 'apk',
                'file_size': 45000000,
                'downloads': 234,
                'rating': 4.5,
                'rating_count': 12
            },
            {
                'name': 'Campus Connect',
                'description': 'Connect with your college mates, share notes, and coordinate study groups.',
                'version': '1.5.2',
                'category': 'Social',
                'developer': 'Priya Sharma',
                'file_type': 'apk',
                'file_size': 32000000,
                'downloads': 189,
                'rating': 4.2,
                'rating_count': 8
            },
            {
                'name': 'Code Compiler Mobile',
                'description': 'Write, compile, and execute code on the go. Supports Python, Java, C++, JavaScript.',
                'version': '3.0.1',
                'category': 'Utility',
                'developer': 'Rahul Patel',
                'file_type': 'apk',
                'file_size': 28000000,
                'downloads': 412,
                'rating': 4.8,
                'rating_count': 25
            },
            {
                'name': 'Exam Timer',
                'description': 'Practice exam timer with realistic test environments and analytics.',
                'version': '1.2.0',
                'category': 'Education',
                'developer': 'Anjali Verma',
                'file_type': 'apk',
                'file_size': 12000000,
                'downloads': 156,
                'rating': 4.7,
                'rating_count': 18
            },
            {
                'name': 'Campus Games',
                'description': 'Collection of fun games built by students. Quiz challenges, puzzles, and more!',
                'version': '2.0.0',
                'category': 'Games',
                'developer': 'Dev Team A',
                'file_type': 'apk',
                'file_size': 67000000,
                'downloads': 523,
                'rating': 4.3,
                'rating_count': 31
            },
            {
                'name': 'Task Master',
                'description': 'Project management and task tracking tool for collaborative assignments.',
                'version': '1.8.5',
                'category': 'Productivity',
                'developer': 'Sana Khan',
                'file_type': 'apk',
                'file_size': 18000000,
                'downloads': 267,
                'rating': 4.6,
                'rating_count': 15
            },
            {
                'name': 'Library Finder',
                'description': 'Find books, reserve them, and track library resources from campus library.',
                'version': '1.0.3',
                'category': 'Utility',
                'developer': 'Vikram Singh',
                'file_type': 'apk',
                'file_size': 15000000,
                'downloads': 98,
                'rating': 4.4,
                'rating_count': 9
            },
            {
                'name': 'Quiz Master',
                'description': 'Create and take quizzes with your classmates. Compete on leaderboards!',
                'version': '2.3.0',
                'category': 'Education',
                'developer': 'Quiz Dev Team',
                'file_type': 'apk',
                'file_size': 22000000,
                'downloads': 345,
                'rating': 4.5,
                'rating_count': 22
            },
            {
                'name': 'College Events',
                'description': 'Stay updated with all college events, clubs, and activities happening around campus.',
                'version': '1.4.1',
                'category': 'Social',
                'developer': 'Event Team',
                'file_type': 'apk',
                'file_size': 19000000,
                'downloads': 201,
                'rating': 4.2,
                'rating_count': 11
            },
            {
                'name': 'Attendance Tracker',
                'description': 'Track your class attendance, marks, and academic performance.',
                'version': '1.1.0',
                'category': 'Education',
                'developer': 'Admin Panel',
                'file_type': 'apk',
                'file_size': 8000000,
                'downloads': 589,
                'rating': 4.7,
                'rating_count': 28
            },
            {
                'name': 'Algorithm Visualizer',
                'description': 'Visualize sorting, searching, and graph algorithms step by step.',
                'version': '1.6.2',
                'category': 'Education',
                'developer': 'Akshay Desai',
                'file_type': 'apk',
                'file_size': 35000000,
                'downloads': 276,
                'rating': 4.9,
                'rating_count': 16
            },
            {
                'name': 'Photo Gallery Pro',
                'description': 'Beautiful photo gallery app with filters, editing, and cloud backup.',
                'version': '2.2.0',
                'category': 'Utility',
                'developer': 'Creative Studio',
                'file_type': 'apk',
                'file_size': 42000000,
                'downloads': 423,
                'rating': 4.4,
                'rating_count': 19
            }
        ]
        
        # Create and add sample apps
        for app_data in sample_apps:
            # Create dummy file path (file doesn't actually need to exist for this sample)
            file_name = f"{app_data['name'].replace(' ', '_')}.{app_data['file_type']}"
            file_path = f"uploads/{file_name}"
            
            new_app = App(
                name=app_data['name'],
                description=app_data['description'],
                version=app_data['version'],
                category=app_data['category'],
                developer=app_data['developer'],
                developer_college='Rajalakshmi Engineering College',
                file_path=file_path,
                file_type=app_data['file_type'],
                file_size=app_data['file_size'],
                downloads=app_data['downloads'],
                rating=app_data['rating'],
                rating_count=app_data['rating_count']
            )
            db.session.add(new_app)
        
        # Create statistics
        stats = Statistics(
            total_apps=len(sample_apps),
            total_downloads=sum(app['downloads'] for app in sample_apps),
            active_users=156
        )
        db.session.add(stats)
        
        # Commit all changes
        db.session.commit()
        
        print(f"✅ Successfully added {len(sample_apps)} sample apps!")
        print(f"📊 Statistics: {len(sample_apps)} apps, {sum(app['downloads'] for app in sample_apps)} total downloads")
        print("\n🎓 Sample apps created by students from various departments:")
        for app_data in sample_apps:
            print(f"   • {app_data['name']} by {app_data['developer']}")

if __name__ == '__main__':
    init_sample_data()
