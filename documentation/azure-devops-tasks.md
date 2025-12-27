---
title: Understanding Azure DevOps Pipeline Tasks
permalink: documentation/azure-devops-tasks.html
layout: home
---

<style>
.button  {
  border: none;
  color: white;
  padding: 12px 28px;
  background-color: #008CBA;
  float: right;
}
</style>

# Understanding Azure DevOps Pipeline Tasks

<button class="button" onclick="window.location.href='https://microsoftlearning.github.io/mslearn-mlops/';">Back to overview</button>

## Overview

This document explains the Azure DevOps Pipeline tasks used in the `_build.yml` file and how to use them for automating the build and release process of this MLOps project.

## What is a Pipeline Task?

In Azure DevOps Pipelines, a **task** is a packaged script or procedure that performs a specific action. Tasks are the building blocks of your CI/CD pipeline. Each task is defined using the `task:` keyword followed by the task name and version number (e.g., `task: Bash@3`).

### Task Syntax

```yaml
- task: TaskName@Version
  displayName: 'Human-Readable Description'
  inputs:
    parameter1: value1
    parameter2: value2
```

- **TaskName@Version**: The name of the task and its version (e.g., `Bash@3` means Bash task version 3)
- **displayName**: A friendly name that appears in the pipeline logs
- **inputs**: Configuration parameters specific to each task

## Tasks Used in `_build.yml`

The `_build.yml` file in this repository uses three main tasks to build, release, and publish the MLOps documentation and lab files.

### 1. Bash@3 Task

**Purpose**: Executes bash scripts within the pipeline.

**Usage in this project**:
```yaml
- task: Bash@3
  displayName: 'Build Content'
  inputs:
    targetType: inline
    script: |
      cp /{attribution.md,template.docx,package.json,package.js} .
      npm install
      node package.js --version $(Build.BuildNumber)
```

**Key Parameters**:
- `targetType: inline` - The script is provided inline (as opposed to a file path)
- `script: |` - The multiline bash script to execute

**What it does**: 
1. Copies necessary files from the container's root directory
2. Installs npm dependencies
3. Runs the `package.js` script to build the documentation with the build number

### 2. GitHubRelease@0 Task

**Purpose**: Creates a release on GitHub with artifacts.

**Usage in this project**:
```yaml
- task: GitHubRelease@0
  displayName: 'Create GitHub Release'
  inputs:
    gitHubConnection: 'github-microsoftlearning-organization'
    repositoryName: '$(Build.Repository.Name)'
    tagSource: manual
    tag: 'v$(Build.BuildNumber)'
    title: 'Version $(Build.BuildNumber)'
    releaseNotesSource: input
    releaseNotes: '# Version $(Build.BuildNumber) Release'
    assets: '$(Build.SourcesDirectory)/out/*.zip'
    assetUploadMode: replace
```

**Key Parameters**:
- `gitHubConnection` - The GitHub service connection configured in Azure DevOps
- `repositoryName` - The target GitHub repository (uses built-in variable)
- `tagSource` - How to determine the release tag (manual vs. automatic)
- `tag` - The Git tag for the release
- `title` - The release title displayed on GitHub
- `releaseNotes` - The description/notes for the release
- `assets` - The files to upload (supports wildcards)
- `assetUploadMode` - How to handle existing assets (replace or fail)

**What it does**: Creates a GitHub release with a version tag and uploads the built lab files as release assets.

### 3. PublishBuildArtifacts@1 Task

**Purpose**: Publishes build artifacts to Azure DevOps so they can be downloaded or used in other pipelines.

**Usage in this project**:
```yaml
- task: PublishBuildArtifacts@1
  displayName: 'Publish Output Files'
  inputs:
    pathtoPublish: '$(Build.SourcesDirectory)/out/'
    artifactName: 'Lab Files'
```

**Key Parameters**:
- `pathtoPublish` - The path to the directory or file to publish
- `artifactName` - The name of the artifact (used to reference it later)

**What it does**: Makes the built lab files available as a pipeline artifact named "Lab Files" that can be downloaded from Azure DevOps.

## Pipeline Variables

The tasks use Azure DevOps built-in variables:

- `$(Build.BuildNumber)` - The build number (defined as `'$(Date:yyyyMMdd)$(Rev:.rr)'` at the top of the file)
- `$(Build.Repository.Name)` - The name of the repository
- `$(Build.SourcesDirectory)` - The root directory of the source code

## How to Use This Pipeline

### Prerequisites

1. An Azure DevOps organization and project
2. A GitHub repository with this code
3. A GitHub service connection configured in Azure DevOps named `github-microsoftlearning-organization`

### Running the Pipeline

1. **Import the pipeline**: In Azure DevOps, create a new pipeline and point it to the `_build.yml` file
2. **Configure service connections**: Ensure the GitHub service connection is properly set up
3. **Run the pipeline**: Trigger the pipeline manually or configure triggers (push, PR, scheduled)
4. **Monitor execution**: View the logs in Azure DevOps to see each task's progress
5. **Download artifacts**: After successful completion, download artifacts from the pipeline run summary

### Customizing Tasks

To modify a task:

1. **Change task inputs**: Update the values under the `inputs:` section
2. **Add new tasks**: Insert additional `- task:` blocks in the `steps:` section
3. **Reorder tasks**: Move task blocks up or down (be mindful of dependencies)
4. **Update versions**: Change the version number (e.g., `Bash@3` to `Bash@4`) if needed

### Example: Adding a New Task

```yaml
- task: PowerShell@2
  displayName: 'Run Tests'
  inputs:
    targetType: 'inline'
    script: |
      Write-Host "Running tests..."
      pytest tests/
```

## Common Task Types

Beyond the tasks used in this pipeline, Azure DevOps offers many other task types:

- **Build tasks**: Compile code, run builds (e.g., `DotNetCoreCLI@2`, `Maven@3`)
- **Test tasks**: Run unit tests, publish test results (e.g., `VSTest@2`, `PublishTestResults@2`)
- **Package tasks**: Create packages, upload to feeds (e.g., `NuGetCommand@2`, `Docker@2`)
- **Deploy tasks**: Deploy to Azure, Kubernetes, etc. (e.g., `AzureWebApp@1`, `KubernetesManifest@0`)
- **Utility tasks**: Copy files, download artifacts, archive files (e.g., `CopyFiles@2`, `ArchiveFiles@2`)

## Useful Resources

- [Azure DevOps Pipeline Tasks Reference](https://docs.microsoft.com/azure/devops/pipelines/tasks/)
- [YAML Schema Reference](https://docs.microsoft.com/azure/devops/pipelines/yaml-schema/)
- [Bash Task Documentation](https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/bash)
- [GitHub Release Task Documentation](https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/github-release)
- [Publish Build Artifacts Task Documentation](https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/publish-build-artifacts)
- [Pipeline Variables](https://docs.microsoft.com/azure/devops/pipelines/build/variables)

## Troubleshooting

### Common Issues

**Task not found**: Ensure the task version is correct and available in your Azure DevOps instance.

**Authentication failed**: Verify that service connections are properly configured with the right permissions.

**Files not found**: Check that paths use the correct predefined variables (e.g., `$(Build.SourcesDirectory)`).

**Script errors**: Enable verbose logging by adding `System.Debug` variable set to `true` in your pipeline.

---

<button class="button" onclick="window.location.href='https://microsoftlearning.github.io/mslearn-mlops/';">Back to overview</button>
