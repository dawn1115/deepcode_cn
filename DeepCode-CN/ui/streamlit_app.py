"""
DeepCode - AI 研究引擎

Streamlit Web 界面主应用程序文件
"""

import os
import sys

# Disable .pyc file generation
os.environ["PYTHONDONTWRITEBYTECODE"] = "1"

# Add parent directory to path for module imports
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Import UI modules
from ui.layout import main_layout


def main():
    """
    主函数 - Streamlit 应用程序入口

    所有UI逻辑已模块化到ui/文件夹中
    """
    # Run main layout
    sidebar_info = main_layout()

    # Additional global logic can be added here if needed

    return sidebar_info


if __name__ == "__main__":
    main()
