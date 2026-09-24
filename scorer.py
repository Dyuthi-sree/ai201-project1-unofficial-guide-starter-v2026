def judge(question, expects, answer, results):
    """
    Return True when the generated answer contains the expected fact.
    """
    return expects.lower() in answer.lower()
