from openai import OpenAI
import config as cfg
client = OpenAI(api_key=cfg.OPENAI_API_KEY)
class ExtractorAgent:
    def run(self, text):
        prompt = f"""你是一名资深产品经理，请从以下内容中抽取：
1. 核心需求与目标
2. 关键用户故事
3. 业务流程关键点
4. 功能范围
文本：
{text}
请输出结构化 JSON："""
        resp = client.chat.completions.create(
            model=cfg.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message["content"]
