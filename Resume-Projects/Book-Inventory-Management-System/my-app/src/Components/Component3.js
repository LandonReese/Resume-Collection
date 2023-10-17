// Check out a book
import React, { useState, useEffect } from "react";

const url = "http://localhost:5000/books";

function BookList() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch(url)
      .then((res) => res.json())
      .then((data) => setBooks(data.filter((book) => book.avail)));
  }, []);

  // This function will handle setting avail to false
  const checkout = (id) => {
    console.log(`Checking out book with ID ${id}`);
    fetch(`${url}/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ avail: false }),
    })
      .then((res) => {
        if (res.ok) {
          console.log(`Book with ID ${id} checked out successfully`);
          setBooks(books.filter((book) => book._id !== id));
        } else {
          throw new Error("Book not found or already checked out");
        }
      })
      .catch((err) => console.error(err));
      window.location.reload();
  };

  return (
    <div>
      <h2>Check Out a Book</h2>
      <ul>
        {books.map((book) => (
          <li key={book._id}>
            {book.title} by {book.author}. ID: {book._id}
            <button onClick={() => checkout(book._id)}>Check Out</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default BookList;