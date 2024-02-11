from flask import Flask #Flask 앱 생성용
from flask import render_template##템플릿 파일(.html) 서비스용
from flask_cors import CORS#CORS에러 해결


#app=Flask(__name__,template_folder='webapp')#템플릿 파일의  기본 폴더 위치명 변경시
app=Flask(__name__)
CORS(app)

@app.route('/frontend')
def frontend():
    return render_template('frontend.html')
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8282)