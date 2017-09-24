import React from 'react';
import ReactDOM from 'react-dom';
import ExampleWork from './example-work';

const myWork = [
	{
		'title': "Work Example",
		'href': "https://example.com",
		'desc': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et mi non nisi luctus consequat. Etiam tristique sem sem, id hendrerit nisl dictum non. Nulla porta accumsan mollis. Aliquam interdum in ex ut placerat. Phasellus mattis magna tellus, sit amet porta urna mattis ut. Suspendisse potenti. Mauris lobortis bibendum elit. Sed malesuada justo et neque consectetur venenatis. Curabitur elementum placerat efficitur. Vivamus gravida ultrices sagittis. Aenean tristique risus sit amet enim porta, id facilisis lacus dapibus. Vivamus et vehicula est. Donec vel magna nec risus sodales sodales.",
		'image': {
			'desc': "example screenshot of a project involving code",
			'src': "images/example1.png",
			'comment': ""
		}
	},
		{
		'title': "A Serverless Portfolio",
		'href': "https://www.datapipe.com",
		'desc': "Duis lectus nibh, ullamcorper quis tortor at, porttitor porta ipsum. Aliquam consequat, velit vel mattis dapibus, leo tortor faucibus diam, eu fermentum tellus ex euismod urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nunc eget tincidunt est. Ut ac mauris pharetra, ullamcorper ex vitae, tempus enim. Maecenas sed ante nisi. Cras purus orci, maximus eu nulla ut, bibendum pretium lacus. Aliquam erat volutpat. Praesent eu faucibus odio. Aenean imperdiet mauris et odio ultricies pellentesque. Pellentesque sit amet orci vitae velit pellentesque varius id a nisi. Phasellus facilisis nisl sed blandit pulvinar. Sed tempor eu metus iaculis pellentesque.",
		'image': {
			'desc': "example screenshot of a project involving chemistry",
			'src': "images/example2.png",
			'comment': ""
		}
	},
	{
		'title': "Bray Wanderers",
		'href': "http://www.braywanderers.com",
		'desc': "This is the site I coded for Bray Wanderers a long time ago...",
		'image': {
			'desc': "placeholder for a Bray redesign",
			'src': "images/example3.png",
			'comment': `/Down by the red rose cafe.... `
		}
	}
]

ReactDOM.render(<ExampleWork work={myWork}/>, document.getElementById('example-work'));
