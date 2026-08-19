from setuptools import setup, find_packages

setup(
    name="smartgrid-secure-kernel",
    version="0.1.0",
    description="Consolidated Smart Grid & Secure Kernel System Architecture",
    author="jasonbasham006-blip",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
        "cryptography>=41.0.0",
        "lxml>=4.9.0",
        "pytest>=7.4.0",
    ],
    entry_points={
        "console_scripts": [
            "verify-kernel=smartgrid_system.core.deterministic:verify_sovereign_kernel_core",
        ],
    },
)
