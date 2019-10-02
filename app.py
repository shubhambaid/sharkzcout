from flask import Flask, render_template
from scapy.all import sniff
dev1=[]
jack=[]
app = Flask(__name__)
pkts = sniff(count = 20)
i=0
#j=0
for i in range(0,19):
    if  pkts[i][0].src=='WIN OF DEV 1' or pkts[i][0].dst=='WIN OF DEV 1':
        dev1=pkts[i].summary()
#for j in range(0,9999):            #For Device 2 and so on
    #if  pkts[j][0].src=='' or pkts[j][0].dst=='':
        #jack=pkts[j].summary
@app.route('/')
def index():
    filter1 = {
        'msisummary':dev1 ,
        #'macsummary':jack ,
    }

    return render_template('index.html',filter1=filter1)

if __name__ == '__main__':
    app.run(debug=True)