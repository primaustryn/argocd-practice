from flask import Flask
from flask import request
import inferencer as inf
import json

app = Flask(__name__)

inferencer = inf.Inferencer()
#inferencer.set_option()

@app.route('/')
def hello_world():
    return '''
<html>
<script>
const input = document.getElementById('input_img')
const output = document.getElementById('output')

document.getElementById('input_img').addEventListener('input', (event) => {
  const files = event.target.files
  output.textContent = Array.from(files).map(file => file.name).join('\n')
})
</script>
<body>
<center>
<h1>Demo on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="https://github.com/tanmaybhandge/CICD_Application_K8s/blob/main/itsworking.jpeg?raw=true">
<label for="mnist-image">값을 추론할 숫자 이미지를 업로드해주세요:
  <input type="file"
         id="input_img"
         accept="image/png, image/jpeg">
</label><br/>
<label id="output"></label>
</center>
</body>
</html>
'''

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