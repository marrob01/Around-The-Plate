import React, { Component } from 'react'
import {
  BrowserRouter,
  Route,

} from "react-router-dom";
import BackRound from './Components/Header/BackroundImg';
import RecipeSearch from './Components/Header/RecipeSearch';
import Home from './Components/Home';
import Create from './Components/CreateRecipe';
import Favorites from './Components/Favorites';
import View from './Components/ViewRecipe';
import Register from './Components/Register';
import Nav from './Components/Nav'

export default class App extends Component {

  constructor(props){
      super(props)
      this.state ={
          username : "",
          email: "",
          password : "",
          loggedIn : false,


        }


  }
  register = async (event) => {
    event.preventDefault()

    let body = JSON.stringify({
      username: this.state.username,
      email: this.state.email,
      password: this.state.password,
    })

    console.log(body)

      const response = await fetch('http://localhost:8000/api/v1/users/register ', {
        credentials: 'include',
        method: "POST",
        headers: {
          'Content-Type': 'application/json',
        },

        body:body


      })

      if(response.status === 200 || response.status === 201){
        this.setState({
          loggedIn: true
        })
      }
      console.log(response)
      const parseData = await response.json()
      console.log(parseData)
      console.log(parseData.data)

    }

    loginChange = (event) => {

         this.setState({
             [event.target.name]: event.target.value
         })
         console.log(this.state)
     }



  render() {

    return (
      <div className="App">




        <BrowserRouter>
          <BackRound />
          <Nav />
          <RecipeSearch />


          <Route path="/" exact component={Home} />

          <Route path="/create_recipe" exact component={Create} />
          <Route path="/view_recipe" exact  component={View} />
          <Route path="/favorites"  exact component={Favorites} />
          <Route path="/users/register"  exact component={() => <Register username={this.state.username}
           email={this.state.email}
            password={this.state.password}
            logInChange={this.loginChange}
           register={this.register}  />} />


        </BrowserRouter>

      </div>
    );

  };

}
