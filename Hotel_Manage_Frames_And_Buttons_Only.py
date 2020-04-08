#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# https://www.youtube.com/watch?v=RaESMr2DnGM -> Captain D.J Oamen
# 1:32, 2:00, 5:53, 7:57, 9:13, 10:11, 10:17, 10:35, 11:25, 14:08
# 20:55, 22:31, 26:57, 32:19, 37:26, 39:37, 42:48

# Craig Miles -> cmiles69@hushmail.com

import tkinter
from tkinter import font
from tkinter import ttk
from tkcalendar import DateEntry  # Need to pip install tkcalendar
import tkinter.scrolledtext as tkst
import tkinter.messagebox as msg_box
import time
import datetime
import random
import secrets

class Hotel:

    def __init__( self, root ):
        self.root = root
        self.initUI()

    def initUI( self ):
        self.root.title( 'Hotel Database Management System' )
        self.geometry = self.screen_size( size = 0.75 )
        # print( self.geometry )
        self.root.geometry( self.geometry )
        self.center_root()
        self.root.configure( background = 'deep sky blue' )
        self.setup_frames()
        self.setup_fonts()
        self.setup_variables()
        self.setup_frame_widgets()
        self.setup_buttons()

    def screen_size( self, size ):
        # Obtain desired screen size
        width = self.root.winfo_screenwidth() * size
        height = self.root.winfo_screenheight() * size
        return( '{}x{}+{}+{}' 
        .format( int( width ), int( height ), 0, 0 ))

    def center_root( self ):
        self.root.update_idletasks()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        pos_right = \
        int( self.root.winfo_screenwidth() // 2 - window_width // 2 )
        pos_down = \
        int( self.root.winfo_screenheight() // 2 - window_height // 2 )
        self.root.geometry( '{}x{}+{}+{}'
        .format( window_width, window_height, pos_right, pos_down ))

    def setup_frames( self ):
        self.setup_main_frame()
        self.setup_button_frame()
        self.setup_reference_frame()
        self.setup_title_frame()
        self.setup_text_frame()
        self.setup_days_frame()
        

#===========================Fonts=======================================

    def setup_fonts( self ):
        self.title_font = font.Font( family = 'DejaVu Serif',
                                   size = 10,
                                   weight = 'bold' )
        self.lbl_font = font.Font( family = 'DejaVu Serif',
                                   size = 12,
                                   weight = 'bold' )
        self.ent_font = font.Font( family = 'DejaVu Serif',
                                   size = 12,
                                   weight = 'bold' )
        self.btn_font = font.Font( family = 'Bitstream Charter',
                                   size = 16,
                                   weight = 'bold' )

#============================Variables==================================

    def setup_variables( self ):
        self.customer_ID = tkinter.StringVar()
        self.firstname = tkinter.StringVar()
        self.surname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.date_of_birth = tkinter.StringVar()
        self.post_code = tkinter.StringVar()
        self.mobile_phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.nationality = tkinter.StringVar()
        self.gender = tkinter.StringVar()
        self.check_in_date = tkinter.StringVar()
        self.check_out_date = tkinter.StringVar()
        self.proof_of_ID = tkinter.StringVar()
        self.meal_type = tkinter.StringVar()
        self.room_type = tkinter.StringVar()
        self.room_number = tkinter.StringVar()
        self.room_phone = tkinter.StringVar()
        self.number_days = tkinter.StringVar()
        self.paid_tax = tkinter.StringVar()
        self.sub_total = tkinter.StringVar()
        self.total_cost = tkinter.StringVar()

#=============================Frames====================================

    def setup_main_frame( self ):
        self.frm_main = tkinter.Frame( self.root,
                                       borderwidth = 10,
                                       background = 'deep sky blue',
                                       relief = tkinter.RIDGE )
        self.frm_main.place( relx = 0,
                             rely = 0,
                             relwidth = 1,
                             relheight = 1 )

    def setup_button_frame( self ):
        self.frm_button = tkinter.Frame( self.frm_main,
                                         borderwidth = 10,
                                         background = 'purple',
                                         relief = tkinter.RIDGE )
        self.frm_button.place( relx = 0,
                               rely = 0.90,
                               relwidth = 1,
                               relheight = 0.10 )

    def setup_reference_frame( self ):
        self.frm_reference = tkinter.Frame( self.frm_main,
                                            borderwidth = 10,
                                            background = 'green',
                                            relief = tkinter.RIDGE )
        self.frm_reference.place( relx = 0,
                                  rely = 0,
                                  relwidth = 0.2857,
                                  relheight = 0.90 )

    def setup_title_frame( self ):
        self.frm_title = tkinter.Frame( self.frm_main,
                                        borderwidth = 10,
                                        background = 'yellow',
                                        relief = tkinter.RIDGE )
        self.frm_title.place( relx = 0.2858,
                              rely = 0,
                              relwidth = 0.7143,
                              relheight = 0.10 )

    def setup_text_frame( self ):
        self.frm_text = tkinter.Frame( self.frm_main,
                                       borderwidth = 10,
                                       background = 'red',
                                       relief = tkinter.RIDGE )
        self.frm_text.place( relx = 0.2858,
                             rely = 0.1005,
                             relwidth = 0.7143,
                             relheight = 0.55 )

    def setup_days_frame( self ):
        self.frm_days = tkinter.Frame( self.frm_main,
                                       borderwidth = 10,
                                       background = 'violet',
                                       relief = tkinter.RIDGE )
        self.frm_days.place( relx = 0.2858,
                             rely = 0.652,
                             relwidth = 0.7143,
                             relheight = 0.246 )

#=======================Frame Widgets===================================

    def setup_frame_widgets( self ):

#=======================Reference Frame=================================

        self.lbl_customer_ID = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Customer Ref:' )
        self.lbl_customer_ID.place( relx = 0.054,
                                    rely = 0.003,
                                    relwidth = 0.35,
                                    relheight = 0.045 )
        self.ent_customer_ID = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.customer_ID )
        self.ent_customer_ID.place( relx = 0.47,
                                    rely = 0,
                                    relwidth = 0.52,
                                    relheight = 0.045 )

        self.lbl_firstname = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'First Name:' )
        self.lbl_firstname.place( relx = 0.082,
                                  rely = 0.051,
                                  relwidth = 0.35,
                                  relheight = 0.045 )
        self.ent_firstname = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.firstname )
        self.ent_firstname.place( relx = 0.47,
                                  rely = 0.049,
                                  relwidth = 0.52,
                                  relheight = 0.045 )

        self.lbl_surname = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Surname:' )
        self.lbl_surname.place( relx = 0.085,
                                rely = 0.099,
                                relwidth = 0.39,
                                relheight = 0.045 )
        self.ent_surname = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.surname )
        self.ent_surname.place( relx = 0.47,
                                rely = 0.099,
                                relwidth = 0.52,
                                relheight = 0.045 )

        self.lbl_address = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Address:' )
        self.lbl_address.place( relx = 0.095,
                                rely = 0.149,
                                relwidth = 0.39,
                                relheight = 0.045 )
        self.ent_address = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.address )
        self.ent_address.place( relx = 0.47,
                                rely = 0.150,
                                relwidth = 0.52,
                                relheight = 0.045 )

        self.lbl_DOB = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Date Of Birth:' )
        self.lbl_DOB.place( relx = 0.030,
                            rely = 0.200,
                            relwidth = 0.39,
                            relheight = 0.045 )
        self.ent_DOB = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.date_of_birth )
        self.ent_DOB.place( relx = 0.47,
                            rely = 0.201,
                            relwidth = 0.52,
                            relheight = 0.045 )

        self.lbl_post_code = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Post Code:' )
        self.lbl_post_code.place( relx = 0.067,
                                  rely = 0.251,
                                  relwidth = 0.39,
                                  relheight = 0.045 )
        self.ent_post_code = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.post_code )
        self.ent_post_code.place( relx = 0.47,
                                  rely = 0.251,
                                  relwidth = 0.52,
                                  relheight = 0.045 )

        self.lbl_mobile = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Mobile Phone:' )
        self.lbl_mobile.place( relx = 0.022,
                               rely = 0.301,
                               relwidth = 0.39,
                               relheight = 0.045 )
        self.ent_mobile = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.mobile_phone )
        self.ent_mobile.place( relx = 0.47,
                               rely = 0.301,
                               relwidth = 0.52,
                               relheight = 0.045 )

        self.lbl_email = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Email Address:' )
        self.lbl_email.place( relx = 0.020,
                              rely = 0.351,
                              relwidth = 0.39,
                              relheight = 0.045 )
        self.ent_email = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.email )
        self.ent_email.place( relx = 0.47,
                              rely = 0.351,
                              relwidth = 0.52,
                              relheight = 0.045 )

        self.lbl_nationality = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Nationality:' )
        self.lbl_nationality.place( relx = 0.056,
                                    rely = 0.401,
                                    relwidth = 0.39,
                                    relheight = 0.045 )
        self.ent_nationality = tkinter.Entry( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.nationality )
        self.ent_nationality.place( relx = 0.47,
                                    rely = 0.401,
                                    relwidth = 0.52,
                                    relheight = 0.045 )

        self.lbl_gender = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Gender:' )
        self.lbl_gender.place( relx = 0.099,
                               rely = 0.451,
                               relwidth = 0.39,
                               relheight = 0.045 )
        self.ent_gender = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.gender )
        self.ent_gender['values'] = ( '',
                                      'Male',
                                      'Female',
                                      'Transsexual',
                                      'Trans Man',
                                      'Trans Women',
                                      'Transitioning',
                                      'Genderqueer',
                                      'Indeterminate Sex',
                                      'Not Stated',
                                      'Refused to answer',
                                      'Response Unidentifiable' )
        self.ent_gender.current( 0 )
        self.ent_gender.place( relx = 0.47,
                               rely = 0.451,
                               relwidth = 0.52,
                               relheight = 0.045 )

        self.lbl_check_in_date = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Check In Date:' )
        self.lbl_check_in_date.place( relx = 0.018,
                                      rely = 0.501,
                                      relwidth = 0.39,
                                      relheight = 0.045 )

