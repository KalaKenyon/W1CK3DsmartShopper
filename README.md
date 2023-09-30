# W1CK3DsmartShopper<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>W1CK3D Smart Shopper</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-top: 50px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        h2 {
            color: #333;
        }

        code {
            background-color: #f9f9f9;
            padding: 2px 6px;
            border-radius: 5px;
        }

        .example {
            font-family: monospace;
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
        }

        .note {
            color: #777;
            font-style: italic;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>W1CK3D Smart Shopper</h1>

        <p>W1CK3D Smart Shopper is a Python script that allows users to calculate the total cost of their shopping items,
            including sales tax. Simply input the product details and quantities, and the Smart Shopper will handle the
            rest.</p>

        <h2>Usage</h2>

        <div class="example">
            <code>&lt;python&gt; python smart_shopper.py</code>
        </div>

        <p>Follow the prompts to enter product names, descriptions, prices, and quantities. Type <code>'done'</code> to
            finish entering products. The script will then calculate the total cost, add sales tax, and generate a
            detailed receipt.</p>

        <h2>Example</h2>

        <div class="example">
            <pre>
Customer Receipt:
Product1: Description1 - $10.00 x 2
Product2: Description2 - $20.00 x 1
Total Cost: $40.00
Sales Tax (8.8%): $3.52
Final Total: $43.52</pre>
        </div>

        <div class="note">
            <p><strong>Note:</strong> This script assumes a fixed sales tax rate of 8.8%. You can modify the script to
                change the tax rate if needed.</p>
        </div>

        <h2>Contributing</h2>

        <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to
            change.</p>

        <h2>License</h2>

        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>

</html>
