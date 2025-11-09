# -*- coding: utf-8 -*-
"""
Streamlit UI 组件模块

包含所有可重用的UI组件
"""

import streamlit as st
import sys
from typing import Dict, Any, Optional, List
from datetime import datetime
import json


def display_header():
    """显示现代化、紧凑的应用程序标题"""
    st.markdown(
        """
    <div class="modern-header">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo-animation">
                    <div class="dna-helix">
                        <div class="helix-strand strand-1"></div>
                        <div class="helix-strand strand-2"></div>
                    </div>
                    <span class="logo-text">◊ DeepCode</span>
                </div>
                <div class="tagline">
                    <span class="highlight">AI 研究引擎</span>
                    <span class="separator">•</span>
                    <span class="org">数据智能实验室 @ 香港大学</span>
                </div>
            </div>
            <div class="status-badge">
                <span class="status-dot"></span>
                <span class="status-text">在线</span>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True,
    )


def display_features():
    """展示DeepCode AI能力，采用世界级、未来感的设计"""

    # Capability Matrix
    st.markdown(
        """
        <div class="capability-matrix">
            <div class="capability-node research-node">
                <div class="node-core">
                    <div class="core-pulse"></div>
                    <div class="core-label">研究</div>
                </div>
                <div class="node-description">
                    <h3>论文转代码 & 文本转代码</h3>
                    <p>神经文档处理和算法合成</p>
                </div>
                <div class="node-metrics">
                    <span class="metric">多智能体</span>
                </div>
            </div>


        </div>
    """,
        unsafe_allow_html=True,
    )

    # Processing Pipeline
    st.markdown(
        """
        <div class="processing-pipeline">
            <div class="pipeline-stage stage-requirements">
                <div class="stage-core">需求</div>
                <div class="stage-description">输入需求</div>
            </div>
            <div class="pipeline-flow">
                <div class="flow-particle"></div>
            </div>
            <div class="pipeline-stage stage-planning">
                <div class="stage-core">规划</div>
                <div class="stage-description">设计与规划</div>
            </div>
            <div class="pipeline-flow">
                <div class="flow-particle"></div>
            </div>
            <div class="pipeline-stage stage-implementation">
                <div class="stage-core">实现</div>
                <div class="stage-description">代码实现</div>
            </div>
            <div class="pipeline-flow">
                <div class="flow-particle"></div>
            </div>
            <div class="pipeline-stage stage-validation">
                <div class="stage-core">验证</div>
                <div class="stage-description">验证与优化</div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )


def display_status(message: str, status_type: str = "info"):
    """
    显示状态消息

    参数:
        message: 状态消息
        status_type: 状态类型 (success, error, warning, info)
    """
    status_classes = {
        "success": "status-success",
        "error": "status-error",
        "warning": "status-warning",
        "info": "status-info",
    }

    icons = {"success": "✅", "error": "❌", "warning": "⚠️", "info": "ℹ️"}

    css_class = status_classes.get(status_type, "status-info")
    icon = icons.get(status_type, "ℹ️")

    st.markdown(
        f"""
    <div class="{css_class}">
        {icon} {message}
    </div>
    """,
        unsafe_allow_html=True,
    )


def system_status_component():
    """系统状态检查组件"""
    st.markdown("### 🔧 系统状态与诊断")

    # Basic system information
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 📊 环境")
        st.info(f"**Python:** {sys.version.split()[0]}")
        st.info(f"**平台:** {sys.platform}")

        # Check key modules
        modules_to_check = [
            ("streamlit", "Streamlit UI 框架"),
            ("asyncio", "异步处理"),
            ("nest_asyncio", "嵌套事件循环"),
            ("concurrent.futures", "线程支持"),
        ]

        st.markdown("#### 📦 模块状态")
        for module_name, description in modules_to_check:
            try:
                __import__(module_name)
                st.success(f"✅ {description}")
            except ImportError:
                st.error(f"❌ {description} - 缺失")

    with col2:
        st.markdown("#### ⚙️ 线程与上下文")

        # Check Streamlit context
        try:
            from streamlit.runtime.scriptrunner import get_script_run_ctx

            ctx = get_script_run_ctx()
            if ctx:
                st.success("✅ Streamlit 上下文可用")
            else:
                st.warning("⚠️ Streamlit 上下文未找到")
        except Exception as e:
            st.error(f"❌ 上下文检查失败: {e}")

        # Check event loop
        try:
            import asyncio

            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    st.info("🔄 事件循环运行中")
                else:
                    st.info("⏸️ 事件循环未运行")
            except RuntimeError:
                st.info("🆕 无事件循环 (正常)")
        except Exception as e:
            st.error(f"❌ 事件循环检查失败: {e}")


def error_troubleshooting_component():
    """错误排查组件"""
    with st.expander("🛠️ 故障排除提示", expanded=False):
        st.markdown("""
        ### 常见问题与解决方案

        #### 1. ScriptRunContext 警告
        - **含义:** Streamlit中的线程上下文警告
        - **解决方案:** 这些警告通常可以安全忽略
        - **预防:** 如果持续出现，请重启应用程序

        #### 2. 异步处理错误
        - **症状:** "事件循环"或"线程"错误
        - **解决方案:** 应用程序使用多种备用方法
        - **操作:** 尝试刷新页面或重新启动

        #### 3. 文件上传问题
        - **检查:** 文件大小 < 200MB
        - **格式:** PDF, DOCX, TXT, HTML, MD
        - **操作:** 尝试不同的文件格式

        #### 4. 处理超时
        - **正常:** 大型论文可能需要5-10分钟
        - **操作:** 耐心等待，检查进度指示器
        - **限制:** 5分钟最大处理时间

        #### 5. 内存问题
        - **症状:** "内存不足"错误
        - **解决方案:** 关闭其他应用程序
        - **操作:** 首先尝试较小/较简单的论文
        """)

        if st.button("🔄 重置应用程序状态"):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.success("应用程序状态已重置！请刷新页面。")
            st.rerun()


