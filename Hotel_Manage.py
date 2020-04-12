#!/usr/bin/env python3
# coding = utf-8

# https://www.youtube.com/watch?v=RaESMr2DnGM -> Captain D.J Oamen
# 1:32, 2:00, 5:53, 7:57, 9:13, 10:11, 10:17, 10:35, 11:25, 14:08
# 20:55, 22:31, 26:57, 32:19, 37:26, 39:37, 42:48, 45:00, 52:08,
# 55:08, 1:00:18, 1:07:43, 1:16:24, 1:20:43,
# 1:21:56, 1:22:33, 1:23:17, 1:23:37, 1:29:27,
# 1:31:16, 1:35:50, 1:37:08

# Craig Miles -> cmiles69@hushmail.com
# https://github.com/cmiles69/Hotel.git

import tkinter
from tkinter import font
from tkinter import ttk
from tkcalendar import DateEntry  # Need to pip3 install tkcalendar 
import tkinter.scrolledtext as tkst
import tkinter.messagebox as msg_box
from datetime import date
from datetime import datetime
import string
import re
import random
import secrets
import names  # Need to pip3 install names --user
from faker import Faker  # Date faker and more - need to pip3 install 
# faker-e164 -> phone numbers pip3 install
import pycountry  # Need to pip3 install pycountry --user
import Hotel_DB

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
        self.root.protocol( 'WM_DELETE_WINDOW', self.Ask_Quit )
        self.setup_frames()
        self.setup_fonts()
        self.setup_variables()
        self.setup_frame_widgets()
        self.setup_buttons()  # 675 -> Button Callbacks
        self.setup_random_booking_information()

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
        self.message_font = font.Font( family = 'Bitstream Charter',
                                       size = 26,
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

#=========================Title Frame===================================

        self.lbl_message = tkinter.Label( self.frm_title,
                                font = self.message_font,
                                background = 'yellow',
                                text = 'Some Kind Of Message Here' )
        self.lbl_message.place( relx = 0.25,
                                rely = 0.1 )


        # self.lbl_customer_reference = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Customer Ref' )
        # self.lbl_customer_reference.place( relx = 0,
        #                                    rely = 0.30 )

        # self.lbl_first_name = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Firstname' )
        # self.lbl_first_name.place( relx = 0.130,
        #                            rely = 0.30 )

        # self.lbl_sur_name = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Surname' )
        # self.lbl_sur_name.place( relx = 0.23,
        #                          rely = 0.30 )

        # self.lbl_street_address = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Street Address' )
        # self.lbl_street_address.place( relx = 0.330,
        #                                rely = 0.30 )

        # self.lbl_sex_type = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Gender' )
        # self.lbl_sex_type.place( relx = 0.470,
        #                          rely = 0.30 )

        # self.lbl_cell_phone = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Mobile' )
        # self.lbl_cell_phone.place( relx = 0.550,
        #                            rely = 0.30 )

        # self.lbl_country = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Nationality' )
        # self.lbl_country.place( relx = 0.630,
        #                         rely = 0.30 )

        # self.lbl_ID = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'ID' )
        # self.lbl_ID.place( relx = 0.745,
        #                    rely = 0.30 )

        # self.lbl_date_in = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'In' )
        # self.lbl_date_in.place( relx = 0.795,
        #                         rely = 0.30 )

        # self.lbl_date_out = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Out' )
        # self.lbl_date_out.place( relx = 0.835,
        #                          rely = 0.30 )

        # self.lbl_E_mail = tkinter.Label( self.frm_title,
        #                         font = self.title_font,
        #                         background = 'yellow',
        #                         text = 'Email' )
        # self.lbl_E_mail.place( relx = 0.890,
        #                        rely = 0.30 )

#=======================Text Frame Scrolled Text========================

        self.tbox = tkst.ScrolledText( self.frm_text,
                                       background = 'red',
                                       foreground = 'blue',
                                       wrap = tkinter.WORD,
                                       relief = tkinter.RIDGE )
        self.tbox.place( relx = 0,
                         rely = 0,
                         relwidth = 1,
                         relheight = 1 )

# Decided to place a 'Treeview' widget into ScrolledText================

        style = ttk.Style()
        style.configure( 'Treeview.Heading', font = self.title_font )
        style.configure( 'Treeview', background = 'red',
                                     foreground = 'blue' )

        self.tree_view = ttk.Treeview( self.tbox,
            column = ( 'column1',
                       'column2',
                       'column3',
                       'column4',
                       'column5' ), show = 'headings' )
        self.tree_view.column( 'column1', width = 100 )
        self.tree_view.column( 'column2', width = 120 )
        self.tree_view.column( 'column3', width = 120 )
        self.tree_view.column( 'column4', width = 120 )
        self.tree_view.heading( '#1', text = 'Reference :' )
        self.tree_view.heading( '#2', text = 'First Name :' )
        self.tree_view.heading( '#3', text = 'Surname :' )
        self.tree_view.heading( '#4', text = 'Mobile :' )
        self.tree_view.heading( '#5', text = 'Email :' )
        self.tree_view.bind( '<<TreeviewSelect>>',
                            self.On_Tree_Select )
        self.tree_view.place( relx = 0,
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

#=======================Button Callbacks================================

    def Ask_Quit( self ):
        exit_program = tkinter.messagebox.askyesno(
            title = 'Hotel Database Management System',
            message = 'Confirm if you want to exit program?' )
        if exit_program > 0:
            self.root.destroy()
        return

    def Reset( self ):
        self.ent_customer_ID.delete( 0, tkinter.END )
        self.ent_firstname.delete( 0, tkinter.END )
        self.ent_surname.delete( 0, tkinter.END )
        self.ent_address.delete( 0, tkinter.END )
        self.ent_DOB.delete( 0, tkinter.END )
        self.ent_post_code.delete( 0, tkinter.END )
        self.ent_mobile.delete( 0, tkinter.END )
        self.ent_email.delete( 0, tkinter.END )
        self.ent_nationality.delete( 0, tkinter.END )
        self.ent_gender.current( 0 )
        self.check_in_date.set( '' )
        self.check_out_date.set( '' )
        self.ent_proof_of_ID.current( 0 )
        self.ent_meal_type.current( 0 )
        self.ent_room_type.current( 0 )
        self.ent_room_number.current( 0 )
        self.ent_room_phone.current( 0 )
        self.number_days.set( '' )
        self.paid_tax.set( '' )
        self.sub_total.set( '' )
        self.total_cost.set( '' )
        # for idx in self.tree_view.get_children():
        #     self.tree_view.delete( idx )
        

    def Random_Data( self ):
        self.setup_random_booking_information()


    def Add_Booking( self ):
        booking = [( self.ent_customer_ID.get(),
                     self.ent_firstname.get(),
                     self.ent_surname.get(),
                     self.ent_address.get(),
                     self.ent_DOB.get(),
                     self.ent_post_code.get(),
                     self.ent_mobile.get(),
                     self.ent_email.get(),
                     self.ent_nationality.get(),
                     self.ent_gender.get(),
                     self.check_in_date.get(),
                     self.check_out_date.get(),
                     self.ent_proof_of_ID.get(),
                     self.ent_meal_type.get(),
                     self.ent_room_type.get(),
                     self.ent_room_number.get(),
                     self.ent_room_phone.get() )]

        last_row = Hotel_DB.insert_hotel_booking( booking )
        print( 'Last Row ID is :', last_row )
        self.total_days()

    def Delete_Booking( self, message = True ):
        customerID = self.On_Tree_Select( event = None )
        print( 'Delete CID', customerID )
        if message == True:
            delete_booking = tkinter.messagebox.askyesno(
                title = 'Hotel Database Management System',
                message = 'Confirm if you want to delete this booking?.' )
            if delete_booking > 0:
                self.Search_Booking()
                RV = Hotel_DB.delete_hotel_booking_record( customerID )
                self.Display_Booking()
                print( RV )
            else:
                return
        

    def Update_Booking( self ):
        ID = self.customer_ID.get()
        booking = [( self.ent_customer_ID.get(),
                     self.ent_firstname.get(),
                     self.ent_surname.get(),
                     self.ent_address.get(),
                     self.ent_DOB.get(),
                     self.ent_post_code.get(),
                     self.ent_mobile.get(),
                     self.ent_email.get(),
                     self.ent_nationality.get(),
                     self.ent_gender.get(),
                     self.check_in_date.get(),
                     self.check_out_date.get(),
                     self.ent_proof_of_ID.get(),
                     self.ent_meal_type.get(),
                     self.ent_room_type.get(),
                     self.ent_room_number.get(),
                     self.ent_room_phone.get(), ID )]

        Hotel_DB.update_hotel_booking_record( booking )
           

    def Search_Booking( self ):
        customerID = self.On_Tree_Select( event = None )
        data = Hotel_DB.search_hotel_booking_record( customerID )
        #print( data.keys())
        #print( data[3] )
        #print( data[r'Address'])
        self.Reset()

        self.customer_ID.set( data[r'Customer_ID'])
        self.firstname.set( data[r'Firstname'])
        self.surname.set( data[r'Surname'])
        self.address.set( data[r'Address'])
        self.date_of_birth.set( data[r'Birth_Date']) 
        self.post_code.set( data[r'Post_Code'])
        self.mobile_phone.set( data[r'Mobile'])
        self.email.set( data[r'Email'])
        self.nationality.set( data[r'Nationality'])
        self.gender.set( data[r'Gender'])
        self.check_in_date.set( data[r'DateIn']) 
        self.check_out_date.set( data[r'DateOut'])
        self.proof_of_ID.set( data[r'ID_Type'])
        self.meal_type.set( data[r'Meal_Type'])
        self.room_type.set( data[r'Room_Type'])
        self.room_number.set( data[r'Room_Number'])
        self.room_phone.set( data[r'Room_Phone'])

    def Display_Booking( self ):
        for idx in self.tree_view.get_children():
            self.tree_view.delete( idx )
        for row in Hotel_DB.display_hotel_booking_record():
            self.tree_view.insert( '', tkinter.END,
                                    values = ( row[r'Customer_ID'],
                                               row[r'Firstname'],
                                               row[r'Surname'],
                                               row[r'Mobile'],
                                               row[r'Email'] ))

    def On_Tree_Select(self, event):
        print("selected items:")
        # curItem = self.tree_view.focus() # These 2 lines work!
        # print( self.tree_view.item( curItem ))

        item = self.tree_view.selection()[0]
        # print( 'Item Clicked :', item )
        # print( 'Customer Reference :',
        #        self.tree_view.item( item )['values'][0] )
        # print( 'Customer First Name :',
        #        self.tree_view.item( item )['values'][1] )
        # print( 'Customer Last Name :',
        #        self.tree_view.item( item )['values'][2] )
        # print( 'Customer Mobile Phone :',
        #        self.tree_view.item( item )['values'][3] )
        # print( 'Customer Email :',
        #        self.tree_view.item( item )['values'][4] )

        ''' Return Customer Reference Number '''

        return( self.tree_view.item( item )['values'][0] )

#===============================Buttons=================================                        

    def setup_buttons( self ): # self.frm_button purple
        self.btn_total_data = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'SlateBlue1',
                                activebackground = 'thistle',
                                command = self.Add_Booking,
                                text = 'AddNew' )
        self.btn_total_data.place( relx = 0.006,
                                   rely = 0,
                                   relheight = 1 )

        self.btn_display = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'blue',
                                activebackground = 'sea green',
                                command = self.Display_Booking,
                                text = 'Display' )
        self.btn_display.place( relx = 0.098,
                                rely = 0,
                                relheight = 1 )

        self.btn_update = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'Orange',
                                activebackground = 'purple',
                                command = self.Update_Booking,
                                text = 'Update' )
        self.btn_update.place( relx = 0.183,
                               rely = 0,
                               relheight = 1 )

        self.btn_delete = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'gray25',
                                activebackground = 'black',
                                command = self.Delete_Booking,
                                text = 'Delete' )
        self.btn_delete.place( relx = 0.267,
                               rely = 0,
                               relheight = 1 )

        self.btn_search = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'blue',
                                activebackground = 'ghost white',
                                command = self.Search_Booking,
                                text = 'Search' )
        self.btn_search.place( relx = 0.344,
                               rely = 0,
                               relheight = 1 )

        self.btn_reset = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'red',
                                activebackground = 'ghost white',
                                command = self.Reset,
                                text = 'Reset' )
        self.btn_reset.place( relx = 0.424,
                              rely = 0,
                              relheight = 1 )

        self.btn_random = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'yellow',
                                activebackground = 'gray34',
                                command = self.Random_Data,
                                text = 'Random' )
        self.btn_random.place( relx = 0.495,
                               rely = 0,
                               relheight = 1 )

        self.btn_total_days = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'yellow',
                                activebackground = 'gray34',
                                command = self.total_days,
                                text = 'Total Days' )
        self.btn_total_days.place( relx = 0.587,
                                   rely = 0,
                                   relheight = 1 )

        self.btn_exit = tkinter.Button( self.frm_button,
                                font = self.btn_font,
                                borderwidth = 4,
                                activeforeground = 'green',
                                activebackground = 'ghost white',
                                command = self.Ask_Quit,
                                text = 'Exit' )
        self.btn_exit.place( relx = 0.695,
                             rely = 0,
                             relheight = 1 )


