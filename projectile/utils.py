def get_string_as_ul(separator, string):
    output = '<ul>\n'
    for v in string.split(separator):
        output += '\t<li>' + v.strip(' ') + '</li>\n'
    output += '</ul>'
    print output

get_string_as_ul(',', 'HTML, CSS, JavaScript, Python Ista')