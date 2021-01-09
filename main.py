import strings

def eng_extractor(d, add_russian_and_azerbaijani):
	if add_russian_and_azerbaijani == True: 
		aze = open('./aze.txt', 'r', encoding='utf-8')
		eng_rus_aze = open('./eng_rus_aze.txt', 'w', encoding='utf-8')
		aze_list = aze.read().split('\n')
		i = 0
		for key in d:
			eng_rus_aze.write(d[key]['en_US']+'\n')
			eng_rus_aze.write(d[key]['ru_RU']+'\n')
			eng_rus_aze.write(aze_list[i]+'\n\n')
			i+=1
		aze.close()
		eng_rus_aze.close()

	else:
		eng = open('eng.txt', 'w', encoding='utf-8')
		for key in d:
			eng.write(d[key]['en_US']+'\n')
		eng.close()


d = strings.emit_strings()
eng_extractor(d, True)