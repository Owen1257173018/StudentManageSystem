from jinja2 import Environment  # jinja2的虚拟环境
from django.templatetags.static import static  # django的一些依赖
from django.urls import reverse  # urls需要和jinja进行一些配置


def environment(**options):
    env = Environment(**options)  # 把一些配置文件添加进去
    env.globals.update({
        'static': static,
        'url': reverse
    })
    return env