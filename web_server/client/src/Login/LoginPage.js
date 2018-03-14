import React from 'react';
import LoginForm from './LoginForm'

class LoginPage extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      errors: {},
      user: {
        email: '',
        password: ''
      }
    }
  }

  processForm(e) {
    e.preventDefault();

    const email = this.state.user.email;
    const password = this.state.user.password;

    console.log('email:', email);
    console.log('password:', password);

    //TODO: post login data
  }

  changeUser(e) {
    const field = e.target.name;
    const user = this.state.user;
    user[field] = e.target.value;

    this.setState({
      user: user
    })
  }


  render() {
    return (
      <LoginForm
      onSubmit={(e) => this.processForm(e)}
      onChange={(e) => this.changeUser(e)}
      errors={this.state.errors}
      user={this.state.user} />
    );
  }
}

export default LoginPage;
