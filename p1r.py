# 練習題1比較 #老師版本

#讀取檔案
def read_file(input_file):
	lines = []
	with open(input_file, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#轉換檔案
def convert(lines):
	new = []
	person = None #其他語言是null
	for line in lines:
		if line == "Allen" or line == "Tom":
			person = line
			continue
		if person: #看person是否有值才會做
			new.append(person + ": " + line)
	return new

#寫入檔案
def write_file(file_name, lines):
	with open(file_name, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')

#主函式
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output2.txt', lines)

main()