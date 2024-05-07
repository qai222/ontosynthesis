from __future__ import annotations

import json
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel, Field


def str_uuid():
    return str(uuid4())


def json_dump(o, fn):
    with open(fn, "w") as f:
        json.dump(o, f, indent=2)


class WritingStyle(str, Enum):
    PATENT = "PATENT"
    MAIN = "MAIN"
    SI = "SI"
    NOTEBOOK = "NOTEBOOK"


class METER(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class UnstructuredReactionDescription(BaseModel):
    """ text description of an organic reaction """

    identifier: str = Field(default_factory=str_uuid)
    """ identifier of this entry """

    text: str
    """ actual text of this entry """

    origin: str
    """ where does it come from? """

    structured_data: dict | None = None
    """ corresponding structured data, if any """

    structured_data_type: str | None = None
    """ type of the corresponding structured data """

    writing_style: WritingStyle
    """ writing style of the unstructured description """

    specificity: float | METER | None = None
    """ how specific is the description? """

    complexity: float | METER | None = None
    """ how complex is the chemical reaction? """


if __name__ == '__main__':
    DATA = []

    # origin = "ORD reaction_id: ord-82f3a3fd62de4975b120aaea7268aa24",
    DES = UnstructuredReactionDescription(
        text="Palladium acetate (45 mg, 0.2 mmol), BINAP (62 mg, 0.1 mmol) and cesium carbonate (650 mg, 2 mmol) were suspended in anhydrous 1,4-dioxane (3 ml) under an argon atmosphere and sonicated for 45 minutes. 2-Bromo-4-methylpyrimidine (173 mg, 1 mmol) and tert-butyl piperazine-1-carboxylate (208 mg, 1.3 mmol) were dissolved in 3 ml anhydrous 1,4-dioxane and the resulting solution was added to the catalyst-containing mixture. The resulting mixture was stirred at 110\u00b0 C. overnight, afterwards diluted with ethyl acetate and filtered. The filtrate was evaporated to dryness under reduced pressure and the residue was purified by column chromatography (silica, gradient from DCM to DCM/ethyl acetate 8/2) to yield 120 mg of a brown oil (0.43 mmol, 43%)",
        origin="ORD reaction_id: ord-82f3a3fd62de4975b120aaea7268aa24",
        structured_data=json.loads(
            "{\"inputs\": {\"m7\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"ethyl acetate\"}], \"reaction_role\": \"SOLVENT\"}]}, \"m8\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"Palladium acetate\"}], \"amount\": {\"mass\": {\"value\": 45.0, \"units\": \"MILLIGRAM\"}}, \"reaction_role\": \"CATALYST\"}]}, \"m1\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"BINAP\"}], \"amount\": {\"mass\": {\"value\": 62.0, \"units\": \"MILLIGRAM\"}}, \"reaction_role\": \"REACTANT\"}]}, \"m2\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"cesium carbonate\"}], \"amount\": {\"mass\": {\"value\": 650.0, \"units\": \"MILLIGRAM\"}}, \"reaction_role\": \"REACTANT\"}]}, \"m3_m4_m6\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"2-Bromo-4-methylpyrimidine\"}], \"amount\": {\"mass\": {\"value\": 173.0, \"units\": \"MILLIGRAM\"}}, \"reaction_role\": \"REACTANT\"}, {\"identifiers\": [{\"type\": \"NAME\", \"value\": \"tert-butyl piperazine-1-carboxylate\"}], \"amount\": {\"mass\": {\"value\": 208.0, \"units\": \"MILLIGRAM\"}}, \"reaction_role\": \"REACTANT\"}, {\"identifiers\": [{\"type\": \"NAME\", \"value\": \"1,4-dioxane\"}], \"amount\": {\"volume\": {\"value\": 3.0, \"units\": \"MILLILITER\"}}, \"reaction_role\": \"SOLVENT\"}]}, \"m5\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"1,4-dioxane\"}], \"amount\": {\"volume\": {\"value\": 3.0, \"units\": \"MILLILITER\"}}, \"reaction_role\": \"SOLVENT\"}]}}, \"conditions\": {\"temperature\": {\"setpoint\": {\"value\": 110.0, \"units\": \"CELSIUS\"}}, \"stirring\": {\"type\": \"CUSTOM\", \"details\": \"The resulting mixture was stirred at 110\\u00b0 C. overnight\"}, \"conditions_are_dynamic\": true}, \"workups\": [{\"type\": \"CUSTOM\", \"details\": \"sonicated for 45 minutes\", \"duration\": {\"value\": 45.0, \"units\": \"MINUTE\"}}, {\"type\": \"ADDITION\", \"details\": \"the resulting solution was added to the catalyst-containing mixture\"}, {\"type\": \"FILTRATION\", \"details\": \"filtered\"}, {\"type\": \"CUSTOM\", \"details\": \"The filtrate was evaporated to dryness under reduced pressure\"}, {\"type\": \"CUSTOM\", \"details\": \"the residue was purified by column chromatography (silica, gradient from DCM to DCM/ethyl acetate 8/2)\", \"input\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"DCM\"}], \"reaction_role\": \"WORKUP\"}, {\"identifiers\": [{\"type\": \"NAME\", \"value\": \"DCM ethyl acetate\"}], \"reaction_role\": \"WORKUP\"}]}}], \"outcomes\": [{\"reaction_time\": {\"value\": 8.0, \"precision\": 8.0, \"units\": \"HOUR\"}, \"products\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"brown oil\"}], \"measurements\": [{\"type\": \"AMOUNT\", \"details\": \"AMOUNT\", \"amount\": {\"moles\": {\"value\": 0.43, \"units\": \"MILLIMOLE\"}}}, {\"type\": \"AMOUNT\", \"details\": \"MASS\", \"amount\": {\"mass\": {\"value\": 120.0, \"units\": \"MILLIGRAM\"}}}, {\"type\": \"YIELD\", \"details\": \"PERCENTYIELD\", \"percentage\": {\"value\": 43.0}}, {\"type\": \"YIELD\", \"details\": \"CALCULATEDPERCENTYIELD\", \"percentage\": {\"value\": 43.0}}], \"isolated_color\": \"brown\", \"texture\": {\"type\": \"OIL\", \"details\": \"oil\"}, \"reaction_role\": \"PRODUCT\"}]}]}"),
        structured_data_type="ord.Reaction",
        writing_style=WritingStyle.PATENT,
        complexity=METER.LOW,
        specificity=METER.MEDIUM,
    )
    DATA.append(DES)

    # origin = "ORD reaction_id: ord-f1cb154ccbe14fc38a6a7306c214d1c6",
    DES = UnstructuredReactionDescription(
        text="In a flask equipped with a stirring blade and a dropping funnel were charged 100 parts of dry methylene chloride and 60 parts of ethylenediamine, and the mixture was stirred in an ice bath. To the solution was slowly added 105 parts of methacrylic chloride through the dropping funnel. After the addition, the mixture was allowed to react at room temperature for 5 hours. The white precipitate thus formed was collected by filtration, thoroughly washed with dry methylene chloride, and dried to obtain aminoethylmethacrylamide hydrochloride. Then, 600 parts of ion-exchanged water, 10 parts of the resulting aminoethylmethacrylamide hydrochloride, and 1.0 part of an anionic surface active agent (\"Perex OTP\" produced by Kao Co., Ltd.) were charged in a flask equipped with a stirring blade and a tube for nitrogen introduction, followed by stirring. To the mixture was added 70 parts of methyl methacrylate to form an emulsion. To the emulsion was added 200 parts of a 3% aqueous solution of potassium persulfate, and the system was heated to 50\u00b0 C., at which the emulsion was allowed to react for 24 hours. There were obtained fine particles of an aminoethylmethacrylamide hydrochloride/methyl methacrylate copolymer having an average particle size of 0.2 \u03bcm. The polymer particles were washed with water by means of a centrifugal separator. Then, 50.0 parts of the polymer particles was washed with a 5% sodium hydroxide aqueous solution to obtain fine particles of a methyl methacrylate copolymer having an amino group on the surface thereof.",
        origin="ORD reaction_id: ord-f1cb154ccbe14fc38a6a7306c214d1c6",
        structured_data=json.loads(
            "{\"inputs\": {\"m5_m1\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"aminoethylmethacrylamide hydrochloride\"}], \"reaction_role\": \"REACTANT\"}, {\"identifiers\": [{\"type\": \"NAME\", \"value\": \"water\"}], \"reaction_role\": \"SOLVENT\"}]}, \"m2\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"methyl methacrylate\"}], \"reaction_role\": \"REACTANT\"}]}, \"m3_m4\": {\"components\": [{\"identifiers\": [{\"type\": \"NAME\", \"value\": \"aqueous solution\"}], \"reaction_role\": \"REACTANT\"}, {\"identifiers\": [{\"type\": \"NAME\", \"value\": \"potassium persulfate\"}], \"reaction_role\": \"REACTANT\"}]}}, \"conditions\": {\"temperature\": {\"setpoint\": {\"value\": 50.0, \"units\": \"CELSIUS\"}}, \"stirring\": {\"type\": \"CUSTOM\", \"details\": \"by stirring\"}, \"conditions_are_dynamic\": true}, \"workups\": [{\"type\": \"ADDITION\", \"details\": \"were charged in a flask\"}, {\"type\": \"CUSTOM\", \"details\": \"equipped with a stirring blade and a tube for nitrogen introduction\"}, {\"type\": \"CUSTOM\", \"details\": \"to form an emulsion\"}, {\"type\": \"CUSTOM\", \"details\": \"to react for 24 hours\", \"duration\": {\"value\": 24.0, \"units\": \"HOUR\"}}], \"outcomes\": [{\"products\": [{\"reaction_role\": \"PRODUCT\"}]}]}"),
        structured_data_type="ord.Reaction",
        writing_style=WritingStyle.PATENT,
        complexity=METER.LOW,
        specificity=METER.HIGH,
    )
    DATA.append(DES)

    # origin = "ORD CRE id: ord-CRE-passage=10.1021/ja000238n-5-5-0",
    DES = UnstructuredReactionDescription(
        text="The reaction of ethylene ( 2b ) with 1a in 1,4-dioxane also gave the corresponding cyclo-pentenone 3e in 65 % yield ( eq 2 ) .",
        origin="ORD CRE id: ord-CRE-passage=10.1021/ja000238n-5-5-0",
        writing_style=WritingStyle.MAIN,
        complexity=METER.LOW,
        specificity=METER.LOW,
    )
    DATA.append(DES)

    # origin = "ORD CRE id: ord-CRE-passage=10.1021/ja00147a007-8-2-0",
    DES = UnstructuredReactionDescription(
        text="Analogous to 1's anodic oxidation dynamics , it appears that monomer 2m forms from 2'+ under CV conditions because the second oxidation wave is always observed , even from colorless solutions of 2 at low temperatures which must contain very little 2m.",
        origin="ORD CRE id: ord-CRE-passage=10.1021/ja00147a007-8-2-0",
        writing_style=WritingStyle.MAIN,
        specificity=METER.LOW,
        complexity=METER.MEDIUM,
    )
    DATA.append(DES)

    # origin = "SI of 10.1002/anie.201812537",  # the "just pour into salt water" one
    DES = UnstructuredReactionDescription(
        text="In a 50 mL round-bottom flask, NaCl (4.8 mmol, 281 mg), 1-bromonaphtalene (1a, 4.8 mmol, 1.0 g) and Pd[P(t-Bu)3]2 (2.5 mol%, 0.12 mmol, 61.3 mg) were sequentially added in 5 mL of deionized; water, at room temperature and in air. The mixture was vigorously stirred for 10 min. During this; time, the colour of the mixture changed from slightly yellow to dark orange. A solution of n-BuLi (2.64 mL, 2 M in cyclohexane, 5.28 mmol), handled under argon using conventional Schlenk; techniques, was rapidly spread over the mixture under air and with vigorous stirring at room temperature to generate an emulsion. Organolithiums, however, are notoriously prone to ignition in air, and caution should be exercised in adopting the recommended procedure, especially on a larger scale.] After 20 s, the reaction mixture was directly extracted with Et2O (3 mL). The organic layer was filtered through a Celite pad and the solvent was removed under reduced pressure. The crude; was purified by column chromatography on silica gel (hexane) to provide the desired product 2aa in; 99% yield (883 mg).",
        origin="SI of 10.1002/anie.201812537",
        writing_style=WritingStyle.SI,
        specificity=METER.HIGH,
        complexity=METER.MEDIUM,
    )
    DATA.append(DES)

    # origin = "SI of 10.1021/jacs.2c04807",  # the extreme one
    DES = UnstructuredReactionDescription(
        text="Stock solution 1 (copper catalyst): A stock solution was prepared such that 0.5 mL of stock contained 5 mol% Cu(terpy)Cl2 with respect to 0.05 mmol limiting reagent. This was accomplished by adding CuCl2 and terpyridine ligand to an 8 mL vial in a 1:1 molar ratio, backfilling with N2 twice and adding THF via syringe. The vial was then sealed with parafilm and sonicated until a fine, green suspension resulted (~15 minutes). After this time, 0.5 mL of this stock solution (corresponding to 5 mol% Cu(terpy)Cl2) was added to each reaction vial (1 or 2 dram) to be evaluated in a given screen. All reactions vials containing copper catalyst suspended in THF were concentrated via Genevac over the course of ~45 minutes. After this time, they were capped, backfilled with N2 (2x) and other reaction components were added via syringe as described below.\nStock solution 2 (other reaction components): A stock solution was prepared such that 1 mL of stock contained 1 mol% photocatalyst, 1.5 equiv. CF3 reagent and 2 equiv. TBACl. This was accomplished by adding photocatalyst, CF3 reagent and TBACl to a 40 mL vial under air, backfilling with N2 (2x) and adding DMSO via syringe. The vial was stirred until homogeneous to furnish stock solution 2. 1 mL of this stock solution was added to the 1- or 2-dram vial containing copper catalyst under nitrogen via syringe.\nStock solution 3 (activated alcohol): A stock solution was prepared such that 1 mL of stock contained 0.05 mmol (1 equiv.) of activated alcohol and 0.08 mmol quinuclidine (1.6 equiv.). This was accomplished through the following procedure: An oven dried 40 mL vial was charged with Alcohol (1 equiv., Note 1), NHC–1 (1.2 equiv.), and an X-shaped stir bar. The vessel was capped, evacuated, and backfilled with N2 three times before t-BuOMe (0.1 M with respect to alcohol) was introduced via syringe. The heterogeneous mixture was stirred vigorously for 5 minutes before Pyridine (1.2 equiv.) was added dropwise (~ 1 drop/5 seconds) via microsyringe. The heterogeneous mixture was vigorously stirred under nitrogen at room temperature for 15 minutes. During this time a white solid precipitated out and the mixture turned from white to paleorange to pale-pink. (If the alcohol is a liquid it was added as a solution in t-BuOMe). After stirring for 15 minutes, the t-BuOMe suspension of activated alcohol was transferred to a syringe under air. A syringe filter was installed, and the suspension was filtered in to a new 40 mL vial containing quinuclidine (1.6 equiv.) also under air (Note 2). Quantitative transfer of activated alcohol was ensured by washing the condensation vial with ~1.5 mL t-BuOMe followed by filtration through the same syringe filter (2x). t-BuOMe was then carefully concentrated in vacuo until the resulting pale-yellow oil displayed no visible changes in volume (~300 à ~150 mbar, 30 °C, ~5 minutes). The vial was then capped and backfilled with nitrogen (3x). The activated alcohol was then redissolved in DMSO (0.05 M with respect to activated alcohol) to furnish stock solution 3. 1 mL of this stock solution was added to the 1- or 2-dram vial containing copper catalyst and all other reaction components via syringe resulting in a final reaction volume of 2 mL (0.025 M with respect to activated alcohol). (Note 2)\nThe complete reaction vial was then sparged with N2 for ~5 minutes before being sealed with parafilm and irradiated with 450 nm LED modules at 100% light intensity with maximum fan speed and 1500 rpm stir rate in a PennOC or PennPhD Integrated Photoreactor for 8 hours. After this time, 1,4,-difluorobenzene (5.14 μL, 1 equiv.) was added as an internal standard via micropipette, and an aliquot was removed for analysis by 19F NMR. The above procedure was modified as necessary to screen desired variables but typically, three stock solutions (1) copper catalyst, (2) activated alcohol + quinuclidine and (3) all other reaction components were always prepared separately and then combined prior to irradiation with Blue LED’s.\nNote 1: This activated alcohol stock solution was typically prepared on > 0.2 mmol scale to ensure reproducible results.\nNote 2: 25 mm, Fisherbrand PTFE 0.2 μm syringe filters were used for this step. This size is effective up to 0.5 mmol of alcohol. Beyond this scale, two syringe filters of this size were required to filter the alcohol condensation mixture. Furthermore, it was found empirically that adding the quinuclidine base in the same stock solution as the activated alcohol led to more consistent results, presumably due to a stabilizing effect on the acid labile NHC-alcohol adduct. ",
        origin="SI of 10.1021/jacs.2c04807",
        writing_style=WritingStyle.SI,
        specificity=METER.HIGH,
        complexity=METER.HIGH,
    )
    DATA.append(DES)

    # origin = "BM: n_sulfonylation",
    DES = UnstructuredReactionDescription(
        text="R1 769-92-6 Amine 1.0eq\n R2 98-59-9 Sulfonyl-Cl 1.25eq\n R3 110-86-1 Pyridine 2.0eq\n S1 75-09-2 DCM\n R1 Concentration 0.2M\n P 697786-47-3 Sulfonamide\n \nScale 0.2 mmol limiting reactant\n \nConsumables List\nC1 10mL glass container with stir bar \n C2 20mL glass container\n \n Procedure\n 1. Add solid R2 to C1\n 2. Add S1 to C1\n 3. Start stirring contents of C1 at 500 rpm\n 4. Wait 5 minutes before next step with C1\n 5. Add liquid R1 to C1\n 6. Add liquid R3 to C1\n 7. Wait 1 hr before next step with C1\n 8. Add 1N HCl (0.5mL) to C1\n 9. Add water (3mL) to C1\n 10. Add DCM (3mL) to C1\n 11. Wait 30 minutes before next step with C1\n 12. Stop stirring C1\n 13. Decant/separate organic bottom layer from aqueous top layer. Organic layer into C2\n 14. Evaporate volatiles from C2\n 15. Submit contents of C2 to ACC purification\n",
        origin="BM: n_sulfonylation",
        writing_style=WritingStyle.NOTEBOOK,
        specificity=METER.HIGH,
        complexity=METER.LOW,
    )
    DATA.append(DES)

    # origin = "BM: alcohol_oxidation",
    DES = UnstructuredReactionDescription(
        text="R1 143426-50-0 triazolybenzenemethanol 1.0eq\n R2 2564-83-2 TEMPO 0.2eq\n R3 3240-34-4 BAIB 2.25eq\n \n S1 75-09-2 DCM	\n S2 7732-18-5 Water \n Ratio 1:1\n R1 Concentration 0.2M\n \n P 162848-16-0 Acid \n \n Consumables List\n 5mL MRV with stir bar\n 20mL HRV x 2\n 1 cartridge celite\n \n Scale 0.2 mmol limiting reactant\n \n Procedure\n 1. Add solid R1 to MRV\n 2. Add solid R2 to MRV\n 3. Add solid R3 to MRV\n 4. Add S1 to MRV (0.5mL)\n 5. Add S2 to MRV (0.5mL)\n 6. Stir at 500 rpm at room temperature\n 7. Wait 24 hours\n 8. Pour into 20mL HRV\n 9. Place HRV on V-10 and evaporate to dryness using 'Mixed' method.\n 10. Add methanol (3mL) to HRV\n 11. Pour contents of HRV into Celite cartridge\n 12. Collect eluting material into second HRV\n 13. Wash celite cartridge with methanol (3mL)\n 14. Place HRV on V-10 and evaporate to dryness using 'Volatile' method.\n 15. Submit for ACC purification\n",
        origin="BM: alcohol_oxidation",
        writing_style=WritingStyle.NOTEBOOK,
        specificity=METER.HIGH,
        complexity=METER.LOW,
    )
    DATA.append(DES)

    json_dump([d.model_dump() for d in DATA], "data_hackathon.json")
