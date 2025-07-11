import streamlit as st
import tempfile
import os
from md2xmind import md_to_xmind

st.set_page_config(
    page_title="Markdown to XMind Converter",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("🧠 Markdown → XMind Converter")
st.sidebar.markdown("""
**Instructions:**
1. Upload your Markdown (.md) file using the uploader below.
2. Click 'Convert' to generate an XMind mind map.
3. Download your .xmind file!

---
**About:**
- Built with Streamlit
- Powered by xmind-sdk
- Designed for technical and professional users
""")

st.title("Markdown to XMind Mind Map Converter")
st.markdown("""
Easily convert your Markdown notes into beautiful XMind mind maps. Perfect for technical documentation, brainstorming, and structured note-taking.

---
""")

uploaded_file = st.file_uploader("Upload your Markdown (.md) file", type=["md"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")
    if st.button("Convert to XMind", type="primary"):
        with st.spinner("Converting to XMind..."):
            with tempfile.TemporaryDirectory() as tmpdir:
                md_path = os.path.join(tmpdir, "input.md")
                xmind_path = os.path.join(tmpdir, "output.xmind")
                with open(md_path, "wb") as f:
                    f.write(uploaded_file.read())
                md_to_xmind(md_path, xmind_path)
                with open(xmind_path, "rb") as f:
                    xmind_bytes = f.read()
                st.success("Conversion complete! Download your XMind file below.")
                st.download_button(
                    label="Download XMind File",
                    data=xmind_bytes,
                    file_name=f"{os.path.splitext(uploaded_file.name)[0]}.xmind",
                    mime="application/octet-stream"
                )
else:
    st.info("Please upload a Markdown file to begin.")

# Custom CSS for a technical, modern look
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(120deg, #232526 0%, #414345 100%);
        color: #f8f8f2;
        font-family: 'Fira Mono', 'Menlo', 'Monaco', 'Consolas', monospace;
    }
    .stButton>button {
        background-color: #0072ff;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        border: none;
        padding: 0.5em 1.5em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .stDownloadButton>button {
        background-color: #43cea2;
        color: #232526;
        border-radius: 6px;
        font-weight: bold;
        border: none;
        padding: 0.5em 1.5em;
        box-shadow: 0 2px 8px rgba(0,0,0,0.15);
    }
    .stSidebar {
        background: #232526;
    }
    </style>
    """,
    unsafe_allow_html=True
) 