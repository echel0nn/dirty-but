<?php
 
$hash     = '$2y$10$FalJ8SmqTDBv7Fr366RC9uW5hKJVZijsDqzgASh1kSGMsUFMMLGZq';
$partial  = 'kztu6fe1m68mwf7vl1g3grjzmocia043pmno83q3ati98c8r324dzc0hc7n41p6tdjg6p';
$chars      = str_split('abcdefghijklmnopqrstuvwxyz0123456789');
 
foreach($chars as $a) {
  foreach($chars as $b) {
    foreach($chars as $c) {
      $pass = $partial . $a . $b . $c;
      echo $a.$b.$c."\r";
      if (password_verify($pass, $hash)) {
       
        echo $pass." : ".$hash."\n";
        echo "Found!\n";
        break 3;
      }
    }
  }
}
?>
