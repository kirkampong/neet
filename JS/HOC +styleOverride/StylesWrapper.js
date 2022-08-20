import React from 'react';
import commonStyles from './commonStyles';

// This wrapper takes a Button functional componenent and returns the same 
// component with translated style props based on the prop 'isDisabled?'


const translateProps = (props) => {
    let _styles = {...commonStyles.default}
    if(props.disable){
        _styles = {..._styles, ...commonStyles.disable};  
    }
    const newProps = {...props,styles:_styles }
    return newProps;
} 


export default (WrappedComponent) => {
    return function wrappedRender(args) {
        return WrappedComponent(translateProps(args));
    }
}