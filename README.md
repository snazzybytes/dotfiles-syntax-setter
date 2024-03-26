[![License: MIT](https://img.shields.io/badge/License-MIT-orange.svg)](https://opensource.org/licenses/MIT)

# Dotfiles Syntax Setter for Sublime Text

This Sublime Text plugin automatically sets the syntax highlighting to Bash for all open dotfiles, enhancing the editing experience for Unix and Linux configuration files. It intelligently excludes certain files where Bash syntax is inappropriate, based on a configurable list of exclusions (in some instances known dotfiles are specified in INI, YAML, JSON and other formats).

## Features

- **Automatic Syntax Detection**: Applies Bash syntax highlighting to dotfiles upon opening.
- **Configurable Exclusions**: Customize the list of files to exclude from automatic syntax setting.

## Installation

Currently, you need to manually install the plugin by cloning or downloading the repository into your Sublime Text's `Packages` directory.\
Future updates may include Package Control installation (once PR gets merged).

1. Clone the repo into your Sublime Text `Packages` directory:
   ```bash
   git clone https://github.com/snazzybytes/dotfiles-syntax-setter.git

## Configuration
By default, the plugin excludes certain files from being automatically set to Bash syntax. You can customize this list by editing the DotfilesSyntaxSetter.sublime-settings file, located in the User package directory.

## Default Excluded Files
The default configuration excludes the following files:

- Configuration files for version control systems (e.g., .gitignore, .gitconfig)
- Editor configuration files (e.g., .editorconfig, .vscode)
- Programming language and environment version managers (e.g., .ruby-version, .nvmrc)
- Linter and formatter configurations (e.g., .eslintrc, .prettierrc)
- Continuous Integration and Continuous Deployment configurations (e.g., .travis.yml, .gitlab-ci.yml)
- Cloud provider CLI configurations (e.g., .gcloud)

## Customizing Exclusions
To customize the list of excluded files, create or edit the DotfilesSyntaxSetter.sublime-settings file in your User directory:

- Open Sublime Text.
- Go to Preferences > Browse Packages... and navigate to the User directory.
- Create or edit `DotfilesSyntaxSetter.sublime-settings` and adjust the excluded_files array as needed.

Example customization:
```json
{
  "excluded_files": [
    ".gitignore",
    ".gitconfig",
    ".dockerignore",
    // Add or remove files as needed
  ]
}
```

## List of files excluded by default:

- `.gitignore` : Specifies intentionally untracked files to ignore for Git.
- `.gitignore_global` : Global gitignore file for ignoring files across all repositories for a user.
- `.gitconfig` : Contains global configurations for Git.
- `.gitattributes` : Defines attributes per path, such as text file line endings for Git.
- `.hgignore` : Specifies patterns to ignore when adding files for Mercurial.
- `.editorconfig` : Helps maintain consistent coding styles across different editors and IDEs.
- `.vscode` : Configuration files for workspace settings, extensions, etc., in Visual Studio Code.
- `.sublime-settings` : Contains configuration settings specific to Sublime Text.
- `.sublime-keymap` : Key bindings configuration for Sublime Text.
- `.ideavimrc` : Configuration file for the IdeaVim plugin in JetBrains IDEs.
- `.ruby-version` : Specifies the Ruby version for a project for version managers like rbenv, RVM.
- `.rvmrc` : Project-specific configuration file for RVM (Ruby Version Manager).
- `.node-version` : Specifies the Node.js version for a project for node version managers like nvm, nodenv.
- `.nvmrc` : Specifies Node.js version to use with nvm (Node Version Manager).
- `.pylintrc` : Configuration for the Python linter pylint.
- `.eslintrc` : Configuration file for ESLint, a JavaScript linter.
- `.eslintrc.js` : JavaScript file defining ESLint rules.
- `.eslintrc.json` : JSON file defining ESLint rules.
- `.prettierrc` : Configuration file for the code formatter Prettier.
- `.npmrc` : Configuration file for npm, can specify registry, auth, and other settings.
- `.yarnrc` : Configuration file for Yarn, specifying registry, resolutions, etc.
- `.yarnrc.yml` : Yarn configuration in YAML format for Yarn 2+.
- `.gemrc` : Configuration file for RubyGems.
- `.env` : Typically used to define environment variables for development.
- `.env.local` : Local overrides for `.env` configurations.
- `.env.production` : Production-specific environment variables.
- `.env.development` : Development-specific environment variables.
- `.dockerignore` : Specifies files and directories to ignore in Docker build contexts.
- `.browserslistrc` : Configuration file to specify target browsers for frontend tools.
- `.htaccess` : Configuration file for directory-level configuration in Apache HTTP Server.
- `.bash_history` : Stores the command history for Bash.
- `.zsh_history` : Stores the command history for Zsh.
- `.bash_logout` : Executes commands upon logging out of Bash.
- `.zlogout` : Executes commands upon logging out of Zsh.
- `.terraformignore` : Specifies files to ignore when creating an archive for Terraform Cloud.
- `.tfvars` : Variable files for Terraform configurations.
- `.tfstate` : Contains state information for Terraform-managed infrastructure.
- `.tfstate.backup` : Backup of the previous Terraform state.
- `.helmignore` : Specifies patterns to ignore when packaging Helm charts.
- `.databrickscfg` : Configuration file for the Databricks CLI.
- `.gcloud` : Configuration directory for the Google Cloud CLI.
- `.circleci` : Configuration for CircleCI for CI/CD pipelines.
- `.travis.yml` : Configuration file for Travis CI.
- `.appveyor.yml` : CI/CD configuration for AppVeyor.
- `.gitlab-ci.yml` : Configuration for GitLab's CI/CD features.
- `.codecov.yml` : Configuration file for Codecov integration.
- `.codeclimate.yml` : Configuration file for Code Climate analysis.


## Contributing
Contributions to the Dotfiles Syntax Setter are welcome! Whether it's adding new features, expanding excluded files list, improving existing functionality, or reporting issues, your input is valuable. Please feel free to submit pull requests or open issues on GitHub.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.