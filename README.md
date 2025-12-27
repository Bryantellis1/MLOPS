# MLOps Challenges

This repository contains hands-on challenges for end-to-end machine learning operations (MLOps) with Azure Machine Learning.

## About This Repository

This is a learning repository that demonstrates how to implement DevOps principles when working with machine learning models. The challenges guide you through:

- Converting Jupyter notebooks to production code
- Creating Azure Machine Learning jobs
- Automating workflows with GitHub Actions
- Implementing CI/CD for ML models
- Managing environments and deployments

## Repository Structure

- **`documentation/`** - Challenge instructions and learning materials
- **`src/`** - Production-ready Python scripts for training ML models
- **`tests/`** - Unit tests for the training code
- **`experimentation/`** - Jupyter notebooks and experimental code
- **`production/`** - Production deployment configurations
- **`.github/workflows/`** - GitHub Actions workflows for automation
- **`_build.yml`** - Azure DevOps Pipeline for building and releasing lab materials

## Getting Started

To complete these challenges, you'll need:

1. A Microsoft Azure subscription ([sign up for free](https://azure.microsoft.com/))
2. A GitHub account
3. Basic knowledge of Python and machine learning concepts

Start with [Challenge 0: Convert a notebook to production code](documentation/00-script.md) and work through the challenges sequentially.

## Understanding the Build Pipeline

The `_build.yml` file contains an Azure DevOps Pipeline that automates the build and release process for this repository's documentation and lab files. This pipeline uses several **tasks** (reusable pipeline building blocks) to:

1. Build the markdown content using Node.js
2. Create a GitHub release with version tags
3. Publish artifacts to Azure DevOps

### What are Pipeline Tasks?

In Azure DevOps, a **task** is a packaged script or procedure defined with the `task:` keyword. For example:

```yaml
- task: Bash@3
  displayName: 'Build Content'
  inputs:
    targetType: inline
    script: |
      npm install
      node package.js
```

The `_build.yml` file uses three main task types:
- **`Bash@3`** - Executes bash scripts to build content
- **`GitHubRelease@0`** - Creates releases on GitHub with artifacts
- **`PublishBuildArtifacts@1`** - Publishes build outputs to Azure DevOps

For detailed information about how these tasks work and how to use them, see the [Azure DevOps Tasks Documentation](documentation/azure-devops-tasks.md).

## Challenges

The repository contains the following challenges:

| Module | Challenge |
| --- | --- |
| 0 | [Convert a notebook to production code](documentation/00-script.md) |
| 1 | [Create an Azure Machine Learning job](documentation/01-aml-job.md) |
| 2 | [Trigger Azure Machine Learning jobs with GitHub Actions](documentation/02-github-actions.md) |
| 3 | [Trigger workflows based on events](documentation/03-trigger-workflow.md) |
| 4 | [Add code quality checks with linting and unit testing](documentation/04-unit-test-linting.md) |
| 5 | [Manage environments for ML workflows](documentation/05-environments.md) |
| 6 | [Deploy and monitor models](documentation/06-deploy-model.md) |

## Additional Documentation

- [Azure DevOps Pipeline Tasks Explained](documentation/azure-devops-tasks.md) - Detailed explanation of the `task:` syntax used in `_build.yml`

## Contributing

This is a learning repository. To create your own version:

1. Click the "Use this template" button on GitHub
2. Create your own public repository
3. Follow the challenge instructions
4. Experiment and learn!

## Resources

- [Azure Machine Learning Documentation](https://docs.microsoft.com/azure/machine-learning/)
- [Azure DevOps Pipelines Documentation](https://docs.microsoft.com/azure/devops/pipelines/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)

## License

This repository is for educational purposes as part of Microsoft Learning content.
