# Android App（Direction A 智能笔记）

## 环境要求

- JDK 17+
- Android SDK（API 35）

## 构建

```bash
cp local.properties.example local.properties
# 编辑 sdk.dir 指向你的 Android SDK

./gradlew assembleDebug
```

## 联调后端

1. 宿主机启动：`uvicorn api:app --host 0.0.0.0 --port 8010`
2. 模拟器访问：`http://10.0.2.2:8010`（已在 `BuildConfig.API_BASE_URL` 配置）
3. 后端未连接时，问候语走端侧 Mock 兜底（见 `NotesRepository.kt`）

## Android Studio

Open → 选择本 `android-app/` 目录。
