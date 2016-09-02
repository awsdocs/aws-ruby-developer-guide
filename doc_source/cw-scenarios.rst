.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cloudwatch-scenarios:

##############
|CW| Scenarios
##############

This section provides solutions to some common |CW| scenarios using the |sdk-ruby|. For more
information about |CW|, see the `CW-gsg`_.

.. _aws-ruby-sdk-cloudwatch-scenario-create-alarm:

Creating a |CW| Alarm
=====================

In this scenario we create a |CW| alarm, possibly including the following methods:

* delete_alarms

* describe_alarm_history

* describe_alarms

* describe_alarms_for_metrics

* disable_alarm_actions

* enable_alarm_actions

* set_alarm_state


.. _aws-ruby-sdk-cloudwatch-scenario-publich-custom-metrics:

Publishing Custom |CW| Metrics
==============================

In this scenario we publich custom metrics, possibly including the following methods:

* put_metric_data

* put_metric_alarm


.. _aws-ruby-sdk-cloudwatch-scenario-use-alarm-actions:

Using |CW| Alarm Actions
========================

In this scenario we use alarm actions, possibly including the following methods:

* disable_alarm_actions

* enable_alarm_actions


.. _aws-ruby-sdk-cloudwatch-scenario-send-events:

Sending Events to |CW| Events
=============================

In this scenario we send events to |CW| events, possibly including the following methods:

* put_events

* test_event_pattern

* enable_rule

* disable_rule

* delete_rule

* put_rule

* put_targets

* remove_targets


.. _aws-ruby-sdk-cloudwatch-scenario-get-metrics:

Getting |CW| Metrics
====================

In this scenario we get |CW| metrics, possibly including the following methods:

* list_metrics

* describe_alarmsFor_metric

* get_metricStatistics



