function App() {
  const firstName = prompt("Enter your first name");
  const lastName = prompt("Enter your last name");

  return (
    <>
      <h1>Hello World--</h1>
      <p>Is this visible??</p>
      <p>{4 + 4}</p>
      <h1>
        Your First Name is {firstName} and your Last Name is {lastName}
      </h1>
    </>
  );
}

export default App;
