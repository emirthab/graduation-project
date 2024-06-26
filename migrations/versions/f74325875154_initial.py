"""initial

Revision ID: f74325875154
Revises: 
Create Date: 2024-01-12 04:03:07.009129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f74325875154'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attributes',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.Column('is_required', sa.Boolean(), nullable=False),
    sa.Column('show_in_filters', sa.Boolean(), nullable=False),
    sa.Column('allow_multiple', sa.Boolean(), nullable=False),
    sa.Column('allow_custom', sa.Boolean(), nullable=False),
    sa.Column('custom_input_type', sa.Enum('string', 'integer', 'decimal', create_constraint=True), nullable=True),
    sa.Column('input_prefix', sa.Unicode(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('files',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('show_name', sa.Unicode(length=255), nullable=False),
    sa.Column('file_path', sa.Unicode(length=255), nullable=False),
    sa.Column('extension', sa.Unicode(length=255), nullable=False),
    sa.Column('size', sa.Unicode(length=255), nullable=False),
    sa.Column('created_by', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('file_path')
    )
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('title', sa.Unicode(length=255), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('category_id', sa.BigInteger(), nullable=False),
    sa.Column('created_by', sa.BigInteger(), nullable=False),
    sa.Column('price', sa.DECIMAL(precision=12, scale=2), nullable=False),
    sa.Column('status', sa.Enum('waiting', 'unpublished', 'published', 'rejected', create_constraint=True), nullable=True),
    sa.Column('published_date', sa.DateTime(), nullable=True),
    sa.Column('reject_reason', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_devices',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('device_id', sa.Unicode(length=255), nullable=False),
    sa.Column('last_token', sa.Text(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_otp',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('secret_key', sa.Unicode(length=255), nullable=False),
    sa.Column('otp_code', sa.Integer(), nullable=False),
    sa.Column('otp_type', sa.Enum('register', 'reset_password', 'change_email', 'change_phone', create_constraint=True), nullable=True),
    sa.Column('expiry_date', sa.DateTime(), nullable=False),
    sa.Column('used', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attribute_values',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('attribute_id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.ForeignKeyConstraint(['attribute_id'], ['attributes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('image_id', sa.BigInteger(), nullable=True),
    sa.Column('parent_id', sa.BigInteger(), nullable=True),
    sa.Column('name', sa.Unicode(length=255), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['files.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_images',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('image_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['image_id'], ['files.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('email', sa.Unicode(length=255), nullable=False),
    sa.Column('phone', sa.Unicode(length=255), nullable=True),
    sa.Column('password_hash', sa.Unicode(length=255), nullable=False),
    sa.Column('full_name', sa.Unicode(length=255), nullable=False),
    sa.Column('profile_image_id', sa.BigInteger(), nullable=True),
    sa.Column('provider', sa.Enum('app', 'google.com', 'apple.com', create_constraint=True), nullable=False),
    sa.Column('explanation', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['profile_image_id'], ['files.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('category_attributes',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('category_id', sa.BigInteger(), nullable=False),
    sa.Column('attribute_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['attribute_id'], ['attributes.id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('event_type', sa.Enum('favorite', 'add_cart', 'purchase', 'detail_open', create_constraint=True), nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product_attributes',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('product_id', sa.BigInteger(), nullable=False),
    sa.Column('attribute_id', sa.BigInteger(), nullable=False),
    sa.Column('attribute_value_id', sa.BigInteger(), nullable=True),
    sa.Column('custom_attribute_value', sa.Unicode(length=255), nullable=True),
    sa.ForeignKeyConstraint(['attribute_id'], ['attributes.id'], ),
    sa.ForeignKeyConstraint(['attribute_value_id'], ['attribute_values.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_attributes')
    op.drop_table('events')
    op.drop_table('category_attributes')
    op.drop_table('users')
    op.drop_table('product_images')
    op.drop_table('categories')
    op.drop_table('attribute_values')
    op.drop_table('user_otp')
    op.drop_table('user_devices')
    op.drop_table('products')
    op.drop_table('files')
    op.drop_table('attributes')
    # ### end Alembic commands ###
