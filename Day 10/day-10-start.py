# Functions with Outputs

#### ma version de noob ###

# def format_name(first_name, last_name):
# 	first_name_f = first_name[0].upper()
# 	last_name_f = last_name[0].upper()
# 	for i in range(len(first_name)):
# 		if i > 0:
# 			first_name_f += first_name[i].lower()
#
# 	for i in range(len(last_name)):
# 		if i > 0:
# 			last_name_f += last_name[i].lower()
#
# 	print(first_name_f, last_name_f)


### la version simplifiée ###

def format_name(first_name, last_name):
	f_name = first_name.title()
	l_name = last_name.title()

	return f"{f_name} {l_name}"


print(format_name("foued", "gasmi"))
