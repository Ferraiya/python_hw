from functools import partial
from attr import attrs

s = attributes = attrs
ib = attr = attrib
dataclass = partial(attrs, auto_attribs=True)

@dataclass(frozen=True)
class UserInfo:
    street: str
    city: str
    zipcode: str
    phone_number: int


user = UserInfo(street='Main', city="NewYork")