#=======================Random Booking Information======================

    # def generate_random_string( self, string_length = 10 ):
    #     ''' Generate a random string of fixed length '''
    #     letters = string.ascii_lowercase
    #     return ''.join( secrets.choice( letters )
    #                     for i in range( string_length ))

    def generate_random_birth_date( self, 
                                    start_date = '-90y',
                                    end_date = '-15y' ):
        fake = Faker()
        FD = fake.date_of_birth()  # Max age = 115
        return( FD.strftime( '%d-%m-%Y' ))

    def generate_random_future_date( self ):
        fake = Faker()
        FD = fake.date_between(start_date = 'today',
                               end_date = '+25d')
        return( FD.strftime( '%d-%m-%Y' ))

    def generate_date_today( self ):
        TD = date.today()
        return( TD.strftime( '%d-%m-%Y' ))

    def generate_random_address( self ):
        fake = Faker()
        return( fake.address())

    def generate_random_email( self ):
        fake = Faker()
        return( fake.email())

    def generate_random_first_name( self ):
        return( names.get_first_name())

    def generate_random_surname( self ):
        return( names.get_last_name())

    def generate_random_mobile_number( self ):
        ''' Yes, well, cell phone number '''
        prefix = ['021', '022', '025', '027', '029']
        pre_cell = str( secrets.choice( prefix ))
        num_cell = str( secrets.randbits( 32 ))
        return( pre_cell + num_cell )

    def generate_random_post_code( self ):
        ''' 7 digit number '''
        lowest_number = int( 1000000 )
        highest_number = int( 9999998 )
        SG = secrets.SystemRandom()
        post_code = SG.randint( lowest_number, highest_number )
        return( str( post_code ))

    def generate_random_country( self ):
        ''' Random Country '''
        rand_num = random.randint( 0, len( pycountry.countries ))
        country_name = list( pycountry.countries)[rand_num].name
        return( country_name )

    def generate_random_gender( self ):
        ''' Random Gender '''
        RG = random.randint( 1, len( self.ent_gender['values'][:-1] ))
        return( self.ent_gender['values'][RG] )

    def generate_random_ID_type( self ):
        ''' Random type of ID '''
        RID = random.randint( 1,
                len( self.ent_proof_of_ID['values'][:-1] ))
        return( self.ent_proof_of_ID['values'][RID] )

    def generate_random_meal( self ):
        ''' Random Meal '''
        RM = random.randint( 1,
                len( self.ent_meal_type['values'][:-1] ))
        return( self.ent_meal_type['values'][RM] )

    def generate_random_room_type( self ):
        ''' Random Room Type '''
        RRT = random.randint( 1,
                len( self.ent_room_type['values'][:-1] ))
        return( self.ent_room_type['values'][RRT] )

    def generate_random_room_number( self ):
        ''' Random Room Number '''
        RRN = random.randint( 1,
                len( self.ent_room_number['values'][:-1] ))
        return( self.ent_room_number['values'][RRN] )

    def generate_random_room_phone( self ):
        ''' Random Room Phone Number '''
        RRPN = random.randint( 1,
                len( self.ent_room_phone['values'][:-1] ))
        return( self.ent_room_phone['values'][RRPN] )

    def setup_random_booking_information( self ):
        ''' Using string variables line 88.
            For the Combo Boxes a Zero entry
            means no choice ( blank ). This is
            Not an error, just a choice.
            Also the fake address generator has
            caused 'subscriptable' problems,
            fixed by 'coding=utf8' on second line
            of this file '''

        self.customer_ID.set( str( secrets.token_hex( 5 )))
        self.firstname.set( self.generate_random_first_name())
        self.surname.set( self.generate_random_surname())
        self.address.set( self.generate_random_address())
        self.date_of_birth.set( self.generate_random_birth_date())
        self.post_code.set( self.generate_random_post_code())
        self.mobile_phone.set( self.generate_random_mobile_number())
        self.email.set( self.generate_random_email())
        self.nationality.set( self.generate_random_country())
        self.gender.set( self.generate_random_gender())
        self.check_in_date.set( self.generate_date_today())
        self.check_out_date.set( self.generate_random_future_date())
        self.proof_of_ID.set( self.generate_random_ID_type())
        self.meal_type.set( self.generate_random_meal())
        self.room_type.set( self.generate_random_room_type())
        self.room_number.set( self.generate_random_room_number())
        self.room_phone.set( self.generate_random_room_phone())