#=============================DateEntry=================================
# pip install tkcalendar -> https://github.com/j4321/tkcalendar
# Make note of the date_pattern
#=======================================================================

        self.ent_check_in_date = DateEntry( self.frm_reference,
                                font = self.ent_font,
                                year = 2020,  # Default to today
                                month = 4,    # If not prescent
                                date_pattern = 'dd-mm-y',
                                textvariable = self.check_in_date )
        self.ent_check_in_date.place( relx = 0.47,
                                      rely = 0.501,
                                      relwidth = 0.52,
                                      relheight = 0.045 )

        self.lbl_check_out_date = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Check Out Date:' )
        self.lbl_check_out_date.place( relx = 0,
                                       rely = 0.551,
                                       relwidth = 0.39,
                                       relheight = 0.045 )
        self.ent_check_out_date = DateEntry( self.frm_reference,
                                font = self.ent_font,
                                year = 2020,
                                month = 4,
                                date_pattern = 'dd-mm-y',
                                textvariable = self.check_out_date )
        self.ent_check_out_date.place( relx = 0.47,
                                       rely = 0.551,
                                       relwidth = 0.52,
                                       relheight = 0.045 )

        self.lbl_proof_of_ID = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Type Of ID:' )
        self.lbl_proof_of_ID.place( relx = 0.06,
                                    rely = 0.601,
                                    relwidth = 0.39,
                                    relheight = 0.045 )
        self.ent_proof_of_ID = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.proof_of_ID )
        self.ent_proof_of_ID['values'] = ( '',
                                           'Driving Licence',
                                           'Student ID',
                                           'Passport',
                                           'Pilot Licence',
                                           'Birth Certificate',
                                           'Social Security Card' )
        self.ent_proof_of_ID.current( 0 )
        self.ent_proof_of_ID.place( relx = 0.47,
                                    rely = 0.601,
                                    relwidth = 0.52,
                                    relheight = 0.045 )

        self.lbl_meal_type = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Type Of Meal:' )
        self.lbl_meal_type.place( relx = 0.03,
                                  rely = 0.651,
                                  relwidth = 0.39,
                                  relheight = 0.045 )
        self.ent_meal_type = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.meal_type )
        self.ent_meal_type['values'] = ( '',
                                         'Breakfast',
                                         'Full Breakfast',
                                         'Champange Breakfast',
                                         'Instant Breakfast',
                                         'Lunch',
                                         'Packed Lunch',
                                         'Dinner',
                                         'Sunday Dinner',
                                         'Full Course Dinner' )
        self.ent_meal_type.current( 0 )
        self.ent_meal_type.place( relx = 0.47,
                                  rely = 0.651,
                                  relwidth = 0.52,
                                  relheight = 0.045 )

        self.lbl_room_type = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Type Of Room:' )
        self.lbl_room_type.place( relx = 0.020,
                                  rely = 0.701,
                                  relwidth = 0.39,
                                  relheight = 0.045 )
        self.ent_room_type = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.room_type )
        self.ent_room_type['values'] = ( '',
                                         'Single Room',
                                         'Double Room',
                                         'Twin Room',
                                         'Studio Room',
                                         'Triple Room',
                                         'Quad Room',
                                         'Queen Room',
                                         'King Room',
                                         'Mini Suite Room',
                                         'Suite Room' )
        self.ent_room_type.current( 0 )
        self.ent_room_type.place( relx = 0.47,
                                  rely = 0.701,
                                  relwidth = 0.52,
                                  relheight = 0.045 )

        self.lbl_room_number = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Room Number:' )
        self.lbl_room_number.place( relx = 0.015,
                                    rely = 0.751,
                                    relwidth = 0.39,
                                    relheight = 0.045 )
        self.ent_room_number = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.room_number )
        self.ent_room_number['values'] = ( '',
                                           '001',
                                           '002',
                                           '003',
                                           '004',
                                           '005',
                                           '006',
                                           '007',
                                           '008',
                                           '009',
                                           '010' )
        self.ent_room_number.current( 0 )
        self.ent_room_number.place( relx = 0.47,
                                    rely = 0.751,
                                    relwidth = 0.52,
                                    relheight = 0.045 )

        self.lbl_room_phone = tkinter.Label( self.frm_reference,
                                font = self.lbl_font,
                                background = 'green',
                                text = 'Room Phone:' )
        self.lbl_room_phone.place( relx = 0.035,
                                   rely = 0.801,
                                   relwidth = 0.39,
                                   relheight = 0.045 )
        self.ent_room_phone = ttk.Combobox( self.frm_reference,
                                font = self.ent_font,
                                textvariable = self.room_phone )
        self.ent_room_phone['values'] = ( '',
                                          '101',
                                          '102',
                                          '103',
                                          '104',
                                          '105',
                                          '106',
                                          '107',
                                          '108',
                                          '109',
                                          '110' )
        self.ent_room_phone.current( 0 )
        self.ent_room_phone.place( relx = 0.47,
                                   rely = 0.801,
                                   relwidth = 0.52,
                                   relheight = 0.045 )

