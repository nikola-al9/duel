from app.common.sql.abstract_query import AbstractQuery
from app.users.sql.serialilzers.account_detail_serializer import AccountDetailInfoSqlSerializer

from app.common.constants import *


class AccountDetailsQuery(AbstractQuery):

    def filter(self):
        self.add_filter(
            None,
            self.WHERE_ARR,
            f'acc.id = {self.pk}'
        )

    def generate_sql(self):
        self.QUERY = f"""
            {self.BEGIN_STR}
            select 
                coalesce(json_agg(_a)->0, '404')
                from
                    (
                        select 
                            {AccountDetailInfoSqlSerializer('acc').fields_to_string()}
                        from 
                            "{TABLE_ACCOUNT}" acc
                        {self.JOIN_STR}
                        {self.WHERE_STR}
                        {self.GROUP_BY_STR}
                        {self.ORDER_BY_STR}
                        {self.LIMIT_STR}
                    ) _a
        """    

    def get_response(self, token=None):
        self.exec_query()
        if not token:
            self.FINAL_RES['results'] = self.res
        else:
            self.FINAL_RES['results'] = {
                "token": token,
                "account": self.res
            }

        return self.FINAL_RES

# class AccountBasicInfoQuery(AbstractQuery):

#     def filter(self):
#         self.add_filter(
#             None,
#             self.WHERE_ARR,
#             f"acc.id = {self.pk}"
#         )

#         # Join Role
#         self.add_filter(
#             None,
#             self.JOIN_ARR,
#             f'LEFT JOIN {TABLE_AUTH_GROUP} r on acc.role_id = r.id'
#         )

#         # Join Company
#         self.add_filter(
#             None,
#             self.JOIN_ARR,
#             f'LEFT JOIN {TABLE_COMPANY} c on acc.company_id = c.id'
#         )

#     def generate_sql(self):
#         self.QUERY = f"""
#             {self.BEGIN_STR}
#             select 
#                 coalesce(json_agg(_a)->0, '404')
#                 from
#                     (
#                         select 
#                             {AccountBasicInfoSqlSerializer('acc').fields_to_string()}
#                         from 
#                             "{TABLE_ACCOUNT}" acc
#                         {self.JOIN_STR}
#                         {self.WHERE_STR}
#                         {self.GROUP_BY_STR}
#                         {self.ORDER_BY_STR}
#                         {self.LIMIT_STR}
#                     ) _a
#         """   

#     def clear(self):
#         if 'avatar' in self.res:
#             self.res['avatar'] = get_file_url(self.res['avatar'])

# class AccountsListQuery(AbstractQuery):

#     def filter(self):

#         # Join Role
#         self.add_filter(
#             None,
#             self.JOIN_ARR,
#             f'LEFT JOIN {TABLE_AUTH_GROUP} r on acc.role_id = r.id'
#         )

#         # Join Company
#         self.add_filter(
#             None,
#             self.JOIN_ARR,
#             f'LEFT JOIN {TABLE_COMPANY} c on acc.company_id = c.id'
#         )

#         # Filter My Company
#         self.add_filter(
#             None,
#             self.WHERE_ARR,
#             f'acc.company_id = {self.user.company_id}'
#         )

#         # Add Limit
#         self.add_limit()

#         # Add Order BY
#         self.add_order_by()

#         # Add Asc Desc
#         self.add_ordering()

#         # Next condition
#         self.set_next_condition('acc')


#     def generate_sql(self):
#         self.QUERY = f"""
#             {self.BEGIN_STR}
#             select 
#                 coalesce(json_agg(_a), '[]')
#                 from
#                     (
#                         select 
#                             {AccountBasicInfoSqlSerializer('acc').fields_to_string()}
#                         from 
#                             "{TABLE_ACCOUNT}" acc
#                         {self.JOIN_STR}
#                         {self.WHERE_STR}
#                         {self.GROUP_BY_STR}
#                         {self.ORDER_BY_STR}
#                         {self.LIMIT_STR}
#                     ) _a
#         """   

#     def clear(self):
#         for i in self.res:
#             if 'avatar' in i:
#                 i['avatar'] = get_file_url(i['avatar'])

class UserMeQuery(AbstractQuery):

    def filter(self):
        self.add_filter(
            None,
            self.WHERE_ARR,
            f'acc.id = {self.user.id}'
        )

    def generate_sql(self):
        self.QUERY = f"""
            {self.BEGIN_STR}
            select 
                coalesce(json_agg(_a)->0, '404')
                from
                    (
                        select 
                            {AccountDetailInfoSqlSerializer('acc').fields_to_string()}
                        from 
                            "{TABLE_ACCOUNT}" acc
                        {self.JOIN_STR}
                        {self.WHERE_STR}
                        {self.GROUP_BY_STR}
                        {self.ORDER_BY_STR}
                        {self.LIMIT_STR}
                    ) _a
        """    




