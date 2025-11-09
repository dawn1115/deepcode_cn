"""
DeepCode UI 应用程序入口点

此文件作为UI模块的统一入口点
"""

from .streamlit_app import main

# Directly export main function for external calls
__all__ = ["main"]

if __name__ == "__main__":
    main()
