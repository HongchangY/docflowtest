from agents.collector import CollectorAgent
from agents.extractor import ExtractorAgent
from agents.structurer import StructAgent
from agents.reviewer import ReviewerAgent
from agents.syncer import SyncAgent
def main():
    c=CollectorAgent(); raw=c.run()
    e=ExtractorAgent(); extracted=e.run(raw)
    s=StructAgent(); prd=s.run(extracted)
    r=ReviewerAgent(); review=r.run(prd)
    sy=SyncAgent(); paths=sy.run(prd, review)
    print("输出文件：", paths)
if __name__=="__main__":
    main()
