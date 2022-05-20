#    Copyright 2022 Masturbino1337

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import httpx

class Client:
    def __init__(self, api_key):
        self.session = httpx.AsyncClient()
        self.api_key = api_key

    async def request(self, endpoint):
        resp = await self.session.get("https://kinggen.wtf/api/v2/" + endpoint + "/?key=" + self.api_key)

        if not resp.status_code == 200:
            raise ApiError(resp.json()["message"])

        return resp.json()

    async def profile(self):
        return Profile(await self.request("profile"))

    async def alt(self):
        return Alt(await self.request("alt"))

class Profile:
    def __init__(self, resp):
        self.username: str = resp["username"]
        self.generated: int = resp["generated"]
        self.generated_today: int = resp["generatedToday"]
        self.stock: int = resp["stock"]

    def __str__(self):
        return f"<Profile username={self.username} generated={self.generated} generated_today={self.generated_today} stock={self.stock}>"

class Alt:
    def __init__(self, resp):
        self.email: str = resp["email"]
        self.password: str = resp["password"]

    def __str__(self):
        return f"<Alt email={self.email} password={self.password}>"

class PyKingError(Exception):
    pass

class ApiError(PyKingError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
