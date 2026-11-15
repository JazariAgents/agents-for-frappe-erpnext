<!-- Frappe documentation: insights, part 2 of 2. Index: docs/INDEX.md -->

<!-- page: insights/insights__querying__expressions.md -->
---
title: "Expressions"
space: "Insights"
url: "https://docs.frappe.io/insights/querying/expressions"
updated: "2026-01-06"
---

### Expressions

The expression/formula language in Insights is based on python syntax. The underlying library used for query building is `ibis`, you can check the documentation [here](https://ibis-project.org/tutorials/ibis-for-sql-users) to know more.

Following are the list of helper functions that make it easier to write expressions in Insights:

#### Aggregate Functions

1. Count
   - Syntax: `count(column)`
   - Description: Returns the count of non-null values in the column.
   - Example: `count(sales)`
   - Returns: 100

2. Count Distinct
   - Syntax: `distinct_count(column)`
   - Description: Returns the count of distinct values in the column.
   - Example: `distinct_count(customer_id)`
   - Returns: 50

3. Sum
   - Syntax: `sum(column)`
   - Description: Returns the sum of values in the column.
   - Example: `sum(sales)`
   - Returns: 10000

4. Average
   - Syntax: `avg(column)`
   - Description: Returns the average of values in the column.
   - Example: `avg(sales)`
   - Returns: 100

5. Minimum
	 - Syntax: `min(column)`
	 - Description: Returns the minimum value in the column.
	 - Example: `min(sales)`
	 - Returns: 50

6. Maximum
	 - Syntax: `max(column)`
	 - Description: Returns the maximum value in the column.
	 - Example: `max(sales)`
	 - Returns: 200

7. Group Concat
	 - Syntax: `group_concat(column)`
	 - Description: Concatenates the values in the column.
	 - Example: `group_concat(product_name)`
	 - Returns: "Product A, Product B, Product C"

8. Sum if
	 - Syntax: `sum_if(condition, column)`
	 - Description: Returns the sum of values in the column that satisfy the condition.
	 - Example: `sum_if(sales > 1000, sales)`
	 - Returns: 5000

9. Count if
	 - Syntax: `count_if(condition, column)`
	 - Description: Returns the count of values in the column that satisfy the condition.
	 - Example: `count_if(sales > 1000, sales)`
	 - Returns: 5

10. Distinct Count if
	 - Syntax: `distinct_count_if(condition, column)`
	 - Description: Returns the count of distinct values in the column that satisfy the condition.
	 - Example: `distinct_count_if(sales > 1000, customer_id)`
	 - Returns: 3

#### Conditional Functions

1. If Else
	 - Syntax: `if_else(condition, true_value, false_value)`
	 - Description: Returns the true_value if the condition is true, else returns the false_value.
	 - Example: `if_else(sales > 1000, "High", "Low")`
	 - Returns: "High"

2. Case
	 - Syntax: `case(condition1, value1, condition2, value2, ..., default_value)`
	 - Description: Returns the value corresponding to the first true condition. If no condition is true, returns the default_value.
	 - Example: `case(sales > 1000, "High", sales > 500, "Medium", "Low")`
	 - Returns: "High"

3. Coalesce
	 - Syntax: `coalesce(column1, column2, ..., default_value)`
	 - Description: Returns the first non-null value from the columns. If all columns are null, returns the default_value.
	 - Example: `coalesce(product_name, product_code, "Unknown")`
	 - Returns: "Product A"

#### String Functions

1. Lower
	 - Syntax: `lower(column)`
	 - Description: Converts the column values to lowercase.
	 - Example: `lower(product_name)`
	 - Returns: "product a"

2. Upper
	 - Syntax: `upper(column)`
	 - Description: Converts the column values to uppercase.
	 - Example: `upper(product_name)`
	 - Returns: "PRODUCT A"

3. Concat
	 - Syntax: `concat(column1, column2, ..., separator)`
	 - Description: Concatenates the columns with the separator.
	 - Example: `concat(first_name, last_name, " ")`
	 - Returns: "John Doe"

4. Replace
	 - Syntax: `replace(column, old_value, new_value)`
	 - Description: Replaces the old_value with the new_value in the column.
	 - Example: `replace(product_name, "A", "B")`
	 - Returns: "Product B"

5. Substring
	 - Syntax: `substring(column, start, length)`
	 - Description: Returns a substring of the column starting from the start index with the specified length.
	 - Example: `substring(product_name, 0, 7)`
	 - Returns: "Product"

6. Contains
	 - Syntax: `contains(column, substring)`
	 - Description: Returns true if the column contains the substring, else false.
	 - Example: `contains(product_name, "Product")`
	 - Returns: True

7. Not Contains
	 - Syntax: `not_contains(column, substring)`
	 - Description: Returns true if the column does not contain the substring, else false.
	 - Example: `not_contains(product_name, "A")`
	 - Returns: False

8. Starts With
	 - Syntax: `starts_with(column, prefix)`
	 - Description: Returns true if the column starts with the prefix, else false.
	 - Example: `starts_with(product_name, "Product")`
	 - Returns: True

9. Ends With
	 - Syntax: `ends_with(column, suffix)`
	 - Description: Returns true if the column ends with the suffix, else false.
	 - Example: `ends_with(product_name, "A")`
	 - Returns: True

10. Length
	 - Syntax: `length(column)`
	 - Description: Returns the length of the column.
	 - Example: `length(product_name)`
	 - Returns: 10

#### Numeric Functions

1. Abs
	 - Syntax: `abs(column)`
	 - Description: Returns the absolute value of the column.
	 - Example: `abs(sales)`
	 - Returns: 100

2. Round
	 - Syntax: `round(column, decimals)`
	 - Description: Rounds the column to the specified number of decimals.
	 - Example: `round(sales, 2)`
	 - Returns: 100.50

3. Floor
	 - Syntax: `floor(column)`
	 - Description: Returns the largest integer less than or equal to the column.
	 - Example: `floor(sales)`
	 - Returns: 100

4. Ceil
	 - Syntax: `ceil(column)`
	 - Description: Returns the smallest integer greater than or equal to the column.
	 - Example: `ceil(sales)`
	 - Returns: 101


#### Date Functions

1. Year
	 - Syntax: `year(column)`
	 - Description: Returns the year part of the date column.
	 - Example: `year(order_date)`
	 - Returns: 2022

2. Quarter
	 - Syntax: `quarter(column)`
	 - Description: Returns the quarter part of the date column.
	 - Example: `quarter(order_date)`
	 - Returns: 3

3. Month
	 - Syntax: `month(column)`
	 - Description: Returns the month part of the date column.
	 - Example: `month(order_date)`
	 - Returns: 10

4. Week of Year
	 - Syntax: `week_of_year(column)`
	 - Description: Returns the week of the year of the date column.
	 - Example: `week_of_year(order_date)`
	 - Returns: 41

5. Day of Year
	 - Syntax: `day_of_year(column)`
	 - Description: Returns the day of the year of the date column.
	 - Example: `day_of_year(order_date)`
	 - Returns: 288

6. Day of Week
	 - Syntax: `day_of_week(column)`
	 - Description: Returns the day of the week (0-6) of the date column.
	 - Example: `day_of_week(order_date)`
	 - Returns: 4

7. Day
	 - Syntax: `day(column)`
	 - Description: Returns the day part of the date column.
	 - Example: `day(order_date)`
	 - Returns: 15

8. Hour
	 - Syntax: `hour(column)`
	 - Description: Returns the hour part of the date column.
	 - Example: `hour(order_date)`
	 - Returns: 10

9. Minute
	 - Syntax: `minute(column)`
	 - Description: Returns the minute part of the date column.
	 - Example: `minute(order_date)`
	 - Returns: 30

10. Second
	 - Syntax: `second(column)`
	 - Description: Returns the second part of the date column.
	 - Example: `second(order_date)`
	 - Returns: 45

11. Microsecond
	 - Syntax: `microsecond(column)`
	 - Description: Returns the microsecond part of the date column.
	 - Example: `microsecond(order_date)`
	 - Returns: 500000

12. Date Diff
	 - Syntax: `date_diff(column1, column2, unit)`
	 - Description: Returns the difference between two date columns in the specified unit. Units can be "year", "quarter", "month", "week", "day", "hour", "minute", "second", "millisecond", "microsecond", "nanosecond".
	 - Example: `date_diff(order_date, delivery_date, "day")`
	 - Returns: 5

13. Format Date
	 - Syntax: `format_date(column, format)`
	 - Description: Formats the date column according to the specified format. The format should be a valid ANSI `strftime` format.
	 - Example: `format_date(order_date, "%Y-%m-%d")`
	 - Returns: "2022-10-15"

15. Now
	 - Syntax: `now()`
	 - Description: Returns the current date and time.
	 - Example: `now()`
	 - Returns: "2022-10-15 10:30:00"

16. Today
	 - Syntax: `today()`
	 - Description: Returns the current date.
	 - Example: `today()`
	 - Returns: "2022-10-15"



#### Boolean Functions

1. Is in
	 - Syntax: `is_in(column, value1, value2, ...)`
	 - Description: Returns true if the column value is in the list of values, else false.
	 - Example: `is_in(product_name, "Product A", "Product B")`
	 - Returns: True

2. Is Not in
	 - Syntax: `is_not_in(column, value1, value2, ...)`
	 - Description: Returns true if the column value is not in the list of values, else false.
	 - Example: `is_not_in(product_name, "Product A", "Product B")`
	 - Returns: False

3. Is Set
	 - Syntax: `is_set(column)`
	 - Description: Returns true if the column value is not null, else false.
	 - Example: `is_set(product_name)`
	 - Returns: True

4. Is Not Set
	 - Syntax: `is_not_set(column)`
	 - Description: Returns true if the column value is null, else false.
	 - Example: `is_not_set(product_name)`
	 - Returns: False

5. Is Between
	 - Syntax: `is_between(column, start, end)`
	 - Description: Returns true if the column value is between the start and end values, else false.
	 - Example: `is_between(sales, 1000, 5000)`
	 - Returns: True

6. Is Not Between
	 - Syntax: `is_not_between(column, start, end)`
	 - Description: Returns true if the column value is not between the start and end values, else false.
	 - Example: `is_not_between(sales, 1000, 5000)`
	 - Returns: False


#### Utility Functions

1. USD to INR
	 - Syntax: `to_inr(currency_column, amount_column, rate=83)`
	 - Description: Converts the values in the amount column from USD to INR based on the rate. If the currency is not USD, the amount is returned as is. Default rate is 83.
	 - Example: `to_inr(currency, amount, 83)`
	 - Returns: 8300

2. INR to USD
	 - Syntax: `to_usd(currency_column, amount_column, rate=83)`
	 - Description: Converts the values in the amount column from INR to USD based on the rate. If the currency is not INR, the amount is returned as is. Default rate is 83.
	 - Example: `to_usd(currency, amount, 83)`
	 - Returns: 100

3. Row Number
	 - Syntax: `row_number()`
	 - Description: Returns the row number of the current row.
	 - Example: `row_number()`
	 - Returns: 1

4. Previous Period Value
	 - Syntax: `previous_period_value(column, date_column, offset=1)`
	 - Description: Returns the value of the column for the previous period based on the date column. Offset specifies the number of periods to go back.
	 - Example: `previous_period_value(sales, order_date, 1)`
	 - Returns: 1000

5. Next Period Value
	 - Syntax: `next_period_value(column, date_column, offset=1)`
	 - Description: Returns the value of the column for the next period based on the date column. Offset specifies the number of periods to go forward.
	 - Example: `next_period_value(sales, order_date, 1)`
	 - Returns: 2000

6. Percentage Change
	 - Syntax: `percentage_change(column, date_column, offset=1)`
	 - Description: Returns the percentage change in the value of the column compared to the previous period based on the date column. Offset specifies the number of periods to go back.
	 - Example: `percentage_change(sales, order_date, 1)`
	 - Returns: 10

7. Is First Row
	 - Syntax: `is_first_row(group_by, order_by, sort_order="asc")`
	 - Description: Returns 1 if the current row is the first row in the group, else 0. Sort order can be "asc" or "desc".
	 - Example: `is_first_row(customer_id, order_date, "asc")`
	 - Returns: 1

8. Create Buckets
	 - Syntax: `create_buckets(column, num_buckets)`
	 - Description: Creates buckets based on the values in the column. The number of buckets specifies the number of buckets to create.
	 - Example: `create_buckets(sales, 5)`
	 - Returns: "1000-2000"

<!-- page: insights/insights__querying__operations.md -->
---
title: "Operations"
space: "Insights"
url: "https://docs.frappe.io/insights/querying/operations"
updated: "2026-01-06"
---

## Common Operations
 
 
[Screenshot on the live page: operations list]
 
### Choose Columns

  What it does: Select which columns you want to include in your results. This helps focus your analysis on the data
  that matters.

##### When to use it
  
  - You only need specific columns from a table
  - You want to hide unnecessary columns to simplify your results
  - You need to improve query performance by reducing data volume

##### How it works
  
  From your available columns, select only those you want to see in your results. All other columns will be hidden.

##### Example
  
  From a Customer table with 20 columns, select only "Customer Name", "Email", "Region", and "Total Orders" for a
  customer contact list.

##### Tips
  
  - Use this operation early in your query to improve performance
  - Fewer columns means faster queries
  - You can add columns back later if needed

### Filter Rows


[Screenshot on the live page: filter operation]

  What it does: Show only the rows that match specific conditions. This helps you focus on relevant data.

####  When to use it:
  
  - You want to analyze a specific time period
  - You need data for a particular region or category
  - You want to exclude certain values (like cancelled orders)
  - You need to remove incomplete or invalid data

####  Available filter types

##### Comparison Filters
  
  - Equals: Exact match
  - Does not equal: Exclude specific values
  - Greater than / Less than: For numbers and dates
  - Greater than or equal to / Less than or equal to: Include boundary values


##### List Filters
  
  - In: Match any value in a list (e.g., "New York", "Los Angeles", "Chicago")
  - Not in: Exclude values in a list


##### Text Filters
  
  - Contains: Find text anywhere in the column
  - Does not contain: Exclude text
  - Starts with: Match beginning of text
  - Ends with: Match end of text

 
#####  Special Filters
  
  - Is set: Has a value (not empty)
  - Is not set: Is empty or null
  - Between: Value falls within a range
  - Within: For relative date ranges (last 7 days, last month, etc.)


  How it works
  You can combine multiple filters using:
  
  - And: All conditions must be true
  - Or: Any condition can be true


##### Examples
  

  - Show orders from the last 30 days
  - Display sales from "North" and "South" regions only
  - Exclude cancelled orders
  - Show customers with email addresses

#####  Tips
 
 - Apply filters early in your query for better performance
  - Use "within" for dynamic date filtering (always shows last 7 days, etc.)
  - Combine multiple filters to create precise conditions

### Join Table

  What it does: Combine data from two tables based on matching values in specific columns. This lets you bring related
   information together.

#### When to use it
  
  - You need information from multiple tables
  - You want to enrich your data with additional details
  - You need to combine related datasets

####  Join types explained

##### Inner Join
  
  - Shows only rows that have matches in both tables
  - Use when you only want complete data
  - Example: Show orders with customer details (only for orders that have a customer)

##### Left Join
  
  - Shows all rows from your current table, plus matching rows from the joined table
  - Use when you want to keep all your original data
  - Example: Show all customers, including those who haven't placed orders yet

##### Right Join
  
  - Shows all rows from the joined table, plus matching rows from your current table
  - Less commonly used than Left Join
  - Example: Show all products, including those that haven't been ordered

##### Full Join
  
  - Shows all rows from both tables, whether they match or not
  - Use when you need comprehensive data from both sides
  - Example: Show all customers and all orders, even if some don't match

##### How it works
  
  1. Select the table you want to join with
  2. Choose the join type
  3. Specify which columns should match between the tables
  4. Select which columns from the joined table you want to include

##### Example

  Join your "Orders" table with a "Customers" table using "Customer ID" to show customer names and contact information
   alongside order details.

##### Tips
  
  - Most common join type is Left Join
  - Join columns should contain matching values (like IDs)
  - Select only the columns you need from the joined table
  - If column names conflict, they will be automatically renamed

###  Append Table

  What it does: Stack rows from another table below your current data. This combines datasets vertically.

#####  When to use it
  
  - You want to combine data from multiple time periods
  - You need to merge data from different regions or locations
  - You have similar data in separate tables that should be analyzed together

##### How it works
  
  1. Select the table to append
  2. Choose whether to remove duplicate rows
  3. Only columns that exist in both tables will be included

##### Options
  
  - Include duplicates: Keep all rows, even if they're identical
  - Remove duplicates: Show each unique row only once

  Example:
  Combine "Q1 Sales" and "Q2 Sales" tables to analyze sales for the first half of the year.

##### Tips
  
  - Both tables must have at least one column with the same name
  - Only matching columns appear in the results
  - Column types are automatically aligned
  - Use "Remove duplicates" if you think there might be overlapping data

### Add New Column

  What it does: Create a new calculated column based on your existing columns using formulas or expressions.

##### When to use it
  
  - You need to perform calculations on your data
  - You want to create derived metrics
  - You need to combine information from multiple columns

##### Common calculations
  
  - Math operations: Add, subtract, multiply, divide
  - Percentages: (part / total) * 100
  - Profit calculations: revenue - cost
  - Text combinations: Combine first and last names
  - Conditional logic: Different values based on conditions

##### How it works
  
  1. Give your new column a name
  2. Choose the data type (Number, Text, Date, etc.)
  3. Enter your formula using existing column names

####  Examples
  
  - Calculate profit: revenue - cost
  - Find profit margin percentage: (profit / revenue) * 100
  - Calculate order total: quantity * unit_price
  - Combine text: first_name + " " + last_name

####  Tips
  
  - Use clear, descriptive names for your calculated columns
  - Make sure columns are the correct data type before calculating
  - Test your formulas with a small sample first
  - You can reference columns by their names in your formulas

### Group & Summarize

  What it does: Group your data by categories and calculate summary statistics like totals, averages, and counts.

##### When to use it
  
  - You want to see totals by category (sales by region, orders by product)
  - You need to calculate averages or other statistics
  - You want to analyze trends over time
  - You need to create aggregated reports

##### Summary functions

  Sum: Add up all values
  
  - Example: Total sales, total quantity

  Count: Count the number of rows
  - Example: Number of orders, number of customers

  Count Distinct: Count unique values only
  - Example: Number of unique customers, number of different products

  Average: Calculate the mean value
  - Example: Average order value, average age

  Minimum: Find the smallest value
  - Example: Lowest price, earliest date

  Maximum: Find the largest value
  - Example: Highest price, most recent date

##### How it works
  
  1. Choose dimensions (what to group by): Categories like Region, Product, Date
  2. Choose measures (what to calculate): Metrics like Total Sales, Average Price, Order Count
  3. Results show one row per unique combination of dimensions

  Time-based grouping:
  When grouping by dates, you can choose the time period:
  
  - Second, Minute, Hour (for detailed timestamps)
  - Day (daily analysis)
  - Week (weekly summaries)
  - Month (monthly trends)
  - Quarter (quarterly reports)
  - Year (yearly comparisons)

##### Examples
  
  - Total sales by region: Group by "Region", Sum of "Sales Amount"
  - Average order value by product: Group by "Product Name", Average of "Order Value"
  - Monthly revenue: Group by "Order Date" (by Month), Sum of "Revenue"
  - Customer count by city: Group by "City", Count of "Customer ID"

##### Tips
  
  - You can group by multiple dimensions (e.g., Region and Product)
  - You can calculate multiple measures (e.g., Total Sales and Average Price)
  - Use descriptive names for your measures
  - For dates, choose the right time granularity for your analysis
  - This operation enables drill-down features in charts
 
### Custom Operation

  What it does: Apply advanced transformations using custom Python expressions. This is for advanced users who need
  operations beyond the standard options.

#####  When to use it
  
  - You need transformations not available in other operations
  - You have complex business logic to implement
  - You need advanced data manipulation
  - You're comfortable with Python programming

#####  What you can do
  
  - Access all your columns as variables
  - Use Python expressions to transform data
  - Apply complex conditional logic
  - Perform advanced calculations

##### Example
  Create ranking or apply windowing functions that aren't available through the standard operations.

  Important notes:
  
  - Requires knowledge of Python and data manipulation
  - Use only when standard operations don't meet your needs
  - Test carefully before applying to large datasets
  - The expression must return a valid data table

<!-- page: insights/insights__querying__overview.md -->
---
title: "Overview"
space: "Insights"
url: "https://docs.frappe.io/insights/querying/overview"
updated: "2026-01-06"
---

## What are Queries?

Queries let you fetch and transform data from your databases. Think of a query as a recipe for getting the exact data you need. You start with a table then add steps to filter, calculate, and organize the data.

Insights offers three ways to build queries:

  1. Query Builder  Visual, no-code interface (recommended for most users)
  2. SQL Editor  Write SQL directly (for SQL experts)
  3. Script Editor  Python scripts for complex transformations

## Creating Your First Query


[Video on the live page]
### Start a New Query
####  1. Open your workbook

1. Click the Queries tab
2. Click New Query
3. Choose your query type:
    * Visual Query Builder  -> Build visually
    * SQL Editor  -> Write SQL
    * Script Editor  -> Write Python

[Screenshot on the live page: Query Builder]

 We'll focus on the Query Builder since it's the easiest to get started with.

####  2. Select Your Data Source

  1. Click Select a table
  2. Choose your database connection
  3. Pick a table to start with

[Screenshot on the live page: select table]

You can select a table from:

* Demo Data
* Site DB
* Uploads
* Other Queries in the WorkBook

Now you're ready to perform operations on the table

<!-- page: insights/insights__querying__script-query-api.md -->
---
title: "Script Query API"
space: "Insights"
url: "https://docs.frappe.io/insights/querying/script-query-api"
updated: "2026-08-31"
---

A script query runs Python through Frappe's `safe_exec`, the Server Script sandbox. Set `"server_script_enabled": 1` in `common_site_config.json` to enable it.

A script query is read-only. Any database change made by the script is rolled back after the run.

## Insights


| Class      | APIs                                                                                                      |
| ---------- | --------------------------------------------------------------------------------------------------------- |
| Output     | `results` — the rows to return. Starts as `[]`. Takes a list of dicts, a list of lists, or a `DataFrame`. |
| Dataframes | `pandas.DataFrame`, `pandas.read_csv`, `pandas.json_normalize`                                            |
| Variables  | One name per query variable, added from **⋯ → Variables**. Always a string.                               |
| Logs       | `print()` — writes to **⋯ → Logs**, with the row count, the run time and any error line.                  |


## Frappe


| Class         | APIs                                                                                                 |
| ------------- | ---------------------------------------------------------------------------------------------------- |
| Documents     | `frappe.get_doc`, `get_cached_doc`, `get_last_doc`, `get_meta`                                       |
| Database      | `frappe.db.get_list`, `get_all`, `get_value`, `get_single_value`, `exists`, `count`, `sql`, `escape` |
| Query builder | `frappe.qb`                                                                                          |
| HTTP          | `frappe.make_get_request`                                                                            |
| Errors        | `frappe.throw`, `frappe.log_error`                                                                   |
| Session       | `frappe.session.user`, `frappe.user`, `frappe.lang`                                                  |
| Settings      | `frappe.get_system_settings`                                                                         |


## `frappe.utils`


| Class      | APIs                                                                                                                                                                                                                    |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dates      | `getdate`, `get_datetime`, `now`, `now_datetime`, `nowdate`, `today`, `add_days`, `add_months`, `add_years`, `add_to_date`, `date_diff`, `month_diff`, `time_diff_in_seconds`, `time_diff_in_hours`                     |
| Periods    | `get_first_day`, `get_last_day`, `get_first_day_of_week`, `get_last_day_of_week`, `get_quarter_start`, `get_quarter_ending`, `get_year_start`, `get_year_ending`, `get_weekday`, `get_month`, `get_timespan_date_range` |
| Time zones | `get_system_timezone`, `convert_utc_to_system_timezone`, `get_datetime_in_timezone`                                                                                                                                     |
| Numbers    | `flt`, `cint`, `cstr`, `floor`, `ceil`, `rounded`, `safe_div`                                                                                                                                                           |
| Strings    | `strip`, `strip_html`, `unique`                                                                                                                                                                                         |
| JSON       | `parse_json`                                                                                                                                                                                                            |


## Python


| Class     | APIs                                                                                                                                                                         |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Built-ins | `abs`, `all`, `any`, `bool`, `dict`, `enumerate`, `isinstance`, `list`, `max`, `min`, `range`, `set`, `sorted`, `sum`, `tuple`, `len`, `str`, `int`, `float`, `round`, `zip` |
| JSON      | `json.loads`, `json.dumps`, `as_json`, `_dict`                                                                                                                               |


## Notes

- This page lists the common APIs. All read APIs from the framework's Server Script sandbox are also available — see the [Server Script API docs](https://docs.frappe.io/framework/user/en/desk/scripting/script-api).
- `frappe.db.sql` runs `select` and `explain` only.
- Results are cached for 5 minutes. The cache key includes the code, the variable values and the runtime filters. Use **Force Run** to skip the cache.

## Example

```python
results = frappe.db.get_all(
    "Sales Order",
    filters={"docstatus": 1},
    fields=["customer", "transaction_date", "grand_total"],
    limit_page_length=0,
)
```

From an external API:

```python
payload = frappe.make_get_request("https://api.example.com/v1/rates")
results = pandas.json_normalize(payload["rates"])
```
