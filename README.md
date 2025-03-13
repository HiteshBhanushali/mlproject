Hi Krishna,

I went through the 25.R1 patch release notes but couldn't find any mention of this change. Could you please share the specific section where it is documented?

Additionally, I have a couple of clarifications:

Tables converted to views – Will these views be refreshed automatically with the latest data as new transactions are recorded?
Base tables replaced by _SEC tables – Could you provide a list of tables where this change has been implemented, at least for the GL and PPM modules?


=-------------------------------
Hi Team,

There was a mention about this tables in the release notes :

https://docs.oracle.com/en/cloud/saas/analytics/25r1/fawwn/index.html#GUID-27505232-5CDD-41B3-9ED2-C253139B49CA

=================

Tables converted to views    
The following GL tables have been converted to views and the WHO columns have been removed from the views:
DW_GL_JOURNAL_CA
DW_GL_BALANCE_CF
DW_GL_BALANCE_CA
If you need to extract the Actuals data using the WHO columns, then use these tables instead with the ACTUAL_FLAG='A' filter:
DW_GL_JOURNAL_ALL_CA
DW_GL_BALANCE_ALL_CF
DW_GL_BALANCE_ALL_CA

====================

Since the old tables are converted to views the base tables are replaced by 

DW_GL_BALANCE_CA_SEC

DW_GL_BALANCE_CF_SEC

DW_GL_JOURNAL_CA_SEC

DW_GL_JOURNAL_CF_SEC

Currently there is no deprecation plan proposed on the existing GL views .

Since the old tables are exiting as views , your custom views will still work .

Regards,

Krishna.


I want to respond above discussion with below detail. can you please frame it accordingly?

Hi Krishna,

I have went through the release not of 25.R1 patch documnet but unable to find anything mentioned related to this change.

Can you please share the section where it is mentioned in the release note?

Tables converted to views -- Will this view will be refreshed with the latest data as and new data comes ?

old tables are converted to views the base tables are replaced by _SEC  --> Can you provide the list of tables where this change is implemented atleast for GL and PPM modules ?


================================
Got it! Here's the updated response:  

This candidate is a great fit for the **Consultant - Microservices & Spring Boot** role at Deloitte. With **6+ years of hands-on experience in Java, Spring Boot, and Microservices**, he exceeds the **3-6 years requirement** and brings strong expertise in **API development, enterprise integration, and cloud technologies (Azure DevOps).**  

He has successfully **migrated legacy applications (Struts & COBOL to Java EE), refactored a 15-year-old codebase (fixing 500+ Sonar issues), and built automated CI/CD pipelines**, demonstrating a solid grasp of **problem-solving, best practices, and DevOps.**  

Beyond technical skills, he has **experience working in Agile teams, collaborating with stakeholders, and ensuring high-quality, secure code**. His **Azure certifications and multiple performance awards** further prove his expertise and commitment.  

Overall, he ticks all the right boxes—**strong tech skills, problem-solving mindset, and a proven track record**—making him a perfect match for this role!

===============


======================
Below is the person's resume which i want to refer

MeProfessional ExperienceAwardsAmbitious, determined, and detail-oriented individualwith strong technical experience of 6+ years with aimto enhance my knowledge and utilize my skills towardsthe growth of the organization.SkillsProgramming Java, Spring Boot ,Spring MVC, HTML5, CSS3, VueJs,HibernateCode Versioning - GIT, BitBucket,Azure ReposCode Quality Tools - SonarQube,Fortify, Nexus CICD Tools - Jenkins , XL Release, XlDeploy, U deploy , Azure PipelinesIDE - Intellij, VS code, EclipseBuild & Test Tools - Maven &NeoLoadCloud : Azure DevOpsIndividual Skill - StakeholderManagement, Analytical ProblemSolving, Agile, Team CollaborationEducation BackgroundMy Contactsameerbhanushali62@gmail.comThane, Maharashtra 400604+91 9619603458https://www.linkedin.com/in/sameer -bhanushali-a90679130 Tata Consultancy Services | IT Analyst /DevOps EngineerICICI Bank | Web DeveloperFeb 2020 – PresentSep 2018 - Feb 2020As a DevOps Engineer I am responsible for JavaDevelopment of our application and also maintaining theapplication.I have successfully migrated an application from Struts toJAVA EE, COBOL to JAVA and hosted on Azure platformwith fully automated CICD pipelines.Development of CICD PipelinesRefactored 15 year old legacy core java application tobring it upto standard by reducing more than 500+ sonarissuesAnalyze technical issues, find resolutions, and providesolutions in an easy to understand Dashboard to ourstakeholders/clients.Maintainance of Website using OpenText CMS ToolCreation of new product pages on website as perrequirement from various product teamsCreation of offer pages for various offers by bankPublishing Quaterly Press Release on websiteUniversity of Mumbai — BE - 6.89 CGPA2014 - 2018Bachelor of Engineering in Electronics &Telecommunications from KJ SomaiyaInstitute of Engineering & InformationTechnologyCertificationMicrosoft Azure 900 Fundamentals &Azure 204 Developer AssociateCertificate of Appreciation for outstanding performancein TCS Info Security FestSustainability Champion Award for implementing greencode to reduce CO2 emissionsSpecial Initiative Award for reducing security issues inapplicationOn The Spot award for providing solutions to make codemore efficientBest Team Award(Twice) for outstanding contribution inproduction implementation

