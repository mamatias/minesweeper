# Javascript DOM manipulation

## Creating elements
```javascript
const element = document.createElement('element')
parentElement.appendChild(element)



const div = document.createElement('div')
body.appendChild(div)

const ul = document.createElement('ul')
const li = document.createElement('li')
ul.appendChild(li)
```
## removing elements
you can remove an element either by using removeChild or with remove methods
```javascript
// with removeChild method
parent.removeChild(child)
// with remove method
child.remove()

ul.removeChild(li)
// or
li.remove()
```
## Querying elements
query an element that has an id
```javascript
const element = document.getElementById('elementId')

const container = document.getElementById('container')
```
query all elements by tag name (there is no similar method to find only one element by tag name)
```javascript
const groupOfElements = document.getElementsByTagName('tag')

const inputs = document.getElementsByTagName('input')
```
All in one
```javascript
// query by id
const element = document.querySelector('#elementId')

// query group of elements by id (which ignores the purpose of having a special id)
const elements.querySelectorAll('#elementId')

// query element by class name
const element = document.querySelector('.className')

// query group of elements by class name
const elements = document.querySelectorAll('.className')
```

## Modify elements
modifying element's attributes
modifying the style object
```javascript
element.style.fontSize = "18px"
element.style.backgroundColor = "#ffffff"
```
modifying the id:
```javascript
element.id = "myId"
```
modifying the class
```javascript
element.classList.add('myClass')

element.classList.remove('myClass')
```
modifying the text
```javascript
const element.innerText = "Hello World"
```
There is also textContent property for this job, However you would rather use innerTextinstead.

modifying the attribute in general
```javascript
element.setAttribute(attribute, value)

input.setAttribute(name, "myInput")

element.removeAttribute(attribute)

input.removeAttribute('name')
```
## Event Listeners
Here is a list of the popular events you'll likely to use: change, click, submit, keydown... and more
```javascript
element.addEventListener('event', () => {
// Do something...
}

button.addEventListener('click', () => {
alert('Hello There!')
}
```
## Conclusion
If this post was helpful for you i would appreciate it if you leave a 💓