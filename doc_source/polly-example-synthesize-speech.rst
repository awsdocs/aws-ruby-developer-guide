.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _polly-example-synthesize-speech:

###################
Synthesizing Speech
###################

.. meta::
    :description:
        Synthesizing speech using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon Polly

This example uses the
:ruby-sdk-api:`synthesize_speech <Aws/Polly/Client.html#synthesize_speech-instance_method>`
method to get the text from a file and produce an MP3 file containing the synthesized speech.

Choose :code:`Copy` to save the code locally.

Create the file *polly_synthesize_speech.rb*.

Add the required gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/polly/polly_synthesize_speech.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Get the name of the text file from the command line.

.. literalinclude:: ./example_code/polly/polly_synthesize_speech.rb
   :lines: 17-22
   :dedent: 2
   :language: ruby

Open the text file and read the contents as a string.

.. literalinclude:: ./example_code/polly/polly_synthesize_speech.rb
   :lines: 26
   :dedent: 4
   :language: ruby

Create an Amazon Polly client and call :code:`synthesize_speech`.

.. literalinclude:: ./example_code/polly/polly_synthesize_speech.rb
   :lines: 35, 37-41
   :dedent: 2
   :language: ruby

Save the resulting synthesized speech as an MP3 file.

.. literalinclude:: ./example_code/polly/polly_synthesize_speech.rb
   :lines: 46, 49-53
   :dedent: 2
   :language: ruby

.. note:: The resulting MP3 file is in the MPEG-2 format.

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/polly/polly_synthesize_speech.rb>`_
on GitHub.
