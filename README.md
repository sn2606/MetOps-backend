<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sn2606/MetOps-backend">
    <img src="assets/cloud.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">MetOps</h3>

  <p align="center">
    MetOps is a state-of-the-art, fully integrated comprehensive solution presented as a substitute for the traditional MET stations used for field artillery atmospheric data collection.
    <br />
    <a href="https://github.com/sn2606/MetOps-backend"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/sn2606/MetOps-backend">View Demo</a>
    ·
    <a href="https://github.com/sn2606/MetOps-backend/issues">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This is a REST API backend for MetOps android application


<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [Django Rest Framework](https://www.django-rest-framework.org/)
* [Meteomatics](https://www.meteomatics.com/en/)
* [positionstack](https://positionstack.com/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

The `requirements.txt` file contains all the prerequisites for the project
* Make sure python is installed
* Create a python virtual environment for this project
  ```sh
  $ python3 -m venv /path/to/new/virtual/environment
  ```
* Activate the virtual environment
  ```sh
  $ source /path/to/new/virtual/environment/bin/activate
  ```
* Install pip in this virtual environment
  ```sh
  $ python -m ensurepip --upgrade
  ```

### Installation

1. Create a folder with the virtual environment activated
2. Clone the repo
   ```sh
   git clone https://github.com/sn2606/MetOps-backend.git
   ```
3. Install Python packages
   ```sh
   pip install -r requirements.txt
   ```
4. Create a database in PostgreSQL
5. Create a [Meteomatics](https://www.meteomatics.com/en/) account
6. Create a [positionstack](https://positionstack.com/) account
7. Create a .env file in the repository folder with following parameters
   ```env
   SECRET_KEY = ''
   DATABASE_NAME = ''
   DATABASE_USER = ''
   DATABASE_PWD = ''
   METOMATICS_UN = ''
   METEOMATICS_PWD = ''
   POSITIONSTACK_API_KEY = ''
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Backend to [this Flutter app](https://github.com/sn2606/MetOps-frontend)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Models
- [x] Database Connected (PostgreSQL)
- [x] DRF
    - [x] API View
    - [x] Authentication Register
    - [x] Authorization Login & Account View
    - [x] Query Response from external API (Meteomatics)
    - [x] Query & Records Save
    - [x] Query & Records View
    - [x] Query & Records Delete
    - [ ] Query & Response Export
- [ ] Current Location Weather on Dashboard


See the [open issues](https://github.com/sn2606/MetOps-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Swaranjana Nayak - swaranjananayak@gmail.com

Project Link: [https://github.com/sn2606/MetOps-backend](https://github.com/sn2606/MetOps-backend)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Django Rest Framework Tutorial](https://www.youtube.com/watch?v=c708Nf0cHrs&t=6568s)
* [Django Documentation](https://docs.djangoproject.com/en/4.1/)
* [Django Rest Framework Documentation](https://www.django-rest-framework.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/sn2606/MetOps-backend.svg?style=for-the-badge
[contributors-url]: https://github.com/sn2606/MetOps-backend/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/sn2606/MetOps-backend.svg?style=for-the-badge
[forks-url]: https://github.com/sn2606/MetOps-backend/network/members
[stars-shield]: https://img.shields.io/github/stars/sn2606/MetOps-backend.svg?style=for-the-badge
[stars-url]: https://github.com/sn2606/MetOps-backend/stargazers
[issues-shield]: https://img.shields.io/github/issues/sn2606/MetOps-backend.svg?style=for-the-badge
[issues-url]: https://github.com/sn2606/MetOps-backend/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/swaranjana
[product-screenshot]: assets/screenshot.png