#=====================Title Frame=======================================

        self.lbl_customer_reference = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Customer Ref' )
        self.lbl_customer_reference.place( relx = 0,
                                           rely = 0.30 )

        self.lbl_first_name = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Firstname' )
        self.lbl_first_name.place( relx = 0.130,
                                   rely = 0.30 )

        self.lbl_sur_name = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Surname' )
        self.lbl_sur_name.place( relx = 0.23,
                                 rely = 0.30 )

        self.lbl_street_address = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Street Address' )
        self.lbl_street_address.place( relx = 0.330,
                                       rely = 0.30 )

        self.lbl_sex_type = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Gender' )
        self.lbl_sex_type.place( relx = 0.470,
                                 rely = 0.30 )

        self.lbl_cell_phone = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Mobile' )
        self.lbl_cell_phone.place( relx = 0.550,
                                   rely = 0.30 )

        self.lbl_country = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Nationality' )
        self.lbl_country.place( relx = 0.630,
                                rely = 0.30 )

        self.lbl_ID = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'ID' )
        self.lbl_ID.place( relx = 0.745,
                           rely = 0.30 )

        self.lbl_date_in = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'In' )
        self.lbl_date_in.place( relx = 0.795,
                                rely = 0.30 )

        self.lbl_date_out = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Out' )
        self.lbl_date_out.place( relx = 0.835,
                                 rely = 0.30 )

        self.lbl_E_mail = tkinter.Label( self.frm_title,
                                font = self.title_font,
                                background = 'yellow',
                                text = 'Email' )
        self.lbl_E_mail.place( relx = 0.890,
                               rely = 0.30 )

