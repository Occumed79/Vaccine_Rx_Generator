from __future__ import annotations

import base64
from pathlib import Path

import streamlit as st
from streamlit.components.v1 import html as components_html


ASSET_DIR = Path(__file__).parent / "assets"
LOGO_PATH = ASSET_DIR / "occu-med-logo.png"


def _asset_data_uri(path: Path) -> str:
    if not path.exists():
        return ""
    suffix = path.suffix.lower().lstrip(".") or "png"
    mime = "image/svg+xml" if suffix == "svg" else f"image/{suffix}"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def render_landing_page() -> None:
    logo_src = _asset_data_uri(LOGO_PATH)
    logo_html = (
        f'<img class="brand-image" src="{logo_src}" alt="Occu-Med logo" />'
        if logo_src
        else '<div class="brand-fallback">OCCU-MED</div>'
    )

    landing_html = """
    <!doctype html>
    <html>
    <head>
      <meta charset="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
        html, body {
          margin: 0;
          width: 100%;
          height: 100%;
          overflow: hidden;
          background: #050913;
          font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .stage {
          position: relative;
          width: 100vw;
          height: 100vh;
          overflow: hidden;
          display: grid;
          place-items: center;
          background: linear-gradient(135deg, #151d24 0%, #0a1119 48%, #050913 100%);
        }
        .frame {
          position: absolute;
          inset: 18px;
          border: 1px solid rgba(205, 216, 224, .15);
          border-radius: 42px;
          box-shadow: 0 34px 120px rgba(0,0,0,.50), inset 0 1px 0 rgba(255,255,255,.08);
          pointer-events: none;
        }
        .frame::after {
          content: "";
          position: absolute;
          inset: 18px;
          border: 1px solid rgba(255,255,255,.07);
          border-radius: 30px;
        }
        .open-link {
          position: absolute;
          inset: 0;
          z-index: 20;
          cursor: pointer;
        }
        .logo-wrap {
          position: absolute;
          left: 50%;
          top: 50%;
          transform: translate(-50%, -50%);
          z-index: 10;
          display: grid;
          place-items: center;
          pointer-events: none;
        }
        .brand-image {
          position: relative;
          width: min(620px, 58vw);
          max-height: min(340px, 42vh);
          object-fit: contain;
          display: block;
          filter: drop-shadow(0 0 18px rgba(255,255,255,.12));
        }
        .brand-fallback {
          color: white;
          font-family: Georgia, 'Times New Roman', serif;
          font-weight: 800;
          font-size: clamp(2.3rem, 5.2vw, 4.6rem);
          letter-spacing: .13em;
          text-shadow: 0 0 18px rgba(255,255,255,.12);
        }
        @media (max-width: 820px) {
          .brand-image { width: min(520px, 72vw); }
        }
      </style>
    </head>
    <body>
      <div class="stage">
        <div class="frame"></div>
        <div class="logo-wrap">
          __LOGO__
        </div>
        <a class="open-link" href="?view=app" target="_parent" aria-label="Open application"></a>
      </div>
    </body>
    </html>
    """.replace("__LOGO__", logo_html)

    st.markdown(
        """
        <style>
        html, body, .stApp, [data-testid="stAppViewContainer"], section.main {
          height: 100vh !important;
          max-height: 100vh !important;
          overflow: hidden !important;
        }
        .block-container {
          max-width: none !important;
          padding: 0 !important;
          margin: 0 !important;
        }
        iframe {
          display: block !important;
        }
        .parent-click-target {
          position: fixed !important;
          inset: 0 !important;
          z-index: 2147483647 !important;
          display: block !important;
          background: rgba(0,0,0,0) !important;
          cursor: pointer !important;
          text-decoration: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    components_html(landing_html, height=900, scrolling=False)
    st.markdown(
        '<a class="parent-click-target" href="?view=app" target="_self" aria-label="Open application"></a>',
        unsafe_allow_html=True,
    )
    st.stop()
