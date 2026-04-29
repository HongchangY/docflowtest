from utils.io_utils import write_file
import config as cfg, time
class SyncAgent:
    def run(self, prd_text, review_text):
        ts=str(int(time.time()))
        p=f"{cfg.OUTPUT_DIR}/PRD_{ts}.md"
        r=f"{cfg.OUTPUT_DIR}/Review_{ts}.md"
        write_file(p, prd_text)
        write_file(r, review_text)
        return {"prd_path":p,"review_path":r}
