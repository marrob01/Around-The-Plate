import React, { Component } from 'react'

export default class Create extends Component {

  constructor(props){
      super(props)
    }
    handleChange = (event) => {
       this.setState({
           [event.target.name]: event.target.value
       })
   }




  render() {

    return (
      <>
    
      </>
    );

  };

}
