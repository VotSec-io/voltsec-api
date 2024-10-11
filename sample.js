[
    {
      "name": "Cross-Site Request Forgery (CSRF)",
      "description": "CSRF vulnerabilities allow an attacker to perform actions on behalf of an authenticated user without their consent.",
      "level": "High",
      "remediation": "Implement anti-CSRF tokens and ensure they are used in all state-changing operations."
    },
    {
      "name": "Open Redirect",
      "description": "Open redirect vulnerabilities allow attackers to redirect users to untrusted websites.",
      "level": "Low",
      "remediation": "Avoid using user-controlled inputs in redirects and validate all redirect URLs."
    },
    [
      {
        "name": "Content-Security-Policy",
        "description": "The Content-Security-Policy header helps prevent cross-site scripting (XSS) attacks.",
        "level": "High",
        "remediation": "Set a strict Content-Security-Policy header."
      },
      {
        "name": "X-Content-Type-Options",
        "description": "The X-Content-Type-Options header prevents MIME type sniffing.",
        "level": "Medium",
        "remediation": "Set the X-Content-Type-Options header to 'nosniff'."
      },
      {
        "name": "X-Frame-Options",
        "description": "The X-Frame-Options header protects against clickjacking attacks.",
        "level": "Medium",
        "remediation": "Set the X-Frame-Options header to 'DENY' or 'SAMEORIGIN'."
      },
      {
        "name": "X-XSS-Protection",
        "description": "The X-XSS-Protection header enables the cross-site scripting filter built into most browsers.",
        "level": "Low",
        "remediation": "Set the X-XSS-Protection header to '1; mode=block'."
      },
      {
        "name": "Referrer-Policy",
        "description": "The Referrer-Policy header controls how much referrer information is included with requests.",
        "level": "Low",
        "remediation": "Set the Referrer-Policy header to 'no-referrer' or 'same-origin'."
      },
      {
        "name": "Permissions-Policy",
        "description": "The Permissions-Policy header controls which features and APIs can be used in the browser.",
        "level": "Medium",
        "remediation": "Set the Permissions-Policy header to restrict feature usage."
      }
    ],
    {
      "name": "Cross-Site Request Forgery (CSRF)",
      "description": "CSRF vulnerabilities allow an attacker to perform actions on behalf of an authenticated user without their consent.",
      "level": "High",
      "remediation": "Implement anti-CSRF tokens and ensure they are used in all state-changing operations."
    },
    {
      "name": "Open Redirect",
      "description": "Open redirect vulnerabilities allow attackers to redirect users to untrusted websites.",
      "level": "Low",
      "remediation": "Avoid using user-controlled inputs in redirects and validate all redirect URLs."
    },
    
    [
      {
        "name": "Content-Security-Policy",
        "description": "The Content-Security-Policy header helps prevent cross-site scripting (XSS) attacks.",
        "level": "High",
        "remediation": "Set a strict Content-Security-Policy header."
      },
      {
        "name": "X-Content-Type-Options",
        "description": "The X-Content-Type-Options header prevents MIME type sniffing.",
        "level": "Medium",
        "remediation": "Set the X-Content-Type-Options header to 'nosniff'."
      },
      {
        "name": "X-Frame-Options",
        "description": "The X-Frame-Options header protects against clickjacking attacks.",
        "level": "Medium",
        "remediation": "Set the X-Frame-Options header to 'DENY' or 'SAMEORIGIN'."
      },
      {
        "name": "X-XSS-Protection",
        "description": "The X-XSS-Protection header enables the cross-site scripting filter built into most browsers.",
        "level": "Low",
        "remediation": "Set the X-XSS-Protection header to '1; mode=block'."
      },
      {
        "name": "Referrer-Policy",
        "description": "The Referrer-Policy header controls how much referrer information is included with requests.",
        "level": "Low",
        "remediation": "Set the Referrer-Policy header to 'no-referrer' or 'same-origin'."
      },
      {
        "name": "Permissions-Policy",
        "description": "The Permissions-Policy header controls which features and APIs can be used in the browser.",
        "level": "Medium",
        "remediation": "Set the Permissions-Policy header to restrict feature usage."
      }
    ]
  ]