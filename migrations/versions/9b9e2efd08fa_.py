"""empty message

Revision ID: 9b9e2efd08fa
Revises: 
Create Date: 2019-02-28 15:35:42.453150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b9e2efd08fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('work_years', sa.SmallInteger(), nullable=True),
    sa.Column('role', sa.Integer(), nullable=True),
    sa.Column('resume_url', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_index(op.f('ix_user_name'), 'user', ['name'], unique=True)
    op.create_table('company',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False, comment='公司名'),
    sa.Column('slogan', sa.String(length=24), nullable=False, comment='slogan'),
    sa.Column('logo', sa.String(length=64), nullable=False),
    sa.Column('website', sa.String(length=64), nullable=False),
    sa.Column('contact', sa.String(length=24), nullable=False, comment='联系方式'),
    sa.Column('location', sa.String(length=24), nullable=False, comment='公司地址'),
    sa.Column('short_description', sa.String(length=10), nullable=True, comment='一句话描述'),
    sa.Column('full_description', sa.String(length=255), nullable=True, comment='关于我们，公司详情描述'),
    sa.Column('tags', sa.String(length=128), nullable=True, comment='公司标签，用多个逗号隔开'),
    sa.Column('stack', sa.String(length=128), nullable=True, comment='公司技术栈，用多个逗号隔开'),
    sa.Column('team_des', sa.String(length=255), nullable=True, comment='团队介绍'),
    sa.Column('welfare', sa.String(length=255), nullable=True, comment='公司福利'),
    sa.Column('trade', sa.String(length=32), nullable=True, comment='行业'),
    sa.Column('funding', sa.String(length=32), nullable=True, comment='融资阶段'),
    sa.Column('city', sa.String(length=32), nullable=True, comment='所在城市'),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_company_name'), 'company', ['name'], unique=True)
    op.create_index(op.f('ix_company_slogan'), 'company', ['slogan'], unique=True)
    op.create_table('job',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True, comment='职位名称'),
    sa.Column('salary_max', sa.Integer(), nullable=True),
    sa.Column('salary_min', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=32), nullable=True, comment='工作地点'),
    sa.Column('tags', sa.String(length=128), nullable=True, comment='职位标签'),
    sa.Column('experience_requirement', sa.String(length=32), nullable=True, comment='工作经验要求'),
    sa.Column('degree_requirement', sa.String(length=32), nullable=True, comment='学历要求'),
    sa.Column('is_fulltime', sa.Boolean(), nullable=True, comment='是否全职'),
    sa.Column('is_open', sa.Boolean(), nullable=True, comment='是否在招聘'),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.Column('view_count', sa.Integer(), nullable=True, comment='该岗位浏览数'),
    sa.Column('description', sa.String(length=1024), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True, comment='投递状态'),
    sa.Column('location', sa.String(length=255), nullable=True, comment='企业回应'),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_job',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('job_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['job_id'], ['job.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_job')
    op.drop_table('delivery')
    op.drop_table('job')
    op.drop_index(op.f('ix_company_slogan'), table_name='company')
    op.drop_index(op.f('ix_company_name'), table_name='company')
    op.drop_table('company')
    op.drop_index(op.f('ix_user_name'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###