def sidebar_control_panel() -> Dict[str, Any]:
    """
    侧边栏控制面板

    返回:
        控制面板状态
    """
    with st.sidebar:
        st.markdown("### 🎛️ 控制面板")

        # Application status
        if st.session_state.processing:
            st.warning("🟡 引擎处理中...")
        else:
            st.info("⚪ 引擎就绪")

        # Workflow configuration options
        st.markdown("### ⚙️ 工作流设置")

        # Indexing functionality toggle
        enable_indexing = st.checkbox(
            "🗂️ 启用代码库索引",
            help="启用GitHub仓库下载和代码库索引。禁用此选项将跳过阶段6（GitHub下载）和阶段7（代码库索引）以加快处理速度。",
            key="enable_indexing",
        )

        if enable_indexing:
            st.success("✅ 完整工作流，索引已启用")
        else:
            st.info("⚡ 快速模式 - 索引已禁用")

        # System information
        st.markdown("### 📊 系统信息")
        st.info(f"**Python:** {sys.version.split()[0]}")
        st.info(f"**平台:** {sys.platform}")

        # Add system status check
        with st.expander("🔧 系统状态"):
            system_status_component()

        # Add error diagnostics
        error_troubleshooting_component()

        st.markdown("---")

        # Processing history
        history_info = display_processing_history()

        return {
            "processing": st.session_state.processing,
            "history_count": history_info["count"],
            "has_history": history_info["has_history"],
            "enable_indexing": enable_indexing,  # Add indexing toggle state
        }


def display_processing_history() -> Dict[str, Any]:
    """
    显示处理历史

    返回:
        历史信息
    """
    st.markdown("### 📊 处理历史")

    has_history = bool(st.session_state.results)
    history_count = len(st.session_state.results)

    if has_history:
        # Only show last 10 records
        recent_results = st.session_state.results[-10:]
        for i, result in enumerate(reversed(recent_results)):
            status_icon = "✅" if result.get("status") == "success" else "❌"
            with st.expander(
                f"{status_icon} 任务 - {result.get('timestamp', '未知')}"
            ):
                st.write(f"**状态:** {result.get('status', '未知')}")
                if result.get("input_type"):
                    st.write(f"**类型:** {result['input_type']}")
                if result.get("error"):
                    st.error(f"错误: {result['error']}")
    else:
        st.info("暂无处理历史")

    # Clear history button
    if has_history:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ 清除历史", use_container_width=True):
                st.session_state.results = []
                st.rerun()
        with col2:
            st.info(f"总计: {history_count} 个任务")

    return {"has_history": has_history, "count": history_count}


def file_input_component(task_counter: int) -> Optional[str]:
    """
    文件输入组件，支持自动PDF转换

    参数:
        task_counter: 任务计数器

    返回:
        PDF文件路径或None
    """
    uploaded_file = st.file_uploader(
        "上传研究论文文件",
        type=[
            "pdf",
            "docx",
            "doc",
            "ppt",
            "pptx",
            "xls",
            "xlsx",
            "html",
            "htm",
            "txt",
            "md",
        ],
        help="支持格式: PDF, Word, PowerPoint, Excel, HTML, Text (所有文件都将转换为PDF)",
        key=f"file_uploader_{task_counter}",
    )

    if uploaded_file is not None:
        # Display file information
        file_size = len(uploaded_file.getvalue())
        st.info(f"📄 **File:** {uploaded_file.name} ({format_file_size(file_size)})")

        # Save uploaded file using cross-platform file handler
        try:
            import sys
            from pathlib import Path

            # Add project root to path for imports
            current_dir = Path(__file__).parent
            project_root = current_dir.parent
            if str(project_root) not in sys.path:
                sys.path.insert(0, str(project_root))

            # Import required modules
            from tools.pdf_converter import PDFConverter
            from utils.cross_platform_file_handler import get_file_handler

            # Get cross-platform file handler
            file_handler = get_file_handler()

            # Save original file using safe method
            file_ext = uploaded_file.name.split(".")[-1].lower()
            original_file_path = file_handler.create_safe_temp_file(
                suffix=f".{file_ext}",
                prefix=f"upload_{uploaded_file.name.split('.')[0]}_",
                content=uploaded_file.getvalue(),
            )

            st.success("✅ File uploaded successfully!")

            # Check if file is already PDF
            if file_ext == "pdf":
                st.info("📑 File is already in PDF format, no conversion needed.")
                return str(
                    original_file_path
                )  # Convert Path to string for compatibility

            # Convert to PDF
            with st.spinner(f"🔄 Converting {file_ext.upper()} to PDF..."):
                try:
                    converter = PDFConverter()

                    # Check dependencies
                    deps = converter.check_dependencies()
                    missing_deps = []

                    if (
                        file_ext in {"doc", "docx", "ppt", "pptx", "xls", "xlsx"}
                        and not deps["libreoffice"]
                    ):
                        missing_deps.append("LibreOffice")

                    if file_ext in {"txt", "md"} and not deps["reportlab"]:
                        missing_deps.append("ReportLab")

                    if missing_deps:
                        st.error(f"❌ Missing dependencies: {', '.join(missing_deps)}")
                        st.info("💡 Please install the required dependencies:")
                        if "LibreOffice" in missing_deps:
                            st.code(
                                "# Install LibreOffice\n"
                                "# Windows: Download from https://www.libreoffice.org/\n"
                                "# macOS: brew install --cask libreoffice\n"
                                "# Ubuntu: sudo apt-get install libreoffice"
                            )
                        if "ReportLab" in missing_deps:
                            st.code("pip install reportlab")

                        # Clean up original file using safe method
                        file_handler.safe_remove_file(original_file_path)
                        return None

                    # Perform conversion
                    pdf_path = converter.convert_to_pdf(str(original_file_path))

                    # Clean up original file using safe method
                    file_handler.safe_remove_file(original_file_path)

                    # Display conversion result
                    pdf_size = Path(pdf_path).stat().st_size
                    st.success("✅ Successfully converted to PDF!")
                    st.info(
                        f"📑 **PDF File:** {Path(pdf_path).name} ({format_file_size(pdf_size)})"
                    )

                    return str(pdf_path)

                except Exception as e:
                    st.error(f"❌ PDF conversion failed: {str(e)}")
                    st.warning("💡 You can try:")
                    st.markdown("- Converting the file to PDF manually")
                    st.markdown("- Using a different file format")
                    st.markdown("- Checking if the file is corrupted")

                    # Clean up original file using safe method
                    file_handler.safe_remove_file(original_file_path)
                    return None

        except Exception as e:
            st.error(f"❌ Failed to process uploaded file: {str(e)}")
            return None

    return None


