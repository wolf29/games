<?php
$target = mktime(0, 0, 0, 7, 13, 2011) ;
$today = time () ;
$difference =($target-$today) ;
$days =(int) ($difference/86400) ;
$hours =(int) ($difference/1440);
$mins =(int) ($difference/24);
$secs =(int) ($difference);
print "Retirement is in $days days\n";
print "Or you could say $hours hours\n";
print "Or you could say $mins minutes\n";
print "Or you could say $secs seconds\n"; 

$rdays =($difference%86400) ;
$rhours =($difference%1440);
$rmins =($difference%24);
$rsecs =($difference);
print "Retirement is in $rdays days\n";
print "Or you could say $rhours hours\n";
print "Or you could say $rmins minutes\n";
print "Or you could say $rsecs seconds\n"; 

#1 day = 24 hours = 1440 minutes = 86400 seconds
?> 

