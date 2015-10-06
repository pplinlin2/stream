#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pypandoc
from jinja2 import Template

path = {
	'path_wlbc': '../wlbc', 
}

with open('tables.txt', 'r') as f:
	template = Template(f.read().decode('utf-8'))
	md = template.render(path).encode('utf-8')
	pypandoc.convert(md, to='html', format='md', outputfile='tables.html', extra_args=['-s'])
