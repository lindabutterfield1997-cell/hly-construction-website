# Deploy HLY Construction Website

目标域名：

```text
hlyconstruction.net
www.hlyconstruction.net
```

## 推荐方式：Render

这个项目是 Streamlit 动态网页，不能像普通静态 HTML 一样直接放到 GitHub Pages。推荐用 Render 的 Web Service，然后把域名 DNS 指向 Render。

## 1. 上传代码到 GitHub

只需要上传这个文件夹：

```text
hly_construction_website/
```

Render 需要从 GitHub / GitLab / Bitbucket 仓库读取代码并自动部署。

## 2. 在 Render 创建 Web Service

在 Render Dashboard 里选择：

```text
New > Web Service
```

如果用手动配置，填写：

```text
Root Directory: hly_construction_website
Build Command: pip install -r requirements.txt
Start Command: streamlit run streamlit_app.py --server.address 0.0.0.0 --server.port $PORT --server.headless true --browser.gatherUsageStats false
```

如果用 Blueprint，则选择这个文件：

```text
hly_construction_website/render.yaml
```

首次部署成功后，Render 会给一个临时地址，类似：

```text
https://hly-construction-website.onrender.com
```

## 3. 在 Render 添加自定义域名

进入 Render 里这个 Web Service：

```text
Settings > Custom Domains
```

添加：

```text
hlyconstruction.net
www.hlyconstruction.net
```

Render 会显示需要添加到域名后台的 DNS 记录。以 Render 实际显示为准。

## 4. 在域名后台设置 DNS

登录你购买 `hlyconstruction.net` 的域名服务商后台，找到 DNS 管理。

通常会设置：

```text
www    CNAME    <Render 给你的目标地址>
@      A/ALIAS/CNAME flattening    <Render 给你的根域名目标>
```

不同域名服务商对根域名 `@` 的叫法不同，可能是 `A`、`ALIAS`、`ANAME` 或 CNAME flattening。按 Render 页面给出的记录填写最稳。

## 5. 等待 HTTPS 生效

DNS 记录保存后通常需要几分钟到数小时生效。Render 会自动签发并续期 HTTPS 证书。

完成后访问：

```text
https://hlyconstruction.net
https://www.hlyconstruction.net
```

## 当前项目文件

- `streamlit_app.py`: 网站主页面
- `requirements.txt`: Python 依赖
- `Procfile`: Web Service 启动命令
- `render.yaml`: Render Blueprint 配置
- `assets/`: logo 图片资源
