package main

import(
	"fmt"
	"github.com/bclicn/color"
	"os/exec"
	"os"
	"flag"
	"log"
)


var usage =`
	sudo change_intfname -i interface_name -t to_interface_name
`


func exec_(program string, args ...string){
	cmd := exec.Command(program,args...)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err := cmd.Run()
	if err != nil{
		log.Fatal(color.Invert("Error!:"+err.Error()))
	}
}

func main() {
	interface_name := flag.String("int","wlp0s20u2","")
	to_interface_name := flag.String("to","echelon","")
	flag.Parse()

	flag.Usage = func(){
		fmt.Println(color.BGreen(usage))
	}
	exec_("ip","link","set","dev",*interface_name,"down")
	exec_("ip","link","set","dev",*interface_name,"name",*to_interface_name)
	exec_("ip","link","set","dev",*to_interface_name,"up")
	fmt.Println(color.BGreen("\tThe interface has been changed."))
}

