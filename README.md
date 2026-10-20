# Builtin Commands Extension

**当前版本：v0.1.1。** 版本号以 [metadata.yaml](metadata.yaml) 为准。

这是 AstrBot 的内置指令扩展插件。

## 安装此维护版

在 AstrBot 中选择「通过仓库地址安装」，填写 `https://github.com/leekooyo/builtin_commands_extension`。本仓库基于 [AstrBotDevs 原项目](https://github.com/AstrBotDevs/builtin_commands_extension) 独立维护，维护差异见 [UPSTREAM.md](UPSTREAM.md)。本插件没有独立配置界面；管理员授权、会话和模型配置由 AstrBot 本机保存，不应加入 Git 仓库。

从 AstrBot `builtin_commands` 中迁出的非核心指令会放在这里维护。核心内置指令仍保留在 AstrBot 主程序中，包括：

当前维护版的 `/plugin` 列表优先显示本地帮助插件提供的简称；本地帮助插件已启用时，`/plugin help <插件标识>` 会使用其详情图。未安装本地帮助时仍使用插件原有信息。

- `/sid`
- `/stop`
- `/reset`
- `/new`
- `/dashboard_update`
- `/help`
- `/name`、`/stats`、`/provider`
- `/set <key> <value>`、`/unset <key>`（会话变量）

## 提供的指令

本插件提供以下扩展指令：

- `/llm`：开启或关闭 LLM 聊天功能
- `/plugin`：插件管理
- `/op`：授权管理员
- `/deop`：取消管理员授权
- `/model`：查看或切换模型
- `/history`：查看对话记录
- `/ls`：查看对话列表
- `/groupnew`：创建群聊对话
- `/switch`：切换对话
- `/rename`：重命名当前对话
- `/del`：删除当前对话
- `/persona`：查看或切换 Persona

## 说明

该插件复用 AstrBot 原有内置指令实现，目录结构与原 `astrbot/builtin_stars/builtin_commands` 保持一致：

```text
builtin_commands_extension/
├── main.py
├── metadata.yaml
└── commands/
```

如需禁用这些扩展指令，可以在 WebUI 的插件管理中停用 `builtin_commands_extension`。
