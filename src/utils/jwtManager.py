"""

 (c) Copyright Ascensio System SIA 2023

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

"""

import config
import jwt

# check if a secret key to generate token exists or not
def isEnabled():
    return bool(config.DOC_SERV_JWT_SECRET)

# encode a payload object into a token using a secret key and decodes it into the utf-8 format
def encode(payload):
    return jwt.encode(payload, config.DOC_SERV_JWT_SECRET, algorithm='HS256')

# decode a token into a payload object using a secret key
def decode(string):
    return jwt.decode(string, config.DOC_SERV_JWT_SECRET, algorithms=['HS256'])