
from owlready2 import onto_path, get_ontology
onto_path.append("/home/qai/workplace/ontosynthesis/protege/ontologies")
onto = get_ontology("file:///home/qai/workplace/ontosynthesis/protege/owx_dump/afo.owx").load()
    
Person = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001083")
# A person is a human that is member of a group or organization. [Allotrope]
    
Group = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001084")
# A group is a an aggregate of people. [Allotrope]
    
Organization = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001085")
# A collection of people organized together into a community or other social, commercial or political structure. The group has some common purpose or reason for existence which goes beyond the set of people belonging to it and can act as an agent. [W3C ORG]
    
FormalOrganization = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001086")
# A formal organization is an organization which is recognized in the world at large, in particular in legal jurisdictions, with associated rights and responsibilities. [W3C ORG]
    
OrganizationalUnit = onto.search_one(iri="http://purl.allotrope.org/ontologies/material#AFM_0001087")
# An organization such as a department or support unit which is part of some larger organization and only has full recognition within the context of that organization. In particular the unit would not be regarded as a legal entity in its own right. [W3C ORG]
    
Membership = onto.search_one(iri="http://purl.allotrope.org/ontologies/quality#AFQ_0000231")
# Membership is the relational quality between a group or organization and its members. [Allotrope]
    
Identifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000917")
# An identifier is a name that identifies (that is, labels the identity of) either a unique object or a unique class of objects, where the &quot;object&quot; or class may be an idea, physical [countable] object (or class thereof), or physical [uncountable] substance (or class thereof). [Wikipedia]
    
Facet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0000923")
# A facet is a partial information that contains an aspect of some information content entity or parts of it when participating in some process. The facet abstracts of the concrete representation of this aspect of information. [Allotrope]
    
FamilyName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001061")
# A family name is a name that is the portion (in some cultures) of a personal name that indicates a person&apos;s family (or tribe or community, depending on the culture). [Wikipedia]
    
GivenName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001062")
# A given name is a name that is a part of a person&apos;s personal name. [Wikipedia]
    
PersonalName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001063")
# A personal name is a name that is composed of a set of names by which an individual is known. [Allotrope]
    
CountryName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001064")
# A country name is a location facet that denotes a country. [Allotrope]
    
LocationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001065")
# A facet that is about some spatial region or site. [Allotrope]
    
HomepageHyperlink = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001066")
# A homepage hyperlink is a web page hyperlink that is a reference to home page of a person or organization. [Allotrope]
    
WebPageHyperlink = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001067")
# A web page hyperlink is a URL that is a reference to web page. [Allotrope]
    
Url = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001068")
# A Uniform Resource Locator (URL), colloquially termed a web address, is a reference to a web resource that specifies its location on a computer network and a mechanism for retrieving it. [Wikipedia]
    
LdapIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001069")
# An LDAP identifier is an online account managed by an LDAP server and follows the LDAP specification. [Allotrope]
    
LocalSystemAccountIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001070")
# An account to a local computer. [Allotrope]
    
Locality = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001071")
# A written name denoting a locality (e.g. city) as part a postal address. [Allotrope]
    
StreetAddress = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001078")
# The street address is a location facet of a postal address, that denotes a street. [Allotrope]
    
TelephoneNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001079")
# A number for calling a telephone. [Allotrope]
    
Title = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001080")
# A title is a prefix or suffix added to a personal name. A title can be a title of honor, that is a title bestowed as an award,  a honorary title (academic), that is a recognition of contributions by a non-employee or employee, a hereditary title, that is a title that remains in a family or a job title, that is a designation of a person&apos;s position in an organization. [Wikipedia]
    
HonorificPrefix = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001081")
# An honorific prefix is a facet that is part of a prefix to a person&apos;s name. [Allotrope]
    
CommunicationFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001082")
# A facet that is about communication channels. [Allotrope]
    
LocationName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001083")
# A location name is a location facet that denotes a geographical place. [Allotrope]
    
PostalCode = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001087")
# A postal code of a postal address. [Allotrope]
    
FaxNumber = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001480")
# A number for calling a fax system. [Allotrope]
    
SkypeIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001481")
# A Skype ID is an online account on the Skype system. [Allotrope]
    
HonorificSuffix = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001482")
# An honorific prefix is a facet that is part of a suffix to a person&apos;s name. [Allotrope]
    
Account = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001483")
# An account describes authority and authorization to access resources on a system. [Allotrope]
    
OnlineAccountIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001484")
# An account that is accessible via remote access. [Allotrope]
    
OpenidIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001485")
# OpenID is an identifier following the OpenID specification. [Allotrope]
    
Gender = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001486")
# The gender facet relates a human to a string representing its gender. [Allotrope]
    
Geolocation = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001488")
# A facet denoting a geographic position. [Allotrope]
    
RegionName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001489")
# A region name is a location facet that denotes a geographic region (state, province). [Allotrope]
    
Birthday = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001490")
# A birthday is a facet indicating the day of birth of a person. [Allotrope]
    
NickName = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001507")
# The nick name is a written name of person that is a substitute for the proper name of a familiar person, place, or thing - commonly used for affection. [Wikipedia]
    
PersonFacet = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0001682")
# A person facet is a facet that describes of a person&apos;s name or parts of it. [Allotrope]
    
AccountIdentifier = onto.search_one(iri="http://purl.allotrope.org/ontologies/result#AFR_0002770")
# An account identifier is an identifier, that identifies an account in a system that people or other systems use to access it. [Allotrope]
    
Head = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000402")
# Role that a organizational entity plays leader or formal head of the organization. [W3C ORG]
    
Post = onto.search_one(iri="http://purl.allotrope.org/ontologies/role#AFRL_0000403")
# A post is some position within an organization that exists independently of the person or persons filling it. Posts may be used to represent situations where a person is a member of an organization ex officio. [W3C ORG]
    
Site_organization = onto.search_one(iri="http://purl.allotrope.org/ontologies/spatial#AFSP_0000001")
# A site (organization) is a site where organizational entities are located such as an office or premise. [Allotrope]
    
PostalAddress = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000422")
# A textual entity that is used as directive to deliver something to a person, or organization. [IAO]
    
EmailAddress = onto.search_one(iri="http://purl.obolibrary.org/obo/IAO_0000429")
# An email address identifies an email box to which email messages are delivered. [Wikipedia]
    