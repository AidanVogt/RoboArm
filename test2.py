import webview

window = webview.create_window('Woah dude!', 'roboSite/index.html')
webview.start(http_server=True, debug=True)
