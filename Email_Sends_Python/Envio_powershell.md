$cred = Get-Credential

Send-MailMessage -From $cred.UserName -To "alexander.ortega@tcs.com" -SmtpServer smtp.office365.com  -Port 587 -UseSsl -Body "test body" -Subject "test using SMTP client submission" -Credential $cred


Send-MailMessage -From $cred.UserName -To "productos.analitica@avianca.com" -SmtpServer smtp.office365.com  -Port 587 -UseSsl -Body "test 20230425 body" -Subject "test 20230425 using SMTP client submission" -Credential $cred


Send-MailMessage -From "productos.analitica@avianca.com" -To "productos.analitica@avianca.com" -SmtpServer smtp.office365.com  -Port 587 -UseSsl -Body "test 20230425 body" -Subject "test 20230425 using SMTP client submission" -Credential "Ad.221232"
