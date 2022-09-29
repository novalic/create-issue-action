import os

from typing import List


def split_input_parameter_list(data) -> List[str]:
    if data and data != '':
        data = data.split(',')
    else:
        data = []

    return data


def get_environment_variable(name: str):
    env_var = os.environ.get(name)

    if env_var == '':
        env_var = None

    return env_var
