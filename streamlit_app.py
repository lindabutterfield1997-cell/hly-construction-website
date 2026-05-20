from __future__ import annotations

import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st


COMPANY_NAME = "HLY Construction Inc."
DOMAIN = "hlyconstruction.net"
CONTACT_EMAIL = "project@hlyconstruction.net"
ROOT = Path(__file__).resolve().parent
ASSET_DIR = ROOT / "assets"
LOGO_MARK_PATH = ASSET_DIR / "hly-logo-mark-transparent.png"
LOGO_HERO_MARK_PATH = ASSET_DIR / "hly-logo-mark-white-tight-transparent.png"
LOGO_FULL_PATH = ASSET_DIR / "hly-logo-construction-transparent.png"

HERO_IMAGE = (
    "https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3"
    "?auto=format&fit=crop&w=1800&q=85"
)

PROJECT_IMAGES = [
    {
        "title": "Residential Remodel",
        "subtitle": "住宅空间改造",
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=900&q=80",
    },
    {
        "title": "Commercial Interior",
        "subtitle": "商业空间升级",
        "image": "https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=900&q=80",
    },
    {
        "title": "ADU & Remodel",
        "subtitle": "加建与翻新项目",
        "image": "https://images.unsplash.com/photo-1600573472592-401b489a3cdc?auto=format&fit=crop&w=900&q=80",
    },
]

SERVICES = [
    ("Interior Design", "室内设计", "从风格定位、材料搭配到灯光与软装，形成完整设计方案。"),
    ("Design-Build", "装修施工一体化", "设计、预算、采购、施工协同推进，减少沟通成本和返工风险。"),
    ("Space Planning", "空间规划设计", "优化动线、收纳、采光和功能分区，让每一平方英尺更好用。"),
    ("Residential Remodel", "住宅空间改造", "厨房、浴室、客厅、整屋翻新，兼顾美观、耐用和生活习惯。"),
    ("Commercial Remodel", "商业空间改造", "办公室、零售、接待区和展示空间，提升品牌形象与运营效率。"),
    ("ADU & Remodel", "ADU & 改建项目", "支持加建、改建、布局调整和翻新项目的设计施工协调。"),
]

PROCESS = [
    ("01", "Consult", "需求沟通", "了解项目目标、预算范围、时间计划和空间现状。"),
    ("02", "Plan", "方案规划", "输出布局方向、材料建议、施工范围和初步预算。"),
    ("03", "Build", "施工执行", "协调现场、材料、工序和质量检查，稳定推进进度。"),
    ("04", "Deliver", "交付收尾", "完成验收、细节调整和后续维护建议。"),
]


