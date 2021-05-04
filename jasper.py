import json

frame = '''
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

tegevusaladStart = '''
<band height="600">
    <!-- tegevusalad -->
    <componentElement>
        <reportElement x="0" y="0" width="444" height="23" uuid="118abb83-369d-408b-a3bc-194b978d3fab"/>
        <jr:list xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
            <datasetRun subDataset="dataset1" uuid="ce33a9a6-0aaf-4df0-abb7-fc52b0553191">
                <dataSourceExpression><![CDATA[$P{tegevusalad}]]></dataSourceExpression>
            </datasetRun>
            <jr:listContents height="600" width="600">
                <rectangle>
                    <reportElement x="0" y="0" width="473" height="23" backcolor="#A2B691" uuid="8f089039-308f-4566-97f3-d91f30c392fd"/>
                    <graphicElement>
                        <pen lineWidth="0.5"/>
                    </graphicElement>
                </rectangle>
                <textField isBlankWhenNull="true">
                    <reportElement x="5" y="0" width="228" height="23" uuid="ab11b6cd-ab29-4fa3-942b-4f298a619a14"/>
                    <textElement verticalAlignment="Middle">
                        <font fontName="Arial Narrow" size="11" isBold="true"/>
                    </textElement>
                    <textFieldExpression><![CDATA[$F{tegevusalaAndmedTekst}]]></textFieldExpression>
                </textField>
                <rectangle>
                    <reportElement x="196" y="23" width="277" height="23" uuid="9d4410e0-a036-4a9b-912d-e41b152a1622"/>
                    <graphicElement>
                        <pen lineWidth="0.5"/>
                    </graphicElement>
                </rectangle>
                <rectangle>
                    <reportElement x="0" y="23" width="196" height="23" uuid="e87c77ba-bf05-42d9-b898-9bf342e96d48"/>
                    <graphicElement>
                        <pen lineWidth="0.5"/>
                    </graphicElement>
                </rectangle>
                <staticText>
                    <reportElement x="5" y="23" width="147" height="23" uuid="c61b2c6c-2100-4788-88b5-2d2f32949f0a"/>
                    <textElement verticalAlignment="Middle">
                        <font fontName="Arial Narrow" size="11" isBold="false"/>
                    </textElement>
                    <text><![CDATA[Tegevuse üldnimetus]]></text>
                </staticText>
                <textField isBlankWhenNull="true">
                    <reportElement x="201" y="23" width="272" height="23" uuid="52375650-164b-4eed-96a9-791005f60f47"/>
                    <textElement verticalAlignment="Middle">
                        <font fontName="Arial Narrow" size="11"/>
                    </textElement>
                    <textFieldExpression><![CDATA[$F{tegevuseYldnimetus}.getNimetus()]]></textFieldExpression>
                </textField>
'''

padevustunnistusedStart = '''
<band height="600">
    <!-- padevustunnistused -->
    <componentElement>
        <reportElement x="0" y="0" width="444" height="20" uuid="118abb83-369d-408b-a3bc-194b978d3fab"/>
        <jr:list xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
            <datasetRun subDataset="dataset2" uuid="ce33a9a6-0aaf-4df0-abb7-fc52b0553191">
                <dataSourceExpression><![CDATA[$P{padevustunnistused}]]></dataSourceExpression>
            </datasetRun>
            <jr:listContents height="555" width="600">
                <rectangle>
                    <reportElement x="0" y="0" width="473" height="23" backcolor="#A2B691" uuid="8f089039-308f-4566-97f3-d91f30c392fd"/>
                    <graphicElement>
                        <pen lineWidth="0.5"/>
                    </graphicElement>
                </rectangle>
                <textField isBlankWhenNull="true">
                    <reportElement x="5" y="0" width="228" height="23" uuid="ab11b6cd-ab29-4fa3-942b-4f298a619a14"/>
                    <textElement verticalAlignment="Middle">
                        <font fontName="Arial Narrow" size="11" isBold="true"/>
                    </textElement>
                    <textFieldExpression><![CDATA[$F{pealkiri}]]></textFieldExpression>
                </textField>
'''

tegevusaladEnd = '''
            </jr:listContents>
        </jr:list>
    </componentElement>
</band>
'''

padevustunnistusedEnd = '''
            </jr:listContents>
        </jr:list>
    </componentElement>
