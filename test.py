# Please install OpenAI SDK first: `pip3 install openai`
def dsllm(prompt):
    from openai import OpenAI

    client = OpenAI(api_key="sk-52750f91594741a388f2db2b6b3261f2",
                    base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt},
        ],
        stream=False
    )

    return (response.choices[0].message.content)


print(dsllm('介绍一下西北民族大学新闻传播学院，文言文，100字'))