#===========================Total Days==================================
    def total_days( self ):
        date_format = '%d-%m-%Y'
        in_date = datetime.strptime( 
                  self.check_in_date.get(), date_format )
        out_date = datetime.strptime(
                  self.check_out_date.get(), date_format )
        self.number_days.set( abs(( out_date - in_date ).days ))

        self.meal_cost = {'Breakfast':          17.00,
                         'Full Breakfast':      22.00,
                         'Champange Breakfast': 32.00,
                         'Instant Breakfast':   15.00,
                         'Lunch':               25.00,
                         'Packed Lunch':        16.00,
                         'Dinner':              35.00,
                         'Sunday Dinner':       38.00,
                         'Full Course Dinner':  45.00}

        self.room_cost = {'Single Room':    34.00,
                         'Double Room':     43.00,
                         'Twin Room':       63.00,
                         'Studio Room':     83.00,
                         'Triple Room':     103.00,
                         'Quad Room':       123.00,
                         'Queen Room':      143.00,
                         'King Room':       163.00,
                         'Mini Suite Room': 183.00,
                         'Suite Room':      250.00}

        # MT = self.generate_random_meal()
        # RT = self.generate_random_room_type()
        MT = self.meal_type.get()
        RT = self.room_type.get()
        print( 'Total Days is :', self.number_days.get()) 
        print( 'Meal Type is :', MT )
        print( 'Meal Cost is :', self.meal_cost[MT] )
        print( 'Room Type is :', RT )
        print( 'Room Cost is :', self.room_cost[RT] )

#===========================Math========================================

        meal_cost = float( self.meal_cost[MT] )
        room_cost = float( self.room_cost[RT] )
        number_of_days = float( self.number_days.get())
        meal_room = float( meal_cost + room_cost )
        days_meal_room = float( number_of_days * meal_room )

        the_tax = '$' + str( '%.2f' % (( days_meal_room ) * 0.09 ))
        sub_total = '$' + str( '%.2f' % (( days_meal_room )))
        the_total = '$' + str( '%.2f' % ( days_meal_room + 
                                        (( days_meal_room ) * 0.09 )))
        self.paid_tax.set( the_tax )
        self.sub_total.set( sub_total )
        self.total_cost.set( the_total )

        print( 'Paid Tax is :', the_tax )
        print( 'Sub Total is :', sub_total )
        print( 'Total Cost is :', the_total )


if __name__ == '__main__':
    root = tkinter.Tk()
    application = Hotel( root )
    root.mainloop()