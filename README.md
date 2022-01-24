# Testovoe
### Run this commands
1. Check variables presented in playbook.yml, change them to your likings if needed
 
2. Run vagrant
```
vagrant up
```
3. Add ssh keys.
*Just in case*
`
eval $(ssh-agent)
`
```
ssh-add .vagrant/machines/minio-*/virtualbox/private_key
```
### ad-hoc commands
4. create user within minio's group
```
ansible all -m ansible.builtin.user -a "name=test group=minio state=present create_home=no" -i hosts.ini -b -u vagrant
```
5. copy file to minio's bucket
```
ansible all -m ansible.builtin.copy -a "src=test.jpg dest=/home/minio/export1/bucket/ owner=minio group=minio" -i hosts.ini -u vagrant -b && ansible all -m ansible.builtin.copy -a "src=test.jpg dest=/home/minio/export2/bucket/ owner=minio group=minio" -i hosts.ini -u vagrant -b
```

6. download file with 1000 byte offset
```
python3 download-img.py
```

### Тестовое задание

1. Создать репозиторий (публичный на https://github.com или приватный в нашем гитлабе) для артефактов,
полученных при работе с тестовым заданием.
2. Подготовить Vagrantfile для трех виртуальных хостов (бокс ubuntu/focal64) с ip
адресами в одном адресном пространстве и разместить Vagrantfile в корне репозитория
3. Подготовить playbook ansible, с помощью которого:
- развернуть Distributed Minio и Nginx на трех хостах (используя ранее подготовленный
Vagrantfile)
- настроить три экземпляра Nginx в режиме обратного прокси и балансировщика нагрузки
для трех развернутых нод Minio
- playbook разместить в корне репозитория
- отобразить команды на развертывание виртуальных хостов и проигрывание playbook в
README.MD репозитория
4. Используя ad-hoc команды Ansible:
- создать пользователя с правами на чтение и запись
- залить в Minio файл, приложенный к этому письму
- сами команды описать в README.MD репозитория
5. Подготовить скрипт на Python, с помощью которого скачать залитый ранее файл из
Minio со смещением 1000 (подробнее - см. Python Client API в Minio Client SDK for
Python)
6. Прислать полученный в результате выполнения скрипта файл изображения и ссылку на
репозиторий по адресу электронной почты ilya.lyubimov@quadcode.com
