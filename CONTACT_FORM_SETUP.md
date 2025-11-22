# Contact Form Email Setup Guide

Your contact form is now configured to send emails! Here's how to complete the setup.

## 🚀 Quick Setup (5 minutes)

### Step 1: Create Free Formspree Account

1. Go to **[Formspree.io](https://formspree.io/)**
2. Click **"Get Started"** or **"Sign Up"**
3. Sign up with **your email address** (where you want to receive contact form submissions)
4. Verify your email address

### Step 2: Create a New Form

1. After logging in, click **"+ New Form"**
2. Give it a name: `BR27 Contact Form`
3. Click **"Create Form"**
4. You'll get a unique form endpoint like: `https://formspree.io/f/xwpkglgl`

### Step 3: Update Your Website

1. Copy your unique form endpoint
2. Open `index.html`
3. Find this line (around line 287):
   ```html
   <form class="contact-form" id="contactForm" action="https://formspree.io/f/xwpkglgl" method="POST">
   ```
4. Replace `xwpkglgl` with **your unique form ID**
5. Save the file

### Step 4: Test It!

1. Restart your server: `./setup.sh restart`
2. Visit: http://localhost:8000
3. Go to Contact section
4. Fill out the form and submit
5. Check your email inbox! 📧

## ✅ What You'll Receive

When someone submits the contact form, you'll get an email with:
- **Name**: Sender's name
- **Email**: Their email address (so you can reply)
- **Subject**: What the message is about
- **Message**: Their full message

## 📊 Formspree Features (Free Tier)

- ✅ **50 submissions/month** (free)
- ✅ Email notifications
- ✅ Spam protection
- ✅ File uploads (if you add them later)
- ✅ Archive of all submissions in dashboard
- ✅ No credit card required

## 🔧 Current Setup

The form is already configured with:
- ✅ All required fields
- ✅ Email validation
- ✅ Loading states
- ✅ Success/error messages
- ✅ Form reset after submission
- ✅ Spam protection

## 🎨 User Experience

When a visitor submits the form:
1. Button changes to "Sending..."
2. Form is disabled during submission
3. On success: Shows "✓ Message Sent!" with green confirmation
4. On error: Shows error message
5. Form resets automatically after 5 seconds

## 💰 Upgrade Options (Optional)

If you need more than 50 submissions/month:

- **Gold Plan**: $10/month
  - 1,000 submissions/month
  - Custom thank you page
  - Remove Formspree branding
  - Priority support

- **Platinum Plan**: $40/month
  - 10,000 submissions/month
  - All Gold features
  - Advanced integrations

## 🔐 Security Features

Formspree includes:
- ✅ Spam filtering (reCAPTCHA)
- ✅ Bot detection
- ✅ Rate limiting
- ✅ HTTPS encryption
- ✅ GDPR compliant

## 🛠️ Alternative Options

If you prefer not to use Formspree, here are alternatives:

### Option 1: EmailJS
- Free tier: 200 emails/month
- Client-side email sending
- Setup: [emailjs.com](https://www.emailjs.com/)

### Option 2: Web3Forms
- Free tier: Unlimited submissions
- Simple API
- Setup: [web3forms.com](https://web3forms.com/)

### Option 3: Netlify Forms (if hosting on Netlify)
- Free tier: 100 submissions/month
- Integrated with Netlify hosting
- No additional signup needed

## 📝 Testing Checklist

After setup, test these scenarios:

- [ ] Submit with all fields filled - Should receive email
- [ ] Submit with invalid email - Should show error
- [ ] Submit with empty required fields - Should prevent submission
- [ ] Check spam folder if email doesn't arrive
- [ ] Try submitting twice quickly - Should handle rate limiting

## 🐛 Troubleshooting

### Email not arriving?

1. **Check spam folder** - Formspree emails might be filtered
2. **Verify form endpoint** - Make sure you updated the action URL
3. **Check Formspree dashboard** - See if submission was received
4. **Wait a few minutes** - Sometimes there's a delay
5. **Check Formspree inbox** - All submissions stored there too

### Form not submitting?

1. **Check browser console** - Look for JavaScript errors
2. **Verify internet connection** - Form needs network access
3. **Check form action URL** - Must be valid Formspree endpoint
4. **Try different browser** - Rule out browser issues

### Getting error message?

1. **Check Formspree status** - Visit status.formspree.io
2. **Verify API key** - Make sure form endpoint is correct
3. **Check rate limits** - Free tier has submission limits
4. **Review error in console** - Browser dev tools show details

## 📧 Email Notification Settings

In Formspree dashboard, you can:
- ✅ Add multiple email recipients
- ✅ Customize email subject line
- ✅ Set up auto-responders
- ✅ Create custom confirmation pages
- ✅ Export submissions to CSV

## 🔄 After Deployment

Once deployed to GitHub Pages or AWS:
1. Form will work automatically
2. No additional configuration needed
3. Same Formspree endpoint works everywhere
4. Test on live site to confirm

## 💡 Pro Tips

1. **Add honeypot field** - Extra spam protection
2. **Enable reCAPTCHA** - In Formspree settings
3. **Create templates** - Save time responding to common queries
4. **Set up notifications** - Get instant email alerts
5. **Archive important messages** - Download from Formspree dashboard

## 📞 Support

- **Formspree Docs**: [docs.formspree.io](https://help.formspree.io/)
- **Formspree Support**: support@formspree.io
- **BR27 Issues**: Create issue on GitHub repo

## 🎉 You're All Set!

Once you update the form endpoint with your Formspree ID, visitors can:
- ✅ Contact you directly from the website
- ✅ You receive emails instantly
- ✅ Professional, spam-free experience
- ✅ No backend server needed!

---

**Need Help?** The form is already set up and working. Just update the Formspree endpoint with your own ID!

*Last updated: Ready for your Formspree account*

