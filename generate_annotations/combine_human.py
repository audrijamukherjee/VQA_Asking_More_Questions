import json
from collections import OrderedDict
answers = json.load(open('./1_extra_human_Q_answers.json', 'r'))
annotations = json.load(open('./v2_mscoco_train2014_annotations.json','r'))

print(len(annotations['annotations']))
anno_results = [];
index=0
for anno in annotations['annotations']:
    found = False
    index = index+1
    print(index)
    temp = {}
    ans_list = [];
    for a in answers:
        if anno['question_id'] == a['question_id']:
            found = True
            for i in range(10):
                ans_entry = OrderedDict([('answer', a['answer']),('answer_confidence', 'yes'), ('answer_id', i+1)])
                ans_list.append(ans_entry.copy())
            temp = OrderedDict([("question_type", anno['question_type']), ("multiple_choice_answer", a['answer']), ("answers", ans_list),("image_id", anno['image_id']), ("answer_type", anno['answer_type']),("question_id", anno['question_id'])])
            anno_results.append(temp)
    if found == False:
        temp = OrderedDict([("question_type", anno['question_type']), ("multiple_choice_answer", a['answer']), ("answers", anno['answers']),("image_id", anno['image_id']), ("answer_type", anno['answer_type']),("question_id", anno['question_id'])])
        anno_results.append(temp)
annotations['annotations'] = anno_results; 

train = {"info": annotations['info'], "data_type": annotations['data_type'], "data_subtype": annotations['data_subtype'], "annotations":annotations['annotations'], "license": annotations['license']}
json.dump(train,open('combined_human_annotations.json','w'))
