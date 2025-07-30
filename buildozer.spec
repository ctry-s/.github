[app]
title = jmcomic downloader
package.name = jmcomicapp
package.domain = org.example
source.dir = .
source.include_exts = py,yml
version = 1.0
requirements = python3,kivy,jmcomic,requests
orientation = portrait
fullscreen = 0
android.api = 34
android.sdk = 34
android.ndk = 25b
android.ndk_api = 34
android.accept_sdk_license = True
android.build_tools_version = 34.0.0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
