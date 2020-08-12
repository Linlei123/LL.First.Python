from selenium import webdriver
# 引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
import time

# 滚动到浏览器顶部
js_top = "var q=document.documentElement.scrollTop=0"

# 滚动到浏览器底部
js_bottom = "var q=document.documentElement.scrollTop=10000"
js_bottom2 = "window.scrollTo(0,document.body.scrollHeight)"

# 页面放大
js_zoom_in = "document.body.style.zoom='1.7'"

# 页面缩小
js_zoom_out = "document.body.style.zoom='0.9'"
# 声明谷歌浏览器对象
# 设置浏览器无头模式
option = webdriver.ChromeOptions()
# 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
# option.add_argument('--headless')
# 谷歌文档提到需要加上这个属性来规避bug
option.add_argument('--disable-gpu')
# 禁用浏览器正在被自动化程序控制的提示
option.add_argument('--disable-infobars')
# 指定浏览器分辨率
option.add_argument('window-size=1920x1580')
# 隐身模式（无痕模式）
option.add_argument('--incognito')
# 隐藏滚动条, 应对一些特殊页面
option.add_argument('--hide-scrollbars')
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(chrome_options=option)
# 最大化浏览器
driver.maximize_window()
# 最大化浏览器
# driver.set_window_size(1920, 1080)
driver.refresh()
# 打开给定地址
driver.get('http://nbld.haiwensoft.com/pc/default/index')

# 截取登录框的页面保存到相应位置(“.”表示当前整个.py文件的路径所在的位置)
driver.save_screenshot('.\\image\\radar_login.png')
# 定位登录页面用户名和密码元素并模拟填入用户名和密码
driver.find_element_by_name("username").send_keys('zhlh')
driver.find_element_by_name("pwd").send_keys('123456')
# 模拟点击登录按钮登录
driver.find_element_by_id('btnSave').click()
# 强制等待time.sleep(s) 强制等待s秒后再进行下面的操作
# 考虑GIS加载过慢，此处先等待35s
time.sleep(30)
print("页面加载完毕")
print("开始页面缩放")
driver.execute_script(js_zoom_out)
time.sleep(10)
print("页面缩放完毕")
# 获取地图要素
element = driver.find_element_by_id("l-map")
# 对定位到的元素执行鼠标点击操作
ActionChains(driver).move_to_element(element).double_click()
# 使用快捷方式执行地图缩小事件(+对应放大，-对应缩小)
element.send_keys("-")
print("开始地图缩放")
time.sleep(10)
print("地图缩放完毕")
# 将登陆成功后的页面截图
driver.get_screenshot_as_file(".\\image\\radar_index.png")
# 退出驱动关闭所有窗口
driver.quit()
