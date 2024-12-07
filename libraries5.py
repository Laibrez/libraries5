import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QTextEdit, QHBoxLayout, QLabel
)
from PyQt6.QtGui import QColor, QPalette


class LibraryUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Book Search and Recommendation")
        self.setGeometry(100, 100, 800, 600)

        # Set main colors (darker blue and dark orange)
        self.set_style()

        # Tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create tabs
        self.book_search_tab = self.create_book_search_tab()
        self.book_details_tab = self.create_book_details_tab()
        self.recommendations_tab = self.create_recommendations_tab()

        # Add tabs to the widget
        self.tabs.addTab(self.book_search_tab, "Book Search")
        self.tabs.addTab(self.book_details_tab, "Book Details")
        self.tabs.addTab(self.recommendations_tab, "Recommendations")

    def set_style(self):
        """Apply blue and orange theme to the entire window."""
        dark_blue = QColor("#000033")  # Darker blue
        dark_orange = QColor("#FF7F00")  # Dark Orange

        # Set background color
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, dark_blue)  # Set the window's background to dark blue
        self.setPalette(palette)

        # General button styles
        self.button_style = f"""
            QPushButton {{
                background-color: {dark_orange.name()};
                color: white;
                border-radius: 5px;
                padding: 8px 12px;  /* Increased padding for larger buttons */
            }}
            QPushButton:hover {{
                background-color: {dark_orange.darker().name()};
            }}
        """
        # Apply button style globally
        self.setStyleSheet(self.button_style)

    def create_book_search_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Search bar
        search_layout = QHBoxLayout()
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Book titles...")
        search_button = QPushButton("Search")
        search_button.clicked.connect(self.mock_search_books)
        search_button.setFixedHeight(40)  # Increase button height

        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(search_button)

        # Search results table
        self.search_results = QTableWidget()
        self.search_results.setRowCount(0)
        self.search_results.setColumnCount(3)
        self.search_results.setHorizontalHeaderLabels(["Titles", "Authors", "Genres"])

        # Style the table (orange background, black text)
        self.search_results.setStyleSheet("""
            QHeaderView::section {
                background-color: black;
                color: white;
            }
            QTableWidget::item {
                color: black;  /* Text in black */
                background-color: orange;  /* Orange background */
            }
        """)

        # View Details button
        view_details_button = QPushButton("View Details")
        view_details_button.clicked.connect(self.mock_view_details)

        # Add widgets to layout
        layout.addLayout(search_layout)
        layout.addWidget(self.search_results)
        layout.addWidget(view_details_button)
        tab.setLayout(layout)

        return tab

    def create_book_details_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Display book details area
        self.book_details_display = QTextEdit()
        self.book_details_display.setReadOnly(True)
        self.book_details_display.setStyleSheet(
            "background-color: white; color: black; border: 1px solid black;"
        )
        self.book_details_display.setText(
            "<b>Book Title:</b> Example Book<br>"
            "<b>Author:</b> John Doe<br>"
            "<b>Genre:</b> Fiction<br>"
            "<b>Description:</b> This is an example book description."
        )

        # Fetch Recommendations button
        fetch_recommendations_button = QPushButton("Fetch Recommendations")
        fetch_recommendations_button.clicked.connect(self.mock_fetch_recommendations)

        # Add widgets to layout
        layout.addWidget(self.book_details_display)
        layout.addWidget(fetch_recommendations_button)
        tab.setLayout(layout)

        return tab

    def create_recommendations_tab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        # Recommendations label
        recommendations_label = QLabel("<h2>Our Recommendations for You</h2>")
        recommendations_label.setStyleSheet("color: yellow; text-align: center;")  # Light yellow text
        layout.addWidget(recommendations_label)

        # Recommendations area
        self.recommendations_area = QTextEdit()
        self.recommendations_area.setReadOnly(True)
        self.recommendations_area.setStyleSheet(
            "background-color: white; color: black; border: 1px solid black;"
        )
        self.recommendations_area.setText(
            "<b>Book 1:</b> Title: The Giver<br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Drama<br><br>"
            "<b>Book 2:</b> Title: The Hunger Games<br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Dystopian<br><br>"
            "<b>Book 3:</b> Title: EXAMPLE 3 <br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Classic<br><br>"
            "<b>Book 4:</b> Title: Alice in Wonderland<br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Fiction<br><br>"
            "<b>Book 5:</b> Title: Steve Jobs<br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Biography<br>"
        )

        # Back to Search button
        back_to_search_button = QPushButton("Back to Search")
        back_to_search_button.clicked.connect(lambda: self.tabs.setCurrentIndex(0))

        # Add widgets to layout
        layout.addWidget(self.recommendations_area)
        layout.addWidget(back_to_search_button)
        tab.setLayout(layout)

        return tab

    def mock_search_books(self):
        print("search_books() function executed")
        self.search_results.setRowCount(5)  
        self.search_results.setItem(0, 0, QTableWidgetItem("Book 1"))
        self.search_results.setItem(0, 1, QTableWidgetItem("Author A"))
        self.search_results.setItem(0, 2, QTableWidgetItem("Genre X"))
        self.search_results.setItem(1, 0, QTableWidgetItem("Book 2"))
        self.search_results.setItem(1, 1, QTableWidgetItem("Author B"))
        self.search_results.setItem(1, 2, QTableWidgetItem("Genre Y"))
        self.search_results.setItem(2, 0, QTableWidgetItem("Book 3"))
        self.search_results.setItem(2, 1, QTableWidgetItem("Author C"))
        self.search_results.setItem(2, 2, QTableWidgetItem("Genre Z"))
        self.search_results.setItem(3, 0, QTableWidgetItem("Book 4"))
        self.search_results.setItem(3, 1, QTableWidgetItem("Author D"))
        self.search_results.setItem(3, 2, QTableWidgetItem("Genre W"))
        self.search_results.setItem(4, 0, QTableWidgetItem("Book 5"))
        self.search_results.setItem(4, 1, QTableWidgetItem("Author E"))
        self.search_results.setItem(4, 2, QTableWidgetItem("Genre V"))

    def mock_view_details(self):
        """Displays detailed information about the selected book."""
        selected_row = self.search_results.currentRow()

        if selected_row >= 0:
            # Retrieve selected book information
            title_item = self.search_results.item(selected_row, 0)
            author_item = self.search_results.item(selected_row, 1)
            genre_item = self.search_results.item(selected_row, 2)

            # Prepare detailed information
            title = title_item.text() if title_item else "Unknown Title"
            author = author_item.text() if author_item else "Unknown Author"
            genre = genre_item.text() if genre_item else "Unknown Genre"
            
            details_text = (
                f"<b>Title:</b> {title}<br>"
                f"<b>Author:</b> {author}<br>"
                f"<b>Genre:</b> {genre}<br>"
                f"<b>Year of Publication:</b> 2023<br>"  # Mock year
                f"<b>Purchase Options:</b><br>"
                f" - <a href='https://www.amazon.com'>Amazon</a><br>"
                f" - <a href='https://www.barnesandnoble.com'>Barnes & Noble</a><br>"
                f" - Local bookstore<br><br>"
                f"<b>Chapters:</b><br>"
                f"1. Introduction<br>"
                f"2. Chapter One<br>"
                f"3. Chapter Two<br>"
                f"4. Conclusion<br>"
            )

            # Display the details in the Book Details tab
            self.book_details_display.setHtml(details_text)
            self.tabs.setCurrentIndex(1)  # Switch to the Book Details tab
        else:
            # Handle no selection case
            self.book_details_display.setHtml("<b>No book selected. Please select a book to view details.</b>")
            self.tabs.setCurrentIndex(1)

    def mock_fetch_recommendations(self):
        """Mock function to simulate fetching recommendations."""
        recommended_text = (
            "<b>Book 1:</b> Title: The Wolf<br>"
            "Author: EXAMPLE AUTHOR 1<br>"
            "Genre: Drama<br><br>"
            "<b>Book 2:</b> Title: THG<br>"
            "Author: EXAMPLE AUTHOR 2<br>"
            "Genre: Dystopian<br><br>"
            "<b>Book 3:</b> Title: Classical music<br>"
            "Author: EXAMPLE AUTHOR 3 <br>"
            "Genre: Classic<br><br>"
            "<b>Book 4:</b> Title: To Kill a Mockingbird<br>"
            "Author: EXAMPLE AUTHOR 4<br>"
            "Genre: Fiction<br><br>"
            "<b>Book 5:</b> Title: Moana<br>"
            "Author: EXAMPLE AUTHOR 5<br>"
            "Genre: Sci-Fi<br>"
        )
        self.recommendations_area.setHtml(recommended_text)
        self.tabs.setCurrentIndex(2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryUI()
    window.show()
    sys.exit(app.exec())
