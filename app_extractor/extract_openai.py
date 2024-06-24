import re

from loguru import logger
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion

from app_extractor.data.data_dump import UnstructuredReactionDescription

SYSTEM_PROMPT_OntoReaction = """Read the complete specification of the Onto Reaction (ontoreaction) ontology in OWL format specified below. Thoroughly understand and remember the provided ontology exactly.

<?xml version="1.0"?>
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:xml="http://www.w3.org/XML/1998/namespace"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:dc="http://purl.org/dc/elements/1.1/"
         xmlns="https://www.theworldavatar.com/kg/ontoreaction/"
         xml:base="https://www.theworldavatar.com/kg/ontoreaction/">
    <owl:Ontology rdf:about="https://www.theworldavatar.com/kg/ontoreaction/">
        <dc:date rdf:datatype="http://www.w3.org/2001/XMLSchema#string">27 April 2023</dc:date>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">An ontology developed for describing
            reaction experiment.
        </rdfs:comment>
        <owl:versionInfo rdf:datatype="http://www.w3.org/2001/XMLSchema#string">1.10</owl:versionInfo>
        <gitCommitHash rdf:datatype="http://www.w3.org/2001/XMLSchema#string">c0599beca8df55873a1ab061dee64e52c510c6a0
        </gitCommitHash>
    </owl:Ontology>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Object Properties
//
///////////////////////////////////////////////////////////////////////////////////////
 -->        
    <owl:ObjectProperty
            rdf:about="http://www.theworldavatar.com/ontology/ontocape/material/substance/reaction_mechanism.owl#hasCatalyst"/>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasBase">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Base"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The relation hasBase denotes the bases of a
            ChemicalReaction.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasCatalyst">
        <rdfs:subPropertyOf
                rdf:resource="http://www.theworldavatar.com/ontology/ontocape/material/substance/reaction_mechanism.owl#hasCatalyst"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Catalyst"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The relation hasCatalyst denotes the
            catalysts of a ChemicalReaction. A catalyst is a MolecularEntity or a ChemicalSpecies that is used to
            accelerate a ChemicalReaction.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasConversion">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Conversion"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its conversion performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasEcoScore">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/EcoScore"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its eco score performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasEnvironmentalFactor">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/EnvironmentalFactor"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its environmental factor performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasInputChemical">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/InputChemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its input chemicals.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasOutputChemical">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/OutputChemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its output chemicals.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and the performance indicator calculated from the measured analytical data of its output chemical.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and all its reaction conditions.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasResTime">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ResidenceTime"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its residence time condition.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRunMaterialCost">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/RunMaterialCost"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its run material cost performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRunMaterialCostPerKilogramProduct">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/RunMaterialCostPerKilogramProduct"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its run material cost per kilogram of product produced performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRxnPressure">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionPressure"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its reaction pressure condition.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRxnScale">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionScale"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its reaction scale specified to an input chemical.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRxnTemperature">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionTemperature"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its reaction temperature condition.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRxnType">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://purl.obolibrary.org/obo/MOP_0000543"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a ChemicalReaction and a
            named reaction class it belongs to.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasSolvent">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Solvent"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The relation hasSolvent denotes the
            solvents of a ChemicalReaction. A solvent is a MolecularEntity or a ChemicalSpecies that is used to host a
            ChemicalReaction.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasSpaceTimeYield">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/SpaceTimeYield"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its space time yield performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasStoichiometryRatio">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasReactionCondition"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/StoichiometryRatio"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and the stoichiometry ratio it applies to each input chemical.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasYield">
        <rdfs:subPropertyOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasPerformanceIndicator"/>
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Yield"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and its yield performance indicator.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/indicatesMultiplicityOf">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/StoichiometryRatio"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/InputChemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation indicates the multiplicity of
            the input chemical participating in a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/indicatesUsageOf">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionScale"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/InputChemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation indicates the reaction scale in
            form of usage of an input chemical.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/isAssignedTo">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontovapourtec/VapourtecR4Reactor"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation indicates the vapourtec R4
            reactor where a reaction experiment happened.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/isOccurenceOf">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between a reaction experiment
            and the chemical reaction it represents.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/isVariationOf">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionVariation"/>
        <rdfs:range rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation links a variation to its parent
            reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>

    <owl:ObjectProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/yieldLimitingSpecies">
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Conversion"/>
                    <rdf:Description rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Yield"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range rdf:resource="http://www.theworldavatar.com/ontology/ontospecies/OntoSpecies.owl#Species"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A relation between yield or conversion of a
            reaction experiment and the yield limiting species based on which the performance indicator was computed.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:ObjectProperty>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Data properties
//
///////////////////////////////////////////////////////////////////////////////////////
 -->        
    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/cdXML">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRDFILE">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/hasRInChI">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ordID">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/rxnCXSMILES">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>

    <owl:DatatypeProperty rdf:about="https://www.theworldavatar.com/kg/ontoreaction/rxnSMILES">
        <rdfs:domain rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:DatatypeProperty>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Classes
//
///////////////////////////////////////////////////////////////////////////////////////
 -->        
    <owl:Class rdf:about="http://purl.obolibrary.org/obo/MOP_0000543"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/AmountOfSubstanceFraction"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/CelsiusTemperature"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/Duration"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/MassFraction"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/Pressure"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/Quantity"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/QuantityOfDimensionOne"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/SpecificAmountOfMoney"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/Volume"/>

    <owl:Class rdf:about="http://www.ontology-of-units-of-measure.org/resource/om-2/VolumeFraction"/>

    <owl:Class rdf:about="http://www.theworldavatar.com/ontology/ontocape/material/material.owl#Material"/>

    <owl:Class
            rdf:about="http://www.theworldavatar.com/ontology/ontocape/material/substance/reaction_mechanism.owl#ChemicalReaction"/>

    <owl:Class rdf:about="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Product"/>

    <owl:Class rdf:about="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Species"/>

    <owl:Class rdf:about="http://www.theworldavatar.com/ontology/ontospecies/OntoSpecies.owl#Species"/>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Base">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Species"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A chemical species or molecular entity
            having an available pair of electrons capable of forming a covalent bond with a hydron (proton) (see
            Bronsted base) or with the vacant orbital of some other species (see Lewis base).
            [doi:10.1351/goldbook.B00601]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Catalyst">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Species"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A substance that increases the rate of a
            reaction without modifying the overall standard Gibbs energy change in the reaction.
            [doi:10.1351/goldbook.C00876]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Chemical">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontocape/material/material.owl#Material"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A chemical is a type of OntoCAPE:Material
            used as the conceptual representation of chemicals used involved in a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction">
        <rdfs:subClassOf
                rdf:resource="http://www.theworldavatar.com/ontology/ontocape/material/substance/reaction_mechanism.owl#ChemicalReaction"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A ChemicalReaction converts some
            ChemicalSpecies (or MolecularEntities) into some other ChemicalSpecies (or MolecularEntities). [OntoCAPE]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Conversion">
        <rdfs:subClassOf
                rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/AmountOfSubstanceFraction"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/yieldLimitingSpecies"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="http://www.theworldavatar.com/ontology/ontospecies/OntoSpecies.owl#Species"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The conversion indicates, which portion of
            the originally used starting material has been converted into other chemical substances by a chemical
            reaction. [UDM https://github.com/PistoiaAlliance/UDM/blob/master/Docs/Glossary.md]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/EcoScore">
        <rdfs:subClassOf
                rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/QuantityOfDimensionOne"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/EnvironmentalFactor">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/MassFraction"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The environmental factor (E-factor) of a
            reaction experiment is the ratio of the mass of waste (impurity) to mass of (desired/target) product.
            [doi:10.1039/B713736M]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Impurity">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Product"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The product that is not the desired outcome
            of a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/InputChemical">
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Chemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">An input chemical is a type of chemical
            used as the feed to a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/OutputChemical">
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/Chemical"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">An output chemical is a type of chemical
            collected as outcome from a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator">
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A quantity that is calculated from the
            measured analytical data of output chemical of a reaction experiment. It is used as objectives of a reaction
            optimisation problem.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition">
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A quantity that is used to specify the
            condition at which the reaction is to be conducted. It can be used as the optimisation variable in a
            reaction development process.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment">
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasResTime"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ResidenceTime"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasRxnPressure"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionPressure"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasRxnScale"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionScale"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/hasRxnTemperature"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionTemperature"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/isOccurenceOf"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ChemicalReaction"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A reaction experiment is a concrete
            realisation of a chemical reaction at a set of reaction conditions.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionPressure">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/Pressure"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The pressure at which a reaction experiment
            is conducted.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionScale">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/Volume"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/indicatesUsageOf"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/InputChemical"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Reaction scale indicates the volume used of
            the reference input chemical.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionTemperature">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/CelsiusTemperature"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The temperature at which a reaction
            experiment is conducted.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ReactionVariation">
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/isVariationOf"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionExperiment"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A reaction variation is defined as the same
            chemical reaction performed at a different set of reaction conditions compared to its original conditions.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/ResidenceTime">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/Duration"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The time required for air or reagent parcel
            to pass from the entrance to the exit of an instrument. Often this is approximated as the ratio of the
            interior volume of the device to the flow rate. [doi:10.1351/goldbook.R05309]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/RunMaterialCost">
        <rdfs:subClassOf
                rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/SpecificAmountOfMoney"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The total cost of input chemical during one
            reaction experiment, normally scaled by the volumetric amount of input chemicals.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/RunMaterialCostPerKilogramProduct">
        <rdfs:subClassOf
                rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/SpecificAmountOfMoney"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The total cost of input chemical during one
            reaction experiment, scaled by per kilogram of product produced.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Solvent">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Species"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">A solvent is the substance used to solve
            the chemical components of the chemical reaction process.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/SpaceTimeYield">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/Quantity"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Space-time yield is a measure of reactor
            productivity calculated from mass of (desired/target) product formed, devided by the the reactor volume, and
            residence time. [doi:10.1002/cmtd.202000044]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/StoichiometryRatio">
        <rdfs:subClassOf rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/VolumeFraction"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/ReactionCondition"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/indicatesMultiplicityOf"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/InputChemical"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The ratio between an input chemical and the
            reference input chemical which is quantified by a reaction scale.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/TargetProduct">
        <rdfs:subClassOf rdf:resource="http://www.theworldavatar.com/ontology/ontokin/OntoKin.owl#Product"/>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">The product that is the desired outcome of
            a reaction experiment.
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontoreaction/Yield">
        <rdfs:subClassOf
                rdf:resource="http://www.ontology-of-units-of-measure.org/resource/om-2/AmountOfSubstanceFraction"/>
        <rdfs:subClassOf rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/PerformanceIndicator"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="https://www.theworldavatar.com/kg/ontoreaction/yieldLimitingSpecies"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="http://www.theworldavatar.com/ontology/ontospecies/OntoSpecies.owl#Species"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Ratio expressing the efficiency of a mass
            conversion process. [doi:10.1351/goldbook.Y06724]
        </rdfs:comment>
        <rdfs:isDefinedBy rdf:datatype="http://www.w3.org/2001/XMLSchema#string">
            https://www.theworldavatar.com/kg/ontoreaction/
        </rdfs:isDefinedBy>
    </owl:Class>

    <owl:Class rdf:about="https://www.theworldavatar.com/kg/ontovapourtec/VapourtecR4Reactor"/>
</rdf:RDF>

You are an assistant to structure user provided input text description in OWL/RDF format using the provided ontoreaction ontology above exclusively. You need to generate the OWL instantiation of the text provided by the user. You are strictly instructed to not introduce any hypothetical classes or properties that are not in the ontoreaction ontology specification above. You are strictly also instructed to not assume existence of properties or classes not in the given ontoreaction specification. Simply structure the input from the user with the ontoreaction ontology above, formatted appropriately for OWL representation. Furthermore, do not provide output as an example. Provide an actual structured representation of the text from the user that fit the precise details and terms from the ontoreaction ontology provided for accurate representation that the user can simply import in their ontology management system. The output should be in RDF format inside one xml code block."""

