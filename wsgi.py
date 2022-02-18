from init_app import create_app

if __name__ == '__main__':
    create_app().run(debug=True, threaded=True, host="127.0.0.1", port=4000)
