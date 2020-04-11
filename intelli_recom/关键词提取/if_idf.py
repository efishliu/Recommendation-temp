from jieba import analyse
# 引入TF-IDF关键词抽取接口
tfidf = analyse.extract_tags

# 原始文本
text ='计算机专业优先，大学本科及以上学历；精通html、css布局，掌握W3C标准；\
至少熟练使用Firebug、Httpwatch等工具进行页面分析和调优，熟悉基础网络知识；\
对javascript、DOM、ajax语言有十分深入地了解，具备优秀的交互开发能力，\
熟悉jQuery、mootools、EXT、EasyUI等常用框架，能独立完成javascript代码的编写和优化工作，\
能够设计有创意的UI新亮点；熟悉各种网页复杂效果的实现，能对模块功能给出前端设计建议，\
能及时掌握web 端新技术发展并深入研究，如WEB2.0/HTML5/CSS3技术；\
熟悉目前主流浏览器的适配和常见浏览器的特点和限制，精通解决IE不同版本、firefox、chrome 等主流浏览器的兼容性问题；\
具有良好的团队合作精神及组织沟通协调能力。'

# 基于TF-IDF算法进行关键词抽取
keywords = tfidf(text)
print "keywords by tfidf:"
# 输出抽取出的关键词
for keyword in keywords:
    print keyword + "/",




