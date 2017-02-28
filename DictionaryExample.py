'''
Create a program to demonstrate dictionaries.
Dictionaries are very useful for things like using Json APIs
Notice the syntax. The first part is the "key" the second part is the "value"
'''

movie1 = {'Title':'The Dark Knight', 'Rating':'5/5', 'Year':'2008', 'Director':'Christopher Nolan'}
#What are they keys? What are the values? Why could this be useful?

movie2 = {'Title':'Good Will Hunting', 'Rating':'4.5/5', 'Year':'1996', 'Director':'Gus Van Sant'}

#example of accessing the value in the dictionary
print("Name of movie1 =", movie1['Title'])

#oops the year on movie2 is wrong, better fix that.
movie2['Year'] = '1997'
#print(movie2['Year'])#make sure it did what we expected.

#create an if-elif-else statement to decide & print which movie came out first or if they
# came out the same year


# YOUR CODE HERE

# we can even print the whole dictionary
#python is really helpful
print("movie 1: ", movie1)
# or even just
#print(movie1)

'''
That's pretty much it. Dictionaries are easy to use and extremely powerful.

What other type of basic data structures are there?!

- Lists [] - Can add any type of variable to the list, get items from an index of the list, single item per spot.
- Tuples () - Just like a list, but it can't be changed.  This is called being immutable.

Make your own too!

'''
