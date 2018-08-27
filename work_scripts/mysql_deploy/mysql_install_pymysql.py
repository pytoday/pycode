#!/usr/bin/env python3
# coding=utf-8
# title          : mysql_install_pymysql.py
# description    : script used to install mysql-server. general binary version.
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/6/22 2:35
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import sys, os, time, subprocess, configparser
import wget, tarfile, pymysql
from myconf import conf_tmp
from log import Log


def initenv(install_dir, base_data_dir, port):
    """create user and dirs. fix dir permission"""
    init_log = Log("/tmp/mysql_install.log", "initenv")
    # create user
    add_user = subprocess.getstatusoutput("useradd -MU -s /sbin/nologin mysql")
    if add_user[0]:
        init_log.warning("Add user with error: %s" % add_user[1])

    # add needed dir
    os.makedirs(install_dir, 0o755, exist_ok=True)
    for sub_d in ['data', 'logs', 'tmp']:
        os.makedirs(base_data_dir+'/mysql'+port+'/'+sub_d, 0o755, exist_ok=True)

    # add permission
    chperm = subprocess.getstatusoutput("chown -R mysql.mysql "+base_data_dir)
    if chperm[0]:
        init_log.warning("Change permission with error: %s" % chperm[1])

    # add PATH
    check_cmd = "grep \"PATH=/usr/local/mysql/bin\" /etc/profile"
    check = subprocess.getstatusoutput(check_cmd)
    if check[0]:
        cmd = "echo 'export PATH=/usr/local/mysql/bin:${PATH}' >> /etc/profile"
        add_path = subprocess.getstatusoutput(cmd)
        if add_path[0]:
            init_log.warning("Add to path fail with error: %s" % add_path[1])
    else:
        init_log.info("Add path ok.")

    init_log.info("Initialize environment complete.")

    """
    # another way to chown
    uid = pwd.getpwnam('mysql').pw_uid
    gid = grp.getgrnam('mysql').gr_gid
    for root, dirs, files in os.walk(base_dir):
        for momo in dirs:
            os.chown(os.path.join(root, momo), uid, gid)
    """


def download(url, install_dir):
    """download binary file and uncompress to install_dir, then link it"""
    down_log = Log("/tmp/mysql_install.log", "download")
    tar_name = os.path.basename(url)
    fname = str(tar_name.split('.tar')[0])
    tar_dst = os.path.join(install_dir, tar_name)
    if not os.path.exists(tar_dst):
        wget.download(url, tar_dst)
    else:
        down_log.info("Binary file downloaded already skip downloading...")
        down_log.info("Decompressing file, please wait....")

    os.chdir(install_dir)
    tar = tarfile.open(tar_name)
    tar.extractall()
    tar.close()

    ins_perm = subprocess.getstatusoutput("chown -R mysql.mysql "+install_dir)
    if ins_perm[0]:
        down_log.warning("Change permission for install file with error: %s" % ins_perm[1])
    links = subprocess.getstatusoutput("ln -s "+os.path.join(install_dir, fname)+' /usr/local/mysql')
    if links[0]:
        down_log.warning("Link installation dir to /usr/local fail with error: %s" % links[1])
    down_log.info("Binary file downloaded and decompressed. soft link ok too..")


def genconf(base_data_dir, port):
    """generate conf and save to file"""
    conf_log = Log("/tmp/mysql_install.log", "genconf")
    config = configparser.ConfigParser()
    config.read_string(conf_tmp)
    # future function: use parser module to change conf file here
    config['mysql']['port'] = port
    config['mysqld']['port'] = port
    config['mysqld']['socket'] = '/tmp/mysql'+port+'.sock'

    conf_name = base_data_dir+'/mysql'+port+'/my'+port+'.cnf'
    with open(conf_name, 'w') as configfile:
        config.write(configfile)
    conf_perm = subprocess.getstatusoutput("chown mysql.mysql "+conf_name)
    if conf_perm[0]:
        conf_log.warning("Change configuration file owner to mysql fail: %s" % conf_perm[1])
    conf_log.info("Generate configuration file ok.")
    return conf_name


def install(conf_name):
    """init db, startup and change password"""
    ins_log = Log("/tmp/mysql_install.log", "install")
    ins_db = subprocess.getstatusoutput("/usr/local/mysql/bin/mysqld --defaults-file="+conf_name
                                        + ' --initialize-insecure')
    if ins_db[0]:
        ins_log.fatal("Init database error with error code(%d), The error message is: %s" % (ins_db[0], ins_db[1]))
        sys.exit(124)
    else:
        ins_log.info("Database init ok.")

    startup_db = subprocess.getstatusoutput("/usr/local/mysql/bin/mysqld --defaults-file="+conf_name
                                            + " --skip-networking &")
    if startup_db[0]:
        ins_log.fatal("Database startup fail with error code(%d), The error message is: %s" % (startup_db[0], startup_db[1]))
        sys.exit(125)
    else:
        ins_log.info("db startup with --skip-networking ok.")


def chpassword(port, password):
    # open log
    log = Log("/tmp/mysql_install.log", "chpassword")

    # make sure mysqld process exist.
    i = 0
    while i < 5:
        i += 1
        time.sleep(1)
        p = subprocess.getstatusoutput("killall -0 mysqld")
        if not p[0]:
            break
        else:
            log.warning("No process of mysql, wait mysqld to start(max_wait=5s).")

    conn = pymysql.connect(unix_socket='/tmp/mysql'+port+'.sock', user='root')     # create connection
    cursor = conn.cursor()      # create cursor
    try:
        effect_row = cursor.execute("alter user user() identified by %s;", password)   # execute
    except pymysql.err.ProgrammingError as e:
        log.error("Change password failed: %s" % e)
    finally:
        stop_db = subprocess.getstatusoutput("killall mysqld")
        if stop_db[0]:
            log.error("Some thing wrong while stoping db.")
            sys.exit(126)
        else:
            log.info("All done, mysqld stopped.")

    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])
    conn.commit()   # commit
    cursor.close()      # close cursor
    conn.close()    # close conn


if __name__ == '__main__':
    url = 'https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.22-linux-glibc2.12-x86_64.tar.gz'
    base_data_dir = '/data'
    install_dir = '/opt/mysql'
    port = '3306'
    password = 'qazwsx'

    initenv(install_dir, base_data_dir, port)
    download(url, install_dir)
    conf_file = genconf(base_data_dir, port)
    install(conf_file)
    chpassword(port, password)
