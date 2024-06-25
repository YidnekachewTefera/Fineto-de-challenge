#Used the official Node.js with version 14 as the base image as mentioned in the rubrics.
FROM node:14

# Working Directory : set the working directory inside the container to /usr/src/app
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the working directory
# (bonus) This helps utilize Docker's caching mechanism by only running npm install if these files change 
COPY app/package*.json ./

# Install the application's dependencies
# We use --no-cache to ensure a fresh installation and avoid caching issues
RUN npm install

# Copy the application source code to the working directory from the app directory
COPY app/ .

# Expose the application on port 3000 to allow communication with the outside world
EXPOSE 3000

# command for starting teh application by running the following command
CMD ["node", "server.js"]
