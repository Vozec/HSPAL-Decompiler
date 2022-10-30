import argparse
from os.path import exists

def pseudo_code(code):
	pc = []
	for i in range(len(code)):
		pc.append(intepret(i,str(code[i])))
	return color("\n".join(pc))

def color(text):
	mapper = {
		'[':'\033[90m%s\033[0m'%('['),
		']':'\033[90m%s\033[0m'%(']'),
		'exit':'\033[91m%s\033[0m'%('exit'),
		'pop':'\033[94m%s\033[0m'%('pop'),
		'size':'\033[94m%s\033[0m'%('size'),
		'push':'\033[93m%s\033[0m'%('push'),
		'label':'\033[92m%s\033[0m'%('label'),
		'print':'\033[92m%s\033[0m'%('print'),
		'reg':'\033[95m%s\033[0m'%('reg'),
		'while':'\033[95m%s\033[0m'%('while'),
		'ret':'\033[96m%s\033[0m'%('ret'),
		')':'\033[90m%s\033[0m'%(')'),
		'(':'\033[90m%s\033[0m'%('('),		
		'stack':'\033[90m%s\033[0m'%('stack'),
		'input_char':'\033[92m%s\033[0m'%('input_char'),
		'input_int':'\033[92m%s\033[0m'%('input_int'),

	}
	for a,b in mapper.items():
		text = text.replace(a,b)
	return text

def intepret(i,ins):
	op_code = ins[:2]
	if(op_code == '00')  :return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'var label && id=%s'%(ins[2:]))
	elif(op_code == '01'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'goto label %s'%(ins[2:]))
	elif(op_code == '02'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'pop 0x%s && goto label (%s)'%(ins[2:4],ins[2:4]))
	elif(op_code == '03'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'pop 0x%s%s'%(ins[2:4],' && skip next' if ins[2:4] != '00' else ''))
	elif(op_code == '04'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'exit (statut_code = 0x%s)\n'%ins[2:])

	elif(op_code == '10'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push input_char stack[0x%s]'%ins[2:4])
	elif(op_code == '11'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push input_int  stack[0x%s]'%ins[2:4])
	elif(op_code == '12'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'print stack[0x%s] (int)last  && pop stack[0x%s]'%(ins[2:4],ins[2:4]))
	elif(op_code == '13'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'print stack[0x%s] (char)last && pop stack[0x%s]'%(ins[2:4],ins[2:4]))
	elif(op_code == '14'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'while(stack[0x%s]): pop(*) && print(*)'%(ins[2:4]))

	elif(op_code == '20'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'reg = 0x%s'%ins[2:6])
	elif(op_code == '21'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) min(last1+last2 ,65535)'%ins[2:4])
	elif(op_code == '22'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) min(last1-last2 ,65535)'%ins[2:4])
	elif(op_code == '23'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) min(last1*last2 ,65535)'%ins[2:4])
	elif(op_code == '24'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) min(last1/last2 ,65535)'%ins[2:4])
	elif(op_code == '25'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) min(last1**last2,65535)'%ins[2:4])
	elif(op_code == '26'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'reg = nextInt(1+%s)'%ins[2:6])

	elif(op_code == '30'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret (stack[0x%s]) last == (stack[0x%s]) last'%(ins[2:4],ins[4:6]))
	elif(op_code == '31'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret (stack[0x%s]) last >  (stack[0x%s]) last'%(ins[2:4],ins[4:6]))
	elif(op_code == '32'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret (stack[0x%s]) last <  (stack[0x%s]) last'%(ins[2:4],ins[4:6]))
	elif(op_code == '33'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret (stack[0x%s]) last +  (stack[0x%s]) last != 0'%(ins[2:4],ins[4:6]))
	elif(op_code == '34'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret (stack[0x%s]) last *  (stack[0x%s]) last != 0'%(ins[2:4],ins[4:6]))
	elif(op_code == '35'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret ((stack[0x%s]) last * (stack[0x%s]) last != 0) && ((stack[0x%s]) last + (stack[0x%s]) last != 0)'%(ins[2:4],ins[4:6],ins[2:4],ins[4:6]))
	elif(op_code == '36'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'ret reg == 0')

	elif(op_code == '40'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'push (stack[0x%s]) reg '%(ins[2:4]))
	elif(op_code == '41'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'reg = stack[0x%s] last && stack[0x%s] pop()'%(ins[2:4],ins[2:4]))
	elif(op_code == '42'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'reg = stack[0x%s] last '%(ins[2:4]))
	elif(op_code == '43'):return '| (%s) | %s | %s'%(str(i).zfill(3),ins,'reg = stack[0x%s] size '%(ins[2:4],ins[2:4]))

	return 'None'

def parse_args():
	parser = argparse.ArgumentParser(add_help=True, description='This tool allows you to generate pseudo-code for the language esolang HSPAL')
	parser.add_argument("-f","--file",dest="file",type=str,required=True, help="file (.hspal)")
	return parser.parse_args()


def main(args):
	if not exists(args.file):
		return 'File not found !'
	code = open(args.file,'r').read().split()
	return pseudo_code(code)

if __name__ == '__main__':
	print(main(parse_args()))