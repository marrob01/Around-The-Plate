import React, { Component } from 'react'
import { Link } from 'react-router-dom';

export default class NavBar extends Component {
    constructor(props){
        super(props)
        this.state={

        }


    }

    render() {
        return(
          <>
          <nav>
            <Link to="/" className="home">
              Home
            </Link>

            <Link to="/favorites" className="favorites">
              Favorites
            </Link>


            <Link to="/create_recipe" className="create-recipe">
              Create Recipe
            </Link>

            <Link to="/view_recipe" className="view-recipe">
              View Recipe
            </Link>

            <Link to="/users/register" className="signup">
              Sign Up
            </Link>


          </nav>

          </>

        )
    }
}
