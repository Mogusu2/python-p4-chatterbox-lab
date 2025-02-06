#!/usr/bin/env python3

from random import choice as rc
from faker import Faker
from app import app
from models import db, Message

fake = Faker()

usernames = [fake.first_name() for i in range(4)]
if "Duane" not in usernames:
    usernames.append("Duane")

def make_messages():
    with app.app_context():
        print("🔄 Deleting old messages...")
        Message.query.delete()  # Clear existing data
        db.session.commit()  

        messages = []

        print("✅ Seeding new messages...")
        for i in range(20):
            message = Message(
                body=fake.sentence(),
                username=rc(usernames),
            )
            messages.append(message)

        db.session.add_all(messages)
        db.session.commit()
        
        print(f"✅ Seeded {len(messages)} messages.")
        for msg in messages[:5]:  # Print the first 5 messages for confirmation
            print(f"📩 {msg.username}: {msg.body}")       

if __name__ == '__main__':
    with app.app_context():
        make_messages()
