.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

######################
aws-doc-shared-content
######################

This repository provides common content and links that are shared between the public `AWS
documentation repositories <https://www.github.com/awsdocs>`_.

To build any of these documentation sets, download one of these repositories and run the
``build_docs.py`` script that's provided in the repository. The script will automatically merge this
shared content into the build directory before building with Sphinx.

What's included in the shared content
=====================================

The shared content is organized into three major categories:

* `Shared roles and substitutions`_
* `Shared text blocks`_
* `Shared extlinks and intersphinx links`_


Shared roles and substitutions
------------------------------

Common text roles and substitution are provided in the following files:

common_includes.txt_
    Defines a number of roles and substitutions specific to AWS documentation, such as AWS service
    and SDK names, example values used for illustrative purposes, and roles used to style code and
    AWS-specific concepts.

    The substitutions follow a similar pattern:

    * AWS service names use the service's acronym. For example, ``|EC2|`` for Amazon
      EC2, ``|S3|`` for Amazon S3, ``|LAM|`` for AWS Lambda, and so on.

    * The *full* version of a service's name uses the service's acronym + 'long'. For example,
      ``|EC2long|`` renders as "Amazon Elastic Compute Cloud".

    * Service guide names use the service's acronym combined with the guide type. For example,
      ``|S3-dg|`` becomes "Amazon S3 Developer Guide", and ``|S3-api|`` becomes "Amazon S3 API
      Reference".

service_links.txt_
    Links to AWS service and SDK landing pages, the AWS console, and other frequently-referenced AWS
    URLs.

    These follow the same pattern as service names. To create a link to the EC2 landing page, use
    ``|EC2|_``. Similarly, ``|EC2long|_`` should provide the same link, but will use the service's
    full name instead.

guide_links.txt_
    Links to AWS documentation. In addition to using these as stand-alone links to the
    documentation, the contents of this file are used to generate extlinks for deep-linking into
    these guides, within default_extlinks.py_.

    Guide links follow the same pattern as for service guide names: Use ``|S3-dg|_`` to create a
    named link to the *Amazon S3 Developer Guide*.

region_includes.txt_
    Substitutions used when referring to AWS regions.

    For example, to refer to the *us-west-2* region, use ``|us-west-2-region|``, which will be
    replaced by "US West (Oregon)" in the text.


Shared text blocks
------------------

Located in the `common <sphinx_shared/common>`_ directory, these files provide common descriptions
and procedures used in the documentation. They're used like this::

   .. include:: common/sdk-shared-credentials.txt

Which inserts the contents of sdk-shared-credentials.txt within the topic.


.. _shared_links:

Shared extlinks and intersphinx links
-------------------------------------

In the `_conf <sphinx_shared/conf>`_ directory, the default_extlinks.py_ file defines a number of
extlinks for deep-linking into AWS documentation, linking to AWS forums, the AWS console and to the
regions and endpoints topic in the AWS General Reference. It also pulls content from
guide_links.txt_ to create extlinks for each guide listed in the file.

Using extlinks
~~~~~~~~~~~~~~

`Extlinks <sphinx-extlinks_>`_ follow the same pattern as substitutions, but you'll declare the page
name in the extlink's body. These do not automatically pick up the page name, so you'll need to name
the link yourself.

For example: ``:s3-dg:`Working with Amazon S3 Objects <UsingObjects>``` links to the `Working with
Amazon S3 Objects <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html>`_ topic in the
*Amazon S3 Developer Guide*.

You can do this with any of the AWS documentation defined in ``guide_links.txt``, along with any
further extlinks that are defined in ``default_extlinks.py``.

Using intersphinx
~~~~~~~~~~~~~~~~~

For any AWS documentation built using Sphinx (that is, open-source documentation hosted at
https://www.github.com/awsdocs/), You can use `intersphinx <sphinx-intersphinx_>`_ to deep-link
within the documentation using the standard Sphinx `:ref: <sphinx-inline-ref_>`_ and `:doc:
<sphinx-inline-doc_>`_ roles, providing the guide's intersphinx prefix as the first parameter of the
link, separated with a colon (``:``) character.

The list of documentation available (along with the prefixes used to link to them) is contained
within `default_extlinks.py`_.

For example, to link to a topic within the *AWS SDK for .NET Developer Guide* (Version 3), you can
use::

    :doc:`netdg3:tutorials-examples`

Which will create a link to the topic `Programming AWS Services with the AWS SDK for .NET
<http://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/tutorials-examples.html>`_.

You can use intersphinx to link to *internal references* within a topic, as well. This works with
any named section in the documentation. For example, to link to the section `Java Futures
<http://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/basics-async.html#java-futures>`_ in the
*AWS SDK for Java Developer Guide*, you'd write::

   :ref:`javadg:basics-async-future`

The section title is automatically retrieved by intersphinx and inserted into a text along with a
link to the section.

Copyright and license
=====================

All content in this repository, unless otherwise stated, is Copyright © 2010-2016, Amazon Web
Services, Inc. or its affiliates. All rights reserved.

Except where otherwise noted, this work is licensed under a `Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License
<http://creativecommons.org/licenses/by-nc-sa/4.0/>`_ (the "License"). Use the preceding link for a
human-readable summary of the license terms. The full license text is available at:
http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode and in the LICENSE file accompanying this
repository.

.. links used in the preceding text

.. _default_extlinks.py: sphinx_shared/_conf/default_extlinks.py
.. _common_includes.txt: sphinx_shared/_includes/common_includes.txt
.. _service_links.txt: sphinx_shared/_includes/service_links.txt
.. _guide_links.txt: sphinx_shared/_includes/guide_links.txt
.. _region_includes.txt: sphinx_shared/_includes/region_includes.txt

.. _sphinx-inline-ref: http://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-arbitrary-locations
.. _sphinx-inline-doc: http://www.sphinx-doc.org/en/stable/markup/inline.html#cross-referencing-documents
.. _sphinx-extlinks: http://www.sphinx-doc.org/en/stable/ext/extlinks.html
.. _sphinx-intersphinx: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