#=======================Text Frame Scrolled Text========================

        self.tbox = tkst.ScrolledText( self.frm_text,
                                       background = 'red',
                                       foreground = 'blue',
                                       relief = tkinter.RIDGE )
        self.tbox.place( relx = 0,
                         rely = 0,
                         relwidth = 1,
                         relheight = 1 )

#=======================Number Of Days Frame============================
        
        self.lbl_number_days = tkinter.Label( self.frm_days,
                                    font = self.lbl_font,
                                    background = 'violet',
                                    text = 'Number Of Days:' )
        self.lbl_number_days.place( relx = 0.0050,
                                    rely = 0.003 )
        self.ent_number_days = tkinter.Entry( self.frm_days,
                                font = self.ent_font,
                                textvariable = self.number_days )
        self.ent_number_days.place( relx = 0.19,
                                    rely = 0.003 )

        self.lbl_paid_tax = tkinter.Label( self.frm_days,
                                    font = self.lbl_font,
                                    background = 'violet',
                                    text = 'Paid Tax:' )
        self.lbl_paid_tax.place( relx = 0.076,
                                 rely = 0.19 )
        self.ent_paid_tax = tkinter.Entry( self.frm_days,
                                font = self.ent_font,
                                textvariable = self.paid_tax )
        self.ent_paid_tax.place( relx = 0.19,
                                 rely = 0.19 )

        self.lbl_sub_total = tkinter.Label( self.frm_days,
                                    font = self.lbl_font,
                                    background = 'violet',
                                    text = 'Sub Total:' )
        self.lbl_sub_total.place( relx = 0.066,
                                  rely = 0.38 )
        self.ent_sub_total = tkinter.Entry( self.frm_days,
                                font = self.ent_font,
                                textvariable = self.sub_total )
        self.ent_sub_total.place( relx = 0.19,
                                  rely = 0.38 )

        self.lbl_total_cost = tkinter.Label( self.frm_days,
                                    font = self.lbl_font,
                                    background = 'violet',
                                    text = 'Total Cost:' )
        self.lbl_total_cost.place( relx = 0.061,
                                   rely = 0.57 )
        self.ent_total_cost = tkinter.Entry( self.frm_days,
                                font = self.ent_font,
                                textvariable = self.total_cost )
        self.ent_total_cost.place( relx = 0.19,
                                   rely = 0.57 )

