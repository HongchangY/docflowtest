from openai import OpenAI
import config as cfg
client = OpenAI(api_key=cfg.OPENAI_API_KEY)
class ReviewerAgent:
    def run(self, prd_text):
        prompt = f"""审查以下 PRD：
{prd_text}
输出：缺失项、风险、澄清问题"""
        resp = client.chat.completions.create(
            model=cfg.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )
        return resp.choices[0].message["content"]
