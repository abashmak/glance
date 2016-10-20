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

"""drop is_public

Revision ID: newton_contract01
Revises: mitaka02
Create Date: 2016-08-04 12:22:01.294934

"""

from alembic import op
from sqlalchemy import MetaData, Table

from glance.db import migration

# revision identifiers, used by Alembic.
revision = 'newton_contract01'
down_revision = 'mitaka02'
branch_labels = (migration.CONTRACT_BRANCH,)
depends_on = None


def upgrade():
    meta = MetaData(bind=op.get_bind())
    images = Table('images', meta, autoload=True)

    op.execute(images.update(values={'visibility': 'public'}).where(
        images.c.is_public))

    # TODO(abashmak) uncomment below when community images codebase
    # including updates to tests gets merged, either upstream or in
    # this 'feature' breanch
    # with op.batch_alter_table("images") as batch_op:
    #    batch_op.drop_index('ix_images_is_public')
    #    batch_op.drop_column('is_public')


def downgrade():
    raise NotImplementedError
