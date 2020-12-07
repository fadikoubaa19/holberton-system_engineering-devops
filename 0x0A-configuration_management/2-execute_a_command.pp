# Kill proc
exec { 'pkill killmenow':
provider  => 'shell',
}

