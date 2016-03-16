"""empty message

Revision ID: 42f0ca2b47de
Revises: b758eb9865f6
Create Date: 2016-03-15 22:41:21.348508

"""

# revision identifiers, used by Alembic.
revision = '42f0ca2b47de'
down_revision = 'b758eb9865f6'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('concepts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('edited_on', sa.DateTime(), nullable=False),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('concept_type', sa.String(length=20), nullable=False),
    sa.Column('input_terms', postgresql.JSON(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('concepts')
    ### end Alembic commands ###
