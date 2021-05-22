def getType(obj):
    return ''.join(c for c in obj if not c.isdigit())

def getInst(obj):
    return ''.join(c for c in obj if c.isdigit())

def getLongType(obj):
    objDict = {
    "AV": "analog-value",
    "EV": "event-enrollment",
    "BV": "binary-value",
    "BI": "binary-input"
    }

    objType = objDict[''.join(c for c in obj if not c.isdigit())]

    return objType
    
def backupFile(row):

    name = row['Name']
    obj = row['Inst']
    
    return (
        f"Version:\t1\n" 
        f"Device:\t15600\n" 
        f"Device_Name:\t{name}\n" 
        f"Date_of_backup:\t2020/10/21/3\n" 
        f"Time_of_backup:\t12:33:02.73\n" 
        f"Vendor_Name:\tDelta Controls\n" 
        f"Vendor_Id:\t8\n" 
        f"Model_Name:\teBMGR\n" 
        f"Firmware_Revision:\t571848\n" 
        f"Application_SW_Version:\tV3.40\n" 
        f"Location:\t(null)\n" 
        f"Description:\t{obj}\n" 
        f"Protocol_Version:\t1\n" 
        f"Protocol_Revision:\t6\n" 
        f"Database_Revision:\t0\n" 
        f"<FILE_LIST_START>\n" 
        f"FIL1\tSTREAM\t{obj}.csml\t0\n" 
        f"<FILE_LIST_END>\n"
    )

def AVcsml(row):

    #Name,Inst,Units

    name = row['Name']
    obj = row['Inst']
    units = row['Units']
        
    return (
        f'<Object name="{obj}">\n'#
        f'<Real name="COV_Increment" value="1"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="analog-value,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="analog-value"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Real name="Present_Value" value="0"/>\n'
        f'<Enumerated name="Reliability" value="no-fault-detected"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Enumerated name="Units" value="{units}"/>\n'#
        f'<Unsigned name="Object_Size" value="0"/>\n'
        f'<BitString name="Flags" value=""/>\n'
        f'<Real name="GCL_Value" value=""/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<ObjectIdentifier name="Last_Writer" value="program,300"/>\n'
        f'<DateTime name="Time_Of_Last_Write" value="2020-10-21 12:33:01.95"/>\n'
        f'<Boolean name="Fixed_Point" value="1"/>\n'
        f'<Unsigned name="Decimal_Places" value="1"/>\n'
        f'<Real name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'</Object>\n'
    )

