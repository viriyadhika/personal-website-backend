

def trim_html():
  output = open('out.html', 'w')

  with open('in.html') as f:
      for line in f:
          if (line.strip() == ''):
              print('hello')
          else:
              output.write(line)

  f.close()

if __name__ == '__main__':
  print('Hello world')