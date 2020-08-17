Vagrant.configure("2") do |config|
  config.vm.box = "fedora/32-cloud-base"
  # network settings
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  # setting the enviourment
  config.vm.provider "virtualbox" do |v|
    v.name = "givit_vm"
  end
end
