from typing import Optional
from urllib import response

from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import get_object_or_404
from app.common.services import DataAbstract, model_update
from app.errors.services import trigger_django_404, trigger_exception

Account = get_user_model()
from app.common.sql.proc import Proc
from app.common.constants import *
import json
import uuid
from app.common.utils import get_response

class AccountService(DataAbstract):

    pass