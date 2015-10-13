# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, a suite of business apps
#    This module Copyright (C) 2014 Therp BV (<http://therp.nl>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.openupgrade import openupgrade


column_renames = {
    'survey_question': [('validation_minimum_no', 'validation_length_min'),
                        ('validation_maximum_no', 'validation_length_max'),
                        ('validation_minimum_float', 'validation_min_float_value'),
                        ('validation_maximum_float', 'validation_max_float_value'),
                        ('validation_minimum_date','validation_min_date'),
                        ('validation_maximum_date','validation_max_date'),],}
                        # ('descriptive_text', None)
    # 'survey_page': [
    #     ('note', None),
    # ],

xmlid_renames = [
    ('base.group_tool_manager', 'base.group_survey_manager'),
    ]


@openupgrade.migrate()
def migrate(cr, version):
    openupgrade.rename_columns(cr, column_renames)
    openupgrade.rename_xmlids(cr, xmlid_renames)
    openupgrade.rename_models(cr, [('survey', 'survey.survey'),('survey.answer','survey.label')])
    openupgrade.rename_tables(cr, [('survey', 'survey_survey'),('survey_answer','survey_label')])
    cr.execute("ALTER TABLE survey_page DROP CONSTRAINT IF EXISTS {}".format('survey_page_survey_id_fkey'))
    cr.execute("ALTER TABLE survey_question DROP CONSTRAINT IF EXISTS {}".format('survey_answer_question_id_fkey'))
