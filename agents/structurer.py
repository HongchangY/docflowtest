from openai import OpenAI
import config as cfg
client = OpenAI(api_key=cfg.OPENAI_API_KEY)
class StructAgent:
    def run(self, extracted_json):
        prompt = f"""根据以下 JSON 生成 PRD：
{extracted_json}
包括：背景、用户故事、流程图、功能需求、非功能需求、API 列表"""
        resp = client.chat.completions.create(
            model=cfg.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message["content"]
