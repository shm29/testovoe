# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"

  (1..3).each do |id|
    config.vm.define "minio-#{id}" do |machine|
      machine.vm.hostname = "minio-#{id}"
      machine.vm.network :private_network, ip: "192.168.29.2#{id}"
      machine.vm.provision :ansible do |ansible|
        ansible.playbook ='playbook.yml'
        ansible.inventory_path = 'hosts.ini'
      end
    end
  end
end
