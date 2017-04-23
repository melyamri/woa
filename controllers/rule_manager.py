class RuleManager():

    def __init__(self):
        return

    def reason(agent):
        class_name = agent.class_name().lower()
        if class_name == 'collector':
            from rules.collector import run_all
        else:
            from rules.custom_agent import run_all

        run_all(agent)
