from django.shortcuts import render,get_object_or_404

# Create your views here.

from .models import BlogArticles
# 视图函数-响应用户请求

# 博客列表list
# request参数负责响应所接收的请求且不能缺少，并总是处于第一参数的位置
def blog_title(request):
    blogs = BlogArticles.objects.all() # 得到所有的BlogArticles的对象实例，QuerySet
    # 从数据库中读取的每一条记录都可以看作一个实例对象
    return render(request,"blog/titles.html",{"blogs":blogs})
    # render() 函数的作用是将数据渲染到指定模版上
    # render_to_response() 也一样，但也有区别，render()是 render_to_response()的快捷方式
    # 会自动使用RequestContext
    # render()的第一个参数必须是request，然后是模版位置和所传送的数据，数据使用类字典的形式传送给模版的


# 博客内容
# 如何向函数传入参数article_id呢？查阅URL配置的相关内容
def blog_article(request,article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles,id=article_id)
    pub = article.publish
    return render(request,"blog/content.html",{"article":article,"publish":pub})

