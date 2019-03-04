"""
paginate:分页类 实例化 返回pagination分页对象
实例化参数：
	page 当前页码
    per_page 每页显示数据的条数
    error_out 当分页出现错误的时候 是否抛出异常默认True
pagination分页对象
	属性：
    	items 当前页面的所有数据
        page	当前页码
        pages	页码总数
        prev_num	上一页的页码
        next_num	下一页的页码
        has_prev	是否有上一页
        has_next	是否有下一页
    方法:
        prev 上一页的分页对象
        next	下一页的分页对象
        iter_pages 页码
"""

"""
前台剩余功能模块
bug

未完成的：
    1.博客管理的搜索 分页
    2.我的收藏的取消收藏 搜索 分页
    1. 缓存
    2. 个人中心
    3. 收藏
    4. 评论回复

细节
    浏览量+1
"""