(require 'package)
(setq package-user-dir (expand-file-name "./.packages"))
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
                         ("elpa" . "https://elpa.gnu.org/packages/")))

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

(package-install 'htmlize)

(require 'ox-publish)

(setq org-html-validation-link nil      
      org-html-head-include-scripts nil 
      org-html-head-include-default-style nil
      org-html-head "
<meta http-equiv=\"Cache-Control\" content=\"no-cache, no-store, must-revalidate\" />
<meta http-equiv=\"Pragma\" content=\"no-cache\" />
<meta http-equiv=\"Expires\" content=\"-1\" />
<script src=\"/static/main.js\" defer></script>
<script src=\"/static/highlight.min.js\" defer></script>
<link rel=\"stylesheet\" href=\"/static/gruvbox-dark-medium.min.css\" />
<link rel=\"stylesheet\" href=\"/static/style.css\" />")

(setq org-publish-project-alist
      (list
       (list "org-site:main"
             :recursive t
             :base-directory "./content"
             :publishing-function 'org-html-publish-to-html
             :publishing-directory "./public"
             :with-author t
             :with-creator nil
             :with-toc nil 
             :section-numbers nil
             :time-stamp-file nil)))

(org-publish-all t)

(message "Build complete!")
