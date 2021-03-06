GPU_ID = 1
BATCH_SIZE = 24
VAL_BATCH_SIZE = 24
NUM_OUTPUT_UNITS = 3000 # This is the answer vocabulary size
MAX_WORDS_IN_QUESTION = 15
MAX_ITERATIONS = 1000000
PRINT_INTERVAL = 2000
SAVE_INTERVAL = 2000
SAVE_PATH=  "../trainval_model_save/" #to save checkpoints
VALIDATE_INTERVAL = 100000000

# what data to use for training
TRAIN_DATA_SPLITS = 'train'

# what data to use for the vocabulary
QUESTION_VOCAB_SPACE = 'train'
ANSWER_VOCAB_SPACE = 'train'

# vqa tools - get from https://github.com/VT-vision-lab/VQA
VQA_TOOLS_PATH = '../../VQA/PythonHelperTools/'
VQA_EVAL_TOOLS_PATH = '../../VQA/PythonEvaluationTools/'

# location of the data
VQA_PREFIX = '../../../data/'
#GENOME_PREFIX = '/y/daylen/vqa/02_tools/genome/'
DATA_PREFIX = '../../../data3/vqa_test_res5c/resnet_res5c_bgrms_large/'

DATA_PATHS = {
	'train': {
		'ques_file': VQA_PREFIX + 'train_subset_orig_3Q.json',
		'ans_file': VQA_PREFIX + 'annotation_1_extra_human_Q.json',
		'features_prefix': DATA_PREFIX + 'train2014/COCO_train2014_'
	},
#	'val': {
#		'ques_file': VQA_PREFIX + 'v2_OpenEnded_mscoco_val2014_questions.json',
#		'ans_file': VQA_PREFIX + 'v2_mscoco_val2014_annotations.json',
#		'features_prefix': DATA_PREFIX + 'val2014/COCO_val2014_'
#	},
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