=========================================================
WITH audit_data AS (
   SELECT
       PROJECT_ID,
       OBJECT_VERSION_NUMBER,
       ATTRIBUTE2_DATE,
       ATTRIBUTE1_DATE,
       nvl(LAG(EFS_PPM_AUDIT_HIST_LKP.ATTRIBUTE2_DATE,1) OVER (PARTITION BY EFS_PPM_AUDIT_HIST_LKP.PROJECT_ID ORDER BY EFS_PPM_AUDIT_HIST_LKP.OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_AIS_IN_SERV_DT,
       nvl(LAG(EFS_PPM_AUDIT_HIST_LKP.ATTRIBUTE1_DATE,1) OVER (PARTITION BY EFS_PPM_AUDIT_HIST_LKP.PROJECT_ID ORDER BY EFS_PPM_AUDIT_HIST_LKP.OBJECT_VERSION_NUMBER),'01-JAN-1900') AS PREV_EST_IN_SERV_DT,
       MIN(OBJECT_VERSION_NUMBER) OVER (PARTITION BY PROJECT_ID) AS MIN_OBJ_VERSION_NUM
   FROM EFS_PPM_AUDIT_HIST_LKP
)
SELECT *  
FROM audit_data
WHERE
   (ATTRIBUTE2_DATE != PREV_AIS_IN_SERV_DT
    OR ATTRIBUTE1_DATE != PREV_EST_IN_SERV_DT)  
AND OBJECT_VERSION_NUMBER != MIN_OBJ_VERSION_NUM;


------------------------------------------------------------
WITH PrimaryProjects AS (
    -- Step 1: Get projects where input projects are sources
    SELECT target_project_id AS project_id
    FROM Project_Relationships
    WHERE source_project_id IN ({INPUT_PROJECTS}) 
    UNION 
    -- Get projects where input projects are targets
    SELECT source_project_id AS project_id
    FROM Project_Relationships
    WHERE target_project_id IN ({INPUT_PROJECTS})
),
SecondaryProjects AS (
    -- Step 2: Get projects acting as sources for the projects identified in Step 1
    SELECT DISTINCT source_project_id AS project_id
    FROM Project_Relationships
    WHERE target_project_id IN (SELECT project_id FROM PrimaryProjects)
),
ConsolidatedProjects AS (
    -- Step 3: Consolidate all unique projects from Step 1, Step 2, and input projects
    SELECT project_id FROM PrimaryProjects
    UNION
    SELECT project_id FROM SecondaryProjects
    UNION
    SELECT project_id FROM (SELECT UNNEST(ARRAY[{INPUT_PROJECTS}]) AS project_id) AS input_projects
)
-- Final Output
SELECT * FROM ConsolidatedProjects;





1.Report should include following projects:
•	All projects identified as target projects where input project list is source projects.
•	All projects identified as source projects where input project list is target projects.
2.Report should include secondary list of projects. This secondary list of projects represents any other project acting as source projects for the projects identified in step 1.
3.Consolidated list of projects should include unique projects identified in step 1, step 2 and input projects.



SELECT DISTINCT "Fiscal Calendar"."Fiscal Period"
FROM "PPM - Project Costs"
WHERE ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']}
       AND "Fiscal Calendar"."Fiscal Period Number" BETWEEN 
           GREATEST(1, @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2) 
           AND @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']})
   OR ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']} - 1
       AND "Fiscal Calendar"."Fiscal Period Number" > 9
       AND "Fiscal Calendar"."Fiscal Period Number" > 
           @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} + 9)
FETCH FIRST 65001 ROWS ONLY

-----------------
SELECT DISTINCT "Fiscal Calendar"."Fiscal Period"
FROM "PPM - Project Costs"
WHERE ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']}
       AND "Fiscal Calendar"."Fiscal Period Number" IN (
           @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']},
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 > 0 
                THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 
                ELSE NULL END,
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 > 0 
                THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 
                ELSE NULL END
       ))
   OR ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']} - 1
       AND "Fiscal Calendar"."Fiscal Period Number" IN (
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 <= 0 
                THEN 12 + (@{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1)
                ELSE NULL END,
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 <= 0 
                THEN 12 + (@{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2)
                ELSE NULL END
       ))
FETCH FIRST 65001 ROWS ONLY

_________

SELECT DISTINCT "Fiscal Calendar"."Fiscal Period"
FROM "PPM - Project Costs"
WHERE ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']}
       AND "Fiscal Calendar"."Fiscal Period Number" IN (
           @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']},
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 > 0 
                THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 
                ELSE 12 END,
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 > 0 
                THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 
                ELSE CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 > 0 
                          THEN 12 
                          ELSE 11 END 
           END
       ))
   OR ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']} - 1
       AND "Fiscal Calendar"."Fiscal Period Number" IN (
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 <= 0 THEN 12 ELSE NULL END,
           CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 <= 0 
                THEN CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} = 1 THEN 12
                          ELSE 11 END 
                ELSE NULL END
       ))
FETCH FIRST 65001 ROWS ONLY

__________
SELECT DISTINCT
    "Fiscal Calendar"."Fiscal Period"
FROM
    "PPM - Project Costs"
