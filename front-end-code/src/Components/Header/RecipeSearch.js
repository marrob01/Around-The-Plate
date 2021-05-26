import React, { Component } from 'react'
import RecipeSearchComponent from './RecipeSearchComponent'

export default class RecipeSearch extends Component {
    constructor(props){
        super(props)

    }

    render() {
        return(
          <div>

            <form onSubmit={this.recipe}>
              <input type ="text" id="recipe-search" name="recipe-search" placeholder="Search Recipe By Ingredient"></input>
              <input type="submit"></input>

            </form>

            <RecipeSearchComponent />

          </div>
        )
    }
}