def image_data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def inject_styles() -> None:
    st.markdown(
        f"""
        <style>
            :root {{
                --ink: #17201d;
                --muted: #63706c;
                --paper: #f7f4ee;
                --panel: #ffffff;
                --line: #ded8cf;
                --copper: #b56d3b;
                --teal: #315f5a;
                --sage: #d6ded6;
                --gold: #d8a44f;
            }}

            .stApp {{
                background: var(--paper);
                color: var(--ink);
            }}

            [data-testid="stHeader"] {{
                background: rgba(247, 244, 238, 0.88);
                backdrop-filter: blur(14px);
                border-bottom: 1px solid rgba(222, 216, 207, 0.72);
            }}

            [data-testid="stToolbar"] {{
                right: 1rem;
            }}

            .block-container {{
                max-width: 1180px;
                padding: 0 1.25rem 3rem;
            }}

            .nav {{
                position: sticky;
                top: 0;
                z-index: 20;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 1rem;
                padding: 0.85rem 0 0.7rem;
                background: rgba(247, 244, 238, 0.96);
            }}

            .brand {{
                display: flex;
                align-items: center;
                gap: 0.75rem;
                font-weight: 800;
                letter-spacing: 0;
                color: var(--ink);
            }}

            .brand-logo {{
                width: clamp(5.6rem, 11vw, 7.2rem);
                height: auto;
                display: block;
                object-fit: contain;
            }}

            .nav-links {{
                display: flex;
                align-items: center;
                gap: 0.35rem;
                flex-wrap: wrap;
                justify-content: flex-end;
            }}

            .nav-links a {{
                color: var(--ink);
                text-decoration: none;
                font-size: 0.92rem;
                font-weight: 650;
                padding: 0.5rem 0.7rem;
                border-radius: 6px;
            }}

            .nav-links a:hover {{
                background: rgba(49, 95, 90, 0.11);
            }}

            .hero {{
                min-height: 76vh;
                margin: 0 -1.25rem 3rem;
                padding: 5.4rem max(1.25rem, calc((100vw - 1180px) / 2 + 1.25rem)) 4rem;
                display: flex;
                align-items: center;
                background:
                    linear-gradient(90deg, rgba(17, 25, 23, 0.78), rgba(17, 25, 23, 0.56) 44%, rgba(17, 25, 23, 0.2)),
                    url("{HERO_IMAGE}");
                background-size: cover;
                background-position: center;
                color: #fff;
            }}

            .hero-content {{
                width: min(780px, 100%);
            }}

            .eyebrow {{
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;
                color: #f4d7a1;
                font-size: 0.86rem;
                font-weight: 760;
                text-transform: uppercase;
                letter-spacing: 0;
                margin-bottom: 1.1rem;
            }}

            .eyebrow::before {{
                content: "";
                width: 2.6rem;
                height: 2px;
                background: #f4d7a1;
            }}

            .hero h1 {{
                margin: 0;
                font-size: clamp(3rem, 7vw, 6.4rem);
                line-height: 0.95;
                letter-spacing: 0;
                font-weight: 850;
            }}

            .hero-title {{
                display: flex;
                flex-direction: column;
                gap: 0.1rem;
                max-width: min(100%, 74rem);
            }}

            .hero-title-main {{
                display: flex;
                align-items: center;
                flex-wrap: wrap;
                column-gap: 0.38rem;
            }}

            .hero-title-logo {{
                height: clamp(3.05rem, 7.05vw, 6.45rem);
                width: auto;
                display: inline-block;
                flex: 0 0 auto;
                transform: translateY(0.03em);
            }}

            .hero-title-word {{
                display: inline-block;
            }}

            .hero-title-inc {{
                display: block;
            }}

            .hero-copy {{
                max-width: 650px;
                margin: 1.4rem 0 0;
                color: rgba(255, 255, 255, 0.88);
                font-size: clamp(1.05rem, 1.8vw, 1.28rem);
                line-height: 1.72;
            }}

            .hero-actions {{
                display: flex;
                gap: 0.85rem;
                flex-wrap: wrap;
                margin-top: 2rem;
            }}

            .btn {{
                display: inline-flex;
                align-items: center;
                justify-content: center;
                min-height: 2.9rem;
                padding: 0.78rem 1rem;
                border-radius: 6px;
                font-weight: 780;
                text-decoration: none;
                border: 1px solid rgba(255,255,255,0.28);
            }}

            .btn-primary {{
                background: var(--gold);
                color: #1e211d !important;
                border-color: var(--gold);
            }}

            .btn-secondary {{
                background: rgba(255,255,255,0.08);
                color: #fff !important;
            }}

            .metrics {{
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 1px;
                background: var(--line);
                border: 1px solid var(--line);
                margin: -4.2rem 0 4rem;
                position: relative;
                z-index: 5;
                box-shadow: 0 20px 50px rgba(23, 32, 29, 0.11);
            }}

            .metric {{
                background: var(--panel);
                min-height: 8.2rem;
                padding: 1.35rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}

            .metric strong {{
                color: var(--teal);
                font-size: clamp(1.75rem, 3vw, 2.6rem);
                line-height: 1;
            }}

            .metric span {{
                color: var(--muted);
                line-height: 1.45;
                font-size: 0.95rem;
            }}

            .section {{
                margin: 4.5rem 0;
            }}

            .section-heading {{
                display: grid;
                grid-template-columns: minmax(0, 0.82fr) minmax(280px, 0.6fr);
                gap: 2rem;
                align-items: end;
                margin-bottom: 1.6rem;
            }}

            .section-kicker {{
                color: var(--copper);
                font-weight: 800;
                text-transform: uppercase;
                font-size: 0.8rem;
                margin-bottom: 0.6rem;
            }}

            .section h2 {{
                margin: 0;
                font-size: clamp(2rem, 3.4vw, 3.45rem);
                line-height: 1.06;
                letter-spacing: 0;
            }}

            .section-desc {{
                color: var(--muted);
                line-height: 1.72;
                margin: 0;
                font-size: 1.02rem;
            }}

            .service-grid {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 1rem;
            }}

            .service-card {{
                min-height: 14rem;
                background: var(--panel);
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 1.25rem;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }}

            .service-card h3 {{
                margin: 0;
                font-size: 1.22rem;
                letter-spacing: 0;
            }}

            .service-card h4 {{
                margin: 0.4rem 0 1rem;
                color: var(--teal);
                font-size: 1rem;
            }}

            .service-card p {{
                color: var(--muted);
                line-height: 1.62;
                margin: 0;
            }}

            .project-grid {{
                display: grid;
                grid-template-columns: repeat(3, minmax(0, 1fr));
                gap: 1rem;
            }}

            .project-card {{
                position: relative;
                overflow: hidden;
                border-radius: 8px;
                min-height: 24rem;
                background: #17201d;
                color: #fff;
            }}

            .project-card img {{
                width: 100%;
                height: 24rem;
                object-fit: cover;
                display: block;
                transform: scale(1.01);
                filter: saturate(0.95) contrast(1.02);
            }}

            .project-card::after {{
                content: "";
                position: absolute;
                inset: 0;
                background: linear-gradient(180deg, rgba(0,0,0,0.05), rgba(0,0,0,0.72));
            }}

            .project-label {{
                position: absolute;
                left: 1.15rem;
                right: 1.15rem;
                bottom: 1.1rem;
                z-index: 2;
            }}

            .project-label h3 {{
                margin: 0 0 0.3rem;
                font-size: 1.35rem;
            }}

            .project-label p {{
                margin: 0;
                color: rgba(255,255,255,0.82);
            }}

            .process {{
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 1rem;
            }}

            .process-step {{
                background: var(--sage);
                border: 1px solid rgba(49, 95, 90, 0.16);
                border-radius: 8px;
                padding: 1.15rem;
                min-height: 14.5rem;
            }}

            .process-number {{
                width: 2.6rem;
                height: 2.6rem;
                border-radius: 6px;
                display: grid;
                place-items: center;
                background: var(--teal);
                color: #fff;
                font-weight: 800;
                margin-bottom: 1.5rem;
            }}

            .process-step h3 {{
                margin: 0;
                font-size: 1.15rem;
            }}

            .process-step h4 {{
                margin: 0.35rem 0 0.8rem;
                color: var(--teal);
                font-size: 1rem;
            }}

            .process-step p {{
                color: #4e5d58;
                line-height: 1.55;
                margin: 0;
            }}

            .split-band {{
                display: grid;
                grid-template-columns: minmax(0, 0.9fr) minmax(320px, 0.65fr);
                gap: 2rem;
                align-items: start;
                padding: 2rem;
                background: #1d2b28;
                color: #fff;
                border-radius: 8px;
            }}

            .contact-overview {{
                grid-template-columns: minmax(0, 1fr);
            }}

            .contact-overview > div {{
                max-width: 920px;
            }}

            .split-band h2 {{
                margin: 0 0 1rem;
                font-size: clamp(2rem, 3.2vw, 3rem);
                line-height: 1.05;
            }}

            .split-band p {{
                color: rgba(255,255,255,0.75);
                line-height: 1.72;
                margin: 0 0 1rem;
            }}

            .scope-list {{
                display: grid;
                gap: 0.7rem;
                margin-top: 1.6rem;
            }}

            .scope-item {{
                border-top: 1px solid rgba(255,255,255,0.16);
                padding-top: 0.75rem;
                color: rgba(255,255,255,0.9);
                font-weight: 700;
            }}

            .form-shell {{
                background: #fff;
                border-radius: 8px;
                padding: 1.25rem;
                border: 1px solid var(--line);
                box-shadow: 0 12px 32px rgba(23, 32, 29, 0.1);
            }}

            .form-shell label, .form-shell [data-testid="stMarkdownContainer"] p {{
                color: var(--ink);
            }}

            .mini-summary {{
                background: #f4efe6;
                border: 1px solid #e2d4c2;
                border-radius: 8px;
                padding: 1rem;
                color: var(--ink);
                line-height: 1.6;
                margin-top: 1rem;
            }}

            .contact-copy {{
                background: #1d2b28;
                color: #fff;
                border-radius: 8px;
                padding: 2rem;
                min-height: 100%;
            }}

            .contact-copy h2 {{
                margin: 0 0 1rem;
                font-size: clamp(2rem, 3.2vw, 3rem);
                line-height: 1.05;
            }}

            .contact-copy p {{
                color: rgba(255,255,255,0.75);
                line-height: 1.72;
                margin: 0 0 1rem;
            }}

            .contact-email-card {{
                margin-top: 1.5rem;
                padding: 1rem;
                background: rgba(255,255,255,0.08);
                border: 1px solid rgba(255,255,255,0.16);
                border-radius: 8px;
            }}

            .contact-email-card span {{
                display: block;
                color: rgba(255,255,255,0.68);
                font-size: 0.9rem;
                margin-bottom: 0.35rem;
            }}

            .contact-email-card a {{
                color: #f0c77b;
                font-weight: 800;
                text-decoration: none;
            }}

            .form-intro {{
                background: #fff;
                border: 1px solid var(--line);
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 1rem;
                color: var(--ink);
                box-shadow: 0 12px 32px rgba(23, 32, 29, 0.08);
            }}

            .footer {{
                margin: 4rem -1.25rem 0;
                padding: 2.5rem max(1.25rem, calc((100vw - 1180px) / 2 + 1.25rem));
                background: #141b19;
                color: rgba(255,255,255,0.78);
                display: grid;
                grid-template-columns: auto 1fr auto;
                gap: 1rem;
                align-items: center;
            }}

            .footer-logo-card {{
                width: 12rem;
                background: #f7f4ee;
                border-radius: 8px;
                padding: 0.75rem 0.9rem;
            }}

            .footer-logo {{
                width: 100%;
                display: block;
                height: auto;
            }}

            .footer strong {{
                color: #fff;
            }}

            .footer a {{
                color: #f0c77b;
                text-decoration: none;
                font-weight: 760;
            }}

            div[data-testid="stForm"] {{
                border: 0;
                padding: 0;
            }}

            div[data-testid="stForm"] button {{
                width: 100%;
                border-radius: 6px;
                background: var(--teal);
                color: #fff;
                border: 0;
            }}

            .stButton > button {{
                border-radius: 6px;
            }}

            @media (max-width: 900px) {{
                .nav {{
                    position: relative;
                    align-items: flex-start;
                    flex-direction: column;
                }}

                .nav-links {{
                    justify-content: flex-start;
                }}

                .hero {{
                    min-height: 70vh;
                    padding-top: 4rem;
                }}

                .metrics,
                .service-grid,
                .project-grid,
                .process,
                .section-heading,
                .split-band,
                .footer {{
                    grid-template-columns: 1fr;
                }}

                .metrics {{
                    margin-top: -2rem;
                }}

                .project-card,
                .project-card img {{
                    min-height: 18rem;
                    height: 18rem;
                }}
            }}

            @media (max-width: 520px) {{
                .block-container {{
                    padding-left: 1rem;
                    padding-right: 1rem;
                }}

                .hero,
                .footer {{
                    margin-left: -1rem;
                    margin-right: -1rem;
                }}

                .hero-actions .btn {{
                    width: 100%;
                }}

                .split-band {{
                    padding: 1.2rem;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_nav() -> None:
    logo_mark = image_data_uri(LOGO_MARK_PATH)
    st.markdown(
        f"""
        <nav class="nav">
            <div class="brand">
                <img class="brand-logo" src="{logo_mark}" alt="HLY logo">
                <div>{COMPANY_NAME}</div>
            </div>
            <div class="nav-links">
                <a href="#services">Services</a>
                <a href="#projects">Projects</a>
                <a href="#process">Process</a>
                <a href="#contact">Contact</a>
            </div>
        </nav>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    hero_logo = image_data_uri(LOGO_HERO_MARK_PATH)
    mailto = (
        f"mailto:{CONTACT_EMAIL}?subject="
        f"{quote('Project inquiry for HLY Construction Inc.')}"
    )
    st.markdown(
        f"""
        <section class="hero">
            <div class="hero-content">
                <div class="eyebrow">Design · Remodel · Build</div>
                <h1 class="hero-title">
                    <span class="hero-title-main">
                        <img class="hero-title-logo" src="{hero_logo}" alt="HLY">
                        <span class="hero-title-word">Construction</span>
                    </span>
                    <span class="hero-title-inc">Inc.</span>
                </h1>
                <p class="hero-copy">
                    室内设计与装修施工一体化服务，专注空间规划、住宅与商业空间改造、
                    ADU & remodel project，让设计落地，让施工更清晰。
                </p>
                <div class="hero-actions">
                    <a class="btn btn-primary" href="#contact">Start a Project</a>
                    <a class="btn btn-secondary" href="{mailto}">Email HLY</a>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_metrics() -> None:
    st.markdown(
        """
        <section class="metrics">
            <div class="metric"><strong>01</strong><span>Design-first planning<br>先规划，再施工</span></div>
            <div class="metric"><strong>02</strong><span>Residential & commercial<br>住宅与商业空间</span></div>
            <div class="metric"><strong>03</strong><span>ADU and remodel scope<br>改建与翻新项目</span></div>
            <div class="metric"><strong>04</strong><span>Integrated delivery<br>设计施工协同</span></div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_services() -> None:
    cards = "\n".join(
        f"""
        <article class="service-card">
            <div>
                <h3>{english}</h3>
                <h4>{chinese}</h4>
            </div>
            <p>{body}</p>
        </article>
        """
        for english, chinese, body in SERVICES
    )
    st.markdown(
        f"""
        <section class="section" id="services">
            <div class="section-heading">
                <div>
                    <div class="section-kicker">What We Do</div>
                    <h2>从空间方案到现场施工的完整服务。</h2>
                </div>
                <p class="section-desc">
                    HLY Construction Inc. 面向房主、业主和商业空间经营者，
                    提供清晰、务实、可执行的设计施工服务。
                </p>
            </div>
            <div class="service-grid">
                {cards}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_projects() -> None:
    cards = "\n".join(
        f"""
        <article class="project-card">
            <img src="{project['image']}" alt="{project['title']}">
            <div class="project-label">
                <h3>{project['title']}</h3>
                <p>{project['subtitle']}</p>
            </div>
        </article>
        """
        for project in PROJECT_IMAGES
    )
    st.markdown(
        f"""
        <section class="section" id="projects">
            <div class="section-heading">
                <div>
                    <div class="section-kicker">Project Types</div>
                    <h2>面向日常居住与商业运营的改造项目。</h2>
                </div>
                <p class="section-desc">
                    厨房、浴室、整屋翻新、办公室、零售展示空间、ADU 与 remodel，
                    都可以从空间功能、预算控制和施工落地三个角度同步推进。
                </p>
            </div>
            <div class="project-grid">
                {cards}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_process() -> None:
    steps = "\n".join(
        f"""
        <article class="process-step">
            <div class="process-number">{number}</div>
            <h3>{english}</h3>
            <h4>{chinese}</h4>
            <p>{body}</p>
        </article>
        """
        for number, english, chinese, body in PROCESS
    )
    st.markdown(
        f"""
        <section class="section" id="process">
            <div class="section-heading">
                <div>
                    <div class="section-kicker">How It Works</div>
                    <h2>每一步都围绕范围、预算和质量展开。</h2>
                </div>
                <p class="section-desc">
                    一个好的 remodel 项目，需要在设计阶段把现场条件、材料选择和施工顺序想清楚。
                </p>
            </div>
            <div class="process">
                {steps}
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_contact() -> None:
    st.markdown(
        f"""
        <section class="section" id="contact">
            <div class="split-band contact-overview">
                <div>
                    <div class="section-kicker">Project Inquiry</div>
                    <h2>把你的项目想法整理成第一版需求。</h2>
                    <p>
                        选择项目类型、面积和预算范围后，页面会生成一份简短项目摘要。
                        正式上线时可以接入邮箱、CRM 或第三方表单服务。
                    </p>
                    <div class="scope-list">
                        <div class="scope-item">室内设计 · Interior Design</div>
                        <div class="scope-item">装修施工一体化 · Design-Build</div>
                        <div class="scope-item">住宅/商业空间改造 · Residential & Commercial</div>
                        <div class="scope-item">ADU & Remodel Project</div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

    project_type = st.selectbox(
        "Project Type",
        [
            "Interior Design / 室内设计",
            "Design-Build Remodel / 装修施工一体化",
            "Residential Remodel / 住宅空间改造",
            "Commercial Remodel / 商业空间改造",
            "ADU & Remodel Project",
            "Space Planning / 空间规划设计",
        ],
    )
    area = st.slider("Estimated Area / 预估面积 sq ft", 300, 5000, 1200, 100)
    budget = st.select_slider(
        "Budget Range / 预算范围",
        options=[
            "$25k - $50k",
            "$50k - $100k",
            "$100k - $200k",
            "$200k+",
            "Need consultation",
        ],
        value="$50k - $100k",
    )
    timeline = st.selectbox(
        "Timeline / 计划时间",
        ["As soon as possible", "1-3 months", "3-6 months", "Planning stage"],
    )

    with st.form("project_inquiry", clear_on_submit=False):
        name = st.text_input("Name / 姓名")
        email = st.text_input("Email / 邮箱")
        notes = st.text_area("Project Notes / 项目说明", height=120)
        submitted = st.form_submit_button("Prepare Inquiry")

    summary = (
        f"Project: {project_type}<br>"
        f"Area: about {area:,} sq ft<br>"
        f"Budget: {budget}<br>"
        f"Timeline: {timeline}"
    )
    if notes.strip():
        summary += f"<br>Notes: {notes.strip()}"

    st.markdown(f'<div class="mini-summary">{summary}</div>', unsafe_allow_html=True)

    if submitted:
        if name.strip() and email.strip():
            subject = quote(f"HLY Project Inquiry - {project_type}")
            body = quote(
                f"Name: {name}\nEmail: {email}\nProject: {project_type}\n"
                f"Area: about {area:,} sq ft\nBudget: {budget}\nTimeline: {timeline}\n\n"
                f"Notes:\n{notes}"
            )
            st.success("项目摘要已生成。你也可以用下面的邮件链接发送给 HLY。")
            st.markdown(
                f'<a class="btn btn-primary" href="mailto:{CONTACT_EMAIL}?subject={subject}&body={body}">Send by Email</a>',
                unsafe_allow_html=True,
            )
        else:
            st.warning("请填写姓名和邮箱，方便生成完整咨询信息。")


def render_footer() -> None:
    logo_full = image_data_uri(LOGO_FULL_PATH)
    st.markdown(
        f"""
        <footer class="footer">
            <div class="footer-logo-card">
                <img class="footer-logo" src="{logo_full}" alt="HLY Construction logo">
            </div>
            <div>
                <strong>{COMPANY_NAME}</strong><br>
                Interior Design · Remodel · Design-Build · ADU
            </div>
            <div>
                <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a><br>
                <a href="https://{DOMAIN}">{DOMAIN}</a>
            </div>
        </footer>
        """,
        unsafe_allow_html=True,
    )


def main() -> None:
    st.set_page_config(
        page_title=f"{COMPANY_NAME} | Design & Remodel",
        page_icon="HLY",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    inject_styles()
    render_nav()
    render_hero()
    render_metrics()
    render_services()
    render_projects()
    render_process()
    render_contact()
    render_footer()


if __name__ == "__main__":
    main()
