#!/usr/bin/env ruby
File.write('pylint.txt', Dir.glob('**/*.py').map { |f| `pylint #{f}` }.join("\n"))