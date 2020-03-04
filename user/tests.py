from django.test import Client
from django.test import TestCase

from user.models import User


class UserTest(TestCase):
    def setUp(self):
        self.cli = Client()
        User.objects.create(
            phonenum='98172364',
            nickname='HelloWorld',
            gender='male',
            birthday='2000-10-21',
            avatar='',
            location='上海',
            vip_id=1,
            vip_end='3000-10-10'
        )

    def test_user_vip(self):
        '''测试 Model 功能'''
        user = User.objects.get(phonenum='98172364')
        user.set_vip(7)
        self.assertEqual(user.vip.level, 2)

    def test_get_vcode(self):
        '''测试 View 函数功能'''
        args = {'phonenum': '15601185621'}
        response = self.cli.get('/api/user/get_vcode', args)

        self.assertEqual(response.status_code, 200)  # 检查状态码
        self.assertDictEqual(response.json(), {'code': 0, 'data': None})  # 结果测试
