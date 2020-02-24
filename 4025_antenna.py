import random
from est import antenna as source
from est import fcarc as source2

print('Generating...')
file_name = 'antenna'

import os
print(__file__)
print(os.path.realpath(__file__))
print(os.path.dirname(os.path.realpath(__file__)))
folderpath = os.path.dirname(os.path.realpath(__file__))

def write_to_file(some_object):   
	if FILEMODE: 
		file.write(some_object.question)
		file.write('\n')
		file.write(some_object.answer)
		file.write('\n\n')

def print_tasks(some_object):
	print(some_object.question)
	print()
	print(some_object.answer)
	print()
	print()

FILEMODE = True
TESTMODE = False


question_list = [source.jma_17_1(),
source.jma_17_2(),
source.jma_17_3(),
source.jma_17_4(),
source.jma_17_5(),
source.jma_17_6(),
source.jma_17_7(),
source.jma_17_8(),
source.jma_17_9(),
source.jma_17_10(),
]


concept_list = [
source2.f_1_480(),
source2.f_1_481(),
source2.f_1_482(),
source2.f_1_483(),
source2.f_1_484(),
source2.f_1_485(),
source2.f_1_486(),
source2.f_1_487(),
source2.f_1_488(),
source2.f_1_489(),
source2.f_1_490(),
source2.f_1_491(),
source2.f_1_492(),
source2.f_1_493(),
source2.f_1_494(),
source2.f_1_495(),
source2.f_1_496(),
source2.f_1_497(),
source2.f_1_498(),
source2.f_1_499(),
source2.f_1_500(),
source2.f_1_501(),
source2.f_1_502(),
source2.f_1_503(),
source2.f_1_504(),
source2.f_1_505(),
source2.f_1_506(),
source2.f_1_507(),
source2.f_1_508(),
source2.f_1_509(),
source2.f_1_510(),
source2.f_1_511(),
source2.f_1_512(),
source2.f_1_513(),
source2.f_1_514(),
source2.f_1_515(),
source2.f_1_516(),
source2.f_1_517(),
source2.f_1_518(),
source2.f_1_519(),
source2.f_1_520(),
source2.f_1_521(),
source2.f_1_522(),
source2.f_1_523(),
source2.f_1_524(),
source2.f_1_525(),
source2.f_1_526(),
source2.f_1_527(),
source2.f_1_528(),
source2.f_1_529(),
source2.f_1_530(),
source2.f_1_531(),
source2.f_1_532(),
source2.f_1_533(),
source2.f_1_534(),
source2.f_1_535(),
source2.f_1_536(),
source2.f_1_537(),
source2.f_1_538(),
source2.f_1_539(),
source2.f_2_351(),
source2.f_2_352(),
source2.f_2_353(),
source2.f_2_354(),
source2.f_2_372(),
source2.f_2_373(),
source2.f_2_706(),
source2.f_2_707(),
source2.f_2_709(),
source2.f_2_718(),
source2.f_2_719(),
source2.f_2_759(),
source2.f_2_760(),
source2.f_2_761(),
source2.f_2_762(),
source2.f_2_763(),
source2.f_2_764(),
source2.f_2_765(),
source2.f_2_766(),
source2.f_2_767(),
source2.f_2_768(),
source2.f_2_769(),
source2.f_2_772(),
source2.f_2_773(),
source2.f_2_775(),
source2.f_2_776(),
source2.f_2_777(),
source2.f_2_779(),
source2.f_2_780(),
source2.f_2_781(),
source2.f_2_782(),
source2.f_2_783(),
source2.f_2_784(),
source2.f_2_785(),
source2.f_2_786(),
source2.f_2_787(),
source2.f_2_788(),
source2.f_2_789(),
source2.f_2_790(),
source2.f_2_791(),
source2.f_2_792(),
source2.f_2_793(),
source2.f_2_794(),
source2.f_2_795(),
source2.f_2_796(),
source2.f_2_798(),
source2.f_2_799(),
source2.f_2_800(),
source2.f_2_801(),
source2.f_2_802(),
source2.f_2_803(),
source2.f_2_804(),
source2.f_2_805(),
source2.f_2_806(),
source2.f_2_807(),
source2.f_2_808(),
source2.f_2_809(),
source2.f_2_810(),
source2.f_2_811(),
source2.f_2_812(),
source2.f_2_813(),
source2.f_2_814(),
source2.f_2_815(),
source2.f_2_816(),
source2.f_2_817(),
source2.f_2_818(),
source2.f_2_819(),
source2.f_2_820(),
source2.f_2_821(),
source2.f_2_822(),
source2.f_2_823(),
source2.f_2_824(),
source2.f_2_825(),
source2.f_2_826(),
source2.f_2_827(),
source2.f_2_828(),
source2.f_2_829(),
source2.f_2_830(),
source2.f_2_831(),

]

if len(concept_list) == 0:
	CONCEPTS = False
else:
	CONCEPTS = True

if not TESTMODE:
	random.shuffle(question_list)
	random.shuffle(concept_list)

file = open(f"{folderpath}/outputs/{file_name}_output_{str(random.randint(1000, 9999))}.txt", 'w+')

if CONCEPTS:
	for i in range (min(len(question_list), len(concept_list))):
		print('-----------------------------------------------------------------------')
		item = random.choice([question_list[i], concept_list[i]])
		print_tasks(item)
		write_to_file(item)
else:
	for i in range (len(question_list)):
		print('-----------------------------------------------------------------------')
		item = question_list[i]
		print_tasks(item)
		write_to_file(item)

print()
file.close()
print('Finished.')
