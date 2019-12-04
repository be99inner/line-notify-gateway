class Payload:
    """
    Class module for create payload for line notification
    """
    def __init__(self,alert, token):
        self.icon = ""
        self.severity = alert['labels']['severity']
        self.summary = alert['annotations']['summary']
        self.desc = alert['annotations']['description']
        # self.stime = re_ftime(alert['startsAt'])
        self.start_time = alert['startAt']
        self.message =  """
                        {}\nSeverity: {}\nTime: {}\nSummary: {}\nDescription: {}
                        """.format(self.icon,self.severity, self.start_time, self.summary, self.desc)
        self.header = {'Authorization': token}
