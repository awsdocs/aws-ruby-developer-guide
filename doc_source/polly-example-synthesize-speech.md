# Synthesizing Speech<a name="polly-example-synthesize-speech"></a>

This example uses the [synthesize\_speech](https://docs.aws.amazon.com/sdkforruby/api/Aws/Polly/Client.html#synthesize_speech-instance_method) method to get the text from a file and produce an MP3 file containing the synthesized speech\.

Choose `Copy` to save the code locally\.

Create the file *polly\_synthesize\_speech\.rb*\.

Add the required gem\.

**Note**  
Version 2 of the AWS SDK for Ruby didn’t have service\-specific gems\.

```
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

require 'aws-sdk-polly'  # In v2: require 'aws-sdk'

begin
  # Get the filename from the command line
  if ARGV.empty?()
    puts 'You must supply a filename'
    exit 1
  end

  filename = ARGV[0]

  # Open file and get the contents as a string
  if File.exist?(filename)
    contents = IO.read(filename)
  else
    puts 'No such file: ' + filename
    exit 1
  end

  # Create an Amazon Polly client using
  # credentials from the shared credentials file ~/.aws/credentials
  # and the configuration (region) from the shared configuration file ~/.aws/config
  polly = Aws::Polly::Client.new

  resp = polly.synthesize_speech({
    output_format: "mp3",
    text: contents,
    voice_id: "Joanna",
  })

  # Save output
  # Get just the file name
  #  abc/xyz.txt -> xyx.txt
  name = File.basename(filename)

  # Split up name so we get just the xyz part
  parts = name.split('.')
  first_part = parts[0]
  mp3_file = first_part + '.mp3'

  IO.copy_stream(resp.audio_stream, mp3_file)

  puts 'Wrote MP3 content to: ' + mp3_file
rescue StandardError => ex
  puts 'Got error:'
  puts 'Error message:'
  puts ex.message
end
```

**Note**  
The resulting MP3 file is in the MPEG\-2 format\.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/polly/polly_synthesize_speech.rb) on GitHub\.