from selenium.webdriver.common.by import By

# 包名和启动名
appPackage = "com.android.settings"
appActivity = ".Settings"

# 定位搜索按钮，搜索文本框，返回按钮
search = (By.ID, "com.android.settings:id/search")
search_src_text = (By.ID, "android:id/search_src_text")
imageButton = (By.CLASS_NAME, "android.widget.ImageButton")

