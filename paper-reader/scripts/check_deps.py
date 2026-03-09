#!/usr/bin/env python3
"""
检查并安装必要的Python依赖
用法: python check_deps.py
"""

import subprocess
import sys

REQUIRED_PACKAGES = ["pdfplumber"]


def check_package(package_name):
    """检查包是否已安装"""
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False


def install_package(package_name):
    """使用uv安装包"""
    try:
        subprocess.run(
            ["uv", "pip", "install", package_name, "-q"],
            check=True,
            capture_output=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def main():
    missing_packages = []

    for package in REQUIRED_PACKAGES:
        if not check_package(package):
            missing_packages.append(package)

    if missing_packages:
        print(f"需要安装以下依赖: {', '.join(missing_packages)}")
        for package in missing_packages:
            print(f"正在安装 {package}...")
            if install_package(package):
                print(f"✓ {package} 安装成功")
            else:
                print(f"✗ {package} 安装失败", file=sys.stderr)
                sys.exit(1)
    else:
        print("所有依赖已安装")

    return 0


if __name__ == "__main__":
    sys.exit(main())
