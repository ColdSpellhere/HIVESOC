# HIVESOC · 蜂巢安全态势感知中心

HIVESOC 将 QQ 群管理、Web 业务管理和管理员活跃度分析分成三个独立版本的组件。本公开仓库只维护组件版本、集成约定和部署说明。

| 子模块 | 仓库 | 职责 |
| --- | --- | --- |
| `napcatbot` | [HIVESOC-NapCatBot](https://github.com/ColdSpellhere/HIVESOC-NapCatBot)（私有） | QQ 入口、原业务引擎、Web 内部桥及 Hermes 适配 |
| `web` | [HIVESOC-Web](https://github.com/ColdSpellhere/HIVESOC-Web)（私有） | 网站账号、违规表单、查询、报告、统计和平台管理 |
| `algorithm` | [HIVESOC-Algorithm](https://github.com/ColdSpellhere/HIVESOC-Algorithm)（私有） | 活跃度采集、小时/每日快照、评分与反馈调优 |

子模块固定到精确提交，`versions.lock.json` 记录同一组版本。访问主仓库不自动获得私有子仓库的访问权。旧仓库历史保留；将源码从当前树迁到私有子仓库不会使原先已公开的历史变为私有。

具有三个子仓库权限的开发者可运行：

```sh
git clone --recurse-submodules git@github.com:ColdSpellhere/HIVESOC.git
cd HIVESOC
python3 tools/check_layout.py
```

已有克隆更新版本后运行 `git submodule update --init --recursive`。不要使用 `git submodule update --remote` 替代固定版本验证。

各私有子仓库在提交和拉取请求时自动测试。生产发布从私有 Web 或 NapCatBot 仓库的 **Actions → Deploy production → Run workflow** 手动触发；仅允许受信任的 `main` 分支，并核对本仓库已锁定的版本。发布包、构建日志和签名密钥均不放在本公开仓库。算法仓库有 CI，生产运行由独立运维流程管理，尚无本仓自动部署入口。

参见 [版本与发布](docs/releases.md) 和 [组件边界](docs/architecture.md)。

协作开发请阅读私有 Web 仓库的 [开发接入](https://github.com/ColdSpellhere/HIVESOC-Web/blob/main/docs/开发接入.md)、[接口文档](https://github.com/ColdSpellhere/HIVESOC-Web/blob/main/docs/API.md) 和 [OpenAPI](https://github.com/ColdSpellhere/HIVESOC-Web/blob/main/docs/api/openapi.json)。上述链接需要组件访问权限；本文不复制内部接口或业务数据。