def url_input_component(task_counter: int) -> Optional[str]:
    """
    URL输入组件

    参数:
        task_counter: 任务计数器

    返回:
        URL或None
    """
    url_input = st.text_input(
        "输入论文URL",
        placeholder="https://arxiv.org/abs/..., https://ieeexplore.ieee.org/..., 等",
        help="输入研究论文的直接链接 (arXiv, IEEE, ACM, 等)",
        key=f"url_input_{task_counter}",
    )

    if url_input:
        # Simple URL validation
        if url_input.startswith(("http://", "https://")):
            st.success(f"✅ 已输入URL: {url_input}")
            return url_input
        else:
            st.warning("⚠️ 请输入以 http:// 或 https:// 开头的有效URL")
            return None

    return None


def requirement_analysis_mode_selector(task_counter: int) -> str:
    """
    需求分析模式选择器

    参数:
        task_counter: 任务计数器

    返回:
        选择的模式 ("direct" 或 "guided")
    """
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 15px;
                border-left: 4px solid #00ff88;">
        <h4 style="color: white; margin: 0 0 10px 0; font-size: 1.1rem;">
            🎯 选择您的输入模式
        </h4>
        <p style="color: #e0f7fa; margin: 0; font-size: 0.9rem;">
            选择您希望如何提供需求
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    mode = st.radio(
        "输入模式:",
        ["🚀 直接输入", "🧠 引导分析"],
        index=0
        if st.session_state.get("requirement_analysis_mode", "direct") == "direct"
        else 1,
        horizontal=True,
        help="直接: 直接输入需求。引导: AI会提问帮助您澄清需求。",
        key=f"req_mode_{task_counter}",
    )

    return "direct" if mode.startswith("🚀") else "guided"


def requirement_questions_component(
    questions: List[Dict], task_counter: int
) -> Dict[str, str]:
    """
    需求问题显示和答案收集组件

    参数:
        questions: 问题列表
        task_counter: 任务计数器

    返回:
        用户答案字典
    """
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 50%, #fecfef 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #ff6b6b;">
        <h4 style="color: #2d3748; margin: 0 0 10px 0; font-size: 1.1rem;">
            📝 帮助我们更好地理解您的需求
        </h4>
        <p style="color: #4a5568; margin: 0; font-size: 0.9rem;">
            请回答以下问题以帮助我们生成更好的代码。您可以跳过任何问题。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    answers = {}

    for i, question in enumerate(questions):
        with st.expander(
            f"📋 {question.get('category', '问题')} - {question.get('importance', '中等')} 优先级",
            expanded=i < 3,
        ):
            st.markdown(f"**{question['question']}**")

            if question.get("hint"):
                st.info(f"💡 {question['hint']}")

            answer = st.text_area(
                "您的答案:",
                placeholder="在此输入您的答案，或留空跳过...",
                height=80,
                key=f"answer_{i}_{task_counter}",
            )

            if answer and answer.strip():
                answers[str(i)] = answer.strip()

    st.markdown("---")
    st.info(f"📊 您已回答了 {len(answers)} 个问题，共 {len(questions)} 个问题。")

    return answers


