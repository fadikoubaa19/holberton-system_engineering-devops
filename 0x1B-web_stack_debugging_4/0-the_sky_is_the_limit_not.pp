#ApacheBench 
exec { 'increase file limit' :
  command => 'sed -i "s/15/10000/g" /etc/default/nginx; sudo service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -e /etc/default/nginx',
}