def EVcoscsml(row):

    #Name,Inst,monDEV,monOBJ,evc

    name = row['Name']
    obj = row['Inst']
    if row['monDEV'] == "":
        monDEV = int(4294967294)
    else:
        monDEV = int(row['monDEV'])
    monOBJ = row['monOBJ']
    evc = int(row['evc'])
        
    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value="to-offnormal;to-fault;to-normal"/>\n'
        f'<Unsigned name="Notification_Class" value="{evc}"/>\n'#
        f'<String name="Description" value=""/>\n'
        f'<BitString name="Event_Enable" value="to-offnormal;to-fault;to-normal"/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<Enumerated name="Event_Type" value="change-of-state"/>\n'
        f'<Enumerated name="Notify_Type" value="alarm"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="event-enrollment,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Sequence name="Object_Property_Reference">\n'
        f'<Unsigned name="deviceIdentifier" value="{monDEV}"/>\n'#
        f'<ObjectIdentifier name="objectIdentifier" value="{getLongType(monOBJ)},{getInst(monOBJ)}"/>\n'#
        f'<Enumerated name="propertyIdentifier" value="present-value"/>\n'
        f'<Unsigned name="propertyArrayIndex" value="4294967295"/>\n'
        f'</Sequence>\n'
        f'<Enumerated name="Object_Type" value="event-enrollment"/>\n'
        f'<Choice name="Event_Parameters">\n'
        f'<Sequence name="change-of-state">\n'
        f'<Unsigned name="time-delay" value="0"/>\n'
        f'<List name="list-of-values">\n'
        f'<Choice name="1">\n'
        f'<Enumerated name="binary-value" value="active"/>\n'
        f'</Choice>\n'
        f'</List>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Unsigned name="Object_Size" value="196"/>\n'
        f'<BitString name="Flags" value=""/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Enumerated name="Pending_Event_State" value="unknown"/>\n'
        f'<Sequence name="Enable_Ref">\n'
        f'<Unsigned name="deviceIdentifier" value="4194303"/>\n'
        f'<ObjectIdentifier name="objectIdentifier" value="*"/>\n'
        f'<Enumerated name="propertyIdentifier" value="4194303"/>\n'
        f'<Unsigned name="propertyArrayIndex" value="4294967295"/>\n'
        f'</Sequence>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Choice name="Context">\n'
        f'<Sequence name="change-of-state">\n'
        f'<Choice name="monitoredValue">\n'
        f'<Enumerated name="binary-value" value="active"/>\n'
        f'</Choice>\n'
        f'<Choice name="previousValue">\n'
        f'<Enumerated name="binary-value" value="255"/>\n'
        f'</Choice>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<ObjectIdentifier name="Event_Class_Ref" value="notification-class,{evc}"/>\n'#
        f'<Unsigned name="Time_Delay_Timer" value=""/>\n'
        f'<Array name="Event_Count">\n'
        f'<Unsigned name="1" value="0"/>\n'
        f'<Unsigned name="2" value="0"/>\n'
        f'<Unsigned name="3" value="0"/>\n'
        f'</Array>\n'
        f'<Array name="Event_Message_Texts_Config">\n'
        f'<String name="1" value=""/>\n'
        f'<String name="2" value=""/>\n'
        f'<String name="3" value=""/>\n'
        f'</Array>\n'
        f'<Enumerated name="Last_Off_Normal_State" value="offnormal"/>\n'
        f'<Boolean name="Enable_Auto_Text" value="1"/>\n'
        f'<Enumerated name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'</Object>\n'
    )

