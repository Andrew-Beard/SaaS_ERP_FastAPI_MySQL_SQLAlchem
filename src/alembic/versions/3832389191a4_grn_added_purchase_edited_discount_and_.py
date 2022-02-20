"""grn added, purchase edited, discount and cost added in invoice line, four new column added in stock table and two deleted, depo price added in medicine, trade and tradehistory tables added on par with manufacturer

Revision ID: 3832389191a4
Revises: 5bbe36046528
Create Date: 2022-02-09 10:40:35.448843

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "3832389191a4"
down_revision = "5bbe36046528"
branch_labels = None
depends_on = None

# fmt: off


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trade_histories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('purchased_amount', sa.Float(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('trades',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('closing_balance', sa.Float(), nullable=True),
    sa.Column('outstanding_amount', sa.Float(), nullable=True),
    sa.Column('overdue_amount', sa.Float(), nullable=True),
    sa.Column('manufacturer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manufacturer_id'], ['manufacturers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('grns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('depo_price', sa.Float(), nullable=False),
    sa.Column('vat', sa.Integer(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=False),
    sa.Column('expiry_date', sa.Date(), nullable=True),
    sa.Column('medicine_id', sa.Integer(), nullable=True),
    sa.Column('purchase_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['medicine_id'], ['medicines.id'], ondelete='SET NULL'),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchase_orders.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('addresses_ibfk_1', 'addresses', type_='foreignkey')
    op.drop_constraint('addresses_ibfk_2', 'addresses', type_='foreignkey')
    op.create_foreign_key(None, 'addresses', 'customers', ['customer_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'addresses', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    op.add_column('invoice_order_lines', sa.Column('unit_price', sa.Float(), nullable=False))
    op.add_column('invoice_order_lines', sa.Column('discount', sa.Integer(), nullable=True))
    op.drop_constraint('invoice_order_lines_ibfk_2', 'invoice_order_lines', type_='foreignkey')
    op.drop_constraint('invoice_order_lines_ibfk_1', 'invoice_order_lines', type_='foreignkey')
    op.create_foreign_key(None, 'invoice_order_lines', 'medicines', ['medicine_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'invoice_order_lines', 'invoice_orders', ['invoice_id'], ['id'], ondelete='CASCADE')
    op.drop_column('invoice_order_lines', 'price')
    op.drop_constraint('invoice_orders_ibfk_1', 'invoice_orders', type_='foreignkey')
    op.drop_constraint('invoice_orders_ibfk_2', 'invoice_orders', type_='foreignkey')
    op.create_foreign_key(None, 'invoice_orders', 'customers', ['customer_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'invoice_orders', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.drop_column('manufacturers', 'growth')
    op.drop_column('manufacturers', 'market_share')
    op.drop_column('manufacturers', 'contact_list')
    op.drop_column('manufacturers', 'total_brands')
    op.drop_column('manufacturers', 'headquarter')
    op.drop_column('manufacturers', 'established_in')
    op.drop_column('manufacturers', 'total_generics')
    op.add_column('medicines', sa.Column('depo_price', sa.Float(), nullable=True))
    op.drop_constraint('medicines_ibfk_1', 'medicines', type_='foreignkey')
    op.create_foreign_key(None, 'medicines', 'manufacturers', ['manufacturer_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint('purchase_order_lines_ibfk_2', 'purchase_order_lines', type_='foreignkey')
    op.drop_constraint('purchase_order_lines_ibfk_1', 'purchase_order_lines', type_='foreignkey')
    op.create_foreign_key(None, 'purchase_order_lines', 'medicines', ['medicine_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'purchase_order_lines', 'purchase_orders', ['purchase_id'], ['id'], ondelete='CASCADE')
    op.drop_column('purchase_order_lines', 'expiry_date')
    op.drop_column('purchase_order_lines', 'cost')
    op.drop_column('purchase_order_lines', 'buying_price')
    op.drop_column('purchase_order_lines', 'selling_price')
    op.drop_constraint('purchase_orders_ibfk_1', 'purchase_orders', type_='foreignkey')
    op.create_foreign_key(None, 'purchase_orders', 'users', ['user_id'], ['id'], ondelete='SET NULL')
    op.add_column('stocks', sa.Column('critical_stock', sa.Integer(), nullable=True))
    op.add_column('stocks', sa.Column('last_date_of_purchase', sa.DateTime(), nullable=True))
    op.add_column('stocks', sa.Column('last_purchased_quantity', sa.Integer(), nullable=True))
    op.add_column('stocks', sa.Column('gross_margin', sa.Float(), nullable=True))
    op.drop_constraint('stocks_ibfk_1', 'stocks', type_='foreignkey')
    op.create_foreign_key(None, 'stocks', 'medicines', ['medicine_id'], ['id'], ondelete='CASCADE')
    op.drop_column('stocks', 'last_transacted_quantity')
    op.drop_column('stocks', 'last_transacted_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stocks', sa.Column('last_transacted_date', mysql.DATETIME(), nullable=True))
    op.add_column('stocks', sa.Column('last_transacted_quantity', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'stocks', type_='foreignkey')
    op.create_foreign_key('stocks_ibfk_1', 'stocks', 'medicines', ['medicine_id'], ['id'])
    op.drop_column('stocks', 'gross_margin')
    op.drop_column('stocks', 'last_purchased_quantity')
    op.drop_column('stocks', 'last_date_of_purchase')
    op.drop_column('stocks', 'critical_stock')
    op.drop_constraint(None, 'purchase_orders', type_='foreignkey')
    op.create_foreign_key('purchase_orders_ibfk_1', 'purchase_orders', 'users', ['user_id'], ['id'])
    op.add_column('purchase_order_lines', sa.Column('selling_price', mysql.FLOAT(), nullable=False))
    op.add_column('purchase_order_lines', sa.Column('buying_price', mysql.FLOAT(), nullable=False))
    op.add_column('purchase_order_lines', sa.Column('cost', mysql.FLOAT(), nullable=False))
    op.add_column('purchase_order_lines', sa.Column('expiry_date', sa.DATE(), nullable=True))
    op.drop_constraint(None, 'purchase_order_lines', type_='foreignkey')
    op.drop_constraint(None, 'purchase_order_lines', type_='foreignkey')
    op.create_foreign_key('purchase_order_lines_ibfk_1', 'purchase_order_lines', 'medicines', ['medicine_id'], ['id'])
    op.create_foreign_key('purchase_order_lines_ibfk_2', 'purchase_order_lines', 'purchase_orders', ['purchase_id'], ['id'])
    op.drop_constraint(None, 'medicines', type_='foreignkey')
    op.create_foreign_key('medicines_ibfk_1', 'medicines', 'manufacturers', ['manufacturer_id'], ['id'])
    op.drop_column('medicines', 'depo_price')
    op.add_column('manufacturers', sa.Column('total_generics', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('manufacturers', sa.Column('established_in', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('manufacturers', sa.Column('headquarter', mysql.VARCHAR(length=500), nullable=True))
    op.add_column('manufacturers', sa.Column('total_brands', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('manufacturers', sa.Column('contact_list', sa.BLOB(), nullable=True))
    op.add_column('manufacturers', sa.Column('market_share', mysql.VARCHAR(length=10), nullable=True))
    op.add_column('manufacturers', sa.Column('growth', mysql.VARCHAR(length=10), nullable=True))
    op.drop_constraint(None, 'invoice_orders', type_='foreignkey')
    op.drop_constraint(None, 'invoice_orders', type_='foreignkey')
    op.create_foreign_key('invoice_orders_ibfk_2', 'invoice_orders', 'users', ['user_id'], ['id'])
    op.create_foreign_key('invoice_orders_ibfk_1', 'invoice_orders', 'customers', ['customer_id'], ['id'])
    op.add_column('invoice_order_lines', sa.Column('price', mysql.FLOAT(), nullable=False))
    op.drop_constraint(None, 'invoice_order_lines', type_='foreignkey')
    op.drop_constraint(None, 'invoice_order_lines', type_='foreignkey')
    op.create_foreign_key('invoice_order_lines_ibfk_1', 'invoice_order_lines', 'invoice_orders', ['invoice_id'], ['id'])
    op.create_foreign_key('invoice_order_lines_ibfk_2', 'invoice_order_lines', 'medicines', ['medicine_id'], ['id'])
    op.drop_column('invoice_order_lines', 'discount')
    op.drop_column('invoice_order_lines', 'unit_price')
    op.drop_constraint(None, 'addresses', type_='foreignkey')
    op.drop_constraint(None, 'addresses', type_='foreignkey')
    op.create_foreign_key('addresses_ibfk_2', 'addresses', 'users', ['user_id'], ['id'])
    op.create_foreign_key('addresses_ibfk_1', 'addresses', 'customers', ['customer_id'], ['id'])
    op.drop_table('grns')
    op.drop_table('trades')
    op.drop_table('trade_histories')
    # ### end Alembic commands ###
