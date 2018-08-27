#!/usr/bin/env python3
# coding=utf_8
# title          : myconf.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/6/29 13:14
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script


conf_tmp = """
[mysql]
auto-rehash = 0
user = root
port = 3306
prompt = "[\\u@\\h [\\d]]"
socket = /tmp/mysql3306.sock
#pager = "less -i -n -S"
#tee = /opt/mysql/query.log

[mysqld]
####: for global
user = mysql 			#mysql
basedir = /usr/local/mysql/ 			#/usr/local/mysql/
datadir = /data/mysql3306/data 			#/usr/local/mysql/data
server_id = 1003306 			#0
port = 3306 			#3306
character_set_server = utf8 			#latin1
explicit_defaults_for_timestamp = off 			#off
log_timestamps = system 			#utc
socket = /tmp/mysql3306.sock 			#/tmp/mysql3306.sock
read_only = 0 			#off
#skip_name_resolve = 1 			#0
auto_increment_increment = 1 			#1
auto_increment_offset = 1 			#1
lower_case_table_names = 1 			#0
#secure_file_priv =  			#null
open_files_limit = 65536 			#1024
max_connections = 1000 			#151
thread_cache_size = 64 			#9
table_open_cache = 81920 			#2000
table_definition_cache = 4096 			#1400
table_open_cache_instances = 64 			#16
max_prepared_stmt_count = 1048576 			#

####: for binlog
binlog_format = row 			#row
log_bin = mysql-bin 			#off
binlog_rows_query_log_events = on 			#off
log_slave_updates = on 			#off
expire_logs_days = 7 			#0
binlog_cache_size = 65536 			#65536(64k)
#binlog_checksum = none 			#CRC32
sync_binlog = 1 			#1
slave-preserve-commit-order = ON 			#

####: for txt log
log_error = error.log 			#/usr/local/mysql/data/localhost.localdomain.err
general_log = off 			#off
general_log_file = general.log 			#hostname.log

####: for slow query log
slow_query_log = on 			#off
slow_query_log_file = slow.log 			#hostname.log
#log_queries_not_using_indexes = on 			#off
long_query_time = 1.000000 			#10.000000

####: for gtid
#gtid_executed_compression_period = 1000 			#1000
gtid_mode = on 			#off
enforce_gtid_consistency = on 			#off

####: for replication
skip_slave_start = 1 			#
#master_info_repository = table 			#file
#relay_log_info_repository = table 			#file
slave_parallel_type = logical_clock 			#database | LOGICAL_CLOCK
slave_parallel_workers = 4 			#0
#rpl_semi_sync_master_enabled = 1 			#0
#rpl_semi_sync_slave_enabled = 1 			#0
#rpl_semi_sync_master_timeout = 1000 			#1000(1 second)
#plugin_load_add = semisync_master.so 			#
#plugin_load_add = semisync_slave.so 			#
binlog_group_commit_sync_delay = 100 			#500s
binlog_group_commit_sync_no_delay_count =  10 			#0

####: for innodb
default_storage_engine = innodb 			#innodb
default_tmp_storage_engine = innodb 			#innodb
innodb_data_file_path = ibdata1:100M:autoextend 			#ibdata1:12M:autoextend
innodb_temp_data_file_path = ibtmp1:12M:autoextend 			#ibtmp1:12M:autoextend
innodb_buffer_pool_filename = ib_buffer_pool 			#ib_buffer_pool
innodb_log_group_home_dir = ./ 			#./
innodb_log_files_in_group = 3 			#2
innodb_log_file_size = 100M 			#50331648(48M)
innodb_file_per_table = on 			#on
innodb_online_alter_log_max_size = 128M 			#134217728(128M)
innodb_open_files = 65535 			#2000
innodb_page_size = 16k 			#16384(16k)
innodb_thread_concurrency = 0 			#0
innodb_read_io_threads = 4 			#4
innodb_write_io_threads = 4 			#4
innodb_purge_threads = 4 			#4 gc
innodb_page_cleaners = 4 			#4 refresh lru
innodb_print_all_deadlocks = on 			#off
innodb_deadlock_detect = on 			#on
innodb_lock_wait_timeout = 20 			#50
innodb_spin_wait_delay = 128 			#6
innodb_autoinc_lock_mode = 2 			#1
innodb_io_capacity = 200 			#200
innodb_io_capacity_max = 2000 			#2000
#--------Persistent Optimizer Statistics
innodb_stats_auto_recalc = on 			#on
innodb_stats_persistent = on 			#on
innodb_stats_persistent_sample_pages = 20 			#20
innodb_adaptive_hash_index = on 			#on
innodb_change_buffering = all 			#all
innodb_change_buffer_max_size = 25 			#25
innodb_flush_neighbors = 1 			#1
#innodb_flush_method =  			#
innodb_doublewrite = on 			#on
innodb_log_buffer_size = 128M 			#16777216(16M)
innodb_flush_log_at_timeout = 1 			#1
innodb_flush_log_at_trx_commit = 1 			#1
innodb_buffer_pool_size = 100M 			#134217728(128M)
innodb_buffer_pool_instances = 4
autocommit = 1 			#1
#--------innodb scan resistant
innodb_old_blocks_pct = 37 			#37
innodb_old_blocks_time = 1000 			#1000
#--------innodb read ahead
innodb_read_ahead_threshold = 56 			#56 (0..64)
innodb_random_read_ahead = OFF 			#OFF
#--------innodb buffer pool state
innodb_buffer_pool_dump_pct = 25 			#25
innodb_buffer_pool_dump_at_shutdown = ON 			#ON
innodb_buffer_pool_load_at_startup = ON 			#ON

####for performance_schema
performance_schema = off 			#on
performance_schema_consumer_global_instrumentation = on 			#on
performance_schema_consumer_thread_instrumentation = on 			#on
performance_schema_consumer_events_stages_current = on 			#off
performance_schema_consumer_events_stages_history = on 			#off
performance_schema_consumer_events_stages_history_long = off 			#off
performance_schema_consumer_statements_digest = on 			#on
performance_schema_consumer_events_statements_current = on 			#on
performance_schema_consumer_events_statements_history = on 			#on
performance_schema_consumer_events_statements_history_long = on 			#off
performance_schema_consumer_events_waits_current = on 			#off
performance_schema_consumer_events_waits_history = on 			#off
performance_schema_consumer_events_waits_history_long = off 			#off
performance-schema-instrument = 'memory/%=COUNTED'
"""
