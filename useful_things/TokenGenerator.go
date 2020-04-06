package main

import (
	"time"
	"gopkg.in/dgrijalva/jwt-go.v3"
	"fmt"
)

func main(){
	var i int = 0

	for i = 0; i < 500; i++{	
	var secret string
	var tokenize string
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"exp":       time.Now().Add(time.Hour * 8650 * 2).Unix(),
		"iss":	     i,
	})

	tokenString, _ := token.SignedString([]byte(secret))
	fmt.Println(tokenString)

	token, err := jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		return []byte(tokenize), nil
	})

	if err != nil {
	panic(err)
	}
}}

