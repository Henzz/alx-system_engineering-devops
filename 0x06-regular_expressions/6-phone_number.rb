#!/usr/bin/env ruby
# puts ARGV[0].scan(/\d[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]{10}/).join
puts ARGV[0].scan(/^\d{10}/).join
