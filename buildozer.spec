[app]
title = jmcomic downloader
package.name = jmcomicapp
package.domain = org.example
source.dir = .
source.include_exts = py,yml
version = 1.0
requirements = python3,kivy,jmcomic,requests
orientation = portrait
osx.python_version = 3
fullscreen = 0
android.api = 34
android.minapi = 21  # 添加最低 API 级别
android.sdk = 34
android.ndk = 25.2.9519653  # 使用与工作流一致的 NDK 版本
android.ndk_api = 21  # 将 NDK API 降低到 21（大多数设备支持）
android.accept_sdk_license = True
android.build_tools_version = 34.0.0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
