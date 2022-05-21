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

#    Made with love for Allah

import httpx

class Client:
    r"""Client class for API queries
    Parameters
    -----------
    api_key: str
        valid KingGen API key
    """
    def __init__(self, api_key):
        self.session = httpx.AsyncClient()
        self.api_key = api_key

    async def _request(self, endpoint):
        resp = await self.session.get("https://kinggen.wtf/api/v2/" + endpoint + "?key=" + self.api_key)

        if 600 > resp.status_code >= 500:
            raise ApiError()

        elif resp.status_code == 401:
            raise InvalidKeyError()

        elif resp.status_code == 403:
            raise DailyLimitError()

        return resp.json()

    async def profile(self):
        r"""Returns a profile object
        Example
        -----------
        repr: str
            <Profile username=Xevier generated=69 generated_today=21 stock=6969>
        str: str
            Xevier:69:21:6969
        """
        return _Profile(await self._request("profile"))

    async def alt(self):
        r"""Returns an alt object
        Example
        -----------
        repr: str
            <Alt email=uwu@gmail.com password=ilovekittens69>
        str: str
            uwu@gmail.com:ilovekittens69
        """
        return _Alt(await self._request("alt"))

class _Profile:
    def __init__(self, resp):
        self.username: str = resp["username"]
        self.generated: int = resp["generated"]
        self.generated_today: int = resp["generatedToday"]
        self.stock: int = resp["stock"]

    def __repr__(self) -> str:
        return f"<Profile username={self.username} generated={self.generated} generated_today={self.generated_today} stock={self.stock}>"

    def __str__(self) -> str:
        return f"{self.username}:{self.generated}:{self.generated_today}:{self.stock}"

class _Alt:
    def __init__(self, resp):
        self.email: str = resp["email"]
        self.password: str = resp["password"]

    def __repr__(self) -> str:
        return f"<Alt email={self.email} password={self.password}>"

    def __str__(self) -> str:
        return f"{self.email}:{self.password}"

class PyKingError(Exception):
    pass

class ApiError(PyKingError):
    def __repr__(self) -> str:
        return "The API is down"

class InvalidKeyError(PyKingError):
    def __repr__(self) -> str:
        return "Invalid API key"

class DailyLimitError(PyKingError):
    def __repr__(self) -> str:
        return "User is at daily limit"
