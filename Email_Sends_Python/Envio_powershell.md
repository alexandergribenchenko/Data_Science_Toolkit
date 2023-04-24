$cred = Get-Credential

Send-MailMessage -From $cred.UserName -To "alexander.ortega@tcs.com" -SmtpServer smtp.office365.com  -Port 587 -UseSsl -Body "test body" -Subject "test using SMTP client submission" -Credential $cred
