#!/bin/sh

# model conf
buxtonctl --direct create-group ro-base model_conf
buxtonctl --direct set-label ro-base model_conf deviced

# model name
buxtonctl --direct set-string ro-base model_conf model_name "b2"
buxtonctl --direct set-label ro-base model_conf model_name deviced

