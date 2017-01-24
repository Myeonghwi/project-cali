# -*- coding: utf-8 -*-
from xml.etree import ElementTree


def output_xml(xml_path):
    # targetXML = open('SmallOffice_Zone_west_wTable.xml', 'r')
    doc = ElementTree.parse(xml_path)
    root = doc.getroot()
    objective_element = []

    # IIC
    for element in root.find("ComponentCostEconomicsSummary")\
            .findall("ConstructionCostEstimateSummary"):
        if element.findtext("name") == 'LineItemSubtotal':
            economics_tag = element.find("CurrentBldgModel")
            objective_element.append(economics_tag.text)
    # NPV
    for element in root.find("LifeCycleCostReport")\
            .findall("PresentValueByYear"):
        if element.findtext("name") == 'Total':
            npv_tag = element.find("PresentValueOfCosts")
            objective_element.append(npv_tag.text)
    # Cooling Energy
    for element in root.findall("Zonecoolingsummarymonthly"):
        if element.findtext("for") == '2F:LIBRARY':
            energy_cooling_tag = element.find('CustomMonthlyReport').find("AnnualSumOrAverage")
            objective_element.append(energy_cooling_tag.text)
    # heating Energy
    for element in root.findall("Zoneheatingsummarymonthly"):
        if element.findtext("for") == '2F:LIBRARY':
            energy_heating_tag = element.find('CustomMonthlyReport').find("AnnualSumOrAverage")
            objective_element.append(energy_heating_tag.text)
    # adaptive PMV
    for element in root.find("AdaptiveComfortSummary")\
            .findall("TimeNotMeetingTheAdaptiveComfortModelsDuringOccupiedHours"):
        if element.findtext("name") == 'People2fLibrary':
            adaptive_pmv_tag = element.find("Ashrae5590AcceptabilityLimits")
            objective_element.append(adaptive_pmv_tag.text)
    # PMV
    for element in root.find("Occupantcomfortdatasummarymonthly")\
            .findall("CustomMonthlyReport"):
        if element.findtext("name") == 'ZoneThermalComfortFangerModelPmvForHoursShown':
            fanger_pmv_tag = element.find("AnnualSumOrAverage")
            objective_element.append(fanger_pmv_tag.text)

    return objective_element
