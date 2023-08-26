selector_to_html = {"a[href=\"#from-specifies-the-base-image\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">FROM: Specifies the base image.<a class=\"headerlink\" href=\"#from-specifies-the-base-image\" title=\"Link to this heading\">\u00b6</a></h1>", "a[href=\"#copy-or-add-copies-files-and-directories-from-the-host-into-the-image\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">COPY or ADD: Copies files and directories from the host into the image.<a class=\"headerlink\" href=\"#copy-or-add-copies-files-and-directories-from-the-host-into-the-image\" title=\"Link to this heading\">\u00b6</a></h1>", "a[href=\"#env-sets-environment-variables-in-the-image\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">ENV: Sets environment variables in the image.<a class=\"headerlink\" href=\"#env-sets-environment-variables-in-the-image\" title=\"Link to this heading\">\u00b6</a></h1>", "a[href=\"#expose-documents-which-ports-the-container-listens-on\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">EXPOSE: Documents which ports the container listens on.<a class=\"headerlink\" href=\"#expose-documents-which-ports-the-container-listens-on\" title=\"Link to this heading\">\u00b6</a></h1>", "a[href=\"#workdir-sets-the-working-directory-for-subsequent-instructions\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">WORKDIR: Sets the working directory for subsequent instructions.<a class=\"headerlink\" href=\"#workdir-sets-the-working-directory-for-subsequent-instructions\" title=\"Link to this heading\">\u00b6</a></h1>", "a[href=\"#cmd-or-entrypoint-defines-the-default-command-when-the-container-starts\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">CMD or ENTRYPOINT: Defines the default command when the container starts.<a class=\"headerlink\" href=\"#cmd-or-entrypoint-defines-the-default-command-when-the-container-starts\" title=\"Link to this heading\">\u00b6</a></h1><p><strong>3.Building Images using Dockerfile:</strong></p><p>To build an image using a Dockerfile:</p>", "a[href=\"#run-executes-commands-in-the-image-during-build\"]": "<h1 class=\"tippy-header\" style=\"margin-top: 0;\">RUN: Executes commands in the image during build.<a class=\"headerlink\" href=\"#run-executes-commands-in-the-image-during-build\" title=\"Link to this heading\">\u00b6</a></h1>"}
skip_classes = ["headerlink", "sd-stretched-link"]

window.onload = function () {
    for (const [select, tip_html] of Object.entries(selector_to_html)) {
        const links = document.querySelectorAll(` ${select}`);
        for (const link of links) {
            if (skip_classes.some(c => link.classList.contains(c))) {
                continue;
            }

            tippy(link, {
                content: tip_html,
                allowHTML: true,
                arrow: true,
                placement: 'auto-start', maxWidth: 500, interactive: false,

            });
        };
    };
    console.log("tippy tips loaded!");
};
