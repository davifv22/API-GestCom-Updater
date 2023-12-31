"""empty message

Revision ID: 9662a843df43
Revises: 
Create Date: 2023-10-08 03:07:41.578244

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9662a843df43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('versao_pacotes',
    sa.Column('tipo_sistema', sa.String(length=10), nullable=False),
    sa.Column('versao', sa.String(length=50), nullable=False),
    sa.Column('release', sa.String(length=50), nullable=False),
    sa.Column('dt_upload', sa.Date(), nullable=False),
    sa.Column('nome_maquina', sa.String(length=50), nullable=False),
    sa.Column('cidade', sa.String(length=50), nullable=False),
    sa.Column('gestcomexec', sa.Boolean(), nullable=False),
    sa.Column('proexec', sa.Boolean(), nullable=False),
    sa.Column('contasexec', sa.Boolean(), nullable=False),
    sa.Column('proggestcomexec', sa.Boolean(), nullable=False),
    sa.Column('requerimentoexec', sa.Boolean(), nullable=False),
    sa.Column('divida_ativaexec', sa.Boolean(), nullable=False),
    sa.Column('atend_publicoexec', sa.Boolean(), nullable=False),
    sa.Column('contasrpt', sa.String(length=255), nullable=False),
    sa.Column('requerimentorpt', sa.String(length=255), nullable=False),
    sa.Column('nome_arquivo', sa.String(length=50), nullable=False),
    sa.Column('link_download', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('tipo_sistema', 'versao', 'release', 'nome_arquivo')
    )
    op.drop_table('responsavel')
    with op.batch_alter_table('versao', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome_arquivo', sa.String(length=31), nullable=False))
        batch_op.alter_column('link_download',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('versao', schema=None) as batch_op:
        batch_op.alter_column('link_download',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
        batch_op.drop_column('nome_arquivo')

    op.create_table('responsavel',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', mysql.VARCHAR(length=50), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('versao_pacotes')
    # ### end Alembic commands ###
