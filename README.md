# HLY Construction Inc. Website

这是一个独立的 Streamlit 公司官网项目，和原来的出图平台没有关系。

## 本地运行

```bash
cd "/Users/liyaotang/Documents/New project/hly_construction_website"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

默认本地地址通常是：

```text
http://localhost:8501
```

## 修改公司信息

主要内容在 `streamlit_app.py` 顶部：

- `COMPANY_NAME`: 公司名称
- `DOMAIN`: 域名
- `CONTACT_EMAIL`: 联系邮箱
- `LOGO_MARK_PATH`: 导航栏使用的 HLY 透明 logo
- `LOGO_HERO_MARK_PATH`: 首页大标题使用的白色 HLY 透明 logo
- `LOGO_FULL_PATH`: 页脚使用的 HLY Construction 透明 logo
- `HERO_IMAGE`: 首页大图
- `PROJECT_IMAGES`: 项目展示图片
- `SERVICES`: 服务内容
- `PROCESS`: 服务流程

logo 文件保存在 `assets/`。如果以后需要替换 logo，可以把新版源文件放好后更新
`tools/prepare_logo_assets.py` 里的源文件路径，再运行：

```bash
python tools/prepare_logo_assets.py
```

目前项目展示仍使用外部样板图片。正式上线前，建议替换成 HLY Construction Inc. 的真实项目照片。

## 部署到 hlyconstruction.net

Streamlit 应用需要一个服务器或托管平台运行，域名本身只负责访问入口。这个项目已经补好 Render 部署文件：

```text
Procfile
render.yaml
DEPLOY.md
```

推荐按 [DEPLOY.md](DEPLOY.md) 的步骤部署到 Render，然后把 `hlyconstruction.net` 和 `www.hlyconstruction.net` 绑定到 Render Web Service。

常见部署方式：

1. 部署到 Streamlit Community Cloud、Render、Railway、Fly.io 或 VPS。
2. 获得部署后的访问地址。
3. 在域名服务商后台设置 DNS：
   - 如果平台给 `CNAME`，添加 `www` 的 CNAME。
   - 如果平台给 IP，添加 `A` 记录。
4. 将 `hlyconstruction.net` 和 `www.hlyconstruction.net` 都绑定到部署平台。

如果以后需要表单真实收件，可以把页面里的 mailto 改成 Formspree、Google Forms、Airtable、HubSpot 或自建后端。
