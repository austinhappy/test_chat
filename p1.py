# 練習題1
import os

#讀取檔案
name_A = "Allen"
name_B = "Tom"
def read_file(input_file):
	chat = []
	name = 'K'
	with open(input_file, 'r', encoding ='utf-8') as f:
		for line in f:
			if  name_A in line.strip() or name_B in line.strip():
				name = line.strip()
				continue
			else:
				chat.append([name, line.strip()])
	return chat

#印出檔案
def print_chat(chat):
	for c in chat:
		print(c[0], "：", c[1])

#寫入檔案

def write_file(output_file, chat):
	with open(output_file, 'w', encoding='utf-8') as f:
		f.write('name, chat_index\n')
		for c in chat:
			f.write(c[0] + ',' + str(c[1]) + '\n')

def main():
	input_file = "input.txt"
	output_file = 'output1.txt'
	if os.path.isfile(input_file):
		print('檔案存在')
		chat = read_file(input_file)
		print_chat(chat)
		write_file(output_file, chat)
	else:
		print('找不到檔案')

main()