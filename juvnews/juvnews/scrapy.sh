#!/bin/bash

scrapy crawl $1 -o $1'.json'