def requirement_summary_component(summary: str, task_counter: int) -> bool:
    """
    需求摘要显示和确认组件

    参数:
        summary: 需求摘要文档
        task_counter: 任务计数器

    返回:
        用户是否确认需求
    """
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #38b2ac;">
        <h4 style="color: #2d3748; margin: 0 0 10px 0; font-size: 1.1rem;">
            📋 详细需求摘要
        </h4>
        <p style="color: #4a5568; margin: 0; font-size: 0.9rem;">
            根据您的输入，这是我们生成的详细需求文档。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Display requirement summary
    with st.expander("📖 查看详细需求", expanded=True):
        st.markdown(summary)

    # Confirmation options
    st.markdown("### 🎯 下一步")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "✅ 看起来不错，继续",
            type="primary",
            use_container_width=True,
            key=f"confirm_{task_counter}",
        ):
            # Mark requirements as confirmed, prepare to enter code generation
            st.session_state.requirements_confirmed = True
            return True

    with col2:
        if st.button(
            "✏️ 编辑需求",
            type="secondary",
            use_container_width=True,
            key=f"edit_{task_counter}",
        ):
            # Enter editing mode
            st.session_state.requirement_analysis_step = "editing"
            st.session_state.edit_feedback = ""
            st.rerun()

    with col3:
        if st.button(
            "🔄 重新开始", use_container_width=True, key=f"restart_{task_counter}"
        ):
            # Complete reset
            st.session_state.requirement_analysis_mode = "direct"
            st.session_state.requirement_analysis_step = "input"
            st.session_state.generated_questions = []
            st.session_state.user_answers = {}
            st.session_state.detailed_requirements = ""
            st.rerun()

    return False


def requirement_editing_component(current_requirements: str, task_counter: int) -> bool:
    """
    交互式需求编辑组件

    参数:
        current_requirements: 当前需求文档内容
        task_counter: 任务计数器

    返回:
        编辑是否完成
    """
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #e17055;">
        <h4 style="color: #2d3748; margin: 0 0 10px 0; font-size: 1.1rem;">
            ✏️ 编辑需求文档
        </h4>
        <p style="color: #4a5568; margin: 0; font-size: 0.9rem;">
            查看当前需求并告诉我们您希望如何修改它们。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Display current requirements
    st.markdown("### 📋 当前需求")
    with st.expander("📖 查看当前需求文档", expanded=True):
        st.markdown(current_requirements)

    # Ask for modification feedback
    st.markdown("### 💭 您希望如何修改需求？")
    st.markdown("请描述您的更改、添加或修正：")

    edit_feedback = st.text_area(
        "您的修改请求：",
        value=st.session_state.edit_feedback,
        placeholder="例如：\n- 添加用户认证功能\n- 将数据库从MySQL更改为PostgreSQL",
        height=120,
        key=f"edit_feedback_{task_counter}",
    )

    # Update session state
    st.session_state.edit_feedback = edit_feedback

    # Action buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "🔄 应用更改",
            type="primary",
            use_container_width=True,
            key=f"apply_edit_{task_counter}",
        ):
            if edit_feedback.strip():
                # Start requirement modification process
                st.session_state.requirements_editing = True
                st.info("🔄 正在处理您的修改请求...")
                return True
            else:
                st.warning("请先提供您的修改请求。")

    with col2:
        if st.button(
            "↩️ 返回摘要",
            type="secondary",
            use_container_width=True,
            key=f"back_summary_{task_counter}",
        ):
            # Go back to summary view
            st.session_state.requirement_analysis_step = "summary"
            st.session_state.edit_feedback = ""
            st.rerun()

    with col3:
        if st.button(
            "🔄 重新开始",
            use_container_width=True,
            key=f"restart_edit_{task_counter}",
        ):
            # Complete reset
            st.session_state.requirement_analysis_mode = "direct"
            st.session_state.requirement_analysis_step = "input"
            st.session_state.generated_questions = []
            st.session_state.user_answers = {}
            st.session_state.detailed_requirements = ""
            st.session_state.edit_feedback = ""
            st.rerun()

    return False


def chat_input_component(task_counter: int) -> Optional[str]:
    """
    增强型聊天输入组件，支持需求分析

    参数:
        task_counter: 任务计数器

    返回:
        用户编码需求或None
    """
    # Select input mode
    selected_mode = requirement_analysis_mode_selector(task_counter)

    # Update requirement analysis mode
    st.session_state.requirement_analysis_mode = selected_mode

    if selected_mode == "direct":
        return _direct_input_component(task_counter)
    else:
        return _guided_analysis_component(task_counter)


def _direct_input_component(task_counter: int) -> Optional[str]:
    """直接输入模式组件"""
    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #4dd0e1;">
        <h4 style="color: white; margin: 0 0 10px 0; font-size: 1.1rem;">
            🚀 直接输入模式
        </h4>
        <p style="color: #e0f7fa; margin: 0; font-size: 0.9rem;">
            直接描述您的编码需求。我们的AI将分析并生成全面的实现计划。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Examples to help users understand what they can input
    with st.expander("💡 查看示例", expanded=False):
        st.markdown("""
        **学术研究示例:**
        - "我需要实现一个用于机器人控制的强化学习算法"
        - "创建一个带有注意力机制的图像分类神经网络"
        - "构建一个用于情感分析的自然语言处理管道"

        **工程项目示例:**
        - "开发一个带有用户认证的项目管理Web应用程序"
        - "创建一个用于销售分析的数据可视化仪表板"
        - "构建一个带有数据库集成的电子商务平台REST API"

        **混合项目示例:**
        - "实现一个带有Web界面的机器学习模型用于实时预测"
        - "创建一个具有用户友好GUI的研究工具用于数据分析"
        - "构建一个同时具有学术评估指标和生产部署的聊天机器人"
        """)

    # Main text area for user input
    user_input = st.text_area(
        "输入您的编码需求：",
        placeholder="""示例：我想构建一个能够分析社交媒体帖子用户情感的Web应用程序。该应用程序应具备：

1. 一个用户友好的界面，用户可以输入文本或上传文件
2. 一个执行情感分析的机器学习后端
3. 带有图表和统计结果的可视化
4. 用户认证和数据存储功能
5. 用于与其他应用程序集成的REST API

系统应具有可扩展性并可用于生产环境，具有适当的错误处理和文档。""",
        height=200,
        help="描述您想要构建的内容，包括功能、技术和任何特定要求",
        key=f"direct_input_{task_counter}",
    )

    if user_input and len(user_input.strip()) > 20:  # Minimum length check
        # Display input summary
        word_count = len(user_input.split())
        char_count = len(user_input)

        st.success(
            f"✅ **需求已捕获！** ({word_count} 个单词, {char_count} 个字符)"
        )

        # Show a preview of what will be analyzed
        with st.expander("📋 预览您的需求", expanded=False):
            st.text_area(
                "您的输入：",
                user_input,
                height=100,
                disabled=True,
                key=f"direct_preview_{task_counter}",
            )

        return user_input.strip()

    elif user_input and len(user_input.strip()) <= 20:
        st.warning(
            "⚠️ 请提供更详细的需求（至少20个字符）"
        )
        return None

    return None


