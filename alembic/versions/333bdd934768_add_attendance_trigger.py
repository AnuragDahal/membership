"""add_attendance_trigger

Revision ID: 333bdd934768
Revises: d7ccdf50b71a
Create Date: 2025-11-27 22:16:22.098799

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '333bdd934768'
down_revision: Union[str, Sequence[str], None] = 'd7ccdf50b71a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create the function that will increment total_checkins
    op.execute("""
        CREATE OR REPLACE FUNCTION increment_member_checkins()
        RETURNS TRIGGER AS $$
        BEGIN
            UPDATE members
            SET total_checkins = total_checkins + 1
            WHERE id = NEW.member_id;
            RETURN NEW;
        END;
        $$ LANGUAGE plpgsql;
    """)
    
    # Create the trigger that fires after insert on attendance
    op.execute("""
        CREATE TRIGGER update_total_checkins_trigger
        AFTER INSERT ON attendance
        FOR EACH ROW
        EXECUTE FUNCTION increment_member_checkins();
    """)


def downgrade() -> None:
    """Downgrade schema."""
    # Drop the trigger first
    op.execute("DROP TRIGGER IF EXISTS update_total_checkins_trigger ON attendance;")
    
    # Then drop the function
    op.execute("DROP FUNCTION IF EXISTS increment_member_checkins();")