def TLcsml(row):

    #Name,Inst,monDEV,monOBJ,bufferSize,logInterval
    
    name = row['Name']
    obj = row['Inst']
    if row['monDEV'] == "":
        monDEV = int(4294967294)
    else:
        monDEV = int(row['monDEV'])
    monOBJ = row['monOBJ']
    bufferSize = int(row['bufferSize'])
    logInterval = int(row['logInterval'] * 100)
    
    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value="to-offnormal;to-fault;to-normal"/>\n'
        f'<Unsigned name="Notification_Class" value="9"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<BitString name="Event_Enable" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<Enumerated name="Notify_Type" value="event"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="trend-log,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="trend-log"/>\n'
        f'<Unsigned name="Buffer_Size" value="{bufferSize}"/>\n'#
        f'<Real name="Client_COV_Increment" value="0"/>\n'
        f'<Unsigned name="COV_Resubscription_Interval" value="1800"/>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Sequence name="Log_DeviceObjectProperty">\n'
        f'<Unsigned name="deviceIdentifier" value="{monDEV}"/>\n'#
        f'<ObjectIdentifier name="objectIdentifier" value="{getLongType(monOBJ)},{getInst(monOBJ)}"/>\n'#
        f'<Enumerated name="propertyIdentifier" value="present-value"/>\n'
        f'<Unsigned name="propertyArrayIndex" value="4294967295"/>\n'
        f'</Sequence>\n'
        f'<Boolean name="Enable" value="1"/>\n'
        f'<Unsigned name="Log_Interval" value="{logInterval}"/>\n'#
        f'<Unsigned name="Notification_Threshold" value="50"/>\n'
        f'<Unsigned name="Records_Since_Notification" value="1"/>\n'
        f'<Unsigned name="Record_Count" value="1"/>\n'
        f'<DateTime name="Start_Time" value="2020-04-10 00:00:00.00"/>\n'
        f'<DateTimePattern name="Stop_Time" value="*-*-* * *:*:*.*"/>\n'
        f'<Boolean name="Stop_When_Full" value="0"/>\n'
        f'<Unsigned name="Total_Record_Count" value="1"/>\n'
        f'<Unsigned name="Last_Notify_Record" value="0"/>\n'
        f'<Unsigned name="Object_Size" value="1202"/>\n'
        f'<BitString name="Flags" value=""/>\n'
        f'<Enumerated name="Present_Value" value="not-trending"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Sequence name="Input_Ref">\n'
        f'<Unsigned name="deviceIdentifier" value="{monDEV}"/>\n'#
        f'<ObjectIdentifier name="objectIdentifier" value="{getLongType(monOBJ)},{getInst(monOBJ)}"/>\n'#
        f'<Enumerated name="propertyIdentifier" value="present-value"/>\n'
        f'<Unsigned name="propertyArrayIndex" value="4294967295"/>\n'
        f'</Sequence>\n'
        f'<Unsigned name="Log_Timer" value="60570010"/>\n'
        f'<Boolean name="Stop_When_Error_Full" value="0"/>\n'
        f'<Boolean name="Restrict_Data_Range" value="0"/>\n'
        f'<Array name="Timestamp_Buffer">\n'
        f'</Array>\n'
        f'<Array name="Flags_Buffer">\n'
        f'</Array>\n'
        f'<Choice name="Data_Buffer">\n'
        f'<List name="real">\n'
        f'</List>\n'
        f'</Choice>\n'
        f'<Array name="Error_Buffer">\n'
        f'<Choice name="1">\n'
        f'<BitString name="eventData" value="log-disabled;buffer-purged"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<BitString name="eventData" value="log-disabled"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="4">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="5">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="6">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="7">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="8">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="9">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'<Choice name="10">\n'
        f'<Sequence name="errorData">\n'
        f'<Enumerated name="error-class" value="device"/>\n'
        f'<Enumerated name="error-code" value="other"/>\n'
        f'</Sequence>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Array name="Err_Buf_2_Data_Buf_Idx">\n'
        f'</Array>\n'
        f'<DateTime name="Time_Reference" value="2000-01-12 13:41:35.00"/>\n'
        f'<Unsigned name="Time_Reference_Count" value="0"/>\n'
        f'<Unsigned name="Next_Error_Index" value="2"/>\n'
        f'<Unsigned name="Error_Count" value="1"/>\n'
        f'<Unsigned name="Error_Buffer_Size" value="10"/>\n'
        f'<Unsigned name="Next_Index" value="2"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Unsigned name="Start_Timer" value="124381057"/>\n'
        f'<Unsigned name="Stop_Timer" value=""/>\n'
        f'<Boolean name="Is_Historical" value="0"/>\n'
        f'<Boolean name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'</Object>\n'
        )

