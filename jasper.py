import json

parameterTemplate = '''
    <!-- REPLACE_TYPE -->
    <frame>
        <reportElement positionType="Float" stretchType="NoStretch" x="0" y="REPLACE_Y" width="473" height="23" isRemoveLineWhenBlank="true" uuid="0140ba9b-f2f0-494c-82bc-caf6b5efc63e">
            <printWhenExpression><![CDATA[REPLACE_CHECK]]></printWhenExpression>
        </reportElement>
        <textField isStretchWithOverflow="true">
            <reportElement stretchType="RelativeToTallestObject" x="0" y="0" width="196" height="23" uuid="a8b7d505-a6ad-4359-9263-23ac087b19ff"/>
            <box topPadding="1" leftPadding="5" bottomPadding="1" rightPadding="1">
                <topPen lineWidth="0.5" lineStyle="Solid"/>
                <leftPen lineWidth="0.5" lineStyle="Solid"/>
                <bottomPen lineWidth="0.5" lineStyle="Solid"/>
                <rightPen lineWidth="0.5" lineStyle="Solid"/>
            </box>
            <textElement verticalAlignment="Middle">
                <font fontName="Arial Narrow" size="11" isBold="false"/>
            </textElement>
            <textFieldExpression><![CDATA[REPLACE_TITLE]]></textFieldExpression>
        </textField>
        <textField isStretchWithOverflow="true" isBlankWhenNull="true">
            <reportElement stretchType="RelativeToTallestObject" x="196" y="0" width="277" height="23" uuid="6a8c4e04-4278-4595-845f-67be590d9210"/>
            <box topPadding="1" leftPadding="5" bottomPadding="1" rightPadding="1">
                <topPen lineWidth="0.5" lineStyle="Solid"/>
                <leftPen lineWidth="0.5" lineStyle="Solid"/>
                <bottomPen lineWidth="0.5" lineStyle="Solid"/>
                <rightPen lineWidth="0.5" lineStyle="Solid"/>
            </box>
            <textElement verticalAlignment="Middle">
                <font fontName="Arial Narrow" size="11"/>
            </textElement>
            <textFieldExpression><![CDATA[REPLACE_PARAMETER]]></textFieldExpression>
        </textField>
    </frame>
    <!-- REPLACE_TYPE -->
'''

frameStart = '''<!-- start REPLACE_TYPE start-->
<frame>
    <reportElement x="0" y="23" width="473" height="0" isRemoveLineWhenBlank="true" uuid="0140ba9b-f2f0-494c-82bc-caf6b5efc63e">
        <printWhenExpression><![CDATA[$F{tegevuseYldnimetus}.getKood().equals("REPLACE_TYPE")]]></printWhenExpression>
    </reportElement>
'''

frameStop = '''</frame>
<!-- END REPLACE_TYPE END-->
'''

def formatTegevusala(file, tegevusala ,y=23):
    for parameter in tegevusala["frames"]:
        frameParameter = parameterTemplate.replace("REPLACE_PARAMETER", parameter["parameter"])
        frameParameter = frameParameter.replace("REPLACE_TYPE", parameter["parameter"])
        frameParameter = frameParameter.replace("REPLACE_Y", str(y))
        frameParameter = frameParameter.replace("REPLACE_TITLE", parameter["title"])
        frameParameter = frameParameter.replace("REPLACE_CHECK", parameter["check"])
        file.write(frameParameter)
        y+=23

with open('template.json', encoding='utf-8') as f:
    data = json.load(f)

    with open("./output/all.txt", "w", encoding='utf-8') as file:
        for tegevusala in data["tegevusalad"]:
            #with open("./output/{}.txt".format(tegevusala["type"]), "w", encoding='utf-8') as file:
            file.write(frameStart.replace("REPLACE_TYPE", tegevusala["type"]))
            formatTegevusala(file, tegevusala)
            file.write(frameStop.replace("REPLACE_TYPE", tegevusala["type"]))