def merge_sources(*sources):
    text = "\n\n".join([s for s in sources if s])
    return f"以下是多渠道原始输入，请进行后续处理：\n{text}"
