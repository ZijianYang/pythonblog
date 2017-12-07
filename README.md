# pythonblog

基本结构
登陆接口

#安装虚拟环境
virtualenv --version #验证是否安装
pip install virtualenv #安装
virtualenv venv #创建虚拟环境
venv\Scripts\activate #激活虚拟环境
deactivate #退出虚拟环境
#安装依赖包
pip install -r requirements/common.txt
#创建数据库
python manage.py db init #创建迁移仓库
如果是mysql则可能需要手动创建库
python manage.py db migrate  -m "initial migration" #创建迁移版本
python manage.py db upgrade #更新