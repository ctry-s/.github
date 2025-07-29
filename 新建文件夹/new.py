try:
    import jmcomic
    # 创建配置对象
    option = jmcomic.create_option_by_file('E:/TEST/option.yml')
    # 让用户输入本子ID
    album_id = input("请输入本子ID: ")
    # 验证输入是否为数字
    if album_id.isdigit():
        jmcomic.download_album(int(album_id), option)
    else:
        print("输入无效，请输入数字ID")
except ImportError as e:
    print(f"导入错误: {e}")
    print("请检查 jmcomic 包是否正确安装")
except Exception as e:
    print(f"运行错误: {e}")