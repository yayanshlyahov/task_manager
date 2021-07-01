from pydantic import BaseModel, ValidationError, validator


class FIO(BaseModel):
    first_name: str
    last_name: str


class UserModel(BaseModel):
    name: FIO
    username: str
    password1: str
    password2: str

    # @validator('name')
    # def name_must_contain_space(cls, v):
    #     if ' ' not in v:
    #         raise ValueError('must contain a space')
    #     return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


base_json = '''
{
    "name": {
        "first_name": "Yan",
        "last_name": "Shlyahov"
    },
    "username": "yayan",
    "password1": "1234567890",
    "password2": "1234567890"
}
'''

# import pdb; pdb.set_trace()
user = UserModel.parse_raw(base_json)
user.name = "Yan Shlyahov"
print(user.json())
import pdb; pdb.set_trace()
