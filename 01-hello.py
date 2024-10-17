print('艰难的第一行')
# 听过注释不会被运行
# 注释可以是多行，多行注释用三个引号标记
# 这还是一行注释
"""
ddddd
dffdd

"""

# 使用等于号定义变量

x = input('请输入年龄:')
print(x)
chosen_weapon = print("请输入你选择的武器：")

# from sparkai.core.messages import ChatMessage
# from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler


# # 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
# SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
# # 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
# SPARKAI_APP_ID = '575a00d1'
# SPARKAI_API_SECRET = 'NDIzNGRlNjUwNjhlNDg4MThjNWM3OGYz'
# SPARKAI_API_KEY = '6730233db135955bbbaf55901b3f296e'
# # 星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
# SPARKAI_DOMAIN = '4.0Ultra'

# if __name__ == '__main__':
#     spark = ChatSparkLLM(
#         spark_api_url=SPARKAI_URL,
#         spark_app_id=SPARKAI_APP_ID,
#         spark_api_key=SPARKAI_API_KEY,
#         spark_api_secret=SPARKAI_API_SECRET,
#         spark_llm_domain=SPARKAI_DOMAIN,
#         streaming=False,
#     )
#     提示词 = input("请输入提示词：")
#     messages = [ChatMessage(
#         role="user",
#         content=提示词
#     )]
#     handler = ChunkPrintHandler()
#     a = spark.generate([messages], callbacks=[handler])
#     print(a)
