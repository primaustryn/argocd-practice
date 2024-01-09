from flask import Flask
from flask import request
import inferencer as inf

app = Flask(__name__)

inferencer = inf.Inferencer()
#inferencer.set_option()
index_html=''
with open('index.html','r', encoding='utf-8') as f:
    index_html = f.read()

@app.route('/')
def hello_world():
    return index_html

@app.route('/inference', methods=['POST'])
def inference_uploaded_file():
    f = request.files['img']    
    return {"result": inferencer.run_inference(f)}

@app.route('/inference_queue', methods=['POST'])
def inference_uploaded_file_queue():
    f = request.files['img']
    {"status":"error", "message": e.message() }
    return {"result": inferencer.run_inference_queue(f)}


@app.route('/inference?params=multi & threading=multi', methods=['POST'])
def inference_uploaded_multi_files_serial():
    f = request.files.getlist('img')
    # print(f)
    return {"result": inferencer.run_inference_multiple_serial(f)}

@app.route('/inference_multi_s_t', methods=['POST'])
def inference_uploaded_multi_files_serial_threading():
    f = request.files.getlist('img')
    return {"result": inferencer.run_inference_multiple_threading_wo_option(f)}


@app.route('/inference_multi_p', methods=['POST'])
def inference_uploaded_multi_files_parallel():
    f = request.files.getlist('img')
    # print(f)
    return {"result": inferencer.run_inference_multiple_parallel(f)}

@app.route('/inference_multi_p_t', methods=['POST'])
def inference_uploaded_multi_files_parallel_threading():
    f = request.files.getlist('img')
    # print(f)
    return {"result": inferencer.run_inference_multiple_threading_w_option(f)}

if __name__ == '__main__':
    app.run(debug=False, port=8000, host="0.0.0.0")