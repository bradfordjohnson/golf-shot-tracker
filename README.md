# Golf shot tracker

## Design

### Functional requirements

#### 1. Shot Tracking and Analysis

- **Track Shot Distances**: Allow users to record and compare shot distances between different clubs, shots and users.

#### 2. Club Management

- **Store and Manage Club Information**: Enable users to add, edit, and delete detailed club information.

#### 3. Quick Shot Entry

- **Minimal Input**: Provide a quick shot entry with pre-populated fields based on context and repeat entry for efficiency.

#### 4. Data Analysis and Reporting

- **Shot Statistics**: Offer statistical analysis of shots, including average distance, accuracy, and club usage.
- **Performance Tracking**: Allow users to monitor their performance trends over time.

#### 5. Data Management

- **Data Validation**: Implement validation to ensure accurate and consistent data input.
- **Storage**: Utilize SQLite for local file database storage.

#### 6. User Interface

- **UI Components**: Implement the user interface using Bootstrap for responsive design and custom UI elements to enhance usability and aesthetics.

#### 7. Technology Stack

- **Front End**: Web-based using React with D3 for data visualization.
- **Back End**: FastAPI with Python for robust backend services.

### Requirements Opportunities

- Adding user preferences (preferred units, measurement methods, etc.) to enhance user experience and cut down on data entry steps.

### Relational Data Model

#### **golfers** table

| Field        | Type   | Description                |
|--------------|--------|----------------------------|
| `id`         | int    | primary key                |
| `first_name` | string | first name of the golfer   |
| `last_name`  | string | last name of the golfer    |
| `handicap`   | float  | handicap of the golfer     |

#### **clubs** table

| Field            | Type   | Description                                  |
| ---------------- | ------ | -------------------------------------------- |
| `id`             | int    | primary key                                  |
| `golfer_id`      | int    | foreign key to `golfers.id`                  |
| `brand`          | string | brand name                                   |
| `model`          | string | club model                                   |
| `type`           | string | club type (e.g. driver, iron, wedge, putter) |
| `loft`           | int    | angle of the club face                       |
| `shaft_material` | string | shaft material                               |
| `shaft_flex`     | string | flexibility of the shaft                     |
| `length`         | int    | length of the club                           |
| `grip_type`      | string | type of grip                                 |

#### **shots** table

| Field               | Type     | Description                                           |
|---------------------|----------|-------------------------------------------------------|
| `id`                | int      | primary key                                           |
| `club_id`           | int      | foreign key to `clubs.id` (club used for the shot)    |
| `golfer_id`         | int      | foreign key to `golfers.id` (golfer who hit the shot) |
| `timestamp`         | datetime | timestamp of the shot observation                     |
| `location`          | string   | location of the shot (at the driving range, on the course) |
| `measurement_method`| string   | method used to measure the shot (GPS, laser rangefinder, course markers) |
| `unit`              | string   | unit of measurement (yards, meters)             |
| `distance`          | int      | distance of the shot                                  |
| `shot_type`         | string   | type of shot (drive, approach, chip)            |
| `notes`             | string   | additional notes about the shot                       |
