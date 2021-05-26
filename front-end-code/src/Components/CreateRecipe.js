import React, { Component } from 'react'
import CreateShow from './CreateShow'
import CreateRecipeForm from './CreateRecipeForm'

export default class Create extends Component {

  constructor(){
      super()
    }



  render() {

    return (
      <>

        <CreateShow  />
        <CreateRecipeForm />




      </>
    );

  };

}
