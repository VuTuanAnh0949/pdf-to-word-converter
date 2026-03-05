import io, zipfile
import streamlit as st
from converter.pdf_to_docx import convert_pdf_to_docx
from utils.file_ops import stem_with_hash, safe_basename, timestamp

# Page configuration
st.set_page_config(
    page_title="PDF to Word Converter",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .header-title {
        color: white;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 0;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Upload section */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Success message styling */
    .success-message {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 0.75rem 1.25rem;
        border-radius: 5px;
        margin: 0.5rem 0;
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #6c757d;
        font-size: 0.9rem;
        border-top: 1px solid #e9ecef;
        margin-top: 3rem;
    }
    
    .footer a {
        color: #667eea;
        text-decoration: none;
        font-weight: 600;
    }
    
    .footer a:hover {
        color: #764ba2;
        text-decoration: underline;
    }
    
    /* Button styling */
    .stDownloadButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    
    .stDownloadButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Info box */
    .info-box {
        background-color: #e7f3ff;
        border-left: 4px solid #2196F3;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">📄 PDF to Word Converter</h1>
        <p class="header-subtitle">Transform your PDF files into editable Word documents instantly - Free & Unlimited!</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar - Settings
with st.sidebar:
    st.markdown("### Conversion Settings")
    st.markdown("---")
    
    strategy = st.selectbox(
        "Conversion Strategy",
        ["auto", "precise", "text"],
        help=(
            "• **Auto**: Smart mode - tries precise layout first, falls back to text\n"
            "• **Precise**: Uses pdf2docx only (best for complex layouts)\n"
            "• **Text**: Simple text extraction (most reliable for basic PDFs)"
        ),
        index=0
    )
    
    batch_zip = st.checkbox(
        "Auto-zip multiple files", 
        value=True,
        help="Automatically package multiple converted files into a ZIP archive"
    )
    
    st.markdown("---")
    st.markdown("### Quick Stats")
    st.info("No file size limits\n\nUnlimited conversions\n\n100% Free & Open Source")
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown(
        """
        Built with Streamlit and pdf2docx
        
        **Contact**: [vutuananh0949@gmail.com](mailto:vutuananh0949@gmail.com)
        
        **GitHub**: [@VuTuanAnh0949](https://github.com/VuTuanAnh0949)
        """
    )

# Main content area
st.markdown("### Upload Your PDF Files")
st.markdown("Drag and drop your PDF files below or click to browse")

# Upload section
uploaded_files = st.file_uploader(
    "Choose PDF files",
    type=["pdf"],
    accept_multiple_files=True,
    help="Select one or more PDF files to convert (supports any size)",
    label_visibility="collapsed"
)

def convert_one(filename: str, data: bytes):
    """Convert a single PDF to DOCX and return (name, bytes)."""
    out_bytes = convert_pdf_to_docx(data, strategy=strategy)
    out_name = stem_with_hash(filename, data, ".docx")
    return out_name, out_bytes

# Processing section
if uploaded_files:
    st.markdown("---")
    st.markdown("### Converting Your Files...")
    
    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, uf in enumerate(uploaded_files, 1):
        status_text.markdown(f"**Processing:** `{uf.name}` ({i}/{len(uploaded_files)})")
        pdf_bytes = uf.read()
        
        try:
            name, docx_bytes = convert_one(uf.name, pdf_bytes)
            results.append((name, docx_bytes))
            st.success(f"✅ Successfully converted: **{uf.name}**")
        except Exception as e:
            st.error(f"❌ Failed to convert **{safe_basename(uf.name)}**: {str(e)}")
        
        progress_bar.progress(i / len(uploaded_files))
    
    status_text.empty()
    progress_bar.empty()

    # Download section
    if results:
        st.markdown("---")
        st.markdown("### Download Your Files")
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            if len(results) == 1 and not batch_zip:
                name, payload = results[0]
                st.download_button(
                    label="⬇️ Download Word Document",
                    data=payload,
                    file_name=name,
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True
                )
                st.success(f"Ready to download: **{name}**")
            else:
                buf = io.BytesIO()
                with zipfile.ZipFile(buf, "w") as zf:
                    for name, payload in results:
                        zf.writestr(name, payload)
                buf.seek(0)
                
                st.download_button(
                    label=f"⬇️ Download All Files ({len(results)} files)",
                    data=buf,
                    file_name=f"converted-{timestamp()}.zip",
                    mime="application/zip",
                    use_container_width=True
                )
                st.success(f"Ready to download: **{len(results)} files** in ZIP format")
else:
    # Instructions when no file uploaded
    st.markdown("""
        <div class="info-box">
            <h4 style="margin-top: 0;">How to use:</h4>
            <ol>
                <li>Choose your conversion strategy in the sidebar (Auto recommended)</li>
                <li>Upload one or more PDF files using the uploader above</li>
                <li>Wait for the conversion to complete</li>
                <li>Download your converted Word documents!</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)
    
    # Features highlight
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h4>Fast Conversion</h4>
                <p style="font-size: 0.9rem; color: #6c757d;">Process files in seconds</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h4>Secure & Private</h4>
                <p style="font-size: 0.9rem; color: #6c757d;">Files processed locally</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div style="text-align: center; padding: 1rem;">
                <h4>Batch Processing</h4>
                <p style="font-size: 0.9rem; color: #6c757d;">Convert multiple files at once</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>
            Made by <a href="https://github.com/VuTuanAnh0949" target="_blank">Vũ Tuấn Anh</a> | 
            <a href="mailto:vutuananh0949@gmail.com">Contact</a> | 
            <a href="https://github.com/VuTuanAnh0949/PDF_to_Word_Converter" target="_blank">GitHub</a>
        </p>
        <p style="font-size: 0.8rem; color: #adb5bd; margin-top: 0.5rem;">
            © 2026 PDF to Word Converter | Open Source under MIT License
        </p>
    </div>
""", unsafe_allow_html=True)
