"""
Copyright 2022 Masturbino1337

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Made with love for Allah
"""

from .errors import ApiError, DailyLimitError, InvalidKeyError, StockError
from .types import Profile, Alt
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

        elif resp.status_code == 204:
            raise StockError()

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
        return Profile(await self._request("profile"))

    async def alt(self):
        r"""Returns an alt object
        Example
        -----------
        repr: str
            <Alt email=uwu@gmail.com password=ilovekittens69>
        str: str
            uwu@gmail.com:ilovekittens69
        """
        return Alt(await self._request("alt"))
