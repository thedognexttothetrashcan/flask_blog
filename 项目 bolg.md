## 项目 bolg

**功能模块**

**前台**

1. 登录注册
2. 个人中心
   + 退出登录
   + 修改个人信息
   + 修改密码
   + 修改头像
   + 我的收藏
   + 我发表的
   + 修改/删除发表过 的博客
3. 发表博客
4. 首页展示
   + 搜索
   + 轮波图
   + 所有的博客的展示
5. 博客的详情页
   + 评论
   + 回复
   + 收藏
   + 取消收藏
   + 时间的展示

**后台**

1. 登录
2. 用户管理
   + 查看所有用户（搜索）
   + 修改用户
   + 删除用户
   + 添加用户
3. 博客管理（是否审核当前博客通过）
   + 查看博客（（搜索））
   + 删除博客
4. 用户回收站
   + 彻底删除用户
   + 恢复用户
5. 博客回收站
   + 彻底删除博客
   + 恢复博客
6. 首页轮波图 后台动态更改



**目录层级**

```python
blog/
	App/
    	__init__.py
        templates/
        	home/
            	common/
                base.html
            admin/
            	common/
        static/
        	admin/
            	img/
                css/
                js/
        	home/
                img/
                css/
                js/
            upload/
        forms/
        	__init__.py
        models/
        	__init__.py
        hmoeviews/
        	__init__.py
        adminviews/
        	__init__.py
        email.py
        extensions.py
        settings.py
    migrations/
    venv/
    manage.py #启动项文件
```

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000

**虚拟环境**

**安装：**

pip3 install virtualenv

**创建虚拟环境**

virtualenv venv(虚拟环境的名字)

**进入虚拟环境**

source venv/bin/activate

**退出虚拟环境**

deactivate