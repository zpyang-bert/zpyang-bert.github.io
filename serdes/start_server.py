#!/usr/bin/env python3
"""
SerDes 224G 知识库 - 本地 HTTP 服务器启动脚本
用法: python3 start_server.py [port]
"""
import sys
import os
import http.server
import socketserver

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
ROOT = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

os.chdir(ROOT)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 SerDes 224G 知识库服务器已启动")
    print(f"📂 根目录: {ROOT}")
    print(f"🌐 访问地址: http://localhost:{PORT}/")
    print(f"📖 知识图谱: http://localhost:{PORT}/serdes/deep_research/SerDes_224G_知识图谱.html")
    print(f"\n按 Ctrl+C 停止")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✋ 服务器已停止")