def AIcsml(row):

    #Name,Inst,cfg,action

    name = row['Name']
    obj = row['Inst']
    cfg = row['cfg']

    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value=""/>\n'
        f'<Unsigned name="Notification_Class" value="0"/>\n'
        f'<Real name="COV_Increment" value="1"/>\n'
        f'<Real name="Deadband" value="0"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<String name="Device_Type" value=""/>\n'
        f'<BitString name="Event_Enable" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<Real name="High_Limit" value="0"/>\n'
        f'<BitString name="Limit_Enable" value=""/>\n'
        f'<Real name="Low_Limit" value="0"/>\n'
        f'<Real name="Max_Pres_Value" value="300"/>\n'
        f'<Real name="Min_Pres_Value" value="-58"/>\n'
        f'<Enumerated name="Notify_Type" value="alarm"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="analog-input,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="analog-input"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Real name="Present_Value" value="300"/>\n'
        f'<Enumerated name="Reliability" value="no-fault-detected"/>\n'
        f'<Real name="Resolution" value="0.0874237"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Unsigned name="Time_Delay" value="0"/>\n'
        f'<Enumerated name="Units" value="°F"/>\n'
        f'<Unsigned name="Update_Interval" value="204"/>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Unsigned name="Object_Size" value="73"/>\n'
        f'<BitString name="Flags" value="not-commissioned"/>\n'
        f'<Real name="Last_Value" value="300"/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Enumerated name="Commission_Flag" value="not-commissioned"/>\n'
        f'<ObjectIdentifier name="Type_Reference" value="analog-input-config,{cfg}"/>\n'#
        f'<Unsigned name="AD_Filter" value="80"/>\n'
        f'<Unsigned name="Filter_Delay_Timer" value="9473"/>\n'
        f'<Unsigned name="AD_Value" value="0"/>\n'
        f'<Real name="Calibration" value="0"/>\n'
        f'<Boolean name="Fixed_Point" value="1"/>\n'
        f'<Unsigned name="Decimal_Places" value="1"/>\n'
        f'<Boolean name="External_Control" value="0"/>\n'
        f'<Enumerated name="Previous_Reliability" value="no-fault-detected"/>\n'
        f'<Real name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'<Boolean name="Event_Detection_Enable" value="0"/>\n'
        f'<Array name="Intrinsic_Info">\n'
        f'</Array>\n'
        f'<Array name="Event_Message_Texts_Config">\n'
        f'<String name="1" value=""/>\n'
        f'<String name="2" value=""/>\n'
        f'<String name="3" value=""/>\n'
        f'</Array>\n'
        f'</Object>\n'
        )

def BIcsml(row):

    #Name,Inst,cfg,action

    name = row['Name']
    obj = row['Inst']
    cfg = row['cfg']
    action = row['action']

    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value=""/>\n'
        f'<String name="Active_Text" value="On"/>\n'
        f'<Enumerated name="Alarm_Value" value="inactive"/>\n'
        f'<Unsigned name="Change_Of_State_Count" value="1"/>\n'
        f'<DateTime name="Change_Of_State_Time" value="2020-10-24 03:19:33.13"/>\n'
        f'<Unsigned name="Notification_Class" value="0"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<String name="Device_Type" value=""/>\n'
        f'<BitString name="Event_Enable" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<String name="Inactive_Text" value="Off"/>\n'
        f'<Enumerated name="Notify_Type" value="alarm"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="binary-input,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="binary-input"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Enumerated name="Polarity" value="{action}"/>\n'#
        f'<Enumerated name="Present_Value" value="active"/>\n'
        f'<Enumerated name="Reliability" value="no-fault-detected"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Unsigned name="Time_Delay" value="0"/>\n'
        f'<DateTime name="Time_Of_State_Count_Reset" value="2020-10-24 03:19:33.08"/>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Unsigned name="Object_Size" value="79"/>\n'
        f'<BitString name="Flags" value="not-commissioned"/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Enumerated name="Commission_Flag" value="not-commissioned"/>\n'
        f'<ObjectIdentifier name="Type_Reference" value="binary-device-configuration,{cfg}"/>\n'#
        f'<Array name="Prev_Change_Of_State_Times">\n'
        f'<DateTimePattern name="1" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTime name="2" value="2020-10-24 03:19:33.13"/>\n'
        f'</Array>\n'
        f'<Unsigned name="Update_Interval" value="204"/>\n'
        f'<String name="Text_Value" value="On"/>\n'
        f'<Enumerated name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'<Enumerated name="Value_Source" value="configuration-(bdc)"/>\n'
        f'<Boolean name="Event_Detection_Enable" value="0"/>\n'
        f'<Array name="Intrinsic_Info">\n'
        f'</Array>\n'
        f'<Array name="Event_Message_Texts_Config">\n'
        f'<String name="1" value=""/>\n'
        f'<String name="2" value=""/>\n'
        f'<String name="3" value=""/>\n'
        f'</Array>\n'
        f'</Object>\n'
        )

