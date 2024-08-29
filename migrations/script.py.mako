"""${message}

Revision ID: ${up_revision}
<<<<<<< Updated upstream
Revises: ${down_revision | comma,n}
Create Date: ${create_date}

"""
from alembic import op
import sqlalchemy as sa
${imports if imports else ""}
=======
Revises: ${down_revision}
Create Date: ${create_date}

"""
>>>>>>> Stashed changes

# revision identifiers, used by Alembic.
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
<<<<<<< Updated upstream
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

=======

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}
>>>>>>> Stashed changes

def upgrade():
    ${upgrades if upgrades else "pass"}


def downgrade():
    ${downgrades if downgrades else "pass"}
