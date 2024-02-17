<h1>Algorithm for file updates in Python</h1>

<h2>Project description</h2>

<p>An organization I'm part of needs me to regularly update a file of employees who can access restricted access-level content. The <q>allow_list.txt</q> includes employee IP addresses that currently have access to personal records, and I have been given a list of IP addresses to remove.</p>
<p>In this project, I will create a Python algorithm that checks whether the allow list contains any of the IP addresses to remove and remove them.</p>

<h2>Open and read the file that contains the allow list</h2>
<p>I first start by storing the <q>allow_list.txt</q> file to a variable that I can use to open it. Then, I'll define the list of IP addresses that are due to be removed from the "allow list".</p>
<p>Then, using the <code>with</code> and <code>open()</code> function, I open the file to read the currently allowed IP addresses listed in the file. The <q>r</q> indicates what I want to do with the file. In this example, I want to read it.</p>
<p>With the file open, I can now read the contents with the <code>.read()</code> method, which converts the contents of the file into a Python string.</p>
 <img src="https://i.imgur.com/mKzEswr.png" width="50%" height="50%">

<h2>Convert the string into a list</h2>
<p>Since I will need to iterate through the list of IP addresses to remove any unallowed IP addresses, I will convert the file contents string into a Python list with <code>.split()</code>.</p> 
<img src="https://i.imgur.com/FGHjXM6.png" width="50%" height="50%">

 
<h2>Iterate through the remove list</h2>
<p>Now that all of the allowed IP addresses are easily available in a list, I will iterate through all the IP addresses I need to remove to check if they exist in the currently allowed IP addresses. 
</p>
<img src="https://i.imgur.com/3ySqen5.png" width="30%" height="30%">
 
<h2>Remove IP addresses that are on the remove list</h2>
<p>While iterating through the IP addresses to remove, I will create a conditional to remove an IP address from the list of allowed IP addresses if it is currently allowed but should be removed. 
</p>
<img src="https://i.imgur.com/9n1lxc8.png" width="50%" height="50%">
 
<h2>Update the file with the revised list of IP addresses</h2>
<p>Now that I have the updated list of IP addresses, I need to update the allow_list.txt file with the updated list. I will first convert the Python list to a string where each IP address is on its own line. Then, I will open the allow_list.txt file with the <q>w</q> parameter to overwrite the file and avoid duplicate information. Finally, I will write the updated string of allowed IP addresses into the file. 
</p>
 <img src="https://i.imgur.com/8QDYY5I.png" width="60%" height="60%">
 <img src="https://i.imgur.com/BpTkzZB.png" width="50%" height="50%">
<h2>Summary</h2>
<p>For this task, I created an algorithm that removes IP addresses identified in a <q>remove_list</q> variable from the <q>allow_list.txt</q> file of approved IP addresses. This algorithm involved opening the file, converting it to a string to be read, and then converting this string to a list stored in the variable <code>ip_addresses</code>. I then iterated through the IP addresses in <q>remove_list</q>. With each iteration, I checked if the element was part of the <q>ip_addresses</q> list. If so, I applied the <code>.remove()</code> method to it to remove the element from <q>ip_addresses</q>. After this, I used the <code>.join()</code> method to convert the <q>ip_addresses</q> back into a string so that I could write over the contents of the <q>allow_list.txt</q> file with the revised list of IP addresses. Finally, I printed the file output using <code>print()</code></p>
