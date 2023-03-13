<div class="container">
  <div class="links">
    <a href="/">01 Home</a>
    <a href="/#contact">02 Contact</a>
  </div>
  <div class="name">
    Reshma
  </div>
</div>

<style lang="scss">
  .container {
    display: flex;
  }

  .links {
    display: flex;
    flex-grow: 1;
    flex-wrap: wrap;

    justify-content: space-around;
    align-items: center;

    a {
      text-decoration: none;
    }
  }

  .name {
    flex-basis: 0;
    flex-grow: 1;

    font-family: 'Clearface';
    text-align: right;
    font-size: 4em;
  }
</style>