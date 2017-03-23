from facepp import API, File
import pickle
class FaceDectect:
    def __init__(self,id='test',API_KEY = 'w1s9SPlbJkhetEnq-BD8puseCT2LDTyj',API_SECRET = 'a8uEA_hK6lzuRHAY-LiqhlNcoDmS3I7A'):
        self.api = API(API_KEY, API_SECRET)
        self.Face = {}
        self.id = id
        self.search_result = {}
    def changeFaceset(self,id):
        try:
            ret = self.api.faceset.create(outer_id=id)
        except Exception as e:
            print "id already exists"
        self.id = id
    def delete_Faceset(self,id):
        self.api.faceset.delete(outer_id=id, check_empty=0)
    def addFaceToSet(self,image_file,info):
        res = self.api.detect(image_file=File(image_file))
        self.Face['%s'%info] = res["faces"][0]["face_token"]
        print "add to Face sucess"
    def addFaceToInternet(self):
        print [i for i in self.Face.itervalues()]
        self.api.faceset.addface(outer_id=self.id,face_tokens=self.Face.itervalues())
        print "add to internet face sucess"
    def getFaceInfo(self,input_file):
        ret = self.api.detect(image_file=File(input_file))
        self.search_result = self.api.search(face_token=ret["faces"][0]["face_token"], outer_id=self.id)
        for k, v in self.Face.iteritems():
            if v == self.search_result['results'][0]['face_token']:
                print 'The person with highest confidence:', k
                return k
                break
    def save_Face(self,face_file="default_face.txt"):
        face_file = open(face_file,'wb')
        pickle.dump(self.Face,face_file)
        face_file.close()
    def load_Face(self,face_file="default_face.txt"):
        face_file = open(face_file,'rb')
        self.Face = pickle.load(face_file)
        face_file.close()
    def print_result(hit, result):
        def encode(obj):
            if type(obj) is unicode:
                return obj.encode('utf-8')
            if type(obj) is dict:
                return {encode(v): encode(k) for (v, k) in obj.iteritems()}
            if type(obj) is list:
                return [encode(i) for i in obj]
            return obj
        print hit
        result = encode(result)
        print '\n'.join("  " + i for i in pformat(result, width=75).split('\n'))