def AOcsml(row):

    #Name,Inst,cfg,action

    name = row['Name']
    obj = row['Inst']
    action = row['action']

    if row['cfg'] == "":
        cfg = ""
    else:
        cfg = "analog-output-config," + str(int(row['cfg']))

    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value=""/>\n'
        f'<Unsigned name="Notification_Class" value="0"/>\n'
        f'<Real name="COV_Increment" value="1"/>\n'
        f'<Real name="Deadband" value="0"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<String name="Device_Type" value=""/>\n'
        f'<BitString name="Event_Enable" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<Real name="High_Limit" value="0"/>\n'
        f'<BitString name="Limit_Enable" value=""/>\n'
        f'<Real name="Low_Limit" value="0"/>\n'
        f'<Real name="Max_Pres_Value" value="100"/>\n'
        f'<Real name="Min_Pres_Value" value="0"/>\n'
        f'<Enumerated name="Notify_Type" value="alarm"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="analog-output,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="analog-output"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Real name="Present_Value" value="0"/>\n'
        f'<Array name="Priority_Array">\n'
        f'<Real name="1" value=""/>\n'
        f'<Real name="2" value=""/>\n'
        f'<Real name="3" value=""/>\n'
        f'<Real name="4" value=""/>\n'
        f'<Real name="5" value=""/>\n'
        f'<Real name="6" value=""/>\n'
        f'<Real name="7" value=""/>\n'
        f'<Real name="8" value=""/>\n'
        f'<Real name="9" value=""/>\n'
        f'<Real name="10" value=""/>\n'
        f'<Real name="11" value=""/>\n'
        f'<Real name="12" value=""/>\n'
        f'<Real name="13" value=""/>\n'
        f'<Real name="14" value=""/>\n'
        f'<Real name="15" value=""/>\n'
        f'<Real name="16" value=""/>\n'
        f'</Array>\n'
        f'<Enumerated name="Reliability" value="no-fault-detected"/>\n'
        f'<Real name="Relinquish_Default" value="0"/>\n'
        f'<Real name="Resolution" value="0.392157"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Unsigned name="Time_Delay" value="0"/>\n'
        f'<Enumerated name="Units" value="%"/>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Unsigned name="Object_Size" value="363"/>\n'
        f'<BitString name="Flags" value="not-commissioned"/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Enumerated name="Commission_Flag" value="not-commissioned"/>\n'
        f'<ObjectIdentifier name="Type_Reference" value="{cfg}"/>\n'#
        f'<Boolean name="Critical_Control" value="1"/>\n'
        f'<Unsigned name="Current_Priority" value="17"/>\n'
        f'<Array name="Last_Writer">\n'
        f'<ObjectIdentifierPattern name="1" value="*"/>\n'
        f'<ObjectIdentifierPattern name="2" value="*"/>\n'
        f'<ObjectIdentifierPattern name="3" value="*"/>\n'
        f'<ObjectIdentifierPattern name="4" value="*"/>\n'
        f'<ObjectIdentifierPattern name="5" value="*"/>\n'
        f'<ObjectIdentifierPattern name="6" value="*"/>\n'
        f'<ObjectIdentifierPattern name="7" value="*"/>\n'
        f'<ObjectIdentifierPattern name="8" value="*"/>\n'
        f'<ObjectIdentifierPattern name="9" value="*"/>\n'
        f'<ObjectIdentifierPattern name="10" value="*"/>\n'
        f'<ObjectIdentifierPattern name="11" value="*"/>\n'
        f'<ObjectIdentifierPattern name="12" value="*"/>\n'
        f'<ObjectIdentifierPattern name="13" value="*"/>\n'
        f'<ObjectIdentifierPattern name="14" value="*"/>\n'
        f'<ObjectIdentifierPattern name="15" value="*"/>\n'
        f'<ObjectIdentifierPattern name="16" value="*"/>\n'
        f'</Array>\n'
        f'<Array name="Time_Of_Last_Write">\n'
        f'<DateTimePattern name="1" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="2" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="3" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="4" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="5" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="6" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="7" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="8" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="9" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="10" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="11" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="12" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="13" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="14" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="15" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="16" value="*-*-* * *:*:*.*"/>\n'
        f'</Array>\n'
        f'<Enumerated name="Polarity" value="{action}"/>\n'#
        f'<Unsigned name="DA_Value" value="0"/>\n'
        f'<Real name="Output_Volt" value="0"/>\n'
        f'<Enumerated name="Port_1_Status" value="not-available"/>\n'
        f'<Enumerated name="Port_2_Status" value="not-available"/>\n'
        f'<Enumerated name="Module_Type" value="none"/>\n'
        f'<Enumerated name="HOA_Status" value="auto"/>\n'
        f'<Real name="FBack_Value" value="0"/>\n'
        f'<Enumerated name="FBack_Enable" value="disable"/>\n'
        f'<Unsigned name="FBack_Input" value="0"/>\n'
        f'<Enumerated name="FBack_Status" value="not-available"/>\n'
        f'<Real name="FBack_High" value="0"/>\n'
        f'<Real name="FBack_Low" value="0"/>\n'
        f'<Unsigned name="Analog_3_PT_Timer" value="0"/>\n'
        f'<Enumerated name="Analog_3_PT_Output_1" value="inactive"/>\n'
        f'<Enumerated name="Analog_3_PT_Output_2" value="inactive"/>\n'
        f'<Enumerated name="Analog_3_PT_Output_Action" value="close"/>\n'
        f'<Real name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'<Boolean name="Event_Detection_Enable" value="0"/>\n'
        f'<Array name="Intrinsic_Info">\n'
        f'</Array>\n'
        f'<Array name="Event_Message_Texts_Config">\n'
        f'<String name="1" value=""/>\n'
        f'<String name="2" value=""/>\n'
        f'<String name="3" value=""/>\n'
        f'</Array>\n'
        f'</Object>\n'
        )