SYSTEM_PROMPT_SOO = """Read the complete specification of the Onto Reaction (ontoreaction) ontology in OWL format specified below. Thoroughly understand and remember the provided ontology exactly.

<?xml version="1.0"?>
<rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/"
         xmlns:owl="http://www.w3.org/2002/07/owl#"
         xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
         xmlns:xml="http://www.w3.org/XML/1998/namespace"
         xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
         xmlns:skos="http://www.w3.org/2004/02/skos/core#"
         xml:base="http://www.ontosynthesis.org/SOO/">
    <owl:Ontology rdf:about="http://www.ontosynthesis.org/SOO">
        <dc:creator>Qianxiang Ai</dc:creator>
        <dc:creator>Cullen Klein</dc:creator>
        <dc:license>http://creativecommons.org/licenses/by/4.0/</dc:license>
        <dc:title>Synthesis Operation Ontology (SOO)</dc:title>
        <skos:definition>SOO (Synthesis Operation Ontology) is a domain ontology for common operations in organic
            synthesis.
        </skos:definition>
        <skos:note>Synthesis Operation Ontology (SOO) is a domain ontology developed for common operations used in
            organic synthesis. The applications of this ontology include
            1. To accurately represent synthesis procedures;
            2. To identify differences between syntheses performed on different hardware platforms;
            3. To facilitate interoperation, such as performing the same synthesis procedure on different hardware
            platforms;
            4. To help troubleshooting procedures by reasoning over operation effects.
        </skos:note>
    </owl:Ontology>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Annotation properties
//
///////////////////////////////////////////////////////////////////////////////////////
 -->

    <owl:AnnotationProperty rdf:about="http://purl.org/dc/elements/1.1/creator"/>
    <owl:AnnotationProperty rdf:about="http://purl.org/dc/elements/1.1/description"/>
    <owl:AnnotationProperty rdf:about="http://purl.org/dc/elements/1.1/license"/>
    <owl:AnnotationProperty rdf:about="http://purl.org/dc/elements/1.1/title"/>
    <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#definition"/>
    <owl:AnnotationProperty rdf:about="http://www.w3.org/2004/02/skos/core#note"/>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Object Properties
//
///////////////////////////////////////////////////////////////////////////////////////
 -->
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000000">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000124"/>
        <rdfs:range rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">is dependent on</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000003">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
        <rdfs:label xml:lang="en">has first step</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000004">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
        <rdfs:label xml:lang="en">has second step</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000005">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
        <rdfs:label xml:lang="en">has third step</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000006">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:domain rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:range rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
        <rdfs:label xml:lang="en">has separation input</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000007">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000026"/>
        <rdfs:label xml:lang="en">has separation output</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000008">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
        <rdfs:range>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:range>
        <rdfs:label xml:lang="en">operates on</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000015">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#TransitiveProperty"/>
        <rdfs:label xml:lang="en">has part</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000016">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#TransitiveProperty"/>
        <rdfs:label xml:lang="en">has proper part</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000023">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label xml:lang="en">has input</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000024">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000023"/>
        <rdfs:domain rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
        <rdfs:range rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
        <rdfs:label xml:lang="en">has material input</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000025">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label xml:lang="en">has output</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000026">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000025"/>
        <rdfs:label xml:lang="en">has material output</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000027">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label xml:lang="en">is contained by</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000029">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
        <rdfs:range rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000014"/>
        <rdfs:label xml:lang="en">is environed by</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000095">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:range>
        <rdfs:label xml:lang="en">is preceded by</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000101">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label xml:lang="en">has start location</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000102">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:label xml:lang="en">has end location</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000115">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:range rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">is realized by</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000128">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000120"/>
        <rdfs:label xml:lang="en">describes</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000133">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has pH adjusting material</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000135">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000095"/>
        <rdfs:domain>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:domain>
        <rdfs:range>
            <owl:Class>
                <owl:unionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
                </owl:unionOf>
            </owl:Class>
        </rdfs:range>
        <rdfs:label xml:lang="en">is immediately preceded by</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000280">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has washing solvent</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000281">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has mobile phase</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000282">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has extracting solvent</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000283">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has sparging gas</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000287">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has crystallizing anti-solvent</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000288">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has precipitation salt</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000289">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has recrystallizing solvent</rdfs:label>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000292">
        <rdfs:subPropertyOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
        <rdfs:label xml:lang="en">has dispersive solvent</rdfs:label>
    </owl:ObjectProperty>
    <!-- 
///////////////////////////////////////////////////////////////////////////////////////
//
// Classes
//
///////////////////////////////////////////////////////////////////////////////////////
 -->
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000">
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000026"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000029"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000014"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">material process</rdfs:label>
        <skos:definition>A material process is a process that invloves
            1. any change of the physical and/or chemical qualities, including location, of any materials;
            2. creation, destroy, or transformation of any materials.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000001">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000315"/>
        <rdfs:label xml:lang="en">syringe plunger</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/equipment#AFE_0000746</rdfs:seeAlso>
        <skos:definition>The plunger of a syringe. Sometimes it cannot be detached from the syringe tube.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000011">
        <rdfs:label xml:lang="en">hardware unit</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/equipment#AFE_0000354</rdfs:seeAlso>
        <skos:definition>A physical thing that is designed to perform a function, as a whole or as a component,
            primarily by means of its mechanical or electrical nature.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000014">
        <rdfs:label xml:lang="en">environment</rdfs:label>
        <skos:definition>An environment is a spatial region within which some assumptions are made about the material
            processes that happen inside this region.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000030">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
        <rdfs:comment>when should we explicitly define an auxiliary material input?
            If it will be in contact with our main inputs/outputs
            e.g. the mobile phase of chromatography should be defined as &apos;has mobile phase&apos;
            counter e.g. the water running through a condenser
        </rdfs:comment>
        <rdfs:label xml:lang="en">physical process</rdfs:label>
        <skos:definition>A material process in or after which no chemical species are created or destroyed.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000031">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
        <rdfs:label xml:lang="en">chemical process</rdfs:label>
        <skos:definition>A material process in or after which one or more chemical species are created or destroyed.
        </skos:definition>
        <skos:note>A chemical process often concurs with a physical process. E.g. A reaction that requires temperature
            change.
        </skos:note>
        <skos:note>Any interface electron transfer is a chemical transformation.</skos:note>
        <skos:note>Example 1: A HCl aqueous solution is being mixed with a NaOH solution;
            Example 2: Ball-milling;
            Example 3: Accumulation of static charges on a surface;
            Example 4: Electrolysis of AgCl aqueous solution.
            Counter example 1: Current passing through a copper wire.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000032">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000030"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000007"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000026"/>
                <owl:minQualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">2
                </owl:minQualifiedCardinality>
                <owl:onClass rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000006"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">separating</rdfs:label>
        <skos:definition>A physical process with the intention to divide a portion of material into two or more portions
            of material whose physical or chemical qualities are different from each other.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000033">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:comment>todo
            mixture sublimating
            fractional sublimating
            vacuum sublimating
            freeze drying
        </rdfs:comment>
        <rdfs:label xml:lang="en">separating by volatility difference</rdfs:label>
        <skos:definition>A separating process based on the volatility difference among individual components.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000034">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000033"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">mixture evaporating</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001574</rdfs:seeAlso>
        <skos:definition>The physical process by which a liquid substance is converted to a gas or vapour. This may
            occur at or below the normal boiling point of the liquid (the temperature at which a liquid boils at 1
            atmosphere pressure) and the process is endothermic.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000039">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000033"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                            <owl:Restriction>
                                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000215"/>
                            </owl:Restriction>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:someValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000006"/>
                <owl:qualifiedCardinality rdf:datatype="http://www.w3.org/2001/XMLSchema#nonNegativeInteger">1
                </owl:qualifiedCardinality>
                <owl:onClass rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">distillating</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001532</rdfs:seeAlso>
        <skos:definition>A method of separating mixtures based on differences in their volatilities in a boiling liquid
            mixture. The components in a sample mixture are vaporised by the application of heat and then cooled by the
            action of cold water in a condenser.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000040">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:label xml:lang="en">separating by grain size</rdfs:label>
        <skos:definition>A separating process based on the grain size difference among individual components. This
            process implies the separating input is already microscopically separated.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000041">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000040"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000127"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">filtering</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/function#AFFN_0000049</rdfs:seeAlso>
        <skos:definition>A separating process by preventing the flow of certain entities based on a quality or qualities
            of the entity while allowing entities which have different qualities to pass through.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000042">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:label xml:lang="en">separating by solubility difference</rdfs:label>
        <skos:definition>A separating process based on the solubility difference among individual components.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000043">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000042"/>
        <rdfs:label xml:lang="en">precipitating</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001688</rdfs:seeAlso>
        <skos:definition>The sedimentation of a solid material (a &apos;precipitate&apos;) from a liquid solution in
            which the material is present in amounts greater than its solubility in the liquid.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000044">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000043"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">crystallizing</rdfs:label>
        <skos:definition>A precipitating process where the precipitates are of crystalline phase.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000045">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000044"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000287"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">anti-solvent crystallizing</rdfs:label>
        <skos:definition>A crystallizing process induced by combining the separation input with an anti-solvent which
            decreases the solubility of the desired component in the separation input.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000046">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000043"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000288"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000086"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">salting out</rdfs:label>
        <skos:definition>A precipitating process induced by combining the separation input with a portion of material,
            often a salt, that increaes the ionic strength of the separation input, which reduces the solubility of the
            desired component.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000047">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000042"/>
        <rdfs:label xml:lang="en">degassing</rdfs:label>
        <skos:definition>A solubility difference-based separating process with the intention to remove some gaseous
            components previously dissolved in the separation input.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000048">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000042"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000280"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">washing material</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/OBI_0302888</rdfs:seeAlso>
        <skos:definition>Washing is a process by which a material entity acting as contaminant (e.g. excess staining
            reagent) is removed by application of one or more cycles of solution in flow.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000049">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000044"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000289"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">recrystallizing</rdfs:label>
        <skos:definition>A crystallizing process starting by dissolving the solid state separation input in a solvent at
            an elevated temperature followed by crystallizing the desired component by gradually cooling.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000050">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000042"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000282"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">liquid-liquid extracting</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001600</rdfs:seeAlso>
        <skos:definition>The process of transferring a dissolved substance from one liquid phase to another (immiscible
            or partially miscible) liquid phase in contact with it.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000052">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:label xml:lang="en">separating by affinity difference</rdfs:label>
        <skos:definition>A separating process based on the interaction strength between individual components and an
            auxiliary material.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000053">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000032"/>
        <rdfs:label xml:lang="en">separating by mass difference</rdfs:label>
        <skos:definition>A separating process based on the density difference among individual components.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000054">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000104"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                            <owl:Restriction>
                                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
                            </owl:Restriction>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:someValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <owl:disjointWith rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000105"/>
        <rdfs:label xml:lang="en">controlling material quality</rdfs:label>
        <skos:definition>Controlling the quality of some material during the process. This requires some controller.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000055">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000054"/>
        <rdfs:label xml:lang="en">controlling temperature</rdfs:label>
        <skos:definition>Controlling the temperature of some material during the process.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000056">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000054"/>
        <rdfs:label xml:lang="en">controlling volume</rdfs:label>
        <skos:definition>Controlling the volume of some material during the process.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000057">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000054"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000133"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:comment>Alternatively, this can be defined as a composite material process that has a proper part of
            combining pH adjusting material and the material whose pH is being controlled.
        </rdfs:comment>
        <rdfs:label xml:lang="en">controlling pH</rdfs:label>
        <skos:definition>Controlling the pH of some material during the process. This requires adding some pH
            controlling agent.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000058">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000030"/>
        <rdfs:label xml:lang="en">transporting</rdfs:label>
        <skos:definition>A physical process with the intention to change the location of some portion of material.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000059">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000030"/>
        <rdfs:comment>1. This process can also increase the interfacial contact among different phases (e.g.,
            solid-liquid, liquid-liquid, gas-liquid).
            2. This process is usually intentionally induced by agitating, but can also be a &quot;side process&quot;
            of, e.g., bulk transfer.
        </rdfs:comment>
        <rdfs:comment>This process often assumes the existence of at least one container that defines the physical
            boundaries of this process.
        </rdfs:comment>
        <rdfs:label xml:lang="en">mixing</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/process#AFP_0001135</rdfs:seeAlso>
        <skos:definition>A process during or after which both the distribution of chemical composition and the
            distribution of thermal energy, often within a container, become more even.
            Example 1: The spontaneous expansion of a gas sample after being injected to a vacuum chamber.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000060">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000059"/>
        <rdfs:label xml:lang="en">dissolving</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/process#AFP_0000112</rdfs:seeAlso>
        <skos:definition>A mixing step where a soluble component is mixed with a liquid component.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000061">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000059"/>
        <rdfs:label xml:lang="en">homogenizing</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/process#AFP_0001649</rdfs:seeAlso>
        <skos:definition>The intensive mixing of mutually insoluble phases (sometimes with addition of surfactants) to
            obtain a soluble suspension or emulsion.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000062">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000030"/>
        <rdfs:label xml:lang="en">phase transitioning</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000063">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">evaporating</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from liquid to
            gas.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000064">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">sublimating</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from solid to
            gas.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000065">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">melting</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from solid to
            liquid.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000066">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">freezing</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from liquid to
            solid.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000067">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">condensing</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from gas to
            liquid.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000068">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000062"/>
        <rdfs:label xml:lang="en">depositing</rdfs:label>
        <skos:definition>A process during or after which the state of matter of some material is changed from gas to
            solid.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000078">
        <rdfs:label xml:lang="en">portion of material</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0000993</rdfs:seeAlso>
        <skos:definition>A thing that is spatially extended whose identity is independent of that of other entities and
            whose chemical composition can be reasonably estimated.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000079">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
        <rdfs:label xml:lang="en">portion of mixed material</rdfs:label>
        <skos:definition>A portion of material resulted from combining compositionally different portions of material.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000080">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000079"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000090"/>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <owl:disjointWith rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000084"/>
        <rdfs:label xml:lang="en">heterogeneous mixture</rdfs:label>
        <skos:definition>A portion of mixed material that is not a homogeneous mixture.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000081">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000080"/>
        <owl:disjointWith rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000083"/>
        <rdfs:label xml:lang="en">suspension</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/material#AFM_0000442</rdfs:seeAlso>
        <skos:definition>A suspension is a heterogeneous mixture in which the solute particles do not dissolve but get
            suspended throughout the bulk of the medium. [Wikipedia]
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000082">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000081"/>
        <rdfs:label xml:lang="en">spray</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/material#AFM_0000494</rdfs:seeAlso>
        <skos:definition>A spray is a heterogeneous mixture where a small amount of liquid is dispersed into a gas.
            [Allotrope]
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000083">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000080"/>
        <rdfs:label xml:lang="en">dispersion</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/material#AFM_0001079</rdfs:seeAlso>
        <skos:definition>A dispersions is a heterogeneous mixture that is comprising more than one phase where at least
            one of the phases consists of finely divided phase domains, often in the colloidal size range, dispersed
            throughout a continuous phase. [IUPAC]
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000084">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000079"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000086"/>
        <rdfs:label xml:lang="en">homogeneous mixture</rdfs:label>
        <skos:definition>A homogeneous mixture is a potion of mixed material whose intensive property does not vary
            throughout the space it occupies.
        </skos:definition>
        <skos:note>Note this definition is not limited to compositionally homogeneous.
            Example 1: A mixture of water and ice is not a homogeneous mixture.
            Example 2: A mixture of diamond and graphite is not a homogeneous mixture.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000085">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000084"/>
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:label xml:lang="en">liquid solution</rdfs:label>
        <skos:definition>A homogeneous mixture of liquid phase that can be made by mixing one or more solvents and one
            or more solutes.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000086">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
        <owl:disjointWith rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000090"/>
        <rdfs:label xml:lang="en">uniphase material</rdfs:label>
        <skos:definition>A uniphase material is a portion of material that exists in a single phase.</skos:definition>
        <skos:note>Note the &quot;phase&quot; here is equivalent to the state of matter that can only be one of solid,
            liquid, gas, and plasma.
            Example 1: A mixture of ice and water is a multiphase material.
            Example 2: A solid mixture of magnetite and hematite crystals is a uniphase material.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000087">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000086"/>
        <rdfs:label xml:lang="en">solid material</rdfs:label>
        <skos:definition>A material of solid phase.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000089">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000086"/>
        <rdfs:label xml:lang="en">liquid material</rdfs:label>
        <skos:definition>A material of liquid phase.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000090">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
        <rdfs:label xml:lang="en">multiphase material</rdfs:label>
        <skos:definition>A multiphase material is a portion of material that exists in more than one phase.
        </skos:definition>
        <skos:note>Note the &quot;phase&quot; here is equivalent to the state of matter that can only be one of solid,
            liquid, gas, and plasma.
            Example 1: A mixture of ice and water is a multiphase material.
            Example 2: A solid mixture of magnetite and hematite crystals is a uniphase material.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091">
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">functional module</rdfs:label>
        <skos:definition>A functional module is a set of hardware units that, as a whole, can realize some process.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000092">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">process controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000093">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
                        <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:label xml:lang="en">composite material process</rdfs:label>
        <skos:definition>A composite material process is a material process that can be described as the combination of
            more than one material process.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000096">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">feedback controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000097">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">feedforward controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000099">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">material transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000104">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000030"/>
        <rdfs:label xml:lang="en">changing material quality</rdfs:label>
        <skos:definition>A process during or after which the quality of some material is changed.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000105">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000104"/>
        <rdfs:label xml:lang="en">changing material quality without control</rdfs:label>
        <skos:definition>Changing the quality of some material without controlling.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000106">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000105"/>
        <rdfs:label xml:lang="en">changing temperature without control</rdfs:label>
        <skos:definition>Changing the temperature of some material without controlling.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000107">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">pH controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000108">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">temperature controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000109">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">process endpoint controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000114">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000096"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000109"/>
        <rdfs:label xml:lang="en">aliquoting controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000116">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
        <rdfs:label xml:lang="en">material quantity controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000117">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000116"/>
        <rdfs:label xml:lang="en">material volume controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000118">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000116"/>
        <rdfs:label xml:lang="en">material mass controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000119">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000099"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
                        <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000092"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:label xml:lang="en">controlled material transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000120">
        <rdfs:label xml:lang="en">information entity</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/IAO_0000030</rdfs:seeAlso>
        <skos:definition>A generically dependent continuant that is about some thing.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000121">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000120"/>
        <rdfs:label xml:lang="en">instrument calibration</rdfs:label>
        <skos:definition>An information entity that describes the calibration of a hardware unit.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000122">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000120"/>
        <rdfs:label xml:lang="en">reaction procedure</rdfs:label>
        <skos:definition>An information entity that describes the procedure of a chemical reaction.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000123">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000014"/>
        <rdfs:label xml:lang="en">lab environment</rdfs:label>
        <skos:definition>A lab environment is the spatially smallest environment encompassing all material processes
            that are of interest. A lab environment is often described by a list of parameters e.g., temperature,
            humidity, which assumes some default material processes would happen in this environment.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000124">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000014"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000000"/>
                <owl:someValuesFrom>
                    <owl:Class>
                        <owl:unionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000304"/>
                        </owl:unionOf>
                    </owl:Class>
                </owl:someValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">module environment</rdfs:label>
        <skos:definition>A module environment is the environment encompassed by a functional module. It is usually
            dependent on this functional module.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000125">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000124"/>
        <rdfs:label xml:lang="en">reflux environment</rdfs:label>
        <skos:definition>A reflux environment is the environment that assumes a reflux process by which volatile
            material components that would otherwise escape from the module are condensed and reintroduced into the
            module.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000126">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000124"/>
        <rdfs:label xml:lang="en">container environment</rdfs:label>
        <skos:definition>A container environment is the environment that depends on a container.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000127">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000134"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">filtration module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000129">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000078"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000027"/>
                        <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000304"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:label xml:lang="en">contained material</rdfs:label>
        <skos:definition>A portion of material that is spatially refined by a hardware unit.</skos:definition>
        <skos:note>Example 1: Water in a jar.
            Example 2: Aceton held in a pipette.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000130">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000099"/>
        <rdfs:label xml:lang="en">solid transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000131">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000099"/>
        <rdfs:label xml:lang="en">liquid transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000134">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">filter</rdfs:label>
        <skos:definition>A hardware unit that selectively allows passing portions of material through it.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000137">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000139"/>
        <rdfs:label xml:lang="en">combining materials to quench reaction</rdfs:label>
        <skos:definition>A combining materials process with the purpose to quench an ongoing reaction.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000138">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000106"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000188"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">quench cooling</rdfs:label>
        <skos:definition>Quench a reaction by applying cooling without controlling the temperature. E.g., applying ice
            bath.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000139">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000093"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000003"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000058"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000003"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000059"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">combining materials</rdfs:label>
        <skos:definition>A combining materials process is to combining more than one portions of materials in a
            container.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000140">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000059"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000141"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">mixing with agitation</rdfs:label>
        <skos:definition>A mixing process induced by an agitator module.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000141">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">agitator module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000142">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000210"/>
        <rdfs:label xml:lang="en">magnetic stirrer module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000143">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000058"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000131"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
                <owl:allValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000129"/>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:allValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000026"/>
                <owl:allValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000129"/>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:allValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">liquid transporting</rdfs:label>
        <skos:definition>A transporting process that transports some liquid.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000144">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000058"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000130"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000024"/>
                <owl:allValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000087"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000129"/>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:allValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000026"/>
                <owl:allValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000087"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000129"/>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:allValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">solid transporting</rdfs:label>
        <skos:definition>A transporting process that transports some solid.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000145">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000131"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000117"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">positive displacement liquid transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000146">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000131"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000016"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000117"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">air displacement liquid transporter module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000147">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000130"/>
        <rdfs:label xml:lang="en">solid hopper module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000149">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000146"/>
        <rdfs:label xml:lang="en">syringe pump module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000163">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">[JUNIOR] component</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000164">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:label xml:lang="en">[JUNIOR] Z1 Syringe Pump</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000165">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000258"/>
        <rdfs:label xml:lang="en">[JUNIOR] Deck</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000166">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000274"/>
        <rdfs:label xml:lang="en">[JUNIOR] Z2 Robot Arm</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000168">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000318"/>
        <rdfs:label xml:lang="en">[JUNIOR] Z1 Syringe</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000169">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000316"/>
        <rdfs:label xml:lang="en">[JUNIOR] Positive Displacement Pipette Tip</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000170">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000275"/>
        <rdfs:label xml:lang="en">[JUNIOR] Positive Displacement Pipette Head</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000171">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000262"/>
        <rdfs:label xml:lang="en">[JUNIOR] Vial Rack Slot (off-deck)</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000174">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000263"/>
        <rdfs:label xml:lang="en">[JUNIOR] Positive Displacement Pipette Tip Rack</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000175">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000262"/>
        <rdfs:label xml:lang="en">[JUNIOR] Positive Displacement Pipette Head Slot</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000176">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000262"/>
        <rdfs:label xml:lang="en">[JUNIOR] Rack Gripper Head Slot</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000180">
        <rdfs:label xml:lang="en">operation</rdfs:label>
        <skos:definition>An operation is a process actively initiated by an agent.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000182">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000008"/>
                <owl:someValuesFrom>
                    <owl:Class>
                        <owl:unionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                        </owl:unionOf>
                    </owl:Class>
                </owl:someValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">hardware operation</rdfs:label>
        <skos:definition>A hardware operation is an operation that changes the state of some hardware unit.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000183">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000052"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000184"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000281"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000183"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">chromatography separating</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/process#AFP_0001321</rdfs:seeAlso>
        <skos:definition>A chromatography is a separation where the components are distributed between two phases, one
            of which is stationary, while the other moves in a definite direction.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000184">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:label xml:lang="en">chromatography module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000185">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000053"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000186"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">centrifugating</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/OBI_0302886</rdfs:seeAlso>
        <skos:definition>A process separating molecules by density using centrifugal forces generated by a spinning
            rotor.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000186">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:label xml:lang="en">centrifugation module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000187">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000146"/>
        <rdfs:label xml:lang="en">manual pipette module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000188">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">cooling module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000191">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000109"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">endpoint controlled process</rdfs:label>
        <skos:definition>An endpoint controlled process is a material process that does not have an a priori defined
            endpoint, so its termination depends on an endpoint controller.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000193">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000182"/>
        <rdfs:label xml:lang="en">prepare equipment</rdfs:label>
        <skos:definition>A hardware operation that sets up the hardware unit so it is ready for other operations.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000194">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">clean hardware unit</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000195">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">dry hardware unit</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000196">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">lubricate joint</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000197">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">assemble hardware units</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000198">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">disassemble hardware unit</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000199">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:label xml:lang="en">prepare glassware</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000200">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000199"/>
        <rdfs:label xml:lang="en">to clean glassware</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000201">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000200"/>
        <rdfs:label xml:lang="en">to wash with detergent</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000202">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000200"/>
        <rdfs:label xml:lang="en">to base bath</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000203">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000199"/>
        <rdfs:label xml:lang="en">to dry glassware</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000204">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000193"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000008"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000303"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">prepare container</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000205">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000204"/>
        <rdfs:label xml:lang="en">to seal container</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000206">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000204"/>
        <rdfs:label xml:lang="en">to cap</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000207">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000204"/>
        <rdfs:label xml:lang="en">to decap</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000208">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000204"/>
        <rdfs:label xml:lang="en">to purge</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000209">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000144"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000119"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">weighing</rdfs:label>
        <skos:definition>A solid transporting process with the intention to measure the mass of the solid that is being
            transported.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000210">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000141"/>
        <rdfs:label xml:lang="en">stirrer module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000211">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000210"/>
        <rdfs:label xml:lang="en">overhead stirrer module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000212">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000141"/>
        <rdfs:label xml:lang="en">sonicator module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000213">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000141"/>
        <rdfs:label xml:lang="en">vortexer module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000214">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000141"/>
        <rdfs:label xml:lang="en">shaker module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000215">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">heating module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000216">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000118"/>
        <rdfs:label xml:lang="en">source mass controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000217">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000118"/>
        <rdfs:label xml:lang="en">target mass controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000218">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000116"/>
        <rdfs:label xml:lang="en">material flow controller</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000219">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000131"/>
        <rdfs:label xml:lang="en">steeredly pouring liquid module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000220">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000124"/>
        <rdfs:label xml:lang="en">airtight environment</rdfs:label>
        <skos:definition>An airtight environment is an environment that does not allow material transporting across its
            boundary.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000245">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000317"/>
        <rdfs:label xml:lang="en">[JUNIOR] Z1 Syringe Needle</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000258">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">hardware unit container</rdfs:label>
        <skos:definition>A hardware unit used to contain other hardware units. E.g., a vial rack.</skos:definition>
        <skos:note>Note: A well plate should not be considered as a hardware unit container as it directly holds some
            portions of material.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000260">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000263"/>
        <rdfs:label xml:lang="en">[JUNIOR] Vial Rack</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000262">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000258"/>
        <rdfs:label xml:lang="en">hardware unit slot</rdfs:label>
        <skos:definition>A well-shaped location that is used to hold one or more hardware units.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000263">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000258"/>
        <rdfs:label xml:lang="en">hardware unit rack</rdfs:label>
        <skos:definition>A rack that is used to hold one or more hardware units.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000274">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">robot arm</rdfs:label>
        <skos:definition>A hardware unit that can move in space. It is often mounted on a base and is motor-driven.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000275">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">robot arm attachment</rdfs:label>
        <skos:definition>An attachment of a robot arm, often used to hold specific hardware units.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000276">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000093"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000003"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000058"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000000004"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000058"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">rinse addition</rdfs:label>
        <skos:definition>A rinse addition process is an addition of A (a contained material) followed by rinsing the
            container of A with a specific liquid B, and the addition of B.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000277">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000047"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000285"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">freeze-pump-thaw</rdfs:label>
        <skos:definition>A degassing process by freezing the separation input to reduce the solubility of gaseous
            components, then reducing the pressure to extract the gaseous components, followed by gradually thawing the
            frozen input.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000278">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000047"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000284"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">sparging</rdfs:label>
        <skos:definition>A degassing process by introducing a flow of gas that has little or no partial pressure of the
            gas(es) to be removed.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000279">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">separating module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000284">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000099"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">sparging module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000285">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000188"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000286"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">freeze-pump-thaw module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000286">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000279"/>
        <rdfs:label xml:lang="en">pressure reducing module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000290">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000050"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000292"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000089"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">dispersive liquid-liquid microextraction</rdfs:label>
        <rdfs:seeAlso>https://doi.org/10.1016/j.chroma.2006.03.007</rdfs:seeAlso>
        <skos:definition>An liquid-liquid extracting process during which the mixture of extraction solvent and
            disperser solvent are rapidly injected into the separation input to form a cloudy solution of fine particles
            of extraction solvent which is dispersed entirely in the separation input. After centrifuging, the fine
            particles of extraction solvent are sedimented in the bottom of the centrifugation tube and extracted.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000291">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000050"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">funnel extraction</rdfs:label>
        <skos:definition>The separation input is placed in the funnel and an immiscible solvent is added, resulting in
            two layers that are shaken together and the layer in which the desired component has a higher relative
            solubility is kept.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000293">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000048"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">washing solid</rdfs:label>
        <skos:definition>A washing process where the material being washed is a solid.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000294">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000048"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">washing liquid</rdfs:label>
        <skos:definition>A washing process where the material being washed is a liquid.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000295">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000034"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000299"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">rotary evaporation</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001576</rdfs:seeAlso>
        <skos:definition>The removal of solvent from a sample by applying heat and lowering the pressure above the
            sample whilst rotating it at 10–300 rpm.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000296">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:label xml:lang="en">condensing module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000297">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000039"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                <owl:someValuesFrom>
                    <owl:Class>
                        <owl:intersectionOf rdf:parseType="Collection">
                            <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                            <owl:Restriction>
                                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000215"/>
                            </owl:Restriction>
                            <owl:Restriction>
                                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000286"/>
                            </owl:Restriction>
                        </owl:intersectionOf>
                    </owl:Class>
                </owl:someValuesFrom>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">vacuum distillating</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/CHMO_0001540</rdfs:seeAlso>
        <skos:definition>A method of separating mixtures based on differences in their volatilities in a boiling liquid
            mixture. The components in a high-boiling-point sample mixture are vaporised by the application of heat at
            low pressure and then cooled by the action of cold water in a condenser.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000299">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
        <rdfs:subClassOf>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000015"/>
                <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000286"/>
            </owl:Restriction>
        </rdfs:subClassOf>
        <rdfs:label xml:lang="en">rotary evaporating module</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000300">
        <owl:equivalentClass>
            <owl:Class>
                <owl:intersectionOf rdf:parseType="Collection">
                    <rdf:Description rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000000"/>
                    <owl:Restriction>
                        <owl:onProperty rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000115"/>
                        <owl:someValuesFrom rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000091"/>
                    </owl:Restriction>
                </owl:intersectionOf>
            </owl:Class>
        </owl:equivalentClass>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000180"/>
        <rdfs:label xml:lang="en">module operation</rdfs:label>
        <skos:definition>A module operation is a material process whose description necessitates defining one or more
            functional modules.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000301">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">condensor</rdfs:label>
        <rdfs:seeAlso>http://purl.obolibrary.org/obo/PROCO_0000178</rdfs:seeAlso>
        <skos:definition>A hardware unit used to condense vapors into liquid by cooling. It is often used with some
            coolant.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000302">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000163"/>
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000275"/>
        <rdfs:label xml:lang="en">[JUNIOR] Solid Hopper Head</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000303">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000011"/>
        <rdfs:label xml:lang="en">material holder</rdfs:label>
        <skos:definition>A hardware unit used to directly hold some portions of material.</skos:definition>
        <skos:note>Note: By definition some of this unit&apos;s surfaces would be in contact with some portions of
            material.
        </skos:note>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000304">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000303"/>
        <rdfs:label xml:lang="en">material container</rdfs:label>
        <skos:definition>A material holder desgined to contain some portions of material.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000305">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000304"/>
        <rdfs:label xml:lang="en">vial</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/equipment#AFE_0000329</rdfs:seeAlso>
        <skos:definition>A vial is a small vessel or bottle.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000306">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000305"/>
        <rdfs:label xml:lang="en">[JUNIOR] HRV</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000307">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000305"/>
        <rdfs:label xml:lang="en">[JUNIOR] MRV</rdfs:label>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000314">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000304"/>
        <rdfs:label xml:lang="en">well plate</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/equipment#AFE_0000029</rdfs:seeAlso>
        <skos:definition>A plate is a tray with multiple &quot;wells&quot; used as small test tubes.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000315">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000303"/>
        <rdfs:label xml:lang="en">material transporting component</rdfs:label>
        <skos:definition>A material holder that is a component of a hardware unit whose primary function is to transport
            some portions of material.
        </skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000316">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000315"/>
        <rdfs:label xml:lang="en">pipette tip</rdfs:label>
        <skos:definition>The tip of a pipette.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000317">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000315"/>
        <rdfs:label xml:lang="en">syringe needle</rdfs:label>
        <skos:definition>The needle of a syringe.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000318">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000315"/>
        <rdfs:label xml:lang="en">syringe tube</rdfs:label>
        <rdfs:seeAlso>http://purl.allotrope.org/ontologies/equipment#AFE_0000746</rdfs:seeAlso>
        <skos:definition>The tube of a syringe, also known as a barrel.</skos:definition>
    </owl:Class>
    <owl:Class rdf:about="http://www.ontosynthesis.org/SOO#SOO_0000322">
        <rdfs:subClassOf rdf:resource="http://www.ontosynthesis.org/SOO#SOO_0000262"/>
        <rdfs:label xml:lang="en">[JUNIOR] Balance Slot</rdfs:label>
    </owl:Class>
</rdf:RDF>

You are an assistant to structure user provided input text description in OWL/RDF format using the provided ontoreaction ontology above exclusively. You need to generate the OWL instantiation of the text provided by the user. You are strictly instructed to not introduce any hypothetical classes or properties that are not in the ontoreaction ontology specification above. You are strictly also instructed to not assume existence of properties or classes not in the given ontoreaction specification. Simply structure the input from the user with the ontoreaction ontology above, formatted appropriately for OWL representation. Furthermore, do not provide output as an example. Provide an actual structured representation of the text from the user that fit the precise details and terms from the ontoreaction ontology provided for accurate representation that the user can simply import in their ontology management system. The output should be in RDF format inside one xml code block."""
SYSTEM_PROMPTS = {
    "OntoReaction": SYSTEM_PROMPT_OntoReaction,
    "SOO": SYSTEM_PROMPT_SOO,
}


def extract_openai(
        unstructured_data: UnstructuredReactionDescription,
        api_key: str,
        ontology_name: str = "OntoReaction",
) -> str:
    if ontology_name not in SYSTEM_PROMPTS:
        raise NotImplementedError
    system_prompt = SYSTEM_PROMPTS[ontology_name]
    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {"role": "user", "content": unstructured_data.text}
        ],
        temperature=0,
        top_p=0.5,
    )
    completion: ChatCompletion
    content = completion.choices[0].message.content
    logger.info(f"completion:\n{content}")
    assert "```xml\n" in content, "xml code block not found in the completion!"
    assert content.count("```") == 2, "there should be only one complete code block"

    pattern = r'```xml(.*?)```'
    result = re.findall(pattern, content, re.DOTALL | re.MULTILINE)
    return result[0]
