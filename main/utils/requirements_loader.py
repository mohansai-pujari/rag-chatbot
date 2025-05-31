import pkg_resources

def write_installed_packages_to_file(filename="../requirements.txt"):
    installed_packages = pkg_resources.working_set
    with open(filename, "w") as f:
        for pkg in sorted(installed_packages, key=lambda x: x.project_name.lower()):
            f.write(f"{pkg.project_name}=={pkg.version}\n")
    print(f"All installed packages have been written to {filename}")

if __name__ == "__main__":
    write_installed_packages_to_file()
