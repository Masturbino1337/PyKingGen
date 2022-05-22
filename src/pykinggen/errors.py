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