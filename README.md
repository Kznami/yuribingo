# 环境配置

安装以下依赖库

```
pip install flask beautifulsoup4 requests flask-cors
```

# 使用方法

在app.py文件夹中运行cmd或powershell，并执行

```
python app.py
```

此时app.py会在http://localhost:5000/上部署

打开index.html即可开始宾果游戏

点击图片即可修改边框颜色

---

关键词可以在python文件中的keyword变量中修改，默认为“百合”

默认搜寻图书类条目，可在url中直接将book替换为其他类别

可指定搜寻数量（page），模拟浏览器请求所以不受limit和offset限制

---

javascript代码中附带通过请求api.bgm.tv的实现方法，但是api请求无法正确排序且有搜索数量限制，所以通过本地爬取再传给前端的方式，如果不想本地部署python文件可以使用注释中的样例数据，打开网页即可使用。