def BOcsml(row):

    #Name,Inst,cfg,action

    name = row['Name']
    obj = row['Inst']
    cfg = row['cfg']
    action = row['action']

    return (
        f'<Object name="{obj}">\n'#
        f'<BitString name="Acked_Transitions" value=""/>\n'
        f'<String name="Active_Text" value="On"/>\n'
        f'<Unsigned name="Change_Of_State_Count" value="0"/>\n'
        f'<DateTimePattern name="Change_Of_State_Time" value="*-*-* * *:*:*.*"/>\n'
        f'<Unsigned name="Notification_Class" value="0"/>\n'
        f'<String name="Description" value=""/>\n'
        f'<String name="Device_Type" value=""/>\n'
        f'<BitString name="Event_Enable" value=""/>\n'
        f'<Enumerated name="Event_State" value="normal"/>\n'
        f'<Enumerated name="Feedback_Value" value="inactive"/>\n'
        f'<String name="Inactive_Text" value="Off"/>\n'
        f'<Unsigned name="Minimum_Off_Time" value="60"/>\n'
        f'<Unsigned name="Minimum_On_Time" value="0"/>\n'
        f'<Enumerated name="Notify_Type" value="alarm"/>\n'
        f'<ObjectIdentifier name="Object_Identifier" value="binary-output,{getInst(obj)}"/>\n'#
        f'<String name="Object_Name" value="{name}"/>\n'#
        f'<Enumerated name="Object_Type" value="binary-output"/>\n'
        f'<Boolean name="Out_Of_Service" value="0"/>\n'
        f'<Enumerated name="Polarity" value="{action}"/>\n'#
        f'<Enumerated name="Present_Value" value="inactive"/>\n'
        f'<Array name="Priority_Array">\n'
        f'<Enumerated name="1" value=""/>\n'
        f'<Enumerated name="2" value=""/>\n'
        f'<Enumerated name="3" value=""/>\n'
        f'<Enumerated name="4" value=""/>\n'
        f'<Enumerated name="5" value=""/>\n'
        f'<Enumerated name="6" value=""/>\n'
        f'<Enumerated name="7" value=""/>\n'
        f'<Enumerated name="8" value=""/>\n'
        f'<Enumerated name="9" value=""/>\n'
        f'<Enumerated name="10" value=""/>\n'
        f'<Enumerated name="11" value=""/>\n'
        f'<Enumerated name="12" value=""/>\n'
        f'<Enumerated name="13" value=""/>\n'
        f'<Enumerated name="14" value=""/>\n'
        f'<Enumerated name="15" value=""/>\n'
        f'<Enumerated name="16" value=""/>\n'
        f'</Array>\n'
        f'<Enumerated name="Reliability" value="no-fault-detected"/>\n'
        f'<Enumerated name="Relinquish_Default" value="inactive"/>\n'
        f'<BitString name="Status_Flags" value=""/>\n'
        f'<Unsigned name="Time_Delay" value="0"/>\n'
        f'<DateTimePattern name="Time_Of_State_Count_Reset" value="*-*-* * *:*:*.*"/>\n'
        f'<Array name="Event_Time_Stamps">\n'
        f'<Choice name="1">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="2">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'<Choice name="3">\n'
        f'<DateTimePattern name="dateTime" value="*-*-* * *:*:*.*"/>\n'
        f'</Choice>\n'
        f'</Array>\n'
        f'<Unsigned name="Object_Size" value="384"/>\n'
        f'<BitString name="Flags" value="private2;not-commissioned"/>\n'
        f'<Boolean name="Reset" value="0"/>\n'
        f'<Enumerated name="Commission_Flag" value="not-commissioned"/>\n'
        f'<ObjectIdentifier name="Type_Reference" value="binary-device-configuration,{cfg}"/>\n'#
        f'<Array name="Prev_Change_Of_State_Times">\n'
        f'<DateTimePattern name="1" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="2" value="*-*-* * *:*:*.*"/>\n'
        f'</Array>\n'
        f'<Unsigned name="Minimum_Delay_Timer" value="0"/>\n'
        f'<Unsigned name="Current_Priority" value="17"/>\n'
        f'<Boolean name="Critical_Control" value="1"/>\n'
        f'<Array name="Last_Writer">\n'
        f'<ObjectIdentifierPattern name="1" value="*"/>\n'
        f'<ObjectIdentifierPattern name="2" value="*"/>\n'
        f'<ObjectIdentifierPattern name="3" value="*"/>\n'
        f'<ObjectIdentifierPattern name="4" value="*"/>\n'
        f'<ObjectIdentifierPattern name="5" value="*"/>\n'
        f'<ObjectIdentifierPattern name="6" value="*"/>\n'
        f'<ObjectIdentifierPattern name="7" value="*"/>\n'
        f'<ObjectIdentifierPattern name="8" value="*"/>\n'
        f'<ObjectIdentifierPattern name="9" value="*"/>\n'
        f'<ObjectIdentifierPattern name="10" value="*"/>\n'
        f'<ObjectIdentifierPattern name="11" value="*"/>\n'
        f'<ObjectIdentifierPattern name="12" value="*"/>\n'
        f'<ObjectIdentifierPattern name="13" value="*"/>\n'
        f'<ObjectIdentifierPattern name="14" value="*"/>\n'
        f'<ObjectIdentifierPattern name="15" value="*"/>\n'
        f'<ObjectIdentifierPattern name="16" value="*"/>\n'
        f'</Array>\n'
        f'<Array name="Time_Of_Last_Write">\n'
        f'<DateTimePattern name="1" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="2" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="3" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="4" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="5" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="6" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="7" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="8" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="9" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="10" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="11" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="12" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="13" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="14" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="15" value="*-*-* * *:*:*.*"/>\n'
        f'<DateTimePattern name="16" value="*-*-* * *:*:*.*"/>\n'
        f'</Array>\n'
        f'<Enumerated name="Port_Status" value="active"/>\n'
        f'<Unsigned name="DA_Value" value="0"/>\n'
        f'<Real name="Output_Volt" value="0"/>\n'
        f'<Enumerated name="Module_Type" value="none"/>\n'
        f'<Enumerated name="HOA_Status" value="auto"/>\n'
        f'<Enumerated name="Delay_Status" value="timer-inactive"/>\n'
        f'<Unsigned name="Start_Delay_Time" value="5"/>\n'
        f'<BitString name="Start_Delay_Flags" value=""/>\n'
        f'<Enumerated name="FBack_Value" value="inactive"/>\n'
        f'<Boolean name="FBack_Reversed" value="0"/>\n'
        f'<Enumerated name="FBack_Enable" value="disable"/>\n'
        f'<Unsigned name="FBack_Input" value="0"/>\n'
        f'<Enumerated name="FBack_Status" value="not-available"/>\n'
        f'<Time name="Delay_Count_Down" value="00:00:00.00"/>\n'
        f'<String name="Text_Value" value="Off"/>\n'
        f'<Enumerated name="Manual_Override" value=""/>\n'
        f'<BitString name="HAL_Flags" value="hvac"/>\n'
        f'<Boolean name="Flick_Warn_Enable" value="0"/>\n'
        f'<Unsigned name="Flick_Warn_Time" value="0"/>\n'
        f'<Unsigned name="Flick_Warn_Timer" value=""/>\n'
        f'<Unsigned name="Flick_Warn_Active" value="0"/>\n'
        f'<Unsigned name="Flick_Warn_Paenable" value="0"/>\n'
        f'<Sequence name="Override_Ref">\n'
        f'<Unsigned name="deviceIdentifier" value="4194303"/>\n'
        f'<ObjectIdentifier name="objectIdentifier" value="*"/>\n'
        f'<Enumerated name="propertyIdentifier" value="4194303"/>\n'
        f'<Unsigned name="propertyArrayIndex" value="4294967295"/>\n'
        f'</Sequence>\n'
        f'<Boolean name="Override_Prev_Val" value="0"/>\n'
        f'<Unsigned name="Override_Time" value="0"/>\n'
        f'<Unsigned name="Override_Timer" value=""/>\n'
        f'<Unsigned name="Reliability_Timer" value="0"/>\n'
        f'<BitString name="Event_List" value=""/>\n'
        f'<Enumerated name="Prev_Reliability" value="no-fault-detected"/>\n'
        f'<Boolean name="Event_Detection_Enable" value="0"/>\n'
        f'<Array name="Intrinsic_Info">\n'
        f'</Array>\n'
        f'<Array name="Event_Message_Texts_Config">\n'
        f'<String name="1" value=""/>\n'
        f'<String name="2" value=""/>\n'
        f'<String name="3" value=""/>\n'
        f'</Array>\n'
        f'<Sequence name="LC_Command">\n'
        f'<Enumerated name="value" value="no-action"/>\n'
        f'<Unsigned name="priority" value="0"/>\n'
        f'<Enumerated name="flickWarnEnable" value="off"/>\n'
        f'<Unsigned name="flickWarnOnTime" value="0"/>\n'
        f'<Unsigned name="flickWarnOffTime" value="0"/>\n'
        f'</Sequence>\n'
        f'<Array name="LC_User_Properties">\n'
        f'</Array>\n'
        f'<Array name="LC_Internal_Properties">\n'
        f'</Array>\n'
        f'<Array name="LC_Priority_Array">\n'
        f'</Array>\n'
        f'</Object>\n'
        )
