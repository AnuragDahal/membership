"""
Database seeding script for the membership management system.

This script populates the database with sample data for:
- Members
- Plans
- Subscriptions

Usage:
    uv run python -m app.lib.seed
"""

import asyncio
from datetime import datetime, timedelta
from app.core.db import AsyncSessionLocal
from app.models.members import Member
from app.models.plans import Plan
from app.models.subscriptions import Subscription


async def seed_database():
    """Seed the database with sample data."""
    async with AsyncSessionLocal() as session:
        try:
            print("🌱 Starting database seeding...")

            # Seed Plans
            print("\n📋 Creating plans...")
            plans_data = [
                {"name": "Monthly Basic", "price": 1000, "duration_days": 30},
                {"name": "Quarterly Premium", "price": 2500, "duration_days": 90},
                {"name": "Annual VIP", "price": 8000, "duration_days": 365},
                {"name": "Weekly Trial", "price": 300, "duration_days": 7},
            ]

            plans = []
            for plan_data in plans_data:
                plan = Plan(**plan_data)
                session.add(plan)
                plans.append(plan)

            await session.commit()
            print(f"✅ Created {len(plans)} plans")

            # Refresh to get IDs
            for plan in plans:
                await session.refresh(plan)

            # Seed Members
            print("\n👥 Creating members...")
            members_data = [
                {
                    "name": "Alice Johnson",
                    "email": "alice.johnson@example.com",
                    "phone": "1234567890",
                    "status": "active",
                },
                {
                    "name": "Bob Smith",
                    "email": "bob.smith@example.com",
                    "phone": "2345678901",
                    "status": "active",
                },
                {
                    "name": "Charlie Brown",
                    "email": "charlie.brown@example.com",
                    "phone": "3456789012",
                    "status": "active",
                },
                {
                    "name": "Diana Prince",
                    "email": "diana.prince@example.com",
                    "phone": "4567890123",
                    "status": "active",
                },
                {
                    "name": "Eve Wilson",
                    "email": "eve.wilson@example.com",
                    "phone": "5678901234",
                    "status": "inactive",
                },
            ]

            members = []
            for member_data in members_data:
                member = Member(**member_data)
                session.add(member)
                members.append(member)

            await session.commit()
            print(f"✅ Created {len(members)} members")

            # Refresh to get IDs
            for member in members:
                await session.refresh(member)

            # Seed Subscriptions
            print("\n📝 Creating subscriptions...")
            subscriptions_data = [
                {
                    "member_id": members[0].id,  # Alice - Monthly Basic
                    "plan_id": plans[0].id,
                    "start_date": datetime.utcnow(),
                    "end_date": datetime.utcnow() + timedelta(days=30),
                },
                {
                    "member_id": members[1].id,  # Bob - Quarterly Premium
                    "plan_id": plans[1].id,
                    "start_date": datetime.utcnow(),
                    "end_date": datetime.utcnow() + timedelta(days=90),
                },
                {
                    "member_id": members[2].id,  # Charlie - Annual VIP
                    "plan_id": plans[2].id,
                    "start_date": datetime.utcnow(),
                    "end_date": datetime.utcnow() + timedelta(days=365),
                },
                {
                    "member_id": members[3].id,  # Diana - Weekly Trial
                    "plan_id": plans[3].id,
                    "start_date": datetime.utcnow(),
                    "end_date": datetime.utcnow() + timedelta(days=7),
                },
            ]

            subscriptions = []
            for sub_data in subscriptions_data:
                subscription = Subscription(**sub_data)
                session.add(subscription)
                subscriptions.append(subscription)

            await session.commit()
            print(f"✅ Created {len(subscriptions)} subscriptions")

            print("\n✨ Database seeding completed successfully!")
            print("\n📊 Summary:")
            print(f"   - Plans: {len(plans)}")
            print(f"   - Members: {len(members)}")
            print(f"   - Subscriptions: {len(subscriptions)}")
            print("\n💡 Tip: Use POST /attendance/ to create attendance records")
            print("   The database trigger will automatically increment total_checkins!")

        except Exception as e:
            print(f"\n❌ Error during seeding: {e}")
            await session.rollback()
            raise


if __name__ == "__main__":
    print("=" * 60)
    print("  MEMBERSHIP MANAGEMENT SYSTEM - DATABASE SEEDER")
    print("=" * 60)
    asyncio.run(seed_database())
