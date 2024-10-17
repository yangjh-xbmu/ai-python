def xfllm(xfchatmessage):
    from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
    from sparkai.core.messages import ChatMessage

    # 星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = 'wss://spark-api.xf-yun.com/v4.0/chat'
    # 星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = '575a00d1'
    SPARKAI_API_SECRET = 'NDIzNGRlNjUwNjhlNDg4MThjNWM3OGYz'
    SPARKAI_API_KEY = '6730233db135955bbbaf55901b3f296e'
    # 星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_DOMAIN = '4.0Ultra'

    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    prompt = xfchatmessage
    messages = [ChatMessage(
        role="user",
        content=prompt
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    return a.generations[0][0].text


def cognitive_load_explain(message):
    prompt = f'''
    请扮演经验丰富的Python教学专家，我是一个Python的初学者，没有任何编程经验。
    请依据认知负荷理论，通俗易懂地解释我的提问:{message}，并在最后生成1个测试题，但不要给出答案。
    要求：每行字数不超过20字符。
    '''
    print(xfllm(prompt))


def detect_text_errors(text):
    # 函数实现
    prompt = f'''
    请扮演严谨的排版编辑，就提供的文本：{text}，查找错别字、标点符号错误。
    要求：将错误和纠正的内容，用表格的形式呈现。
    '''
    print(xfllm(prompt))

#
# print(cognitive_load_explain('什么是函数'))
