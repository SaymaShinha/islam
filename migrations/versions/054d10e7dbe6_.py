"""empty message

Revision ID: 054d10e7dbe6
Revises: d0e5fae72c27
Create Date: 2020-12-24 22:40:57.487616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '054d10e7dbe6'
down_revision = 'd0e5fae72c27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rev__quran__info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chronological_order', sa.Integer(), nullable=False),
    sa.Column('traditional_order', sa.Integer(), nullable=False),
    sa.Column('surah_ar_name', sa.String(length=50), nullable=False),
    sa.Column('surah_en_name', sa.String(length=50), nullable=False),
    sa.Column('surah_en_name_translation', sa.String(length=50), nullable=False),
    sa.Column('location_of_revelation', sa.String(length=50), nullable=False),
    sa.Column('total_ayah', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rev__quran__info')
    # ### end Alembic commands ###
