# ============================================================
# FILE: app.py  —  Enterprise RAG  |  Simple Clean UI
# ============================================================

import os
import tempfile
import streamlit as st

# ── Must be FIRST st.* call ────────────────────────────────
st.set_page_config(
    page_title="Enterprise Knowledge Base",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

from bedrock_rag import query_knowledge_base, upload_document_to_s3
from config import APP_TITLE, APP_ICON, S3_BUCKET_NAME


# ══════════════════════════════════════════════════════════
#  CSS  —  Simple Clean Light UI
# ══════════════════════════════════════════════════════════
st.markdown("""
<style>
/* Hide Streamlit chrome */
#MainMenu, footer { visibility: hidden !important; }
header[data-testid="stHeader"] { background: transparent !important; }

/* Stat cards */
.stat-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 0.75rem 1rem;
  text-align: center;
}
.stat-label {
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #94a3b8;
  margin-bottom: 4px;
}
.stat-value {
  font-size: 0.95rem;
  font-weight: 600;
  color: #1e293b;
}

/* Citation row */
.cite-header {
  font-size: 0.75rem;
  font-weight: 600;
  color: #475569;
  background: #f1f5f9;
  border-left: 3px solid #3b82f6;
  padding: 0.4rem 0.75rem;
  border-radius: 0 4px 4px 0;
  margin-bottom: 4px;
}

/* Title accent */
.title-accent {
  width: 36px;
  height: 2px;
  background: #3b82f6;
  border-radius: 2px;
  margin: 6px 0 16px 0;
}

/* Section tag */
.section-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 1.25rem 0 0.6rem;
}
.section-tag-line {
  flex: 1;
  height: 1px;
  background: #e2e8f0;
}
.section-tag-text {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #94a3b8;
}

/* Badge */
.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: #f0fdf4;
  border: 1px solid #bbf7d0;
  border-radius: 99px;
  padding: 4px 10px;
  font-size: 0.72rem;
  font-weight: 500;
  color: #16a34a;
}
.badge-dot {
  width: 5px;
  height: 5px;
  border-radius: 50%;
  background: #16a34a;
}

/* Sidebar brand */
.sidebar-brand {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 1.25rem;
}
.sidebar-brand-text {
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #1e293b;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════
with st.sidebar:

    # Brand
    st.markdown("""
    <div class="sidebar-brand">
      <div class="sidebar-brand-text">◈ RAG System</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="badge"><span class="badge-dot"></span>Knowledge Base Live</div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # ── Knowledge Base ──
    st.markdown("""<div class="section-tag">
      <div class="section-tag-line"></div>
      <div class="section-tag-text">Knowledge Base</div>
      <div class="section-tag-line"></div>
    </div>""", unsafe_allow_html=True)

    st.info(f"Bucket: `{S3_BUCKET_NAME}`")

    # ── Upload ──
    st.markdown("""<div class="section-tag">
      <div class="section-tag-line"></div>
      <div class="section-tag-text">Upload Docs</div>
      <div class="section-tag-line"></div>
    </div>""", unsafe_allow_html=True)

    st.write("Add documents to the knowledge base.")

    uploaded_file = st.file_uploader(
        label="Choose a file",
        type=["pdf", "txt", "docx"],
        help="PDF, TXT or DOCX"
    )

    if uploaded_file is not None:
        if st.button("⬆  Upload to S3"):
            with st.spinner("Uploading..."):
                temp_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                success = upload_document_to_s3(temp_path, uploaded_file.name)
                if success:
                    st.success("Done! Sync your Bedrock KB.")
                else:
                    st.error("Upload failed — check logs.")

    # ── How to use ──
    st.markdown("""<div class="section-tag">
      <div class="section-tag-line"></div>
      <div class="section-tag-text">How to use</div>
      <div class="section-tag-line"></div>
    </div>""", unsafe_allow_html=True)

    st.markdown("""
    1. Type your question below
    2. Press **Enter** to submit
    3. Read the AI-generated answer
    4. Expand **Sources** for citations
    """)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("↺  Clear History"):
        st.session_state.messages = []
        st.rerun()


# ══════════════════════════════════════════════════════════
#  MAIN HEADER
# ══════════════════════════════════════════════════════════
st.markdown(f"""
<div style="margin-bottom: 0.25rem;">
  <div style="font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;
              color:#94a3b8;margin-bottom:0.4rem;">
    ◈ Enterprise Intelligence
  </div>
  <h1 style="font-size:1.9rem;font-weight:700;color:#0f172a;margin:0;">{APP_ICON} {APP_TITLE}</h1>
  <div class="title-accent"></div>
  <p style="color:#64748b;font-size:0.88rem;margin:0;">
    Ask questions about company documents — accurate, cited answers via Amazon Bedrock RAG.
  </p>
</div>
""", unsafe_allow_html=True)

# ── Stat strip ──
msg_count = len([m for m in st.session_state.get("messages", []) if m["role"] == "user"])

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        '<div class="stat-card"><div class="stat-label">Engine</div>'
        '<div class="stat-value">Amazon Bedrock</div></div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        '<div class="stat-card"><div class="stat-label">Method</div>'
        '<div class="stat-value">RAG Pipeline</div></div>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        f'<div class="stat-card"><div class="stat-label">Queries</div>'
        f'<div class="stat-value">{msg_count} this session</div></div>',
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════
#  SESSION STATE
# ══════════════════════════════════════════════════════════
if "messages" not in st.session_state:
    st.session_state.messages = []


# ══════════════════════════════════════════════════════════
#  CHAT HISTORY
# ══════════════════════════════════════════════════════════
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ══════════════════════════════════════════════════════════
#  CHAT INPUT
# ══════════════════════════════════════════════════════════
if question := st.chat_input("Ask anything about your company documents…"):

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append({"role": "user", "content": question})

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base…"):
            result = query_knowledge_base(question)

        if result["success"]:
            st.markdown(result["answer"])

            if result["citations"]:
                with st.expander(f"◎  Sources  —  {len(result['citations'])} document(s) referenced"):
                    for i, citation in enumerate(result["citations"], start=1):
                        file_name = citation["source"].split("/")[-1]
                        st.markdown(
                            f'<div class="cite-header">Source {i} &nbsp;/&nbsp; {file_name}</div>',
                            unsafe_allow_html=True
                        )
                        st.markdown(f"> {citation['excerpt']}")
                        if i < len(result["citations"]):
                            st.divider()
            else:
                st.warning("No citations found for this answer.")
        else:
            st.error(f"Error: {result['answer']}")

    st.session_state.messages.append({"role": "assistant", "content": result["answer"]})