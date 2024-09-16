from abc import ABC
from typing import List, Dict, Any, Tuple

from app.common.types import DjangoModelType
from app.common.validators import FileValidator

import uuid

import json
from django.db import connection


def model_update(
    *,
    instance: DjangoModelType,
    fields: List[str],
    data: Dict[str, Any]
) -> Tuple[DjangoModelType, bool]:
    """
    Generic update service meant to be reused in local update services

    For example:

    def user_update(*, user: User, data) -> User:
        fields = ['first_name', 'last_name']
        user, has_updated = model_update(instance=user, fields=fields, data=data)

        // Do other actions with the user here

        return user

    Return value: Tuple with the following elements:
        1. The instance we updated
        2. A boolean value representing whether we performed an update or not.
    """
    has_updated = False

    for field in fields:
        # Skip if a field is not present in the actual data
        if field not in data:
            continue

        if getattr(instance, field) != data[field]:
            has_updated = True
            setattr(instance, field, data[field])

    # Perform an update only if any of the fields was actually changed
    if has_updated:
        instance.full_clean()
        # Update only the fields that are meant to be updated.
        # Django docs reference:
        # https://docs.djangoproject.com/en/dev/ref/models/instances/#specifying-which-fields-to-save
        instance.save(update_fields=fields)

    return instance, has_updated


class DataAbstract(ABC):
    """
    Args: 1) data 2) check_ser 3) pk 4)files 
    Kwargs: token
    """
    data = None
    files = None
    check_ser = None
    pk = None
    token = None
    user = None
    validated_data = None

    def __init__(self, *args, **kwargs):
        self.reset()
        self.token = kwargs.get('token', None)
        if len(args) >= 1:
            self.data = args[0]

            if len(args) >= 2:
                self.check_ser = args[1]

                if len(args) >= 3:
                    self.pk = args[2]

                    if len(args) >= 4:
                        self.files = args[3]
                        if 'data' in self.data:
                            self.data = json.loads(self.data['data'])
                        else:
                            self.data = {}
                        
        self.user = kwargs.get('user', None)
        
        self.check_request_data()
        print(self.data)

    def reset(self):
        self.data = None
        self.files = None
        self.check_ser = None
        self.pk = None
        self.token = None
        self.user = None
        self.validated_data = None

    def check_request_data(self):
        if self.check_ser:
            if self.pk: self.data['pk'] = self.pk
            print("Provjera podataka...")
            ser = self.check_ser(data = self.data)
            ser.is_valid(raise_exception=True)
            self.validated_data = ser.data
        return True


class FilesService:
    files = []
    path_to_save = ''
    full_path = []
    title = []
    data = [] #Type and path

    def __init__(self, files, path_to_save):
        self.files = files
        self.path_to_save = path_to_save
        self.title = []
        self.full_path = []

    def generate_file_name(self, file):
        title = uuid.uuid4().hex[:10].lower() + file.name
        print(title)
        return title

    def get_file_type(self, file):
        if file.name.lower().endswith(FileValidator.VALID_IMG_EXT):
            return 'img'
        if file.name.lower().endswith(FileValidator.VALID_FILE_EXT):
            return 'file'


    def prepare_part_file(self):
        FileValidator(['img', 'file'], self.files).validate()
        for file in self.files:
            title = self.generate_file_name(file)
            # self.title.append(self.generate_file_name(file))
            self.full_path.append(f'{self.path_to_save}{title}')
            self.data.append(
                {
                    "type": self.get_file_type(file),
                    "full_path": f'{self.path_to_save}{title}',
                    "title": file.name
                }
            )
        return self.data


    def prepare_part_qty_file(self):
        FileValidator(['img', 'file'], self.files).validate()
        for file in self.files:
            self.title.append(self.generate_file_name(file))
            self.full_path.append(f'{self.path_to_save}{self.title[0]}')
            return self.full_path[0]
        return ''

    def prepare_part_avatar_file(self):
        FileValidator('img', self.files).validate()
        for file in self.files:
            self.title.append(self.generate_file_name(file))
            self.full_path.append(f'{self.path_to_save}{self.title[0]}')
            return self.full_path[0]
        return ''

    def save_file(self):
        if self.files:
            i = 0

            for file in self.files:
                print(file)
                with open(f'media/{self.full_path[i]}', 'wb') as fp:
                    fp.write(file.read())
                i += 1


class CountConnections:
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        print("Queries Counted: {}".format(len(connection.queries)))
        return response