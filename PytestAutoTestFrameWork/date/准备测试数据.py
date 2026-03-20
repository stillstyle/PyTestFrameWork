import pandas as pd
import tempfile
import os

# ==================== 1. 构造login工作表的测试数据 ====================
login_data = [
    ["admin", "123456", "登录成功"],          # 正常用例：正确账号密码
    ["admin", "654321", "密码错误"],          # 异常用例：密码错误
    ["test_user", "123456", "用户不存在"],    # 异常用例：用户名错误
    ["", "123456", "用户名不能为空"],         # 异常用例：用户名空
    ["admin", "", "密码不能为空"],            # 异常用例：密码空
    ["  ", "123456", "用户名不能为空"],       # 异常用例：用户名仅空格
]
df_login = pd.DataFrame(login_data, columns=["用户名", "密码", "期望结果"])

# ==================== 2. 构造contact工作表的测试数据 ====================
contact_data = [
    ["张三", "zhangsan@test.com", "是", "13800138000", "常用客户", "添加成功"],  # 正常用例：完整正确信息
    ["李四", "lisi@test.com", "否", "13900139000", "", "添加成功"],              # 正常用例：备注为空
    ["王五", "wangwu#test.com", "是", "13700137000", "邮箱格式错误", "邮箱格式非法"],  # 异常用例：邮箱错误
    ["赵六", "zhaoliu@test.com", "是", "136abc136000", "手机号含字母", "手机号格式非法"],  # 异常用例：手机号错误
    ["", "qianqi@test.com", "否", "13500135000", "姓名为空", "姓名不能为空"],    # 异常用例：姓名空
]
df_contact = pd.DataFrame(contact_data, columns=["姓名", "邮箱", "是否星标", "电话", "备注", "期望结果"])

# ==================== 3. 构造mail工作表的测试数据 ====================
mail_data = [
    ["recipient1@test.com", "工作汇报", "这是本周的工作汇报，请查收。", ""],  # 正常用例：无附件
    ["recipient1@test.com;recipient2@test.com", "会议通知", "周五下午3点开项目会", "会议资料.pdf"],  # 正常用例：多收件人+有附件
    ["", "无收件人测试", "正文内容", ""],  # 异常用例：收件人空
    ["recipient3@test.com", "", "无主题邮件", ""],  # 异常用例：主题空
    ["recipient4@test.com", "测试附件", "带不存在附件", "不存在的文件.txt"],  # 异常用例：附件路径不存在
]
df_mail = pd.DataFrame(mail_data, columns=["收件人", "主题", "正文", "附件路径"])

# ==================== 写入Excel文件（修复权限问题） ====================
# 创建临时目录，获取可写入的文件路径
temp_dir = tempfile.gettempdir()  # 获取系统临时目录
excel_path = os.path.join(temp_dir, "tcData.xlsx")  # 拼接临时路径+文件名

# 写入Excel文件到临时目录
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    df_login.to_excel(writer, sheet_name="login", index=False)
    df_contact.to_excel(writer, sheet_name="contact", index=False)
    df_mail.to_excel(writer, sheet_name="mail", index=False)

print(f"Excel文件创建成功！路径：{excel_path}")