#===============================Buttons=================================                        

    def setup_buttons( self ): # self.frm_button purple
        self.btn_total_data = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'SlateBlue1',
                                activebackground = 'thistle',
                                text = 'AddNew/Total' )
        self.btn_total_data.place( relx = 0.006,
                                   rely = 0,
                                   relheight = 1 )

        self.btn_display = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'blue',
                                activebackground = 'sea green',
                                text = 'Display' )
        self.btn_display.place( relx = 0.141,
                                rely = 0,
                                relheight = 1 )

        self.btn_update = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'Orange',
                                activebackground = 'purple',
                                text = 'Update' )
        self.btn_update.place( relx = 0.225,
                               rely = 0,
                               relheight = 1 )

        self.btn_delete = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'gray25',
                                activebackground = 'black',
                                text = 'Delete' )
        self.btn_delete.place( relx = 0.307,
                               rely = 0,
                               relheight = 1 )

        self.btn_search = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'blue',
                                activebackground = 'ghost white',
                                text = 'Search' )
        self.btn_search.place( relx = 0.382,
                               rely = 0,
                               relheight = 1 )

        self.btn_reset = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'red',
                                activebackground = 'ghost white',
                                text = 'Reset' )
        self.btn_reset.place( relx = 0.461,
                              rely = 0,
                              relheight = 1 )

        self.btn_exit = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'green',
                                activebackground = 'ghost white',
                                text = 'Exit' )
        self.btn_exit.place( relx = 0.530,
                             rely = 0,
                             relheight = 1 )


        

        


    
if __name__ == '__main__':
    root = tkinter.Tk()
    application = Hotel( root )
    root.mainloop()