from selenium import webdriver
import time
# 声明谷歌浏览器对象
# 设置浏览器无头模式
option = webdriver.ChromeOptions()
# option.add_argument('headless')
# option.add_argument('disable-gpu')
# option.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=option)
# 最大化浏览器(使用maximize_window方法无效,暂时使用set_window_size方法来指定浏览器大小)
# driver.maximize_window()
driver.refresh()
# 最大化浏览器
driver.set_window_size(1920, 1080)
# 打开给定地址
driver.get('http://nbld.haiwensoft.com/pc/default/index')

# 截取登录框的页面保存到相应位置
driver.save_screenshot('screenshot\\image\\radar_login.png')
# 定位登录页面用户名和密码元素并模拟填入用户名和密码
driver.find_element_by_name("username").send_keys('zhlh')
driver.find_element_by_name("pwd").send_keys('123456')
# 模拟点击登录按钮登录
driver.find_element_by_id('btnSave').click()
# 强制等待time.sleep(s) 强制等待s秒后再进行下面的操作
# 考虑GIS加载过慢，此处先等待35s
time.sleep(35)
# 将登陆成功后的页面截图
driver.get_screenshot_as_file("screenshot\\image\\radar_index.png")
# 退出驱动关闭所有窗口
driver.quit()