WHERE
    (("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']} AND "Fiscal Calendar"."Fiscal Period Number" IN ( @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']}, CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 > 0 THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 ELSE NULL END, CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 > 0 THEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 ELSE NULL END)) OR ("Fiscal Calendar"."Fiscal Year" = @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_YEAR']} - 1 AND "Fiscal Calendar"."Fiscal Period Number" IN ( CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 1 = 0 THEN 12 ELSE NULL END, CASE WHEN @{biServer.variables['NQ_SESSION.EFS_CURRENT_FISCAL_PERIOD_NUMBER']} - 2 <= 0 THEN 11 ELSE NULL END )))
FETCH FIRST 65001 ROWS ONLY
  
  
  
  SELECT
    DISTINCT ALIAS,DATALAYER_TABLE
    INTO v_alias_name,v_data_layer_tab
    FROM
        EFS_DATA_LAYER.EFS_HIERARCHY_LIST
	WHERE
        lower(alt_hier_extract) = lower(v_in_ext_name);
          open cur for 'SELECT DISTINCT FIXED_HIER_LEVEL FROM '|| v_data_layer_tab;
          LOOP
          fetch cur into  fixed_hier_level_var;
          exit when cur%NOTFOUND;
          Counter:=31-fixed_hier_level_var;
            FOR i IN 0..31 - fixed_hier_level_var LOOP
              -- Construct column names dynamically
                  if i=Counter then 
                      DECLARE
                        level_segment_col VARCHAR2(100);
                        level_valueset_col VARCHAR2(100); 
                        --level_segment_id_col VARCHAR2(100);
                      BEGIN
                        level_segment_col := 'LEVEL' || i || '_'||v_alias_name||'_SEGMENT';
                        level_valueset_col := 'LEVEL' || i || '_'||v_alias_name||'_SEGMENT_NAME';
                        EXECUTE IMMEDIATE 'UPDATE EFS_'||v_alias_name||'_DIMH
                                          SET ' || level_valueset_col || ' = CONCAT(CONCAT(' || level_segment_col || ', ''~''),' || level_valueset_col || ')
                                          WHERE fixed_hier_level = :1
                                          AND YEAR='||varrawyear||'
                                          AND ' || level_segment_col || ' NOT LIKE ''%~''' USING fixed_hier_level_var;
                      END;
                ELSE
                    DECLARE
                        level_segment_col VARCHAR2(100);
                        level_valueset_col VARCHAR2(100); 
                        --level_segment_id_col VARCHAR2(100);
                    BEGIN
                        level_segment_col := 'LEVEL' || i || '_'||v_alias_name||'_SEGMENT';
                        level_valueset_col := 'LEVEL' || i || '_'||v_alias_name||'_SEGMENT_NAME';
                        EXECUTE IMMEDIATE 'UPDATE EFS_'||v_alias_name||'_DIMH
                                          SET ' || level_segment_col || ' = CONCAT(' || level_segment_col || ', ''~''),
                                              ' || level_valueset_col || ' = CONCAT(CONCAT(CONCAT(' || level_segment_col || ', ''~''),' || level_valueset_col || '), ''~'')
                                          WHERE fixed_hier_level = :1
                                          AND YEAR='||varrawyear||'
                                          AND ' || level_segment_col || ' NOT LIKE ''%~''' USING fixed_hier_level_var;
                      END;
                END IF;
            END LOOP;
          END LOOP;
 
 
END IF;




- describe the role: As part of CEG (Hypercare phase & Go-Live) project from 1 Jan to 30 Apr 2024. I was an OAC/FAW developer & tester. 
- During this time frame I have fixed 15+ High to Medium complex Defect Post Go-live and Hypercare.
- Upskilled my self as an ODI developer and fill the gap within the ETL team. Played a pivotal role during the CEG (Hypercare phase & Go-Live) by providing extremely quick turnarounds. Contributed to 10+ High to Medium defect to ensure seamless reports availability to Users.
- As part of EU Apollo Phase 2 project, accelerated delivery by up-skilling on ODI to Built 12+ ETL pipelines as part of Project Change Tracking, GL Detail, Project Costing and Data level Scurity functional areas.
- Developed ODI Job Execution and logging Unix wrapper script for DSeries scheduling team.
- Understanding the existing dataflow, I have optimized the data extraction process for 9 ETL Scenarios, reducing the overall runtime by 80%, leads to faster daily load execution and data availability.
- Contributed to 3+ business use-cases by closelly discussing the design with the client to finalize scenario & approach, lead to POCs completion on time, enabling scope expansion of 2 reports and 1 custom SA.
- Contributed to ODI Technical doc, Master Integration doc and standardizing the ODI Objects.
- As part of repoting POD, worked as OAC/FAW Developer, Build 5+ High to medium complex reports and Technical Spec(TS) with ODI extensions. 
- Contributed to more the 10% of overall of reports MA & TestCase writing documentation for SIT cycle.
- Trained ODI team members on OAC/FAW to bridge the gap between ETL and reports.  

For your reference on sentence framing, below is the example of other team member:
•	Led the CC&B project's(Exelon account's) Reporting ETL thread of 10+ members, delivering 108 reports, used by CXOs to analyze data, identify insights & create better solutions, contributing to the overall value of $2M.

•	Delivered 60+ custom reporting dataflows, conducted & closed design discussions with the client & SI partners to finalize development approaches, enabling the client to build the desired framework for 4+ business use-cases.

•	Played a pivotal role during the BRV/BCT phase(UAT) by providing extremely quick turnarounds, to ensure seamless report user demos, delivering 75+ Critical Day 0 enhancements & 40+ P0 change requests, receiving an award & multiple appreciations from the leadership for the same.

•	As part of Cloud Modernization, accelerated delivery by up-skilling on Azure to deliver 15+ dataflows & lead a 5-member team, training them on ADF & Synapse, enabling autonomous development of 10+ objects. Conducted code reviews, guaranteeing code standards & improved quality.


Point to be focussed:
• Understand technical requirements and develop understanding towards technical specifications
• Demonstrate strong understanding of primary area of technology/work
• Able to execute assigned tasks independently
• Understand technical/design problem and come-up with suggestions
• Help others on the team with any technical issues/problems
• Understand project delivery processes and leverages knowledge of best practices, checklists to support deliverables



- Addressed 15+ defects during go-live, resolving multi-load execution issues in ODI load plans (CLN framework).  
- Fixed missing partial data scenarios caused by length mismatches in custom extensions.  
- Upskilled as an ODI backup resource and contributed to ETL and reporting PODs.  
- Earned two professional certifications in OAC/FAW.  
- Optimized ERP data extraction for 9 BIP ETL mappings, reducing runtime from 60-75 minutes to 2-3 minutes per report.  
- Automated ODI job scheduling using DSeries and implemented purging scripts.  
- Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions, leading to scope expansion of 2 reports and 1 custom SA.  
- Built and implemented an end-to-end FERC-GAAP custom ETL extension and reporting solution.  
- Built 12+ ETL pipelines and optimized solutions using functional understanding.  
- Authored complete ODI technical specifications and developed 5+ reports and 5+ technical specs.  
- Contributed to the Master Attribute (MA) sheet, Master Integration document, and authored 10+ test scripts.  
- Supported two Oracle patches, data refreshes, and performed regression testing to ensure seamless functionality.




Addressed 15+ defects during go-live.
Resolved multi-load execution issues in ODI load plans (CLN framework).
Fixed missing partial data scenarios due to length mismatch in custom extensions.
Upskilled as an ODI backup resource.
Contributed to ETL and reporting PODs.
Earned two professional-level certifications in OAC/FAW.
Optimized the Existing ERP data extraction process for 9 BIP ETL mappings from 60-75 min to 2-3 min per BIP report.
Automated ODI job scheduling with Dseries and implemented purging scripts.
Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions lead to scope expansion of 2 reports and 1 custom SA. Build End to end solution of FERC-GAAP Custom ETL extension and reporting.
12+ ETL pipeline build. Optimized ETL solutions using Functional understanding. 
Owned complete ODI technical specification documentation.
Completed 5+ technical specs, Built 5+ reports.
Contributed to the Master Attribute (MA) sheet, Master Integration document, wrote 10+ test Scripts, Fixed FUT defects.
Supported 2 oracle patch and data refresh and performed regression testing to ensure the nothing is broken.


---
Let’s confirm:  

### Points Mentioned:  
1. Addressed 15+ defects during go-live.  
2. Resolved multi-load execution issues in ODI load plans (CLN framework).  
3. Fixed missing partial data scenarios in custom extensions.  
4. Upskilled as an ODI backup resource.  
5. Contributed to ETL and reporting PODs.  
6. Earned two professional-level certifications in OAC/FAW.  
7. Reduced job execution time for 9 BIP ETL mappings from 60-75 minutes to 2-3 minutes by redesigning ERP data extraction using the BIP reports approach.  
8. Automated ODI job scheduling with Dseries and implemented purging scripts.  
9. Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions.  
10. Scope expansion of 2 reports and 1 custom SA.  
11. Improved ETL accuracy by translating complex functional requirements.  
12. Resolved missing scenarios in GAAP-FERC.  
13. Optimized EIS/AIS data solutions.  
14. Owned complete ODI technical specification documentation.  
15. Completed 5+ technical specs.  
16. Built 5+ reports.  
17. Contributed to the Master Attribute (MA) sheet.  
18. Wrote test cases.  
19. Fixed FUT defects.  

### Verification:  
All 19 points are included in the revised impact statement. Would you like me to rephrase or emphasize any specific areas?


**Impact Statement for Promotion**  

Addressed 15+ defects during go-live, resolved multi-load execution issues in ODI load plans (CLN framework), and fixed missing partial data scenarios in custom extensions. Upskilled as an ODI backup resource, contributed to ETL and reporting PODs, and earned two professional-level certifications in OAC/FAW. Reduced job execution time for 9 BIP ETL mappings from 60-75 minutes to 2-3 minutes by redesigning ERP data extraction processes using the BIP reports approach. Automated ODI job scheduling with Dseries and implemented purging scripts to enhance performance. Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions, enabling scope expansion of 2 reports and 1 custom SA. Improved ETL accuracy by translating complex functional requirements, resolving missing scenarios in GAAP-FERC, and optimizing EIS/AIS data solutions. Owned the complete ODI technical specification documentation, completed 5+ technical specs, built 5+ reports, contributed to the Master Attribute sheet, wrote test cases, and fixed FUT defects.


Constellation Apollo (1 Jan 2024 - 30 Apr 2024):

Addressed 15+ defects during go-live, resolved multi-load execution issues in ODI load plans (CLN framework), and fixed missing partial data scenarios in custom extensions.
Upskilled as an ODI backup resource, contributed to ETL and reporting PODs, and earned two professional-level certifications in OAC/FAW.
Exelon Apollo (1 May 2024 - 20 Dec 2024):

Reduced job execution time for 9 BIP ETL mappings from 60-75 minutes to 2-3 minutes by redesigning processes used to extract ERP data without PVOs using BIP reports approach.
Automated ODI job scheduling with Dseries and implemented purging scripts to enhance performance.
Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions, enabling scope expansion of 2 reports and 1 custom SA.
Improved ETL accuracy by translating complex functional requirements, resolving missing scenarios in GAAP-FERC, and optimizing EIS/AIS data solutions.
Owned complete ODI Tech spec documenting.
As OAC/FAW developer, Completed 5+ Techspec, 5+ report Build. Contributed to Master Attribute(MA) sheet, TestCase writing documnets. FUT defects fixing.
Maintained strong communication, demonstrated flexibility, and consistently improved skills in FAW and ODI.


**Impact Statement for Promotion**  

**Constellation Apollo (1 Jan 2024 - 30 Apr 2024):**  
- Addressed 15+ defects during go-live, resolved multi-load execution issues in ODI load plans (CLN framework), and fixed missing partial data scenarios in custom extensions.  
- Upskilled as an ODI backup resource, contributed to ETL and reporting PODs, and earned two professional-level certifications in OAC/FAW.  

**Exelon Apollo (1 May 2024 - 20 Dec 2024):**  
- Reduced job execution time for 9 BIP ETL mappings from 60-75 minutes to 2-3 minutes by redesigning processes using the BIP approach.  
- Automated ODI job scheduling with Dseries and implemented purging scripts to enhance performance.  
- Delivered 3+ POCs, including custom sorting and GAAP-FERC solutions, enabling scope expansion of 2 reports and 1 custom SA.  
- Improved ETL accuracy by translating complex functional requirements, resolving missing scenarios in GAAP-FERC, and optimizing EIS/AIS data solutions.  
- Supported ETL and reporting during hypercare and resolved critical production defects, ensuring system stability.  
- Maintained strong communication, demonstrated flexibility, and consistently improved skills in FAW and ODI.  



**Impact Statement for Promotion**  

As a proactive and results-driven professional, I have consistently delivered high-impact contributions in the ETL and reporting domains. My end-to-end rebuild of 9 BIP ETL mappings reduced total job execution time from 60-75 minutes per report to just 2-3 minutes, optimizing critical processes and earning leadership approval for wider implementation. Leveraging my functional knowledge and technical expertise, I effectively bridged the gap between client requirements and technical execution, streamlining data integration and reporting workflows.  

I took ownership of complex POCs, including custom sorting requirements and GAAP-FERC solutions, enabling timely project delivery and expanding scope. My implementation of the Dseries automation script streamlined ODI job scheduling, while purging scripts enhanced system efficiency. Additionally, I resolved critical production defects, addressed 15+ go-live issues, and introduced robust solutions to mitigate patch impacts.  

Committed to continuous learning, I upskilled in OAC/FAW and ODI, earning certifications and contributing seamlessly across ETL and reporting tracks.


**Impact Statement for Promotion**  

- Reduced job execution time for 9 BIP ETL mappings from 60-75 minutes per report to 2-3 minutes by redesigning the process using the BIP approach.  
- Successfully implemented Dseries automation for ODI job scheduling and purging scripts, enhancing efficiency and reducing manual effort.  
- Demonstrated strong functional knowledge by understanding client requirements and translating them into efficient ETL solutions, improving team delivery.  
- Delivered 3+ POCs for custom sorting requirements and GAAP-FERC design, enabling timely project delivery and scope expansion (2 additional reports, 1 custom SA).  
- Resolved critical production defects, including multi-load execution issues and missing partial data scenarios, ensuring smooth operations in ODI load plans.  
- Provided go-live support by addressing 15+ defects and assessing patch impacts on applications, ensuring system stability post-deployment.  
- Actively contributed to ETL and reporting tracks, taking ownership of tasks and providing regular updates to leads.  
- Upskilled in OAC/FAW and ODI, earning professional certifications and becoming a backup ODI resource.  
- Redesigned complex ERP data retrieval processes, removing dependency on PVOs and improving system performance.  
- Maintained strong communication and collaboration with teams, contributing to seamless project execution and delivery.  




Exelon Apollo (1 May 2024 to 20 Dec 2024):

Leads comments:
Hitesh is a consistent performer and has worked exceptionally well in reporting and ETL track. His contribution to GAAP-FERC solution is really commendable. He has gained functional knowledge on the client data which has helped team to develop code in much efficient way
Hitesh has stepped up and took the new responsibility as an ETL developer when there was need in the project. He has upskilled on ODI and supported both ETL and reporting tracks during hypercare phase of the project. Keep up the same zeal.
Hitesh is performing exceptionally well in ETL track of the project. He is constantly improving his technical skills at reporting(FAW) and ETL(ODI) front. He is ready to take any new work give to him. He has performed 3+POC on ETL side for custom sorting requirement. His contribution to GAAP-FERC design helped team to close the POC on time which helped us to get additional scope( 2 reports and 1 custom SA). He effectively communicates with team and takes ownership of the assigned task and keep his leads posted on the updates. Hitesh can increase his involvement in requirement discussions and improve his functional knowledge.

I have performed end to end rebuild of 9 BIP approach ETL mapping and dimentions. Using new approach, we are able to reduce the total job execution time from 

Implemented Dseries automation script to schedule all ODI jobs.
Implemented the Purging logs and 

Functional knowledge upskill:
Under standing functional requirement with reporting understanding helped me to effectively build ETL objects and helped etl team to understand the requirement more easy and effective which help etl team to understand all the required scenarios. Scenario where it help. While building one of the EIS and AIS related data where multiple scenarios of tracking change was required. Understanding the requirement functionally and then converting in to ETL technical understanding helped to develop efficient.
Another Scenarios, while developing solution for FERC and GAAP account side by side, understanding functionally help me to understand all the scenario and also raise one of the missing case to Onshre team which help to build better solution. with that completed the POC build and ETL extenstion end to end.

Major Performance improvement ownership:
Redesigned one of the most complex processes in the existing system to retrieve ERP data without relying on PVOs, utilizing the BIP approach. This optimization significantly reduced job execution time from 60-75 minutes per BIP report to just 2-3 minutes. The solution has been successfully implemented in Dev01 for all 9 BIP reports, and the proof of concept (POC) was approved by the leadership team.

Constellation Apollo (1 Jan 2024 to 30 Apr 2024):
- As OAC/FAW Developer, Provided go-live support, addressing 15+ defects. assessing patch impact on applications. provided post golive support upskilled with two additional professional level certificates in OAC/FAW.
- up skilled my self as ODI backup resource.
- Implemented missing parshial data due to midmatch in lenght cound between source and target accross custom extensions.
- implementated major PROD defect of multi load execution on same day was not handled at ODI load plan CLN framework.

Leads comment:
Hitesh is actively contributing wherever there is a scope and taking up additional responsibilities. Keep up the good work and be consistent on what you do .
Hitesh upskilled in ETL . He is contributing to both ETL and reporting PODS as when it is required.

Practical No. 1
Aim: Exploring Color Maps in Matplotlib: Visualizing Random Data with Different Color Schemes.
Code:
# Import the necessary libraries
import matplotlib.pyplot as plt  # For creating plots
import numpy as np  # For numerical operations, especially for generating random numbers

# Loop through the color maps, limiting to the first 5
for index, i in enumerate(plt.colormaps()):
    if index >= 3:  # Stop the loop after 5 iterations
        break

    # Set the title for each plot based on the color map name
    sTitle = 'KSMSCIT005 Hitesh Bhanushali \n Color Map: ' + i

    # Create a figure for the plot with a specific size
    fig = plt.figure(figsize=(4, 4))

    # Set the title for the plot
    plt.title(sTitle)
    # Generate a random 10x10 matrix and plot it as an image
    imgplot = plt.imshow(np.random.rand(10, 10))
    # Apply the current color map to the image plot
    imgplot.set_cmap(i)
    # Display the plot
    plt.show()

Output:










Practical No. 2
Aim: Geospatial Visualization with GeoPandas
Code:
#Visualising Geospecial data with geopanda
import geopandas as gpd
import matplotlib.pyplot as plt
import fiona
from shapely.geometry import Point
# Set the SHAPE_RESTORE_SHX config option to YES
fiona.drvsupport.supported_drivers['ESRI Shapefile'] = 'rw'
with fiona.Env(SHAPE_RESTORE_SHX='YES'):
    india_gdf = gpd.read_file("/content/sample_data/indian_borders_for_indian_viewers.shp")
for x,y,label in zip(devgad.geometry.x,devgad.geometry.y,devgad['City']):
  ax.text(x,y,label)
plt.title("KSMSCIT005 Hitesh Bhanushali ")
plt.show()
Output:



Practical No. 3
Aim: Interactive Geospatial Visualization with Folium: 
. Mapping Major Cities of India
Code:
import numpy as np
import pandas as pd
import folium

print(‘KSMSCIT005 Hitesh Bhanushali')
# Create a base map centered on India's geographical coordinates with a starting zoom level of 5
rm = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# List of cities with their name, geographic coordinates, and population
cities = [
    {"name": "Tamil Nadu", "location": [11.1271, 78.6569], "population": "21.75 million"},
    {"name": "Mumbai", "location": [19.0760, 72.8777], "population": "20.18 million"},
    {"name": "Punjab", "location": [31.1471, 75.3412], "population": "8.42 million"},
    {"name": "Chennai", "location": [13.0827, 80.2707], "population": "10.97 million"},
    {"name": "Uran", "location": [18.8772, 72.9283], "population": "14.85 million"}
# Loop through each city in the list to add a marker to the map
for city in cities:
    folium.Marker(
        location=city["location"],
        popup=f"<b>{city['name']}</b><br>Population: {city['population']}",
        tooltip=city['name']
    ).add_to(rm)

# Generate random latitude and longitude points within India's approximate geographical bounds
# Latitude range: 6 to 35 (north to south India), Longitude range: 68 to 97 (west to east India)
latitudes = np.random.uniform(6, 35, 5)
longitudes = np.random.uniform(68, 97, 5)

# List of random village names for the generated points
village_names = ['Village A', 'Village B', 'Village C', 'Village D', 'Village E']

# Loop through the random latitudes and longitudes to add markers for random villages
for lat, lon, village_name in zip(latitudes, longitudes, village_names):
    folium.Marker(
        location=[lat, lon],
        popup=f"<b>{village_name}</b><br>Randomly Generated Location",
        tooltip=village_name
    ).add_to(rm)

# Save the map to an HTML file
rm.save('india_map_with_random_villages.html')

# Display the map in a Jupyter notebook or similar environment (optional)
rm

Output:








Practical No. 4
Aim: Calculating and Visualizing the Current Position of the Moon Using Astropy
Code:
import warnings
warnings.filterwarnings('ignore')
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_moon, AltAz, EarthLocation
import astropy.units as u
import matplotlib.pyplot as plt

print(‘KSMSCIT005 Hitesh Bhanushali')
print("---------------------------")
# Set up the ephemeris and get the current time in UTC
solar_system_ephemeris.set('builtin')
time_utc = Time.now()

# Calculate the Moon's current position in celestial coordinates
moon = get_moon(time_utc)

# Define the observer's location and transform the Moon's position to AltAz coordinates
location = EarthLocation.of_site('Kitt Peak')
moon_altaz = moon.transform_to(AltAz(obstime=time_utc, location=location))

# Print the Moon's Right Ascension (RA), Declination (Dec), Altitude, and Azimuth
print(f'Moon coordinates (RA, Dec): {moon.ra}, {moon.dec}')
print(f'Moon Altitude: {moon_altaz.alt}')
print(f'Moon Azimuth: {moon_altaz.az}')

# Create a polar plot to visualize the Moon's position in the sky
plt.figure(figsize=(10, 8))
plt.subplot(111, projection='polar')
plt.title('\n KSMSCIT005 Hitesh Bhanushali \n Moon Position', y=1.1)
plt.polar(moon.ra.radian, moon.dec.radian, 'o', markersize=10)
plt.grid(True)
plt.show()






Output:




Practical No. 5
Aim: Visualizing New COVID-19 Cases Using Plotly Express:
. Daily COVID-19 Case Trends: A Line Plot Visualization
. Monthly COVID-19 Case Trends: A Bar Plot Visualization
Code:
Part A:
!pip install pandas plotly
import pandas as pd
import plotly.express as px

# URL for the COVID-19 data
URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(URL)

# Filter the DataFrame for the specific country
country = 'Germany'
df_country = df[df['location'] == country]

# Select relevant columns for the plot
df_country = df_country[['date', 'new_cases']]

# Create a line plot to visualize COVID-19 new cases over time for the selected country
fig = px.line(df_country, x='date', y='new_cases', title=f'KSMSCIT005 Hitesh Bhanushali | Corona Cases in {country} over time')

# Show the plot
fig.show()


Part B:
 import pandas as pd
import plotly.express as px

# URL for the COVID-19 data
URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

# Load the dataset into a DataFrame
df = pd.read_csv(URL)

# Define the country of interest
country = 'Germany'

# Filter the DataFrame for the specific country
df_country = df[df['location'] == country]

# Check if the filtered DataFrame is empty and raise an error if so
if df_country.empty:
    raise ValueError(f'Country {country} not found in the dataset')

# Convert the 'date' column to datetime format
df_country['date'] = pd.to_datetime(df_country['date'])

# Extract the month from the date and create a new column for it
df_country['month'] = df_country['date'].dt.to_period('M')

# Aggregate the data to get the total number of new cases per month
monthly_cases = df_country.groupby('month')['new_cases'].sum().reset_index()

# Convert the 'month' period to a string for plotting
monthly_cases['month'] = monthly_cases['month'].astype(str)

# Create a bar plot to visualize the total number of new COVID-19 cases per month
fig = px.bar(monthly_cases, x='month', y='new_cases', title=f'KSMSCIT005 Hitesh Bhanushali | Total Corona Cases in {country} over time')

# Show the plot
fig.show()



Output:
Part A:

Part B:



Practical No. 6
Aim: Linear Regression Analysis of Diabetes Data: 
. Predicting Age from BMI
Code:
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
print("KSMSCIT005 Hitesh Bhanushali")
print("---------------------------")

# Load the diabetes dataset
diabetes = datasets.load_diabetes()

# Use only one feature
diabetes_X = diabetes.data[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-50:]
print("BMI:",diabetes_X_test)

# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-50:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='blue')
plt.plot(diabetes_X_test, diabetes_y_pred, color='red', linewidth=2)

plt.xticks(())
plt.yticks(())

plt.axis('tight')
plt.title("KSMSCIT005 Hitesh Bhanushali \n Diabetes")
plt.xlabel("BMI")
plt.ylabel("Age")
plt.show()

Output:




Practical No 7
Aim: Creating a Word Cloud
Code:
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Sample text related to data science
text = """
data science is an interdisciplinary field that uses scientific methods processes algorithms and systems to extract knowledge….
"""

# Generate a word cloud from the text
wordcloud = WordCloud(width=800, height=800, background_color='white').generate(text)

# Plot the word cloud
plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

Output:


Practical No. 8
Aim: Introduction to Cassandra:
. Basic Commands
. KeySpace Creation
Implementation:









Practical No. 9
Aim: Using OpenCV and File Management Libraries:
. Extracting Frames from Video: Converting MP4 to JPEG Images
. Reconstructing a Video from Image Frames
Code:
Part A:
import os
import shutil
import cv2

print("KSMSCIT005 Hitesh Bhanushali")
# Define input file and output directory
sInputFileName = '/content/sample.mp4'
sDataBaseDir = '/content/Video to Images'

# Remove the output directory if it already exists, and create a new one
if os.path.exists(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)

# Notify the user that the process is starting
print('=====================================================')
print('Start Movie to Frames')
print('=====================================================')

# Open the video file
vidcap = cv2.VideoCapture(sInputFileName)
success, image = vidcap.read()
count = 0

# Read and process frames from the video
while success:
    success, image = vidcap.read()  # Read the next frame
    if not success:
        break

    # Define the filename for the extracted frame
    sFrame = sDataBaseDir + str('/pic-frame-' + str(format(count, '04d')) + '.jpg')
    print('Extracted: ', sFrame)

    # Save the frame as a JPEG file
    cv2.imwrite(sFrame, image)

    # Check if the saved frame is empty, and remove it if so
    if os.path.getsize(sFrame) == 0:
        count -= 1  # Decrement the frame count
        os.remove(sFrame)  # Remove the empty frame
        print('Removed: ', sFrame)

    # Exit if the Escape key is pressed
    if cv2.waitKey(10) == 27:
        break

    # Exit after processing a certain number of frames (e.g., 15)
    if count > 100:
        break

    # Increment the frame count
    count += 1

# Notify the user that the process is complete
print('=====================================================')
print('Generated : ', count, ' Frames')
print('=====================================================')
print('Movie to Frames HORUS - Done')
print('=====================================================')


Part B:
#9 - B
import cv2
import os
print("KSMSCIT005 Hitesh Bhanushali")

# Define the directory containing the images and the path for the output video
sDataBaseDir = "/content/Video to Images"
output_video_file = "/content/Image to Video/OutputVideo.mp4"

# Ensure the output directory exists
os.makedirs(os.path.dirname(output_video_file), exist_ok=True)

# List all image files in the directory and sort them
frame_files = [f for f in os.listdir(sDataBaseDir) if f.endswith('.jpg')]
frame_files.sort()  # Ensure images are processed in the correct order

# Check if there are any images to process
if not frame_files:
    print("No frames found in the directory.")
    exit()

# Read the first frame to get the dimensions for the video
first_frame_path = os.path.join(sDataBaseDir, frame_files[0])
first_frame = cv2.imread(first_frame_path)

if first_frame is None:
    print(f"Error reading the first frame: {first_frame_path}")
    exit()

# Get the height and width of the frames
height, width, _ = first_frame.shape

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4 format
fps = 30  # Frames per second
out = cv2.VideoWriter(output_video_file, fourcc, fps, (width, height))

print("===================================================")
print("Creating video from frames")
print("===================================================")

# Write each frame to the video file
for frame_file in frame_files:
    frame_path = os.path.join(sDataBaseDir, frame_file)
    frame = cv2.imread(frame_path)
    if frame is not None:
        out.write(frame)
        print(f"Added frame: {frame_path}")
    else:
        print(f"Failed to read frame: {frame_path}")

# Release the VideoWriter object
out.release()

print("=====================================================")
print(f'Video saved as: {output_video_file}')
print("=====================================================")


Output:
Part A:



Part B:





Practical No. 10
Aim: Working with MongoDB:
. Python
. R
Code:
Part A:
# MongoDB Atlas URI connection string
ATLAS_URI = "mongodb://localhost:27017"
# Install pymongo library with the srv extra required for MongoDB Atlas
#! pip install pymongo[srv]==4.6.2
# Import MongoClient from the pymongo library
from pymongo import MongoClient

# Define a class to interact with MongoDB Atlas
class AtlasClient:
    # Constructor to initialize the MongoClient and select a specific database
    def __init__(self, atlas_uri, dbname):
        # Connect to the MongoDB Atlas instance using the URI
        self.mongodb_client = MongoClient(atlas_uri)
        # Set the database we will be working with
        self.database = self.mongodb_client[dbname]

    # Quick method to check if the connection to MongoDB Atlas is successful
    def ping(self):
        # Sends a ping command to the server to ensure it's reachable
        self.mongodb_client.admin.command('ping')

    # Method to get a specific collection from the database
    def get_collection(self, collection_name):
        # Return the collection specified by 'collection_name'
        collection = self.database[collection_name]
        return collection

    # Method to find documents in a collection with an optional filter and limit
    def find(self, collection_name, filter={}, limit=0):
        # Get the specified collection
        collection = self.database[collection_name]
        # Perform a query on the collection, return as a list
        items = list(collection.find(filter=filter, limit=limit))
        return items

# Database name and collection name we want to interact with
DB_NAME = 'Practice'
COLLECTION_NAME = 'UserList'

# Create an instance of AtlasClient using the MongoDB URI and database name
atlas_client = AtlasClient(ATLAS_URI, DB_NAME)

# Ping the MongoDB Atlas instance to test the connection
atlas_client.ping()
print('Connected to Atlas instance! We are good to go!')

# Retrieve all documents from the 'UserList' collection
names = atlas_client.find(collection_name=COLLECTION_NAME)
print(f"Found {len(names)} names")

# Loop through each document (name) found and print details (id, name, address)
for idx, name in enumerate(names):
    print(f'{idx+1}\nid: {name["_id"]}\nname: {name["name"]},\naddress: {name["Rollno"]}')


Part B:
# Install the mongolite library
# install.packages("mongolite")

# Load the mongolite library
library(mongolite)

# MongoDB Atlas URI connection string
ATLAS_URI <- "mongodb://localhost:27017"

# Define a function to create an object that interacts with MongoDB Atlas
AtlasClient <- function(atlas_uri, dbname) {
  client <- list()
  
  # Connect to the MongoDB Atlas instance using the URI
  client$mongodb_client <- mongo(url = atlas_uri)
  
  # Set the database we will be working with
  client$database <- function(collection_name) {
    mongo(collection = collection_name, db = dbname, url = atlas_uri)
  }
  
  # Quick method to check if the connection to MongoDB Atlas is successful
  client$ping <- function() {
    tryCatch({
      client$mongodb_client$run('{"ping": 1}')
      print("Ping successful")
    }, error = function(e) {
      print(paste("Ping failed:", e$message))
    })
  }
  
  # Method to find documents in a collection with an optional filter and limit
  client$find <- function(collection_name, filter = '{}', limit = 0) {
    collection <- client$database(collection_name)
    result <- collection$find(query = filter, limit = limit)
    return(result)
  }
  
  return(client)
}

# Database name and collection name we want to interact with
DB_NAME <- 'Practice'
COLLECTION_NAME <- 'UserList'

# Create an instance of AtlasClient using the MongoDB URI and database name
atlas_client <- AtlasClient(ATLAS_URI, DB_NAME)

# Ping the MongoDB Atlas instance to test the connection
atlas_client$ping()

# Retrieve all documents from the 'UserList' collection
names <- atlas_client$find(collection_name = COLLECTION_NAME)

# Print how many documents (names) were found
print(paste("Found", nrow(names), "names"))

# Loop through each document (name) found and print details (id, name, address)
for (idx in 1:nrow(names)) {
  name <- names[idx, ]
  cat(paste0(idx, "\nid: ", name$`_id`, "\nname: ", name$Name, ",\naddress: ", name$Rollno, "\n\n"))
}


Output:
Part A:

Part B:
  


Practical No. 11
Aim: Horus:
. Audio to CSV File
. Image to CSV File
Code:
Part A:
from scipy.io import wavfile
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("KSMSCIT005 Hitesh Bhanushali")

# Display audio file info and plot the audio signal
def show_info(aname, a, r):
    print(f"Audio: {aname}\nRate: {r}\nShape: {a.shape}")
    plot_info(aname, a, r)

# Plot the audio signal for each channel
def plot_info(aname, a, r):
    plt.title(f'Signal Wave - {aname} at {r}hz')
    sLegend = []
    for c in range(a.shape[1]):
        sLabel = 'Ch' + str(c + 1)
        sLegend.append(sLabel)
        plt.plot(a[:, c], label=sLabel)
    plt.legend(sLegend)
    plt.show()

sInputFileName = '/content/4ch-sound.wav'
print('Processing: ', sInputFileName)

# Read audio file
InputRate, InputData = wavfile.read(sInputFileName)
show_info("4 channel", InputData, InputRate)

# Convert audio data to DataFrame
ProcessData = pd.DataFrame(InputData)
ProcessData.columns = ['Ch1', 'Ch2', 'Ch3', 'Ch4']

# Save DataFrame to CSV
sOutputFileName = '/content/Output/AudioToCSV.csv'
ProcessData.to_csv(sOutputFileName, index=False)

print(ProcessData)

Part B:
from PIL import Image
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("KSMSCIT005 Hitesh Bhanushali")

def image_to_csv_and_show(image_path, csv_output_path):
    # Open and convert image to RGB
    img = Image.open(image_path).convert('RGB')

    # Convert image to NumPy array
    img_array = np.array(img)

    # Print image info
    print(f"Image Path: {image_path}")
    print(f"Shape: {img_array.shape}")
    print(f"Dtype: {img_array.dtype}")
    print(f"Min, Max: {img_array.min()}, {img_array.max()}")

    # Reshape array to 2D (rows of pixel values) and convert to DataFrame
    df = pd.DataFrame(img_array.reshape(-1, 3), columns=['R', 'G', 'B'])

    # Save DataFrame to CSV
    df.to_csv(csv_output_path, index=False, header=False)  # Avoid header and index

    # Show the image
    plt.imshow(img_array)
    plt.title('Image Preview')
    plt.axis('off')  # Hide axis
    plt.show()

def visualize_csv(csv_path, image_shape):
    df = pd.read_csv(csv_path, header=None, names=['R', 'G', 'B'])

    # Reshape DataFrame to image shape (height, width, 3)
    img_array = df.values.reshape(image_shape)

    # Plot a horizontal strip of the image (e.g., the middle row) for each channel
    mid_row = img_array.shape[0] // 2

    plt.figure(figsize=(15, 5))

    # Plot Red channel
    plt.subplot(3, 1, 1)
    plt.plot(img_array[mid_row, :, 0], color='red')
    plt.title('Red Channel Pixel Values')

    # Plot Green channel
    plt.subplot(3, 1, 2)
    plt.plot(img_array[mid_row, :, 1], color='green')
    plt.title('Green Channel Pixel Values')

    # Plot Blue channel
    plt.subplot(3, 1, 3)
    plt.plot(img_array[mid_row, :, 2], color='blue')
    plt.title('Blue Channel Pixel Values')

    plt.tight_layout()
    plt.show()

# Define file paths
image_path = '/content/p11#2.jpg'  # Replace with your image path
csv_output_path = '/content/Output/ImageToCSV.csv'  # Replace with your desired CSV output path

# Get image array and shape
img_array = np.array(Image.open(image_path).convert('RGB'))
shape = img_array.shape

# Process image and save as CSV
image_to_csv_and_show(image_path, csv_output_path)

# Visualize data from CSV
visualize_csv(csv_output_path, shape)

Output:
Part A:


Part B:

 














Practical No. 12
Aim : Data analysis and Visualization 
Part A
Code: 
print("KSMSCIT005 Hitesh Bhanushali")
import pandas as pd
ages=[18,23,22,25,46,34,45,87,100,6]
bins=[0,25,50,75,100]
bin_label=["Young","Mid","Senior","Old"]
age_bin=pd.cut(ages,bins=bins,labels=bin_label,right=True)
print(age_bin)
Output:

Part B
Code: 
import numpy as np
import pandas as pd
print('Latitude')
print(latitudeset)
print('Latitude avg',latitudeavg)
print("==============================")
print(longitudeset)
print('Longitude')
print('Longitude avg',longitudeavg)
Output:
 
Part C
Code: 
print("KSMSCIT005 Hitesh Bhanushali")
import matplotlib.pyplot as plt
!pip install basemap
from mpl_toolkits.basemap import Basemap
# Plotting on a world map
plt.figure(figsize=(12, 6))
map = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
              llcrnrlon=-180, urcrnrlon=180, resolution='c')

map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='lightgreen', lake_color='aqua')

# Convert latitude and longitude to map projection coordinates
x, y = map(longitudeset.values, latitudeset.values)

# Plot the sampled points
map.scatter(x, y, marker='o', color='red', s=100, label='Sampled Points')

# Plot the average point
avg_x, avg_y = map(longitudeavg, latitudeavg)
map.scatter(avg_x, avg_y, marker='X', color='blue', s=200, label='Average Point')

# Add title and legend
plt.title('Randomly Sampled Latitude and Longitude Points on World Map')
plt.legend()
plt.show()
Output:
