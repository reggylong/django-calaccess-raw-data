#!/usr/bin/env python
# -*- coding: utf-8 -*-
from calaccess_raw.models.base import FilingForm

all_filing_forms = [
    FilingForm(
        'F400',
        'Statement of Organization (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781370-400-2016-01',
        description='Form 400 must be filed within 10 days after the slate \
mailer organization receives, or is promised to receive, $500 or more for \
producing one or more slate mailers.',
    ),
    FilingForm(
        'F401',
        'Slate Mailer Organization Campaign Statement',
        group='CAMPAIGN',
        documentcloud_id='2781366-401-2005-01',
        description='Form 401 is filed by slate mailer organizations to \
disclose payments made and received in connection with producing slate mailers.',
        sections=[
            ('CVR', 'Cover Page', 3, 4),
            ('F401A', 'Schedule A, Payments Received', 5, 7),
            ('F401B', 'Schedule B, Payments Made', 8, 9),
            ('F401B-1', 'Schedule B-1, Payments Made by Agent or Independent Contractor', 10),
            ('F401C', 'Schedule C, Persons Receiving $1,000 or More', 11, 12),
            ('F401D', 'Schedule D, Candidates and Measures Not Listed on Schedule A', 13, 14),
        ]
    ),
    FilingForm(
        'F402',
        'Statement of Termination (Slate Mailer Organization)',
        group='CAMPAIGN',
        documentcloud_id='2781369-402-2005-01',
        description='Form 402 is filed by slate mailer organizations to \
terminate the organization.'
    ),
    FilingForm(
        'F410',
        'Statement of Organization Recipient Committee',
        group='CAMPAIGN',
        documentcloud_id='2781368-410-2016-01',
        description='Form 410 must be filed within 10 days of receiving \
$2,000 in contributions. If the committee has not yet reached the $2,000 \
threshold, the not yet qualified box should be checked.'
    ),
    FilingForm(
        'F425',
        'Semi-Annual Statement of no Activity',
        group='CAMPAIGN',
        documentcloud_id='2781365-425-2001-01',
        description='Form 425 is filed by recipient committees that have not \
received any contributions and have not made any expenditures during the six-\
month period covered by a semi-annual statement.'
    ),
    FilingForm(
        'F450',
        'Recipient Committee Campaign Disclosure Statement - Short Form',
        group='CAMPAIGN',
        documentcloud_id='2781364-450-2016-01',
        description='Form 450 is filed by recipient committees that meet \
certain specific criteria listed in the Form 450.',
        sections=[
            ('F450P5', 'Payments Made', 6, 7),
        ]
    ),
    FilingForm(
        'F460',
        'Recipient Committee Campaign Statement',
        group='CAMPAIGN',
        documentcloud_id='2781363-460-2016-01',
        description='Form 460 is filed by recipient committees to report \
expenditures and contributions. It can be used to file a pre-election statement, \
semi-annual statement, quarterly statement, termination statement, special odd-\
year report, or an amendment to a previously filed statement.',
        sections=[
            ('CVR', 'Cover Page', 3, 4),
            ('CVR2', 'Cover Page - Part 2', 5),
            ('SMRY', 'Summary Page', 7, 8),
            ('A', 'Schedule A, Monetary Contributions Received', 9, 11),
            ('A-1', 'Schedule A-1, Contributions Transferred to Special Election Committees'),
            ('B1', 'Schedule B - Part 1, Loans Received', 12, 13),
            ('B2', 'Schedule B - Part 2, Loan Guarantors', 14, 15),
            ('B3', 'Schedule B - Part 3, Outstanding Bal'),
            ('C', 'Schedule C, Non-Monetary Contributions Received', 16, 17),
            ('D', 'Schedule D, Summary of Expenditures Supporting / Opposing \
Other Candidates, Measures and Committees', 18, 20),
            ('E', 'Schedule E, Payments Made', 21, 24),
            ('F', 'Schedule F, Accrued Expenses (Unpaid Bills)', 25, 27),
            ('G', 'Schedule G, Payments Made by an Agent or Independent \
Contractor (on Behalf of This Committee)', 28, 29),
            ('H', 'Schedule H, Loans Made to Others', 29, 30),
            ('H1', 'Schedule H1, Loans Made'),
            ('H2', 'Schedule H2, Repayments Rcvd'),
            ('H3', 'Schedule H3, Outstanding Loan'),
            ('I', 'Schedule I, miscellanous increases to cash', 31, 32),
        ]
    ),
    FilingForm(
        'F461',
        'Independent Expenditure Committee & Major Donor Committee Campaign Statement',
        group='CAMPAIGN',
        documentcloud_id='2781361-461-2016-01',
        description='Form 461 is filed by major donors, independent \
expenditure committees, and multipurpose organizations including nonprofits.',
        sections=[
            ('F461P1', 'Name and Address of Filer', 3),
            ('F461P2', 'Nature and Interests of Filer', 3),
            ('F461P5', 'Part 5, Contributions (Including Loans, Forgiveness of \
Loans, and Loan Guarantees) and Expenditures Made', 5, 6),
        ]
    ),
    FilingForm(
        'F465',
        'Supplemental Independent Expenditure Report',
        group='CAMPAIGN',
        documentcloud_id='2781358-465-2009-06',
        description='Form 465 is filed by officeholders, candidates, recipient \
committees, major donor committees, and independent expenditure committees that \
make independent expenditures totaling $1,000 or more in a calendar year to support \
or oppose: a single candidate, a single measure, or the qualification of one single \
measure. Form 465s are filed in the same period(s) the candidate or committee \
supported or opposed by the independent expenditure(s) is required to file.',
        sections=[
            ('F465P3', 'Part 3, Independent Expenditures Made', 2),
        ],
    ),
    FilingForm(
        'F470',
        'Officeholder and Candidate Campaign Statement, Short Form',
        group='CAMPAIGN',
        documentcloud_id='2781357-470-2016-01',
        description='Form 470 is filed by officeholders and candidates who do \
not have a controlled committee, do not receive contributions totaling $2,000 or \
more during the calendar year, and do not spend $2,000 or more during the \
calendar year.'
        ),
    FilingForm(
        'F495',
        'Supplemental Pre-Election Campaign Statement',
        group='CAMPAIGN',
        documentcloud_id='2781356-495-2005-01',
        description='Form 495 is filed by recipient committees that make \
contributions totaling $10,000 or more in connection with an election in which \
the committee is not required to file regular preelection reports. Form 495 is \
filed as an attachment to a campaign disclosure statement (Form 450 or 460).'
    ),
    FilingForm(
        'F496',
        'Late Independent Expenditure Report',
        group='CAMPAIGN',
        documentcloud_id='2781355-496-2016-01',
        description='Form 496 is filed by committees that make independent \
expenditures whose combined total is $1,000 or more to support or oppose a single \
candidate for elective office, or a single ballot measure. Form 496 should be \
filed within 24-hours of making the expenditure during the 90 days immediately \
preceding the election.',
        sections=[
            ('F496P3', 'Part 3, contributions > $100 received', 3),
        ]
    ),
    FilingForm(
        'F497',
        'Late Contribution Report',
        group='CAMPAIGN',
        documentcloud_id='2781353-497-2016-01',
        description='Form 497 is filed by state and local committees making \
or receiving contribution(s) whose combined total is $1,000 or more in the 90 \
days before an election, committees reporting contributions of $5,000 or more in \
connection with a state ballot measure, and state candidates as well as state \
ballot measure committees that receive $5,000 or more at any time other than a \
90-day election cycle.',
        sections=[
            ('F497P1', 'Part 1, Contribution(s) Received', 2),
            ('F497P2', 'Part 2, Contribution(s) Made', 4),
        ]
    ),
    FilingForm(
        'F498',
        'Slate Mailer Late Payment Report',
        group='CAMPAIGN',
        documentcloud_id='2781352-498-2016-01',
        description='Form 498 is filed by a slate mailer organization upon \
receipt of a late payment.',
        sections=[
            ('F498-A', 'Part A: late payments attributed to'),
            ('F498-R', 'Part R: late payments received from', 2),
        ]
    ),
    FilingForm(
        'F501',
        'Candidate Intention Statement',
        group='CAMPAIGN',
        documentcloud_id='2781351-501-2016-01',
        description='Form 501 is filed each election by candidates for state \
or local office.'
    ),
    FilingForm(
        'F502',
        'Campaign bank account statement',
        group='CAMPAIGN',
        description='Form 502 must be filed within 10 days of opening a \
campaign bank account at a financial institution in California.'
    ),
    FilingForm(
        'F511',
        'Paid Spokesperson Report',
        group='CAMPAIGN',
        documentcloud_id='2781350-511-2015-01',
        description='Form 511 is filed by committees that make expenditures \
totaling $5,000 or more to an individual for his or her appearance in a printed, \
televised, or radio advertisement, or in a telephone message, to support or \
oppose the qualification, passage, or defeat of a state or local ballot measure.'
    ),
    FilingForm(
        'E530',
        'Electronic Issue Advocacy Report',
        group='CAMPAIGN',
        documentcloud_id='2781349-E530-Instructions',
        description='On-line Form E-530 reports must be filed by anyone \
spending or promising to pay $50,000 or more for a communication disseminated \
within 45 days of an election, if the communication clearly identifies a candidate \
for state elective office but does not expressly advocate the election or defeat \
of that candidate.'
    ),
    FilingForm(
        'F601',
        'Lobbying Firm Registration Statement',
        group='LOBBYIST',
        documentcloud_id='2781348-601-2014-10',
        description='Form 601 is filed on a biennial basis by a lobbying \
firm of individual contract lobbyist wishing to register or renew an existing \
registration. The form must be filed within 10 days of qualifying as a lobbying \
firm. Renewal of existing registration is due between November 1 and December 31 \
of each even-numbered year. This registration is valid for the complete two-year \
cycle of such session.'
        ),
    FilingForm(
        'F602',
        'Lobbying Firm Activity Authorization',
        group='LOBBYIST',
        documentcloud_id='2781347-602-1998-07',
        description='Form 602 is an authorization form filed by each person \
who employs or contracts with a lobbying firm. This form serves as an attachment \
to Form 601, and is filed by the applicable lobbying firm. Form 602 also contains \
a schedule which describes by category the nature and interest of the client of \
the firm. Like Form 601 this registration attachment is valid for the length of \
the State Legislative session for which it is filed. Form 602 must be filed by \
a firm or its client, prior to attempting to influence legislative or \
administrative action on behalf of that client.'
    ),
    FilingForm(
        'F603',
        'Lobbyist Employer or Lobbying Coalition Registration Statement',
        group='LOBBYIST',
        documentcloud_id='2781346-603-2014-10',
        description='Form 603 is a registration statement filed by registered \
lobbyists employers or lobbying coalitions upon qualifying as an employer or \
coalition. This form is also used to renew an existing registration on a biennial \
basis. Form 603 must be filed within 10days of qualifying as a lobbyist employer \
or lobbying coalition. Renewal of an existing registration is due between November \
1 and December 31 of each even-numbered year. This registration is valid for the \
complete two-year cycle of such session.'
    ),
    FilingForm(
        'F604',
        'Lobbyist Certification Statement',
        group='LOBBYIST',
        documentcloud_id='2781345-604-2014-10',
        description="Form 604 is the certification statement filed by an \
individual who qualifies as a lobbyist (including an individual contract lobbyist\
). Form 604 is the initial certification statement and is also used as a renewal \
of a previous lobbyist certification. This form includes verification as to \
whether the lobbyist has attended a required course within the previous 12 months \
on ethical issues and laws relating to lobbying. When submitted as a paper filing\
, this form is an attachment to either the firm's Form 601 or the employer's Form \
603. If the form is filed electronically, it is filed separately by the lobbyist."
    ),
    FilingForm(
        'F605',
        'Amendment to Registration, Lobbying Firm, Lobbyist Employer, Lobbying Coalition',
        group='LOBBYIST',
        documentcloud_id='2781344-605-2014-10',
        description='Form 605 is the standard amendment form used to amend \
any previously-filed registration information. It is used to add or delete both \
lobbyists and clients to an existing registration. It is also used to change name\
, address, and responsible officer information, as well as any other pertinent \
information found on Forms 601, 602, 603 or 604.'
    ),
    FilingForm(
        'F606',
        'Notice of Termination',
        group='LOBBYIST',
        documentcloud_id='2781343-606-1997',
        description='Form 606 is filed by any lobbying firm, registered \
lobbyist employer, lobbying coalition or lobbyist who wishes to terminate a filed \
registration or certification statement. A client of a firm (non-registered employer\
) does not use this form to cease lobbying activity. Instead it is deleted by the \
associated firm, which files a Form 605. Form 606 is filed within 20 days of \
ceasing all lobbying activity. A final quarterly disclosure statement must be filed \
for the quarter in which the date of termination is effective.'
    ),
    FilingForm(
        'F607',
        'Notice of Withdrawal',
        group='LOBBYIST',
        documentcloud_id='2781342-607-1997-08',
        description='Form 607 is filed by a lobbying firm or lobbyist wishing \
to withdraw the filed registration statement of a firm which has never met the \
statutory definition of a lobbying firm or lobbyist. Submittal of this form \
relieves the filer of any duty to file any previously-required quarterly \
disclosure statements.'
    ),
    FilingForm(
        'F615',
        'Lobbyist Report',
        group='LOBBYIST',
        documentcloud_id='2781341-615-1990',
        description='Form 615 is the quarterly disclosure statement completed \
by the in-house lobbyist of a lobbying firm, lobbyist employer, or lobbying \
coalition. It is not filed on its own, but rather, for paper filers, it is an \
attachment to either Form 625 (Report of Lobbying Firm) or Form 635 (Report of \
Lobbyist Employer/Lobbying Coalition) Electronic or online filers file these as \
separate documents.'
    ),
    FilingForm(
        'F625',
        'Report of Lobbying Firm',
        group='LOBBYIST',
        documentcloud_id='2781340-625-1990',
        description='Form 625 is the quarterly disclosure statement filed by \
a lobbying firm (including individual contract lobbyists) each calendar quarter. \
If the firm employs one or more in-house lobbyists, then, for paper filers, a \
separate Form 615 (Lobbyist Report) must be attached for each lobbyist. Electronic \
or online filers file these as separate documents.'
    ),
    FilingForm(
        'S630',
        'Payments Made to Lobbying Coalitions (Attachment to Form 625 or 635) ',
        group='LOBBYIST',
        documentcloud_id='2782806-630-1990',
        description='An attachment to the quarterly disclosure report filed \
by a lobbying firm or lobbyist employer which makes payments to a lobbying \
coalition. This attachment itemizes such payments.'
    ),
    FilingForm(
        'F635',
        'Report of Lobbyist Employer or Report of Lobbying Coalition',
        group='LOBBYIST',
        documentcloud_id='2781339-635-1993',
        description='Form 635 is the quarterly disclosure statement filed by \
a lobbyist employer or a lobbying coalition. For employers and lobbying \
coalitions filing on paper, a separate Form 615 must be completed for each in \
house lobbyist and attached to Form 635. Electronic or online filers file these \
as separate documents. This form is also used as a quarterly disclosure statement \
for a client of a firm which has no in-house lobbyist (also referred to as a \
non-registered employer).'
    ),
    FilingForm(
        'S635C',
        'Payments Received by Lobbying Coalitions',
        group='LOBBYIST',
        documentcloud_id='2781338-635C-1990',
        description='Form 635-C is filed by a lobbying coalition as an \
attachment to the Form 635 (Report of a Lobbying Coalition) and discloses all \
payment received from the members of a coalition.'
    ),
    FilingForm(
        'S640',
        'Governmental Agencies Reporting (Attachment to Form 635 or Form 645)',
        group='LOBBYIST',
        documentcloud_id='2781337-640-1993',
        description='Form 640 is filed by a state or local governmental agency \
which qualifies as a lobbyist employer, or $5,000 filer. The attachment replaces \
Section D of Form 635 and Section B of Form 645 (both labeled Other Payments to \
Influence Legislative or Administrative Action ). It is filed in conjunction with \
either Form 635 (if a lobbyist employer) or Form 645 (if a $5,000 filer).'
    ),
    FilingForm(
        'F645',
        'Report of Person Spending $5,000 or More',
        group='LOBBYIST',
        documentcloud_id='2781336-645-1993',
        description='Form 645 is the quarterly disclosure document filed by a \
$5,000 filer (person who does not employ a lobbyist or contract with a lobbying \
firm, but who makes payments to influence legislative or administrative action \
in aggregation of $5,000 or more in any calendar quarter). The filer does not \
submit a registration or termination statement, and is only required to file Form \
645 in those calendar quarters which $5,000 or more is spent to influence legislative \
or administrative action. Form 645 must be filed electronically.'
    ),
    FilingForm(
        'F690',
        'Amendment to Lobbying Disclosure Report',
        group='LOBBYIST',
        documentcloud_id='2781335-690-1990',
        description='Form 690 is filed by a lobbying firm, lobbyist employer, \
lobbying coalition, $5,000 filer or lobbyist seeking to amend any information \
previously submitted on a quarterly disclosure report. Any amendment to the \
registration statement should be made on Form 605 rather than Form 690. \
Amendments must be filed by the same method (paper or electronic) as the original \
form.'
    ),
    FilingForm(
        'F700',
        'Statement of Economic Interest',
        group='FINANCIAL DISCLOSURE',
        documentcloud_id='2792958-700-2015-12',
        description='Every public official who makes or participates in making \
governmental decisions is required to file a Statement of Economic Interest, \
commonly referred to as the Form 700.',
    ),
    FilingForm(
        'F900',
        'Public employee\'s retirement board, candidate campaign statement',
        group='CAMPAIGN',
    ),
]


def get_filing_form(id):
    """
    Takes an id for a filing form and returns a FilingForm object
    """
    return next((x for x in all_filing_forms if x.id == id), None)
