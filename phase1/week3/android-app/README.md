# Android App（Week 3 端侧聊天骨架）

## 环境要求

- JDK 17+
- Android SDK（API 35）
- 可选：Android Studio Ladybug+

## 构建

```bash
# 1. 配置 SDK 路径
cp local.properties.example local.properties
# 编辑 sdk.dir=...

# 2. 命令行构建
./gradlew assembleDebug

# 3. 或在 Android Studio 中 Open → 选择本目录
```

## 说明

本工程为 **教学骨架**：`MockOnDeviceLLM` 本地回复，为接入 MLC LLM / LiteRT-LM 预留 `OnDeviceLLM` 接口。
