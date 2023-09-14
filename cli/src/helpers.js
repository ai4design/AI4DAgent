import chalk from "chalk";
import figlet from "figlet";

export const printTitle = () => {
  console.log(
    chalk.red(
      figlet.textSync("AI4DAgent", {
        horizontalLayout: "full",
        font: "ANSI Shadow",
      })
    )
  );
  console.log(
    "Welcome to the AI4DAgent CLI! This CLI will generate the required .env files."
  );
  console.log(
    "Copies of the generated envs will be created in `./next/.env` and `./platform/.env`.\n"
  );
};

// Function to check if entered api key is in the correct format or empty
export const isValidKey = (apikey, pattern) => {
  return (apikey === "" || pattern.test(apikey))
};

export const validKeyErrorMessage = "\nInvalid api key. Please try again."
