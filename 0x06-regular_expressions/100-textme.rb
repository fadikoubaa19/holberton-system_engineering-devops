#!/usr/bin/env ruby
//TASK 100
puts ARGV[0].scan(/\[(?:from|to|flags):(.*?)\]/).join(',')
