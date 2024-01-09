import numpy as np
import cv2
import os
import onnxruntime as ort
import numpy as np
import threading
from multiprocessing.dummy import Pool as ThreadPool


class Inferencer:
    session = None
    option = None
    flag_parallel = False
    
    def __init__(self):
        self.session = ort.InferenceSession('mnist-7.onnx')        

    def run(self, input_tensor):
        return self.session.run(None, {'Input3': input_tensor})

    def run_parallel(self, input_tensors):
        return self.session.run(["output3"], input_tensors)


    def get_session(self):
        return self.session

    def set_session(self, option):
        self.session = ort.InferenceSession('mnist-7.onnx', sess_options=option)

    def get_option(self):
        return self.option

    def set_option(self, option):
        self.option = option
        ort.InferenceSession('mnist-7.onnx', sess_options=option)

    @classmethod
    def _option_parallel(cls):
        sess_options = ort.SessionOptions()
        sess_options.inter_op_num_threads = 3
        sess_options.intra_op_num_threads = 1
        sess_options.execution_mode = ort.ExecutionMode.ORT_PARALLEL
        sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
        return sess_options

    def preprocess(self, file):
        # read file
        npimg = np.fromstring(file.read(), np.uint8)
        image = cv2.imdecode(npimg,1)

        # convert, resize
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.resize(gray, (28,28)).astype(np.float32)/255
        
        # reshape
        ipt = np.reshape(gray, (1,1,28,28))
        return ipt

    def postprocess(self, output):
        result = output[0].argmax(axis=1)
        return int(result[0])

    def run_inference(self, file):
        # preprocess
        ipt = self.preprocess(file)

        # run. ort session
        output = self.run(ipt)
        
        # Print Result
        result = self.postprocess(output)

        return result

    def run_inference_queue(self, file):
        # preprocess
        ipt = self.preprocess(file)

        # run. ort session
        output = self.run(ipt)
        
        # Print Result
        result = self.postprocess(output)

        return result


    def run_inference_multiple_serial(self, files):
        if(self.flag_parallel is True):
            self.set_option(None)
            self.flag_parallel = False
        result = []
        for file in files:
            tmp_rst = self.run_inference(file)
            result.append(tmp_rst)
        return result

    def run_inference_multiple_threading_wo_option(self, files):
        if(self.flag_parallel is True):
            self.set_option(None)
            self.flag_parallel = False
    
        result = []
    
        threads=[]

        pool = ThreadPool(4)
        result = pool.map(self.run_inference, files)
        pool.close()
        pool.join()        
        
        return result

    def run_inference_multiple_parallel(self, files):
        if(self.flag_parallel is False):
            self.set_option(Inferencer._option_parallel())
            self.flag_parallel = True
        
        queue = []            

        for file in files:
            queue.append(self.preprocess(file)) 

        # outputs = self.session.run(["output1", "output2"], {"Input3": queue[0], queue[1]})
        # print(outputs)

        outputs=[]
        for ipt in queue:
            output = self.run(ipt)
            result = self.postprocess(output)
            outputs.append(result)

        return outputs

    def run_inference_multiple_threading_w_option(self, files):
        if(self.flag_parallel is False):
            self.set_option(Inferencer._option_parallel())
            self.flag_parallel = True

        pool = self.pool                
        threads=[]
        result = pool.map(self.run_inference, files)
        pool.close()
        pool.join()
        
        return result

