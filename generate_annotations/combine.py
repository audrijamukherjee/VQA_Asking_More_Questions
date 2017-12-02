import json
from collections import OrderedDict
answers = json.load(open('./correct_answers_generated_train_questions.json', 'r'))
anno = json.load(open('./v2_mscoco_train2014_annotations.json','r'))
questions = json.load(open('generated_questions_train_all.json','r'))
def find_type(question, *types):
    found = False;
    while(found == False):
        if any(question in type for type in types):
            found = True
        else:
            question = question.rsplit(' ', 1)[0]
    return question

#question_type
with open('./question_types') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
num = 0
out = []
#for n in anno['annotations']:
#    temp_ann = OrderedDict([("question_type", n['question_type']), ("multiple_choice_answer", n['multiple_choice_answer']), ("answers", n['answers']),("image_id", int(n['image_id'])), ("answer_type", n['answer_type']),("question_id", int(n['question_id']))])
#    out.append(temp_ann.copy())
for a in answers:
    temp = {}
    ans_list = [];
    for i in range(10):
        ans_entry = OrderedDict([('answer', a['answer']),('answer_confidence', 'yes'), ('answer_id', i+1)])
        ans_list.append(ans_entry.copy())
    for q in questions['questions']:
        q_ques_id = int(q['question_id'][6:]);
        if a['question_id'] == q_ques_id:
            q_type = find_type(q['question'],content )
            temp = OrderedDict([("question_type", q_type), ("multiple_choice_answer", a['answer']), ("answers", ans_list),("image_id", int(q['image_id'])), ("answer_type", "other"),("question_id", int(q['question_id'][6:]))])
            #out.append(temp.copy())
            anno['annotations'].append(temp)
	    num = num+1
	    print(num) 
	    break       
train = {"info": anno['info'], "data_type": anno['data_type'], "data_subtype": anno['data_subtype'], "annotations":anno['annotations'], "license": anno['license']}

json.dump(train,open('v2_combined_train_annotations.json','w'))

