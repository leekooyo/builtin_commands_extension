from astrbot.api import star
from astrbot.api.event import AstrMessageEvent, MessageChain


class LLMCommands:
    def __init__(self, context: star.Context) -> None:
        self.context = context

    async def llm(self, event: AstrMessageEvent) -> None:
        """开启/关闭 LLM"""
        cfg = self.context.get_config(umo=event.unified_msg_origin)
        enable = cfg["provider_settings"].get("enable", True)
        if enable:
            cfg["provider_settings"]["enable"] = False
            status = "关闭"
        else:
            cfg["provider_settings"]["enable"] = True
            status = "开启"
        cfg.save_config()
        before = "开启" if enable else "关闭"
        await event.send(MessageChain().message(
            f"LLM 聊天：{before} → {status}。\n作用范围：当前会话使用的配置；共用该配置的会话也会受影响。\n/llm 每次切换开关，不接受 on/off 参数。"
        ))
