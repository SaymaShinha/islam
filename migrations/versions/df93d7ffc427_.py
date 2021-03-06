"""empty message

Revision ID: df93d7ffc427
Revises: 79da1214a30f
Create Date: 2020-12-23 08:58:31.423671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df93d7ffc427'
down_revision = '79da1214a30f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allah__names',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Ar_name', sa.String(length=300), nullable=False),
    sa.Column('Ar_transliteration', sa.String(length=300), nullable=False),
    sa.Column('Pronunciation', sa.String(length=300), nullable=False),
    sa.Column('Meaning_En', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('allah__names')
    # ### end Alembic commands ###
