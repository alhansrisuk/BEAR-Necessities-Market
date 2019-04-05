"""empty message

Revision ID: 66070572435d
Revises: a7852c8b3c34
Create Date: 2019-04-05 17:26:00.833661

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66070572435d'
down_revision = 'a7852c8b3c34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('authenticated', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('registered_on', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('role', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'username')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=80), nullable=True))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'role')
    op.drop_column('users', 'registered_on')
    op.drop_column('users', 'authenticated')
    # ### end Alembic commands ###