def _guided_analysis_component(task_counter: int) -> Optional[str]:
    """引导分析模式组件"""

    # Check if requirements are confirmed, if confirmed return detailed requirements directly
    if st.session_state.get("requirements_confirmed", False):
        detailed_requirements = st.session_state.get("detailed_requirements", "")
        if detailed_requirements:
            # Show confirmation message and return requirements for processing
            st.success("🎉 需求分析完成！开始代码生成...")
        st.info(
            "🔄 根据您确认的需求自动进行代码生成。"
        )
        return detailed_requirements

    st.markdown(
        """
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                border-left: 4px solid #00ff88;">
        <h4 style="color: white; margin: 0 0 10px 0; font-size: 1.1rem;">
            🧠 引导分析模式
        </h4>
        <p style="color: #e0f7fa; margin: 0; font-size: 0.9rem;">
            让我们的AI通过一系列问题引导您，以更好地理解您的需求。
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Check current step
    current_step = st.session_state.get("requirement_analysis_step", "input")

    if current_step == "input":
        return _guided_input_step(task_counter)
    elif current_step == "questions":
        return _guided_questions_step(task_counter)
    elif current_step == "summary":
        return _guided_summary_step(task_counter)
    elif current_step == "editing":
        return _guided_editing_step(task_counter)
    else:
        # Reset to initial state
        st.session_state.requirement_analysis_step = "input"
        st.rerun()


def _guided_input_step(task_counter: int) -> Optional[str]:
    """引导模式的初始输入步骤"""
    st.markdown("### 📝 步骤1：告诉我们您的基本想法")

    user_input = st.text_area(
        "您想要构建什么？（简要描述即可）",
        placeholder="示例：一个用于社交媒体帖子情感分析的Web应用程序",
        height=120,
        help="不用担心细节 - 我们接下来会问具体问题！",
        key=f"guided_input_{task_counter}",
    )

    if user_input and len(user_input.strip()) > 10:
        col1, col2 = st.columns([3, 1])

        with col1:
            st.info(f"📝 已捕获初始想法：{len(user_input.split())} 个单词")

        with col2:
            if st.button(
                "🚀 生成问题", type="primary", use_container_width=True
            ):
                # Save initial input and enter question generation step
                st.session_state.initial_requirement = user_input.strip()
                st.session_state.requirement_analysis_step = "questions"
                st.rerun()

    elif user_input and len(user_input.strip()) <= 10:
        st.warning(
            "⚠️ 请至少提供一个简要描述（超过10个字符）"
        )

    return None


def _guided_questions_step(task_counter: int) -> Optional[str]:
    """引导模式的问题回答步骤"""
    st.markdown("### 🤔 步骤2：回答问题以完善您的需求")

    # Display initial requirements
    with st.expander("📋 您的初始想法", expanded=False):
        st.write(st.session_state.get("initial_requirement", ""))

    # Check if questions have been generated
    if not st.session_state.get("generated_questions"):
        st.info("🔄 正在为您的项目生成个性化问题...")

        # Async call needed here, but we show placeholder in UI first
        if st.button("🎯 立即生成问题", type="primary"):
            st.session_state.questions_generating = True
            st.rerun()
        return None

    # Display questions and collect answers
    questions = st.session_state.generated_questions
    answers = requirement_questions_component(questions, task_counter)
    st.session_state.user_answers = answers

    # Continue button
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button(
            "📋 生成详细需求",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.requirement_analysis_step = "summary"
            st.rerun()

    with col1:
        if st.button("⬅️ 返回", use_container_width=True):
            st.session_state.requirement_analysis_step = "input"
            st.rerun()

    return None


def _guided_summary_step(task_counter: int) -> Optional[str]:
    """引导模式的需求摘要步骤"""
    st.markdown("### 📋 步骤3：查看并确认您的详细需求")

    # Check if detailed requirements have been generated
    if not st.session_state.get("detailed_requirements"):
        st.info("🔄 正在根据您的答案生成详细需求...")

        if st.button("📋 立即生成需求", type="primary"):
            st.session_state.requirements_generating = True
            st.rerun()
        return None

    # Display requirement summary and get confirmation
    summary = st.session_state.detailed_requirements
    confirmed = requirement_summary_component(summary, task_counter)

    if confirmed:
        # Return detailed requirements as final input
        return summary

    return None


def _guided_editing_step(task_counter: int) -> Optional[str]:
    """引导模式的需求编辑步骤"""
    st.markdown("### ✏️ 步骤4：编辑您的需求")

    # Get current requirements
    current_requirements = st.session_state.get("detailed_requirements", "")
    if not current_requirements:
        st.error("未找到要编辑的需求。请重新开始。")
        st.session_state.requirement_analysis_step = "input"
        st.rerun()
        return None

    # Show editing component
    editing_requested = requirement_editing_component(
        current_requirements, task_counter
    )

    if editing_requested:
        # User has provided editing feedback, trigger requirement modification
        st.session_state.requirements_editing = True
        st.rerun()
        return None

    return None


def input_method_selector(task_counter: int) -> tuple[Optional[str], Optional[str]]:
    """
    输入方法选择器

    参数:
        task_counter: 任务计数器

    返回:
        (input_source, input_type)
    """
    st.markdown(
        """
    <h3 style="color: var(--text-primary) !important; font-family: 'Inter', sans-serif !important; font-weight: 600 !important; font-size: 1.5rem !important; margin-bottom: 1rem !important;">
            🚀 开始处理
        </h3>
    """,
        unsafe_allow_html=True,
    )

    # Input options
    st.markdown(
        """
    <p style="color: var(--text-secondary) !important; font-family: 'Inter', sans-serif !important; font-weight: 500 !important; margin-bottom: 1rem !important;">
        选择输入方法：
    </p>
    """,
        unsafe_allow_html=True,
    )

    input_method = st.radio(
        "选择您的输入方法：",
        ["📁 上传文件", "🌐 输入URL", "💬 聊天输入"],
        horizontal=True,
        label_visibility="hidden",
        key=f"input_method_{task_counter}",
    )

    input_source = None
    input_type = None

    if input_method == "📁 上传文件":
        input_source = file_input_component(task_counter)
        input_type = "file" if input_source else None
    elif input_method == "🌐 输入URL":
        input_source = url_input_component(task_counter)
        input_type = "url" if input_source else None
    else:  # Chat input
        input_source = chat_input_component(task_counter)
        input_type = "chat" if input_source else None

    return input_source, input_type


def results_display_component(result: Dict[str, Any], task_counter: int):
    """
    结果显示组件

    参数:
        result: 处理结果
        task_counter: 任务计数器
    """
    st.markdown("### 📋 处理结果")

    # Display overall status
    if result.get("status") == "success":
        st.success("🎉 **所有工作流成功完成！**")
    else:
        st.error("❌ **处理遇到错误**")

    # Create tabs to organize different phase results
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "📊 分析阶段",
            "📥 下载阶段",
            "🔧 实现阶段",
            "📁 生成的文件",
        ]
    )

    with tab1:
        st.markdown("#### 📊 论文分析结果")
        with st.expander("分析输出详情", expanded=True):
            analysis_result = result.get(
                "analysis_result", "无分析结果可用"
            )
            try:
                # Try to parse JSON result for formatted display
                if analysis_result.strip().startswith("{"):
                    parsed_analysis = json.loads(analysis_result)
                    st.json(parsed_analysis)
                else:
                    st.text_area(
                        "原始分析输出",
                        analysis_result,
                        height=300,
                        key=f"analysis_{task_counter}",
                    )
            except Exception:
                st.text_area(
                    "分析输出",
                    analysis_result,
                    height=300,
                    key=f"analysis_{task_counter}",
                )

    with tab2:
        st.markdown("#### 📥 下载与准备结果")
        with st.expander("下载过程详情", expanded=True):
            download_result = result.get(
                "download_result", "无下载结果可用"
            )
            st.text_area(
                "下载输出",
                download_result,
                height=300,
                key=f"download_{task_counter}",
            )

            # Try to extract file path information
            if "paper_dir" in download_result or "path" in download_result.lower():
                st.info(
                    "💡 **提示:** 在上面的输出中查找文件路径以定位生成的文件"
                )

    with tab3:
        st.markdown("#### 🔧 代码实现结果")
        repo_result = result.get("repo_result", "无实现结果可用")

        # Analyze implementation results to extract key information
        if "successfully" in repo_result.lower():
            st.success("✅ 代码实现成功完成！")
        elif "failed" in repo_result.lower():
            st.warning("⚠️ 代码实现遇到问题")
        else:
            st.info("ℹ️ 代码实现状态不明确")

        with st.expander("实现详情", expanded=True):
            st.text_area(
                "仓库与代码生成输出",
                repo_result,
                height=300,
                key=f"repo_{task_counter}",
            )

        # Try to extract generated code directory information
        if "Code generated in:" in repo_result:
            code_dir = repo_result.split("Code generated in:")[-1].strip()
            st.markdown(f"**📁 生成的代码目录:** `{code_dir}`")

        # Display workflow stage details
        st.markdown("#### 🔄 已完成的工作流阶段")
        stages = [
            ("📄 文档处理", "✅"),
            ("🔍 参考分析", "✅"),
            ("📋 计划生成", "✅"),
            ("📦 仓库下载", "✅"),
            ("🗂️ 代码库索引", "✅" if "indexing" in repo_result.lower() else "⚠️"),
            (
                "⚙️ 代码实现",
                "✅" if "successfully" in repo_result.lower() else "⚠️",
            ),
        ]

        for stage_name, status in stages:
            st.markdown(f"- {stage_name}: {status}")

    with tab4:
        st.markdown("#### 📁 生成的文件与报告")

        # Try to extract file paths from results
        all_results = (
            f"{result.get('download_result', '')} {result.get('repo_result', '')}"
        )

        # Look for possible file path patterns
        import re

        file_patterns = [
            r"([^\s]+\.txt)",
            r"([^\s]+\.json)",
            r"([^\s]+\.py)",
            r"([^\s]+\.md)",
            r"paper_dir[:\s]+([^\s]+)",
            r"saved to ([^\s]+)",
            r"generated in[:\s]+([^\s]+)",
        ]

        found_files = set()
        for pattern in file_patterns:
            matches = re.findall(pattern, all_results, re.IGNORECASE)
            for match in matches:
                if isinstance(match, tuple):
                    found_files.update(match)
                else:
                    found_files.add(match)

        if found_files:
            st.markdown("**📄 检测到的生成文件:**")
            for file_path in sorted(found_files):
                if file_path and len(file_path) > 3:  # Filter out too short matches
                    st.markdown(f"- `{file_path}`")
        else:
            st.info(
                "在输出中未检测到具体的文件路径。请检查上面的详细结果以查找文件位置。"
            )

        # Provide option to view raw results
        with st.expander("查看原始处理结果"):
            st.json(
                {
                    "analysis_result": result.get("analysis_result", ""),
                    "download_result": result.get("download_result", ""),
                    "repo_result": result.get("repo_result", ""),
                    "status": result.get("status", "unknown"),
                }
            )

    # Action buttons
    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 处理新论文", type="primary", use_container_width=True):
            st.session_state.show_results = False
            st.session_state.last_result = None
            st.session_state.last_error = None
            st.session_state.task_counter += 1
            st.rerun()

    with col2:
        if st.button("💾 导出结果", type="secondary", use_container_width=True):
            # Create result export
            export_data = {
                "timestamp": datetime.now().isoformat(),
                "processing_results": result,
                "status": result.get("status", "unknown"),
            }
            st.download_button(
                label="📄 下载结果JSON",
                data=json.dumps(export_data, indent=2, ensure_ascii=False),
                file_name=f"paper_processing_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
                use_container_width=True,
            )


def progress_display_component():
    """
    进度显示组件

    返回:
        (progress_bar, status_text)
    """
    # Display processing progress title
    st.markdown("### 📊 处理进度")

    # Create progress container
    progress_container = st.container()

    with progress_container:
        # Add custom CSS styles
        st.markdown(
            """
        <style>
        .progress-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 15px;
            padding: 20px;
            margin: 10px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .progress-steps {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
            flex-wrap: wrap;
        }
        .progress-step {
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
            padding: 8px 12px;
            margin: 2px;
            color: white;
            font-size: 0.8rem;
            font-weight: 500;
            border: 2px solid transparent;
            transition: all 0.3s ease;
        }
        .progress-step.active {
            background: rgba(255,255,255,0.3);
            border-color: #00ff88;
            box-shadow: 0 0 15px rgba(0,255,136,0.3);
        }
        .progress-step.completed {
            background: rgba(0,255,136,0.2);
            border-color: #00ff88;
        }
        .status-text {
            color: white;
            font-weight: 600;
            font-size: 1.1rem;
            margin: 10px 0;
            text-align: center;
        }
        </style>
        """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="progress-container">', unsafe_allow_html=True)

        # Create step indicator
        st.markdown(
            """
        <div class="progress-steps">
            <div class="progress-step" id="step-init">🚀 Initialize</div>
            <div class="progress-step" id="step-analyze">📊 Analyze</div>
            <div class="progress-step" id="step-download">📥 Download</div>
            <div class="progress-step" id="step-references">🔍 References</div>
            <div class="progress-step" id="step-plan">📋 Plan</div>
            <div class="progress-step" id="step-repos">📦 Repos</div>
            <div class="progress-step" id="step-index">🗂️ Index</div>
            <div class="progress-step" id="step-implement">⚙️ Implement</div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Create progress bar and status text
        progress_bar = st.progress(0)
        status_text = st.empty()

        st.markdown("</div>", unsafe_allow_html=True)

    return progress_bar, status_text


def enhanced_progress_display_component(
    enable_indexing: bool = True, chat_mode: bool = False
):
    """
    Enhanced progress display component

    Args:
        enable_indexing: Whether indexing is enabled
        chat_mode: Whether in chat mode (user requirements input)

    Returns:
        (progress_bar, status_text, step_indicator, workflow_steps)
    """
    # Display processing progress title
    if chat_mode:
        st.markdown("### 💬 AI Chat Planning - Requirements to Code Workflow")
    elif enable_indexing:
        st.markdown("### 🚀 AI Research Engine - Full Processing Workflow")
    else:
        st.markdown(
            "### ⚡ AI Research Engine - Fast Processing Workflow (Indexing Disabled)"
        )

    # Create progress container
    progress_container = st.container()

    with progress_container:
        # Workflow step definitions - adjust based on mode and indexing toggle
        if chat_mode:
            # Chat mode - simplified workflow for user requirements
            workflow_steps = [
                ("🚀", "Initialize", "Setting up chat engine"),
                ("💬", "Planning", "Analyzing requirements"),
                ("🏗️", "Setup", "Creating workspace"),
                ("📝", "Save Plan", "Saving implementation plan"),
                ("⚙️", "Implement", "Generating code"),
            ]
        elif enable_indexing:
            workflow_steps = [
                ("🚀", "Initialize", "Setting up AI engine"),
                ("📊", "Analyze", "Analyzing paper content"),
                ("📥", "Download", "Processing document"),
                (
                    "📋",
                    "Plan",
                    "Generating code plan",
                ),  # Phase 3: code planning orchestration
                (
                    "🔍",
                    "References",
                    "Analyzing references",
                ),  # Phase 4: now conditional
                ("📦", "Repos", "Downloading repositories"),  # Phase 5: GitHub download
                ("🗂️", "Index", "Building code index"),  # Phase 6: code indexing
                ("⚙️", "Implement", "Implementing code"),  # Phase 7: code implementation
            ]
        else:
            # Fast mode - skip References, Repos and Index steps
            workflow_steps = [
                ("🚀", "Initialize", "Setting up AI engine"),
                ("📊", "Analyze", "Analyzing paper content"),
                ("📥", "Download", "Processing document"),
                (
                    "📋",
                    "Plan",
                    "Generating code plan",
                ),  # Phase 3: code planning orchestration
                (
                    "⚙️",
                    "Implement",
                    "Implementing code",
                ),  # Jump directly to implementation
            ]

        # Display step grid with fixed layout
        # Use a maximum of 8 columns for consistent sizing
        max_cols = 8
        cols = st.columns(max_cols)
        step_indicators = []

        # Calculate column spacing for centering steps
        total_steps = len(workflow_steps)
        if total_steps <= max_cols:
            # Center the steps when fewer than max columns
            start_col = (max_cols - total_steps) // 2
        else:
            start_col = 0

        for i, (icon, title, desc) in enumerate(workflow_steps):
            col_index = start_col + i if total_steps <= max_cols else i
            if col_index < max_cols:
                with cols[col_index]:
                    step_placeholder = st.empty()
                    step_indicators.append(step_placeholder)
                    step_placeholder.markdown(
                        f"""
                    <div style="
                        text-align: center;
                        padding: 12px 8px;
                        border-radius: 12px;
                        background: rgba(255,255,255,0.05);
                        margin: 5px 2px;
                        border: 2px solid transparent;
                        min-height: 90px;
                        display: flex;
                        flex-direction: column;
                        justify-content: center;
                        align-items: center;
                        box-sizing: border-box;
                    ">
                        <div style="font-size: 1.5rem; margin-bottom: 4px;">{icon}</div>
                        <div style="font-size: 0.75rem; font-weight: 600; line-height: 1.2; margin-bottom: 2px;">{title}</div>
                        <div style="font-size: 0.6rem; color: #888; line-height: 1.1; text-align: center;">{desc}</div>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

        # Create main progress bar
        st.markdown("#### Overall Progress")
        progress_bar = st.progress(0)

        # Status text display
        status_text = st.empty()

        # Display mode information
        if not enable_indexing:
            st.info(
                "⚡ Fast Mode: Reference analysis, GitHub repository download and codebase indexing are disabled for faster processing."
            )

    return progress_bar, status_text, step_indicators, workflow_steps


def update_step_indicator(
    step_indicators, workflow_steps, current_step: int, status: str = "active"
):
    """
    Update step indicator

    Args:
        step_indicators: Step indicator list
        workflow_steps: Workflow steps definition
        current_step: Current step index
        status: Status ("active", "completed", "error")
    """
    status_colors = {
        "pending": ("rgba(255,255,255,0.05)", "transparent", "#888"),
        "active": ("rgba(255,215,0,0.2)", "#ffd700", "#fff"),
        "completed": ("rgba(0,255,136,0.2)", "#00ff88", "#fff"),
        "error": ("rgba(255,99,99,0.2)", "#ff6363", "#fff"),
    }

    for i, (icon, title, desc) in enumerate(workflow_steps):
        if i < current_step:
            bg_color, border_color, text_color = status_colors["completed"]
            display_icon = "✅"
        elif i == current_step:
            bg_color, border_color, text_color = status_colors[status]
            display_icon = icon
        else:
            bg_color, border_color, text_color = status_colors["pending"]
            display_icon = icon

        step_indicators[i].markdown(
            f"""
        <div style="
            text-align: center;
            padding: 12px 8px;
            border-radius: 12px;
            background: {bg_color};
            margin: 5px 2px;
            border: 2px solid {border_color};
            color: {text_color};
            transition: all 0.3s ease;
            box-shadow: {f'0 0 15px {border_color}30' if i == current_step else 'none'};
            min-height: 90px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-sizing: border-box;
        ">
            <div style="font-size: 1.5rem; margin-bottom: 4px;">{display_icon}</div>
            <div style="font-size: 0.75rem; font-weight: 600; line-height: 1.2; margin-bottom: 2px;">{title}</div>
            <div style="font-size: 0.6rem; opacity: 0.8; line-height: 1.1; text-align: center;">{desc}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )


def footer_component():
    """Footer component"""
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>🧬 <strong>DeepCode</strong> | Open-Source Code Agent | Data Intelligence Lab @ HKU |
        <a href="https://github.com/your-repo" target="_blank" style="color: var(--neon-blue);">GitHub</a></p>
        <p>⚡ Revolutionizing Research Reproducibility • Multi-Agent Architecture • Automated Code Generation</p>
        <p><small>💡 Join our growing community in building the future of automated research reproducibility</small></p>
    </div>
    """,
        unsafe_allow_html=True,
    )


def format_file_size(size_bytes: int) -> str:
    """
    Format file size

    Args:
        size_bytes: Size in bytes

    Returns:
        Formatted file size
    """
    if size_bytes == 0:
        return "0B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f}{size_names[i]}"
