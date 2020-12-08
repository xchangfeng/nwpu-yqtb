import json
from selenium import webdriver
import time
data = []
with open('name.json', 'r') as f:
    data = f.read()
d = json.loads(data)
stu_number = d['username']
stu_password = d['password']
# print(stu_number, stu_password)
f.close()

#西工大 参考：https://blog.csdn.net/wjl_zyl_1314/article/details/107036245
# 打开chrome浏览器
driver = webdriver.Chrome()
# 进入健康情况填报官网
url = r'http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp'
driver.get(url)
# 最大化窗口
driver.maximize_window()
# 登录信息
username = driver.find_element_by_id('username')
# stu_number = '学号'
username.send_keys(stu_number)
# stu_password = '密码'
password = driver.find_element_by_id('password')
password.send_keys(stu_password)
# 点击登录 //*[@id="fm1"]/div[4]/div/input[5]
# driver.find_element_by_class_name('el-button el-button--primary el-button--small is-round').click()
driver.find_element_by_xpath("/html/body/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div/div[1]/div[1]/form/div[4]/div/input[5]").click()
# print(driver.find_elements_by_id)
time.sleep(1)
# 点击健康登记
driver.find_element_by_partial_link_text('健康登记').click()

# 因为西工大会自动记录上一天的信息，所以不需要填报其他信息可直接提交
'''
#如果需要更改一些内容可参考以下代码
# 当前所在位置
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[3]/label[3]').click()

# 由于本人选取的国内，所有还有省市区的选择
driver.find_element_by_xpath('//*[@id="province"]/option[18]').click()
driver.find_element_by_xpath('//*[@id="city"]/option[4]').click()
driver.find_element_by_xpath('//*[@id="district"]/option[4]').click()

# 近15天是否前往或经停过武汉市、湖北省，或其他有病例报告的社区？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[6]/label[3]').click()
driver.find_element_by_xpath('//*[@id="sfjthb_ms"]').clear()
driver.find_element_by_xpath('//*[@id="sfjthb_ms"]').send_keys('人在湖北')

# 近15天接触过出入或居住在武汉市、湖北省的人员，以及其它有病例社区的发热或呼吸道症状患者？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[8]/label[3]').click()
driver.find_element_by_xpath('//*[@id="hbjry_ms"]').clear()
driver.find_element_by_xpath('//*[@id="hbjry_ms"]').send_keys('人在湖北')

# 近15天您或家属是否接触过疑似或确诊患者，或无症状感染患者（核酸检测阳性者）？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[10]/label[1]').click()

# 今天的体温范围
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[12]/label[1]').click()

# 您或家属有无疑似症状?（可多选） 选择不上不明原因
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[14]/label[1]/div[1]').click()

# 您或家属当前健康状态
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[17]/label[1]').click()

# 您或家属是否正在隔离？（隔离是根据上级单位、医院相关要求的居家或封闭性隔离，宅在家的不属隔离）
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[20]/label[1]').click()
'''

# 点击提交信息
driver.find_element_by_partial_link_text('提交填报信息').click()
time.sleep(1)
# 郑重承诺
driver.find_element_by_xpath('/html/body/div[3]/form/div[6]/div[2]/div[10]/label/div[1]/i').click()
# 确认提交
driver.find_element_by_partial_link_text('确认提交').click()
time.sleep(2)
# 关闭浏览器
driver.close()
