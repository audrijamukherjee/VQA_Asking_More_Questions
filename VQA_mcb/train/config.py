GPU_ID = 0
BATCH_SIZE = 48
VAL_BATCH_SIZE = 48
NUM_OUTPUT_UNITS = 3000 # This is the answer vocabulary size
MAX_WORDS_IN_QUESTION = 15
MAX_ITERATIONS = 1000000
PRINT_INTERVAL = 100
VALIDATE_INTERVAL = 100000000

# what data to use for training
TRAIN_DATA_SPLITS = 'train+val'

# what data to use for the vocabulary
QUESTION_VOCAB_SPACE = 'train+val'
ANSWER_VOCAB_SPACE = 'train+val'

# vqa tools - get from https://github.com/VT-vision-lab/VQA
VQA_TOOLS_PATH = '../../VQA/PythonHelperTools'
VQA_EVAL_TOOLS_PATH = '../../VQA/PythonEvaluationTools'

# location of the data
VQA_PREFIX = '../../../../data/'
#GENOME_PREFIX = '/y/daylen/vqa/02_tools/genome/'
DATA_PREFIX = '/srv/share/data/mscoco/resnet_features/'

DATA_PATHS = {
	'train': {
		'ques_file': VQA_PREFIX + 'OpenEnded_mscoco_train2017_questions.json',
		'ans_file': VQA_PREFIX + 'mscoco_train2017_annotations.json',
		'features_prefix': DATA_PREFIX + 'train2014/COCO_train2014_'
	},
	'val': {
		'ques_file': VQA_PREFIX + 'OpenEnded_mscoco_val2017_questions.json',
		'ans_file': VQA_PREFIX + 'mscoco_val2017_annotations.json',
		'features_prefix': DATA_PREFIX + 'val2014/COCO_val2014_'
	},
#	'test-dev': {
#		'ques_file': VQA_PREFIX + '/Questions/OpenEnded_mscoco_test-dev2015_questions.json',
#		'features_prefix': VQA_PREFIX + '/Features/resnet_res5c_bgrms_large/test2015/COCO_test2015_'
#	},
#	'test': {
#		'ques_file': VQA_PREFIX + '/Questions/OpenEnded_mscoco_test2015_questions.json',
#		'features_prefix': VQA_PREFIX + '/Features/resnet_res5c_bgrms_large/test2015/COCO_test2015_'
#	},
#	# TODO it would be nice if genome also followed the same file format as vqa
#	'genome': {
#		'genome_file': GENOME_PREFIX + '/question_answers_prepro.json',
#		'features_prefix': DATA_PREFIX + '/genome/Features/resnet_res5c_bgrms_large/whole/'
#	}
}
