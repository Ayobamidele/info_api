# HNG12 Backend API

This is a public API developed for the HNG12 Stage 0 Backend task. It provides basic information such as your email, the current date and time in ISO 8601 format, and the GitHub URL of this repository.

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/Ayobmidele/info_api.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Find the `.env.sample` file. This file contains sample environment variable settings that you need to customize.

4. Open the `.env.sample` file in a text editor. Copy all the contents of the file.

5. In the same project directory, create a new file named `.env`.

6. Paste the contents you copied from `.env.sample` into your newly created `.env` file.

7. Replace the placeholder values with your own information. For example:

```env
   EMAIL=your-email@example.com
   GITHUB_URL=https://github.com/yourusername/your-repo
```

8. Run the API locally:

```bash
uvicorn main:app --reload
```

or

```bash
fastapi dev
```

## API Documentation

### Endpoint

**GET** `/api/v1/info`

### Response

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/Ayobamidele/info_api"
}
```

## Example Usage

Here’s an example of how to use the API:

![Info API](/assets/image.png)

This image shows how the API returns the expected JSON response when you make a `GET` request.

### Backlinks

- [Python Developers](https://hng.tech/hire/python-developers)
