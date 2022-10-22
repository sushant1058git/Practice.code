
var obj={
  name:"sushant",
  age:'50'
}

function removeProperty(obj,property){
  if (obj.hasOwnProperty(property)){
    delete obj[property];
    console.log(obj)
    return true;
  }
  else{
    return false;
  }
}


console.log(removeProperty(obj,'name'))