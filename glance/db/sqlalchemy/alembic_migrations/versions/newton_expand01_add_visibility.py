# Copyright 2013 OpenStack Foundation
# Copyright 2013 Intel Corporation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""add visibility

Revision ID: newton_expand01
Revises: mitaka02
Create Date: 2016-08-04 12:08:08.258679

"""
from alembic import op
from sqlalchemy import MetaData, Column, Enum

from glance.db import migration

# revision identifiers, used by Alembic.
revision = 'newton_expand01'
down_revision = 'mitaka02'
branch_labels = (migration.EXPAND_BRANCH,)
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())

    # TODO(tsymanczyk): would be nice if this enum weren't copypaste
    enum = Enum('private', 'public', 'shared', 'community',
                metadata=meta,
                name='image_visibility')
    enum.create()

    op.add_column('images', Column('visibility',
                                   enum,
                                   nullable=False,
                                   server_default='private'))
    op.create_index('visibility_image_idx',
                    'images',
                    ['visibility'],
                    unique=False)


def downgrade():
    raise NotImplementedError
