from app import app, db
from app.models import User, Program, Run, Product, Order
from datetime import date

def seed_database():
    with app.app_context():
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()

        print("Seeding Programs (20 rows)...")
        programs = [
            Program(program_name="Couch to 5K", target_level="Beginner", duration_weeks=8, description="Gradual program for new runners."),
            Program(program_name="5K Speed Builder", target_level="Intermediate", duration_weeks=6, description="Improve your 5k personal record."),
            Program(program_name="10K Foundation", target_level="Beginner", duration_weeks=10, description="Step up from 5k to 10k."),
            Program(program_name="10K Performance", target_level="Intermediate", duration_weeks=8, description="Optimize pace for 10k races."),
            Program(program_name="Half Marathon Intro", target_level="Intermediate", duration_weeks=12, description="Prepare for your first 21k."),
            Program(program_name="Half Marathon Endurance", target_level="Advanced", duration_weeks=12, description="Build sustained half marathon pace."),
            Program(program_name="Marathon Base Builder", target_level="Intermediate", duration_weeks=16, description="High mileage base building for marathon."),
            Program(program_name="Marathon Mastery", target_level="Advanced", duration_weeks=18, description="Comprehensive 42k marathon preparation."),
            Program(program_name="Ultra Endurance 50K", target_level="Advanced", duration_weeks=20, description="Introductory trail ultra marathon plan."),
            Program(program_name="Heart Rate Zone Training", target_level="All Levels", duration_weeks=6, description="Aerobic engine development."),
            Program(program_name="Interval & Hill Repeats", target_level="Intermediate", duration_weeks=4, description="Power and VO2 max improvement."),
            Program(program_name="Recovery & Mobility Run", target_level="All Levels", duration_weeks=4, description="Active recovery routine for runners."),
            Program(program_name="Trail Running Essentials", target_level="Beginner", duration_weeks=6, description="Technique and endurance for off-road."),
            Program(program_name="5km Sub-20 Challenge", target_level="Advanced", duration_weeks=8, description="Targeted track workouts for sub-20min 5k."),
            Program(program_name="10km Sub-45 Challenge", target_level="Advanced", duration_weeks=8, description="Pace-focused training for sub-45min 10k."),
            Program(program_name="Post-Injury Return to Run", target_level="Beginner", duration_weeks=6, description="Low impact return-to-running plan."),
            Program(program_name="Weight Loss Aerobic Plan", target_level="Beginner", duration_weeks=10, description="Fat burning zone running schedules."),
            Program(program_name="Senior Runner Fitness", target_level="Beginner", duration_weeks=8, description="Gentle joint-friendly running routines."),
            Program(program_name="Sprint & Agility Prep", target_level="Intermediate", duration_weeks=4, description="Short burst speed work."),
            Program(program_name="Winter Base Maintenance", target_level="All Levels", duration_weeks=8, description="Maintain aerobic fitness off-season.")
        ]
        db.session.add_all(programs)

        print("Seeding Sample Users...")
        user1 = User(username="Catriona", email="catriona@example.com", password_hash="hashed_pw_1", fitness_level="Intermediate", running_goal="Sub-20 5K", program_id=2)
        user2 = User(username="JohnRunner", email="john@example.com", password_hash="hashed_pw_2", fitness_level="Beginner", running_goal="Complete 5K", program_id=1)
        db.session.add_all([user1, user2])

        print("Seeding Sample Products...")
        products = [
            Product(product_name="Pro Trail Shoes", category="Footwear", price=129.99, stock_quantity=15),
            Product(product_name="GPS Fitness Watch", category="Electronics", price=199.99, stock_quantity=10),
            Product(product_name="Hydration Vest", category="Accessories", price=49.99, stock_quantity=25)
        ]
        db.session.add_all(products)

        db.session.commit()
        print("Database populated successfully with 20+ records!")

if __name__ == "__main__":
    seed_database()