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

SYSTEM_PROMPTS = {
    "OntoReaction": SYSTEM_PROMPT_OntoReaction,

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
