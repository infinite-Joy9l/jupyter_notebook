
# coding: utf-8

# Link taken from https://github.com/XoriantOpenSource/Jupyter-WebComponents

# In[*]

#Read data from files and prepare for analysis
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')

#Read first 8 columns of the flight data file
df = pd.read_csv('329994478_72017_3649_airline_delay_causes.csv').iloc[:,:8]

#Function to analyse delays
def ontime(df) :
    x=df[['carrier_name','arr_flights','arr_del15']].groupby('carrier_name').sum()
    x['on_time_%'] = np.round(100*(1 - (x.arr_del15/x.arr_flights)),2)
    return x.sort_values(by='on_time_%',ascending=False)


# In[*]

get_ipython().run_cell_magic('javascript', '', 'class XTable extends HTMLElement {\n    constructor() {\n        super() ;\n        if ( this.sroot == undefined )\n            this.sroot = this.attachShadow({mode:\'open\'}) ;\n    }\n    connectedCallback() {\n        this.sroot.innerHTML = \'\'\n    }\n    static get observedAttributes() { return [\'data-command\',\'data-style\'] ; }\n    attributeChangedCallback(name,oldValue,newValue) {\n        if ( name == \'data-style\' ) {\n            if ( this._style ) {\n                alert(\'Style can be set only once\') ;\n                return\n            }\n            this._style = \'<style>\' + newValue + \'</style>\';\n            return ;\n        }\n        if ( newValue == undefined || newValue.length == 0 )\n            return ;\n        this._command = newValue ;\n        this._commandChanged() ;\n    }\n    _commandChanged() {\n        if ( this._command == undefined || this._command.length == 0 )\n            return ;\n        var container = this ;\n        IPython.notebook.kernel.execute( this._command, {\n            iopub : {\n                output : function(res) {\n                    container.sroot.innerHTML = \'\'\n                    if ( container.style )\n                        container.sroot.innerHTML += container._style ;\n                    if (res.content.evalue) {\n                        container.sroot.innerHTML += res.content.traceback;\n                        return ;\n                    }\n                    if ( res.content.data[\'image/png\'] ) {\n                        container.sroot.innerHTML += \'<img src="data:image/png;base64,\' + res.content.data[\'image/png\'] +\'">\' ;\n                        return ;\n                    }\n                    if ( res.msg_type == \'execute_result\' )\n                        if ( res.content.data[\'text/html\'] ) {\n                            container.sroot.innerHTML += res.content.data[\'text/html\'];\n                        }\n                    var table = container.sroot.querySelector(\'table\') ; //Assume only one table for now\n                    if ( table )\n                        table.setAttribute(\'border\',0) ;\n                }\n            }\n        }, {\n            silent : false\n        })\n    }\n\n}\n(function() {\n    if ( window.customElements == undefined ) {\n        alert(\'Unsupported browser\') ;\n        return ;\n    }\n    if ( customElements.get(\'x-table\') == undefined )\n        customElements.define(\'x-table\',XTable) ;\n})() ;')


# In[*]

get_ipython().run_cell_magic('html', '', 'Select an option <select onchange=\'xtable_01.setAttribute("data-command",this.value);\'>\n    <option value=\'\'></option>\n    <option value=\'ontime(df)\'>On time comparison</option>\n    <option value=\'p=ontime(df)["on_time_%"].plot(kind="bar",figsize=(14,5));plt.plot();\'>On time graph</option>\n</select>\nOr search for :\nAirline Code <input type=\'text\' size=\'3\' \n    onchange=\'xtable_01.setAttribute("data-command", \n        "df[df.carrier.str.contains(\\""+this.value+"\\",case=False)]")\'> \nAirport Name <input type=\'text\' size=\'30\' \n    onchange=\'xtable_01.setAttribute("data-command", \n    "df[df.airport_name.str.contains(\\""+this.value+"\\",case=False)].sort_values(by=\\"arr_flights\\",ascending=False)")\'> \n<hr>\n<div style=\'border: solid 1px lightgray;min-height:300px;\'>\n    <x-table id=\'xtable_01\' data-command=\'\' data-style=\'td {font-size:9pt}\'></x-table>\n</div>')


# In[*]



