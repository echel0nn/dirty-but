 <?  
  $orig_cookie = base64_decode('ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw');  
  function xor_encrypt($in) {  
         	$text = json_encode(array("showpassword"=>"yes", "bgcolor"=>"#ffffff"));
            $key = "qw8J";  
            $outText = '';   
                for($i=0;$i<strlen($text);$i++) {  
                   $outText .= $text[$i] ^ $key[$i % strlen($key)];  
                      }  
                         return $outText;  
                          }  
                           print base64_encode(xor_encrypt($orig_cookie));
?>