</band>
'''

veovahendStart = '''
<band height="600">
    <!-- veovahendid -->
    <componentElement>
        <reportElement x="0" y="0" width="444" height="20" uuid="118abb83-369d-408b-a3bc-194b978d3fab"/>
        <jr:list xmlns:jr="http://jasperreports.sourceforge.net/jasperreports/components" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports/components http://jasperreports.sourceforge.net/xsd/components.xsd">
            <datasetRun subDataset="dataset2" uuid="ce33a9a6-0aaf-4df0-abb7-fc52b0553191">
                <dataSourceExpression><![CDATA[$P{veovahendid}]]></dataSourceExpression>
            </datasetRun>
            <jr:listContents height="555" width="600">
                <rectangle>
                    <reportElement x="0" y="0" width="473" height="23" backcolor="#A2B691" uuid="8f089039-308f-4566-97f3-d91f30c392fd"/>
                    <graphicElement>
                        <pen lineWidth="0.5"/>
                    </graphicElement>
                </rectangle>
                <textField isBlankWhenNull="true">
                    <reportElement x="5" y="0" width="228" height="23" uuid="ab11b6cd-ab29-4fa3-942b-4f298a619a14"/>
                    <textElement verticalAlignment="Middle">
                        <font fontName="Arial Narrow" size="11" isBold="true"/>
                    </textElement>
                    <textFieldExpression><![CDATA[$F{pealkiri}]]></textFieldExpression>
                </textField>
'''

veovahendEnd = '''
            </jr:listContents>
        </jr:list>
    </componentElement>
</band>
'''

frameStart = '''
            <!-- start REPLACE_TYPE start-->
            <frame>
                <reportElement x="0" y="23" width="473" height="0" isRemoveLineWhenBlank="true" uuid="0140ba9b-f2f0-494c-82bc-caf6b5efc63e">
                    <printWhenExpression><![CDATA[$F{tegevuseYldnimetus}.getKood().equals("REPLACE_TYPE")]]></printWhenExpression>
                </reportElement>
'''

frameStop = '''
            </frame>
            <!-- END REPLACE_TYPE END-->
'''

#def addTegevusalad(file, tegevusalad):
def padevustunnistused(file, padevustunnistused, y=23):
    file.write(padevustunnistusedStart)
    for padevustunnistus in padevustunnistused:
        padevustunnistusedFrame(file, padevustunnistus, y)
        y+=23
    file.write(padevustunnistusedEnd)

def addVeovahendid(file, veovahendid, y=23):
    file.write(veovahendStart)
    for veovahend in veovahendid:
        addVeovahendidFrame(file, veovahend, y)
        y+=23
    file.write(veovahendEnd)

def padevustunnistusedFrame(file, veovahend, y):
    completedFrame = frame.replace("REPLACE_TYPE", veovahend["parameter"])
    completedFrame = completedFrame.replace("REPLACE_CHECK", veovahend["check"])
    completedFrame = completedFrame.replace("REPLACE_TITLE", veovahend["title"])
    completedFrame = completedFrame.replace("REPLACE_PARAMETER", veovahend["parameter"])
    completedFrame = completedFrame.replace("REPLACE_Y", str(y))

    file.write(completedFrame)

def addVeovahendidFrame(file, veovahend, y):
    completedFrame = frame.replace("REPLACE_TYPE", veovahend["parameter"])
    completedFrame = completedFrame.replace("REPLACE_CHECK", veovahend["check"])
    completedFrame = completedFrame.replace("REPLACE_TITLE", veovahend["title"])
    completedFrame = completedFrame.replace("REPLACE_PARAMETER", veovahend["parameter"])
    completedFrame = completedFrame.replace("REPLACE_Y", str(y))

    file.write(completedFrame)

def addTegevusalad(file, tegevusalad, y=23):
    file.write(tegevusaladStart)
    for tegevusala in tegevusalad:
        file.write(frameStart.replace("REPLACE_TYPE", tegevusala["type"]))
        formatTegevusala(file, tegevusala)
        file.write(frameStop.replace("REPLACE_TYPE", tegevusala["type"]))
    file.write(tegevusaladEnd)

def formatTegevusala(file, tegevusala ,y=23):
    for parameter in tegevusala["frames"]:
        frameParameter = frame.replace("REPLACE_PARAMETER", parameter["parameter"])
        frameParameter = frameParameter.replace("REPLACE_TYPE", parameter["parameter"])
        frameParameter = frameParameter.replace("REPLACE_Y", str(y))
        frameParameter = frameParameter.replace("REPLACE_TITLE", parameter["title"])
        frameParameter = frameParameter.replace("REPLACE_CHECK", parameter["check"])
        file.write(frameParameter)
        y+=23

with open('template.json', encoding='utf-8') as f:
    data = json.load(f)

    with open("./output/all.xml", "w", encoding='utf-8') as file:
        addTegevusalad(file, data["tegevusalad"])
        addVeovahendid(file, data["veovahendid"])
        padevustunnistused(file, data["padevustunnistused"])