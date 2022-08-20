# React Architecture

## Higher Order Components
  Takes a component, and return and enhanced component, Better than using mixins.
  ```
  Eg:
  function withLogging(wrappedFunction) {
    // Returns a function with the same API...
    return function(x, y) {
      var result = wrappedFunction(x, y);
      console.log('result:', result);
      return result;
    };
  }
  var addAndLog = withLogging(add);
  ```

## Definitions:
* JSX - XML syntax for generating javscript renders. Though it looks like you;re creating HTML-like elements Under the hood this is syntactic sugar around react.createElement.  
Under the hood babel transpiles JSX into javascript (a reason why className is used since class is reserved under JS)

* Redux - State Managmenent Library consisiting of (Store, Action, Reducer...)

* RegisterServiceWorker() = The service worker is a web API that helps you cache your assets and other files so that when the user is offline or on slow network, he/she can still see results on the screen, as such, it helps you build a better user experience, that's what you should know about service worker's for now. It's all about adding offline capabilities to your site.


## Todo:
* Render Props: https://reactjs.org/docs/render-props.html
* Data Flow: Unidirectional, Context, PropDrilling, Redux, Global State
* How to replicate lifecycle methods using useEffect:https://codegino.com/blog/lifecycle-methods-to-useeffect , https://blog.logrocket.com/using-react-useeffect-hook-lifecycle-methods/
* Scrolling?
* useRef : see FocusOnPageLoad.js
* UI: 3StepForm, Forms, listMaps... 
