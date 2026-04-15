# Bad Patch Example｜功能可跑，但風格不合群

## 情境
目標是修補 `/profile/3` 在缺少 nested email 時的 500，並讓 profile UI 至少能安全顯示。

## 問題
下面這種 patch 可能功能上能跑，但會讓 codebase 更不一致。

```python
# anti-pattern example only
from dataclasses import dataclass

class EmailFallbackHelper:
    def build_missing_email_payload(self, user):
        return {
            "displayName": user.get("name", ""),
            "emailAddress": "",
            "hasMissingEmail": True,
            "statusLabel": "missing-email",
        }


def build_profile_payload(user: dict[str, object]):
    helper = EmailFallbackHelper()
    if "email" in user:
        return {
            "displayName": user["name"],
            "emailAddress": user["email"],
            "hasMissingEmail": False,
        }
    contact = user.get("contact", {})
    if not contact.get("email"):
        return helper.build_missing_email_payload(user)
    return {
        "displayName": user["name"],
        "emailAddress": contact["email"],
        "hasMissingEmail": False,
    }
```

## 為什麼它不合群
- invent 新的 `EmailFallbackHelper`，但 repo 目前沒有這種抽象習慣
- 回傳 dict shape，而現有 `profiles.service` 用的是 `ProfilePayload`
- 命名突然改成 `displayName` / `emailAddress`，和現有 repo 不一致
- 在 profile adapter 層偷偷塞進 UI 專用旗標，讓 contract 更混亂
- 這是「功能可能可跑」，但 codebase 會更不一致的典型例子
