from myspider.echo import Echo

echo_screen = Echo('screen')
echo_file = Echo('file')
echo_xls = Echo('xls')
text = 'Hello World'

def test_screen(text):
    echo_screen.echo(text)

def test_file(text):
    echo_file.echo_to_file(text)

test_screen(text)
test_file(text)
