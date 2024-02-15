<h1>Algorithm for file updates in Python</h1>
<h1>Summary</h1>
<p>For this task, I created a Python algorithm that takes in a file of IP addresses and uses a list of IP addresses to remove to update the file. Using Python functionalities like with open, .read(), and .remove() I convert the file to a Python list and iterate through the list of IP addresses to remove and compare them to the IP addresses currently listed in the file. After removing the invalid IP addresses, I convert the list back to a string to then update the valid IP addresses file with the new list. 
</p>

<h2>Project description</h2>

<p>An organization I'm part of needs me to regularly update a file of employees who can access restricted access level content. The <q>allow_list.txt</q> includes employee IP addresses that currently have access to personal records, and I have been given a list of IP addresses to remove.</p>
<p>In this project, I create a Python algorithm that checks whether the allow list contains any of the IP addresses to remove, and remove them.</p>

<h2>Open and read the file that contains the allow list</h2>
<p>I first start by storing the <q>allow_list.txt</q> file to a variable that I can use to open it. Then, I'll define the list of IP addresses that are due to be removed from the allow list.</p>
<p>Then, using the <code>with</code> and <code>open()</code> function, I open the file to read the currently allowed IP addresses listed in the file. The <q>r</q> indicates what I want to do with the file. In this example, I want to read it.</p>
<p>With the file open, I can now read the contents with the <code>.read()</code> method, which converts the contents of the file into a python string.</p>
 <img src="https://i.imgur.com/mKzEswr.png" width="50%" height="50%">

<h2>Convert the string into a list</h2>
<p>Since I will need to iterate through the list of IP addresses to remove any unallowed IP addresses, I convert the file contents string into a Python list with <code>.split()</code>.</p> 
<img src="https://i.imgur.com/FGHjXM6.png" width="50%" height="50%">

 
<h2>Iterate through the remove list</h2>
<p>Now that all of the allowed IP addresses were easily available in a list, I iterated through all of the IP addresses I needed to remove so that I could check if they existed in the currently allowed IP addresses. 
</p>
<img src="https://i.imgur.com/3ySqen5.png" width="30%" height="30%">
 
<h2>Remove IP addresses that are on the remove list</h2>
<p>While iterating through the IP addresses to remove, I created a conditional to remove an IP address from the list of allowed IP addresses if it was currently allowed but should be removed. 
</p>
<img src="https://i.imgur.com/9n1lxc8.png" width="50%" height="50%">
 
<h2>Update the file with the revised list of IP addresses</h2>
<p>Now that I had the updated list of IP addresses, I needed to update the allow_list.txt file with the updated list. I first converted the Python list back to a string where each IP address is on its own line. Then I opened the allow_list.txt file with the <q>w</q> parameter to completely overwrite the file to avoid duplicate information. Finally, I wrote the updated string of allowed IP addresses to the file. 
</p>
 <img src="https://i.imgur.com/8QDYY5I.png" width="60%" height="60%">
 <img src="https://i.imgur.com/BpTkzZB.png" width="50%" height="50%">

