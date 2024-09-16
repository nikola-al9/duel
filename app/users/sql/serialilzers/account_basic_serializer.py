from app.common.sql.abstract_serializer import AbstractSqlSerializer

class AccountBasicInfoSqlSerializer(AbstractSqlSerializer):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields = [
            'id',
            'email',
            'name',
        ]

        self.json_build_object_fields = [
            # {
            #     "name": "company",
            #     "object": CompanyBasicInfoSqlSerializer("c"),
            #     "column": "company_id"
            # }
        ]