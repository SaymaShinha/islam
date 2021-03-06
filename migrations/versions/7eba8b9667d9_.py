"""empty message

Revision ID: 7eba8b9667d9
Revises: a4c153faa8a3
Create Date: 2020-12-29 05:22:30.288792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eba8b9667d9'
down_revision = 'a4c153faa8a3'
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
