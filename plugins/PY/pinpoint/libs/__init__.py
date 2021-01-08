# ------------------------------------------------------------------------------
#  Copyright  2020. NAVER Corp.                                                -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#   http://www.apache.org/licenses/LICENSE-2.0                                 -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------


def monkey_patch_for_pinpoint(mongo=True,pymysql=True,pyredis=True,requests=True,urllib=True,
                            sqlalchemy=True,aioHttp=False,mysqldb=True):
    if pymysql:
        from .PyMysql import monkey_patch
        monkey_patch()

    if mongo:
        from .pymongo import monkey_patch
        monkey_patch()

    if pyredis:
        from .pyRedis import monkey_patch
        monkey_patch()

    if requests:
        from .requests import monkey_patch
        monkey_patch()

    if sqlalchemy:
        from .sqlalchemy import monkey_patch
        monkey_patch()

    if urllib:
        from .urllib import monkey_patch
        monkey_patch()

    if mysqldb:
        from .MySQLdb import monkey_patch
        monkey_patch()

__all__=['monkey_patch_for_pinpoint']