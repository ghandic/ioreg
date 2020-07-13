import re
import json
import subprocess


class IOReg(object):
    @staticmethod
    def to_dict(options=["-rlk", "BatteryPercent"]):
        p = subprocess.Popen(["ioreg", *options], stdout=subprocess.PIPE)
        output = p.communicate()[0].decode("utf-8")

        # Remove junk lines
        output = "\n".join([n for n in output.split("\n") if not n.startswith("+-o")])
        # Making JSON compliant syntax
        output = (
            output.replace("=", ":")
            .replace(": No", ": false")
            .replace(": Yes", ": true")
            .replace("(", "[")
            .replace(")", "]")
        )
        # Wrapping quotes around none json compliant types
        output = re.sub(r'"BD_ADDR"\s*:\s*(.*)', r'"BD_ADDR": "\1"', output)
        # Adding comma between every key value and then remove the last comma before end of object
        output = re.sub(r'"(.*)"\s*:\s*(.*)', r'"\1": \2,', output)
        output = re.sub(r"\s*,\s*}", r"}", output)
        # Add comma between each object if there isnt one already
        output = re.sub(r"}\s*{", r"},\n{", output)
        # Wrap into a list to be JSON compliant
        output = f"[{output}]"
        # Load into dictionary
        return json.loads(output)
