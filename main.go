package main
 
import (
    "database/sql"
    "fmt"
 
    _ "github.com/go-sql-driver/mysql"
)
 
func main() {
    db, err := sql.Open("mysql", "root:123456@tcp(apple:3306)/action")
    if err != nil {
        panic(err)
    }
    defer db.Close()
    err = db.Ping()
    if err != nil {
        panic(fmt.Sprintf("連接失敗: %s", err.Error()))
    }
    fmt.Println("SUCCESS")
}
