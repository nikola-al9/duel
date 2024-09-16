from app.common.sql.abstract_serializer import AbstractSqlSerializer

class AccountDetailInfoSqlSerializer(AbstractSqlSerializer):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields = [
            'id',
            'email',
            'name',
        ]

        self.json_build_object_fields = [
            # {
            #     "name": "role",
            #     "object": RoleSqlSerializer("r"),
            #     "column": "role_id"
            # },
            # {
            #     "name": "company",
            #     "object": CompanyBasicInfoSqlSerializer("c"),
            #     "column": "company_id"
            # }
        ]