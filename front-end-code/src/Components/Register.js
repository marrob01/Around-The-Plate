import React, { Component } from 'react'




export default class Register extends Component {
    constructor(props){
        super(props)
      }
      


    render() {
      console.log(this.props)
      console.log("-----------------------")
        return(
            <>

              <form onSubmit={this.props.register} >
                <label htmlFor="username" >Username</label>

                <input onChange={(event)=> this.props.logInChange(event)} type="text" name="username" id="username" value={this.props.username}></input>

                <label htmlFor="email">Email</label>
                <input onChange={(event)=> this.props.logInChange(event)} type="text" name="email" id="email" value={this.props.email}></input>

                <label htmlFor="password"> Password</label>
                <input onChange={(event)=> this.props.logInChange(event)} type="text" name="password" id="password" value={this.props.password}></input>

                <input type="submit"></input>

              </form>


            </>
        )

      }

}


// whoWillCleanTheKitchenTonight =["Marcus", "Marlene", "Garl"];
//
// const clenUp = Math.floor(Math.random()*whoWillCleanTheKitchenTonight.length);
//
// console.log(clenUp)
