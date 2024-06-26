"""fixRealtionship

Revision ID: 2a9465852d10
Revises: 
Create Date: 2024-03-29 16:15:43.654567

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a9465852d10'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=30), nullable=False),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('iden_doc', sa.String(length=30), nullable=True),
    sa.Column('address', sa.String(length=30), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.Column('status', sa.String(length=1), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('username'),
    sa.UniqueConstraint('email')
    )
    op.create_table('send',
    sa.Column('id_record', sa.Integer(), nullable=False),
    sa.Column('send_date', sa.Date(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id_record', 'send_date')
    )
    op.create_table('admin',
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['person.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('patient',
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['person.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('degree',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('created_by', sa.String(length=15), nullable=False),
    sa.Column('updated_by', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['admin.username'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['admin.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('evaluation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('result', sa.Numeric(precision=2, scale=2), nullable=False),
    sa.Column('image', sa.String(length=500), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['patient.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recommendation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('entry_value', sa.Integer(), nullable=False),
    sa.Column('end_value', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.String(length=15), nullable=False),
    sa.Column('updated_by', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['admin.username'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['admin.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('speciality',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('created_by', sa.String(length=15), nullable=False),
    sa.Column('updated_by', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['admin.username'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['admin.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(length=500), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('created_by', sa.String(length=15), nullable=False),
    sa.Column('updated_by', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['admin.username'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['admin.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('university',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('created_by', sa.String(length=15), nullable=False),
    sa.Column('updated_by', sa.String(length=15), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['admin.username'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['admin.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctor',
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('contact', sa.String(length=30), nullable=False),
    sa.Column('gradution_year', sa.String(length=5), nullable=False),
    sa.Column('address', sa.String(length=300), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.Column('degree', sa.Integer(), nullable=False),
    sa.Column('speciality', sa.Integer(), nullable=False),
    sa.Column('university', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['degree'], ['degree.id'], ),
    sa.ForeignKeyConstraint(['speciality'], ['speciality.id'], ),
    sa.ForeignKeyConstraint(['university'], ['university.id'], ),
    sa.ForeignKeyConstraint(['username'], ['person.username'], ),
    sa.PrimaryKeyConstraint('username')
    )
    op.create_table('record',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_evaluation', sa.Integer(), nullable=False),
    sa.Column('seq_no', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id_evaluation'], ['evaluation.id'], ),
    sa.PrimaryKeyConstraint('id', 'id_evaluation')
    )
    op.create_table('response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('answer', sa.String(length=500), nullable=False),
    sa.Column('created_at', sa.Date(), nullable=True),
    sa.Column('updated_at', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['id'], ['survey.id'], ),
    sa.ForeignKeyConstraint(['username'], ['patient.username'], ),
    sa.PrimaryKeyConstraint('id', 'username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('response')
    op.drop_table('record')
    op.drop_table('doctor')
    op.drop_table('university')
    op.drop_table('survey')
    op.drop_table('speciality')
    op.drop_table('recommendation')
    op.drop_table('evaluation')
    op.drop_table('degree')
    op.drop_table('patient')
    op.drop_table('admin')
    op.drop_table('send')
    op.drop_table('person')
    # ### end Alembic commands ###
