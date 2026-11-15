from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, World!</h1><p>我的第一个 Termux 网站</p>"

if __name__ == "__main__":
    # host="0.0.0.0" 允许局域网内其他设备访问
    # debug=True 开启调试模式，修改代码后自动重载
    app.run(host="0.0.0.0", port=5000, debug=True)
