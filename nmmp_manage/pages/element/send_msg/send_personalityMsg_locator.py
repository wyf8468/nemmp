from selenium.webdriver.common.by import By


class SendPersonMsgLocator:
    # 收件号码-文件导入（导入）
    receipt_phone = (By.XPATH, '//*[@id="uploadPhoneNumber"]')
    # 收件号码-文件导入（导入）
    msg_content = (By.XPATH, '//*[@id="sendContent"]')
    # 预处理
    pre_processing = (By.XPATH, '//*[@id="pNode"]/div[1]/div[8]/a')
    # 弹窗-发送按钮
    send_ensure = (By.XPATH, '//*[@id="msgBoxId"]/div[2]/div[2]/div/a[1]')
    