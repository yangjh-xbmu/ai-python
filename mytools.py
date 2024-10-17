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

# Please install OpenAI SDK first: `pip3 install openai`


def dsllm(message):
    from openai import OpenAI

    client = OpenAI(api_key="sk-36ce9aa77bf540f8ac82a7e940f6dcfe",
                    base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "请如实回答用户的问题，如果不知道，请不要虚构。"},
            {"role": "user", "content": message},
        ],
        stream=False
    )

    return (response.choices[0].message.content)


def fy(中文内容):
    中文内容 = 中文内容
    提示词 = f'''
    请扮演地道美国人，将{中文内容}翻译成英语，给出音标、例句
    '''
    result = dsllm(提示词)
    print(result)
    return result


def genAnkiCard(学习内容, 文件名称):
    学习内容 = 学习内容
    提示词 = f'''
    请扮演教学专家，能熟练应用各种学习相关的理论。

    请根据【卡片格式资料】，为【学习内容】{学习内容}</content>生成 Anki for VSCode 学习卡片。

    卡片格式资料：


    Anki for VSCode splits cards by ## headline. For example, below markdown will generate 2 cards where headlines will be on the front side and its description - on the back.

    ## What's the Markdown?

    Markdown is a lightweight markup language with plain-text-formatting syntax.
    Its design allows it to be converted to many output formats,
    but the original tool by the same name only supports HTML.

    ## Who created Markdown?

    John Gruber created the Markdown language in 2004 in collaboration with
    Aaron Swartz on the syntax.


    要求：

    1. 每张卡片只有一个主要知识点
    '''
    result = dsllm(提示词)
    with open(文件名称, "w", encoding='UTF-8') as file:
        # 将Markdown内容写入文件
        file.write(result)
    print(result)


def openfile(文件名称):
    with open(文件名称, 'r', encoding='UTF-8') as file:
        # 读取文件内容
        content = file.read()
        # 打印文件内容
        return content
