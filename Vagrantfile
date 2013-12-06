# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # All Vagrant configuration is done here. The most common configuration
  # options are documented and commented below. For a complete reference,
  # please see the online documentation at vagrantup.com.

  # Every Vagrant virtual environment requires a box to build off of.

  config.vm.define :master do |master_conf|
    master_conf.vm.host_name = "mir"
    master_conf.vm.box = "mir-3.0"
    master_conf.vm.network :private_network, ip: "33.33.66.100"
    master_conf.vm.provider :virtualbox do |v|
      v.name = "mir"
      v.gui = (ENV['OS'] == 'Windows_NT')
      v.customize ["modifyvm", :id, "--memory", "1024", "--cpus", "1"]
    end
    master_conf.vm.provision :shell do |shell|
      shell.inline = "truncate -s 0 /var/log/mir_*.log&&service mir start"
    end

  end

#  config.vm.define :dc do |dc_conf|
#    dc_conf.vm.host_name = "dc"
#    dc_conf.vm.box = "windows-2008r2-standard"
#    dc_conf.vm.network :private_network, ip: "33.33.66.99"
#    dc_conf.vm.provider :virtualbox do |v|
#      v.name = "dc"
#      v.gui = (ENV['OS'] == 'Windows_NT')
#      v.customize ["modifyvm", :id, "--memory", "1024", "--cpus", "1"]
#    end
#    dc_conf.windows.halt_timeout = 25
#  
#    # Admin user name and password
#    dc_conf.winrm.username = "vagrant"
#    dc_conf.winrm.password = "vagrant"
#
#    dc_conf.vm.guest = :windows
#    dc_conf.vm.network :forwarded_port, guest: 5985, host: 5984
#    
#    dc_conf.winrm.port = 5984
#
#    dc_conf.vm.provision :shell do |shell|
#      shell.inline = "msiexec /i \\\\VBOXSRV\\vagrant\\AgentSetup_10.6.12_x64.msi /passive"
#      shell.args = "'n/a'"
#    end    
#
#    dc_conf.vm.provision :chef_solo do |chef|
#      chef.cookbooks_path = "cookbooks"
#      chef.json = {}
#      chef.add_recipe("windows-fromscratch::_annoyances")
#      chef.add_recipe("windows-fromscratch::sysinternals")
#      chef.add_recipe("windows-fromscratch::bginfo")
#      chef.add_recipe("windows-fromscratch::_ie_annoyances")
#      # domain_controller forces a reboot!
#      chef.add_recipe("windows-fromscratch::domain_controller")
#    end
#  end

  (1..2).each do |i|
    vmname = "slave#{i}"
    config.vm.define vmname.to_sym do |slave_conf|
      slave_conf.vm.box = "windows-2008r2-standard"
      slave_conf.vm.network :private_network, ip: "33.33.66.#{i+100}"
      slave_conf.vm.provider :virtualbox do |v|
        v.name = "mirclient#{i}"
        v.gui = (ENV['OS'] == 'Windows_NT')
        v.customize ["modifyvm", :id, "--memory", "1024", "--cpus", "1"]
      end

      slave_conf.windows.halt_timeout = 25
    
      # Admin user name and password
      slave_conf.winrm.username = "vagrant"
      slave_conf.winrm.password = "vagrant"

      slave_conf.vm.guest = :windows
      slave_conf.vm.network :forwarded_port, guest: 3389, host: 3389+i
      slave_conf.vm.network :forwarded_port, guest: 5985, host: 5985+i
      
      slave_conf.winrm.port = 5985+i
      slave_conf.vm.provision :shell do |shell|
        shell.inline = "msiexec /i \\\\VBOXSRV\\vagrant\\AgentSetup_10.6.14_universal.msi /passive"
        shell.args = "'n/a'"
      end
      slave_conf.vm.provision :chef_solo do |chef|
        chef.cookbooks_path = "cookbooks"
        chef.json = {}
        chef.add_recipe("windows-fromscratch::_annoyances")
        chef.add_recipe("windows-fromscratch::sysinternals")
        chef.add_recipe("windows-fromscratch::bginfo")
        chef.add_recipe("windows-fromscratch::_ie_annoyances")
      end
    end
  end

end
