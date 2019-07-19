import re, datetime

class HandleLog:
    def __init__(self):
        self.file_path = "api1_info.20190716/info.20190716.log"
        self.v1_getOrgInfos = []
        self.v3_getOrgInfos = []
        self.v1_msgCardDatas = []
        self.v3_msgCardDatas = []
        self.v1_updateTimeIntervals = []
        self.v3_updateTimeIntervals = []
        self.v1_disposts = []
        self.v1_getJsContents = []

    def get_data(self,):
        with open(self.file_path, "rb") as fp:
            for line in fp:
                fLine = str(line, "utf-8")
                self.process_data(fLine)
            v1_getOrgInfo_dic = {"v1_getOrgInfo": self.v1_getOrgInfos}
            v3_getOrgInfo_dic = {"v3_getOrgInfo": self.v3_getOrgInfos}
            v1_msgCardData_dic = {"v1_msgCardData": self.v1_msgCardDatas}
            v3_msgCardData_dic = {"v3_msgCardData": self.v3_msgCardDatas}
            v1_updateTimeInterval_dic = {"v1_updateTimeInterval": self.v1_updateTimeIntervals}
            v3_updateTimeInterval_dic = {"v3_updateTimeInterval": self.v3_updateTimeIntervals}
            v1_dispost_dic = {"v1_dispost": self.v1_disposts}
            v1_getJsContent_dic = {"v1_getJsContent": self.v1_getJsContents}

            return [v1_getOrgInfo_dic, v3_getOrgInfo_dic, v1_msgCardData_dic, v3_msgCardData_dic,
                    v1_updateTimeInterval_dic, v3_updateTimeInterval_dic, v1_dispost_dic, v1_getJsContent_dic]


    def process_data(self, fLine):
        v1_getOrgInfo = self.find_v1_getOrgInfo(fLine)
        if self.is_contain(v1_getOrgInfo, self.v1_getOrgInfos):
            self.v1_getOrgInfos.append(v1_getOrgInfo)
        v3_getOrgInfo = self.find_v3_getOrgInfo(fLine)
        if self.is_contain(v3_getOrgInfo, self.v3_getOrgInfos):
            self.v3_getOrgInfos.append(v3_getOrgInfo)
        v1_msgCardData = self.find_v1_msgCardData(fLine)
        if self.is_contain(v1_msgCardData, self.v1_msgCardDatas):
            self.v1_msgCardDatas.append(v1_msgCardData)
        v3_msgCardData = self.find_v3_msgCardData(fLine)
        if self.is_contain(v3_msgCardData, self.v3_msgCardDatas):
            self.v3_msgCardDatas.append(v3_msgCardData)
        v1_updateTimeInterval = self.find_v1_updateTimeInterval(fLine)
        if self.is_contain(v1_updateTimeInterval, self.v1_updateTimeIntervals):
            self.v1_updateTimeIntervals.append(v1_updateTimeInterval)
        v3_updateTimeInterval = self.find_v3_updateTimeInterval(fLine)
        if self.is_contain(v3_updateTimeInterval, self.v3_updateTimeIntervals):
            self.v3_updateTimeIntervals.append(v3_updateTimeInterval)
        v1_dispost = self.find_v1_dispost(fLine)
        if self.is_contain(v1_dispost, self.v1_disposts):
            self.v1_disposts.append(v1_dispost)
        v1_getJsContent = self.find_v1_getJsContent(fLine)
        if self.is_contain(v1_getJsContent, self.v1_getJsContents):
            self.v1_getJsContents.append(v1_getJsContent)


    def find_v1_getOrgInfo(self, line):
        v1_regex = re.compile('api/v1/getOrgInfo.*?"phoneManufacturer":"(.*?)"')
        v1_result = v1_regex.search(line)
        if v1_result != None:
            result = v1_result.group(1)
            return result

    def find_v3_getOrgInfo(self, data):
        v3_regex = re.compile('api/v3/getOrgInfo.*?"phoneManufacturer":"(.*?)"')
        v3_result = v3_regex.search(data)
        if v3_result != None:
            result = v3_result.group(1)
            return result

    def find_v1_msgCardData(self, data):
        v1_regex = re.compile('api/v1/msgCardData.*?"phoneManufacturer":"(.*?)"')
        v1_result = v1_regex.search(data)
        if v1_result != None:
            result = v1_result.group(1)
            return result

    def find_v3_msgCardData(self, data):
        v3_regex = re.compile('api/v3/msgCardData.*?"phoneManufacturer":"(.*?)"')
        v3_result = v3_regex.search(data)
        if v3_result != None:
            result = v3_result.group(1)
            return result

    def find_v1_updateTimeInterval(self, data):
        v1_regex = re.compile('api/v1/updateTimeInterval.*?"phoneManufacturer":"(.*?)"')
        v1_result = v1_regex.search(data)
        if v1_result != None:
            result = v1_result.group(1)
            return result

    def find_v3_updateTimeInterval(self, data):
        v3_regex = re.compile('api/v3/updateTimeInterval.*?"phoneManufacturer":"(.*?)"')
        v3_result = v3_regex.search(data)
        if v3_result != None:
            result = v3_result.group(1)
            return result

    def find_v1_dispost(self, data):
        v1_regex = re.compile('api/v1/dispost.*?"phoneManufacturer":"(.*?)"')
        v1_result = v1_regex.search(data)
        if v1_result != None:
            result = v1_result.group(1)
            return result

    def find_v1_getJsContent(self, data):
        v1_regex = re.compile('api/v1/getJsContent.*?"phoneManufacturer":"(.*?)"')
        v1_result = v1_regex.search(data)
        if v1_result != None:
            result = v1_result.group(1)
            return result

    def is_contain(self, str_1, array):
        if str_1 in array:
            return False
        else:
            return True


if __name__ == "__main__":
    start_time = datetime.datetime.now()
    print("开始时间 %s:" % start_time)
    hand_log = HandleLog()
    result = hand_log.get_data()
    print(type(result))
    for i in result:
        print(i)
    end_time = datetime.datetime.now()
    print("结束时间 %s" % end_time)
    print(end_time - start_time)



