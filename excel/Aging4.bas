Attribute VB_Name = "Aging4"

Sub CopySheet(ByVal conn, ByVal sql, ByVal headRange, ByVal destSheetName)

    Application.ScreenUpdating = False
     
    Worksheets.Add after:=Sheets(Sheets.Count)
    With ActiveSheet

        .Name = destSheetName
        '������ͷ

        For num = 1 To UBound(headRange, 2)

            .Cells(1, num) = headRange(1, num)

        Next num
        
        .Range("A2").CopyFromRecordset conn.Execute(sql)

    End With
    
    
    Worksheets(1).Activate

    '��������еĸ�ʽ���ƣ���Ŀ�����������н��и��Ƶ�

    'Sheets(1).Range(Cells(1, 1), Cells(2, Sheets(1).UsedRange.Columns.Count)).Select

    'Sheets(1).Cells.Select
    
    '��ͷ��ʽ����
    ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select
    
    Selection.Copy

    Worksheets(Sheets.Count).Activate

    'ActiveSheet.Cells.Select
    
    ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select

    ':= ָ���ض��Ĳ���ֵ.����Python�еĹؼ��ֲ�����

    Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    
    
    
    '���ݸ�ʽ����
    Worksheets(1).Activate

    ActiveSheet.Range(Cells(2, 1), Cells(2, ActiveSheet.UsedRange.Columns.Count)).Select
    
    Selection.Copy

    Worksheets(Sheets.Count).Activate
    
    ActiveSheet.Range(Cells(2, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).Select

    Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    
    
    
    Application.ScreenUpdating = True
    

End Sub



Sub FormatSheet(sheetName)

    Sheets(sheetName).Activate
    'ȡ���Զ�����
    ActiveSheet.Range(Cells(1, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).WrapText = False
    '���ᴰ�� �̶�����
    'ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select
    'ActiveWindow.FreezePanes = True
    ActiveWindow.SplitRow = 1
    ActiveWindow.FreezePanes = True
    

    
    'ȡ�����
    ActiveSheet.Range(Cells(2, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).Interior.ColorIndex = xlColorIndexNone
    
    'https://baijiahao.baidu.com/s?id=1621006684338092173&wfr=spider&for=pc
    
    ActiveSheet.Range(Cells(2, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).Font.Size = 10
    
    
End Sub

Sub SortSheet(sheetName, ParamArray cols())

    Application.ScreenUpdating = False
 
    Sheets(sheetName).Activate
    
    Dim day_late_col
    
    For col = 1 To Sheets(sheetName).UsedRange.Columns.Count
        If Cells(1, col) = "Days Late" Then
          day_late_col = col
        End If
    Next col

    
    'currency/customer name/ days late(����
    
    'Set k1 = Range("B3") '�ؼ���
    'Set k2 = Range("E3") '�ؼ���
    'ʹ�ÿɱ��������
    For i = 0 To UBound(cols, 1)
        If cols(i) = day_late_col Then
            '��daylate����
            Sheets(sheetName).Sort.SortFields.Add Key:=Sheets(sheetName).Range(Cells(1, cols(i)), Cells(1, cols(i))), Order:=2
        Else
            Sheets(sheetName).Sort.SortFields.Add Key:=Sheets(sheetName).Range(Cells(1, cols(i)), Cells(1, cols(i)))
        End If
    Next i
    
    
    With Sheets(sheetName).Sort
        .SetRange Range(Cells(2, 1), Cells(Sheets(sheetName).UsedRange.Rows.Count, Sheets(sheetName).UsedRange.Columns.Count))
        .Apply
    End With
    
    'Set k1 = Sheets(sheetName).Range(Cells(1, CustCol), Cells(1, CustCol))
    
    'Set k2 = Sheets(sheetName).Range(Cells(1, TrCol), Cells(1, TrCol))
    
    'Set k3 = Sheets(sheetName).Range(Cells(1, DayCol), Cells(1, DayCol))
    
    
    '������ָ������������Ӧ������ ע��ָ��������Ҫ����������С�
    'Sheets(sheetName).Range(Cells(2, CustCol), Cells(Sheets(sheetName).UsedRange.Rows.Count, CustCol)).Sort key1:=k1, Order1:=1, key2:=k2, Order2:=1
    
    'Sheets(sheetName).Range(Cells(2, 1), Cells(Sheets(sheetName).UsedRange.Rows.Count, Sheets(sheetName).UsedRange.Columns.Count)).Sort key1:=k1, Order1:=1, key2:=k2, Order2:=1, key3:=k3, Order3:=2
    
    Application.ScreenUpdating = True
    
End Sub



'������ܣ�����ĳ�����࣬�ٸ��ݻ�������ܣ�
Sub MySubtotal(sheetName, groupByCol, col1, col2, col3, col4, col5, col6, col7, col8)
    Worksheets(sheetName).Activate
    Sheets(sheetName).Range("A1").CurrentRegion.Subtotal GroupBy:=groupByCol, Function:=xlSum, TotalList:=Array(col1, col2, col3, col4, col5, col6, col7, col8)
End Sub


'������ʽ
Sub FormatConditions(sheetName, col)
    
    Worksheets(sheetName).Activate
    
    Sheets(sheetName).Range(Cells(2, col), Cells(Sheets(sheetName).UsedRange.Rows.Count, col)).Select
     
    Selection.FormatConditions.Add Type:=xlCellValue, Operator:=xlGreaterEqual, Formula1:="-10"
    
    Selection.FormatConditions(1).Interior.Color = RGB(255, 197, 197) '����ɫ
    Selection.FormatConditions(1).Font.Color = RGB(204, 51, 0)
    
    'Selection.FormatConditions(1).Font.ColorIndex = 3

End Sub


Function CountTrxCurrency(sheetName, trxCol)

    Sheets(sheetName).Activate
    
    Set conn = CreateObject("adodb.connection")
    
    Dim rsSQL
    
    conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
    
    '�ֶ��к��ո�� ��[]
    sql = "select [" & Cells(1, trxCol) & "] from [" & sheetName & "$] group by [" & Cells(1, trxCol) & "]"
    
    Set rsSQL = conn.Execute(sql) ' ����RecordSet
    
    'MsgBox (rsSQL.BOF)
    'MsgBox (rsSQL.EOF)
    'MsgBox (rsSQL.Fields.Count) '������ �ֶεĸ���
    'MsgBox (TypeName(rsSQL)) 'RecordSet
    'MsgBox (rsSQL.RecordCount)
    
    
    'Dim arr(0 To 100) '������ [0,100]
    Dim arr()
    ReDim arr(0 To 100)
    Dim i
    i = 0
     
    Do While Not rsSQL.EOF
        If Not IsNull(rsSQL.Fields(0)) Then
            'MsgBox (rsSQL.Fields(0)) ' Fields ���ֶ��е�ֵ
            'MsgBox (rsSQL.Fields(0).Value) '��ͬ����
            'MsgBox (rsSQL.Fields(0).Name) '�ֶ���
             arr(i) = rsSQL.Fields(0)
             'MsgBox (arr(i))
             i = i + 1
        End If
        rsSQL.MoveNext
    Loop
    
    '���¶����Сʱ ����ԭ��������
    ReDim Preserve arr(i - 1) ' [0,i-1]
    'ReDim arr(0 To i - 1)
    
  
   ' useless
   ' For i = 1 To rsSQL.Fields.Count
    
   '     MsgBox (rsSQL.Fields(i))
        
  '  Next i
    
    conn.Close

    Set conn = Nothing

    CountTrxCurrency = arr '��������
End Function


'��ȡsheetname�ж�Ӧ�Ļ���dict��
Function GetRateDict(destSheetName, trxColumn, sheetDict)
    arr = CountTrxCurrency(destSheetName, trxColumn)
    
    
    rowTemp = Sheets(destSheetName).UsedRange.Rows.Count + 1
     
    '����Dict
    Dim rateDict
    Set rateDict = CreateObject("Scripting.Dictionary")
    
    '����cell��ʱ�ģ�ֻ�����ڴ�Ź�ʽ�����㡣��ȡ����function currency�Ļ��ʡ�
    Cells(rowTemp, 1).Formula = "=VLOOKUP(""" & sheetDict.Item(destSheetName) & """,Sheet2!$B$7:$C$41,2,0)"
    rateDict(sheetDict.Item(destSheetName)) = Cells(rowTemp, 1).Value
        
    rateDict("USD") = 1
    
    For arr_idx = 0 To UBound(arr)
        If arr(arr_idx) <> "USD" Then
            formulaStr = "=VLOOKUP(""" & arr(arr_idx) & """,Sheet2!$B$7:$C$41,2,0)"
            Cells(rowTemp, 1).Formula = formulaStr
            rateDict(arr(arr_idx)) = Cells(rowTemp, 1).Value
        End If
    Next arr_idx
    
    Cells(rowTemp, 1).Clear
    
    Set GetRateDict = rateDict
End Function


Sub CalculateCurrency(destSheetName, trxColumn, accountColumn, totalColumn, day361Column, trxClassColumn, sheetDict)

        arr = CountTrxCurrency(destSheetName, trxColumn)
        
        startIndex = Sheets(destSheetName).UsedRange.Rows.Count + 3
        
        For arr_idx = 0 To UBound(arr)
            rowIdx = startIndex + arr_idx
            'If arr_idx = 0 Then
            '    rowIdx = Sheets(destSheetNames(i)).UsedRange.Rows.Count + 3
            ' Else
            '    rowIdx = Sheets(destSheetNames(i)).UsedRange.Rows.Count + 1
            'End If
            
            Cells(rowIdx, accountColumn) = arr(arr_idx) & " SUM"
            
            trxChr = Split(Cells(rowIdx, trxColumn).Address, "$")(1)
            For idx2 = totalColumn To day361Column
                idx2Chr = Split(Cells(rowIdx, idx2).Address, "$")(1)
                'ע���ַ�����������˫����
                condStr = "=SUMIF($" & trxChr & ":$" & trxChr & ",""" & arr(arr_idx) & """," & idx2Chr & ":" & idx2Chr & ")"
                Cells(rowIdx, idx2).Formula = condStr
            Next idx2
           
        Next arr_idx
        
      
      
        '����Dict
        Set rateDict = GetRateDict(destSheetName, trxColumn, sheetDict)
        
        totalUSDIdx = Sheets(destSheetName).UsedRange.Rows.Count + 3
        
        
        
        For arr_idx = 0 To UBound(arr)
        
            rowIdx = totalUSDIdx + arr_idx
            
            Cells(rowIdx, accountColumn) = arr(arr_idx) & "2USD"
            
            If arr(arr_idx) = "USD" Then
                Cells(rowIdx, accountColumn + 1) = 1
            Else
                'Cells(rowIdx, accountColumn + 1).Formula = "=VLOOKUP(" & Split(Cells(rowIdx, accountColumn).Address, "$")(1) & Split(Cells(rowIdx, accountColumn).Address, "$")(2) & ",Sheet2!$B$7:$C$41,2,0)"
                formulaStr = "=VLOOKUP(""" & arr(arr_idx) & """,Sheet2!$B$7:$C$41,2,0)"
                Cells(rowIdx, accountColumn + 1).Formula = formulaStr
            End If
            
            
            rateChr = Split(Cells(rowIdx, accountColumn + 1).Address, "$")(1)
            For idx2 = totalColumn To day361Column
                idx2Chr = Split(Cells(rowIdx, idx2).Address, "$")(1)
                condStr = "=" & idx2Chr & (startIndex + arr_idx) & "*$" & rateChr & "$" & rowIdx
                Cells(rowIdx, idx2).Formula = condStr
            Next idx2
        Next arr_idx
        
        
        '����payment
        totalCount = Sheets(destSheetName).UsedRange.Rows.Count
        UnappliedRow = totalCount + 1
        
        Cells(UnappliedRow, accountColumn) = "Unapplied"
        
        For rowIdx = 1 To totalCount
            If Cells(rowIdx, trxClassColumn) = "Payment" Then
                cRate = rateDict.Item(Cells(rowIdx, trxColumn).Value)
                For idx2 = totalColumn To day361Column
                    Cells(UnappliedRow, idx2) = Cells(UnappliedRow, idx2) + Cells(rowIdx, idx2) * cRate * (-1)
                Next idx2
            End If
        Next rowIdx
        
        
        '����total
        Cells(UnappliedRow + 1, accountColumn) = "total"
        For idx2 = totalColumn To day361Column
            formulaStr = "=SUM(" & Split(Cells(totalUSDIdx, idx2).Address, "$")(1) & Split(Cells(totalUSDIdx, idx2).Address, "$")(2) & ":" & Split(Cells(UnappliedRow, idx2).Address, "$")(1) & Split(Cells(UnappliedRow, idx2).Address, "$")(2) & ")"
            Cells(UnappliedRow + 1, idx2).Formula = formulaStr
        Next idx2
        
       ' For rowIdx = totalUSDIdx To UnappliedRow
           ' For idx2 = totalColumn To day361Column
           '     Cells(UnappliedRow + 1, idx2) = Cells(UnappliedRow + 1, idx2) + Cells(rowIdx, idx2)
           ' Next idx2
        'Next rowIdx
        
        '����function currency
        If destSheetName <> "Country IN" Then
            fcRow = Sheets(destSheetName).UsedRange.Rows.Count + 1
            Cells(fcRow, accountColumn) = sheetDict.Item(destSheetName)
            Cells(fcRow, accountColumn + 1) = rateDict(sheetDict.Item(destSheetName))
            For idx2 = totalColumn To day361Column
                'i1 = Cells(UnappliedRow + 1, idx2).Value
                'i2 = rateDict.Item(Cells(fcRow, accountColumn).Value)
                'Cells(fcRow, idx2) = i1 / i2
                formulaStr = "=" & Split(Cells(UnappliedRow + 1, idx2).Address, "$")(1) & Split(Cells(UnappliedRow + 1, idx2).Address, "$")(2) & "/" & Split(Cells(fcRow, accountColumn + 1).Address, "$")(1) & Split(Cells(fcRow, accountColumn + 1).Address, "$")(2)
                Cells(fcRow, idx2) = formulaStr
            Next idx2
        End If
        
        
        '�����ʽ
        'http://www.360doc.com/content/16/0802/12/6076639_580221192.shtml
        'https://zhidao.baidu.com/question/1495713913788426939.html?sort=11&rn=5&pn=0#wgt-answers
        'https://zhidao.baidu.com/question/344215136.html
        'Range(Cells(2, totalColumn), Cells(fcRow, day361Column)).NumberFormat = "Accounting"
        Range(Cells(2, totalColumn), Cells(Sheets(destSheetName).UsedRange.Rows.Count, day361Column)).NumberFormat = "#,###0.00"
        
        

End Sub

Sub HandleINRUSD(destSheetName, trxColumn, totalColumn, day361Column, sheetDict)

     '����Dict. ����(���ֵ����)��ֵ��ҪSet ��ֱ��=�ǲ��е�
    Set rateDict = GetRateDict(destSheetName, trxColumn, sheetDict)
        
    For rowIdx = 2 To Sheets(destSheetName).UsedRange.Rows.Count
        'http://www.360doc.com/content/17/0422/23/30583536_647746454.shtml
        If Cells(rowIdx, trxColumn) <> "" Then
            rowRate = rateDict.Item(Cells(rowIdx, trxColumn).Value)
            For col = totalColumn To day361Column
                Cells(rowIdx, col) = Cells(rowIdx, col) * rowRate
            Next col
        End If
    Next rowIdx
    
End Sub


Sub preProcess()

    '�������Ԫ���Ǻϲ�ʱ��ֻ�ڵ�һ����Ԫ��λ����ʾֵ������Ϊ�ա�
    'MsgBox (Cells(1, 1))
    'MsgBox (Cells(1, 2))
    'MsgBox (Cells(2, 1))
    'MsgBox (Cells(2, 2))
    Sheets(1).Activate
    Sheets(1).Range(Cells(1, 1), Cells(Sheets(1).UsedRange.Rows.Count, 1)).Delete
    
    Sheets(1).Range(Cells(1, 1), Cells(2, Sheets(1).UsedRange.Columns.Count)).Delete
    
    Dim totalCol

    For col = 1 To Sheets(1).UsedRange.Columns.Count
        If Cells(1, col) = "Total" Then
            totalCol = col
        End If
    Next col
     
     
    Sheets(1).Range(Cells(1, 1), Cells(1, totalCol - 1)).Delete
    
    Sheets(1).Range(Cells(2, totalCol), Cells(2, Sheets(1).UsedRange.Columns.Count)).Delete
    
    ' �Ե� Credit �� Operation
    
    
   ' ������

   ' ActiveSheet.Range("A:A").Select
    
   ' Selection.Copy
    
   ' ActiveSheet.Range("AO:AO").Select
    
   ' Selection.PasteSpecial Paste:=xlPasteFormats, SkipBlanks:=False, Transpose:=False
    
    
    
    
    'ActiveSheet.Range("A:A").Copy
    'ActiveSheet.Range("AO1").PasteSpecial
    'ֱ�Ӹ�ֵ����
    ActiveSheet.Range("AO:AO") = ActiveSheet.Range("A:A").Value
    ActiveSheet.Range("A:A") = ActiveSheet.Range("B:B").Value
    ActiveSheet.Range("B:B") = ActiveSheet.Range("AO:AO").Value
    
    ActiveSheet.Range("AO:AO").Delete
    
End Sub


Sub processAging()

    Sheets(1).Activate
    If Cells(1, 1) <> "Operating Unit Desc" Then
         Call preProcess
    End If
    
        
    Application.DisplayAlerts = False

    'ע��ǰ���ű���ԭʼ�̶��ı�
    For i = Sheets.Count To 3 Step -1
        Sheets(i).Delete
    Next i
    Application.DisplayAlerts = True
    

    mydate = Application.InputBox(prompt:="���������ڣ�")
    
    If mydate = "" Then
        mydate = Format(Now(), "yyyy/MM/dd")
    End If
        

    'MsgBox (Sheets(1).UsedRange.Rows.Count)
    
    
    Dim sourceSheetColumnCount
    
    Dim sourceSheetName
    
    Dim headRange

    sourceSheetColumnCount = Sheets(1).UsedRange.Columns.Count
    
    sourceSheetName = Sheets(1).Name
    
    headRange = Range(Cells(1, 1), Cells(1, sourceSheetColumnCount))
    
    
    
    Dim OperatingColumn
    
    Dim customerNameColumn
    
    Dim trxColumn
    
    Dim dueDateColumn
    
    Dim dayslateColumn
    
    Dim totalColumn
    
    Dim currentColumn
    
    Dim day30Column
    
    Dim day60Column
    
    Dim day90Column
    
    Dim day180Column
    
    Dim day360Column
     
    Dim day361Column
    
    Dim accountColumn
    
    Dim trxClassColumn
    
    
    
    
    For col = 1 To sourceSheetColumnCount
        If headRange(1, col) = "Operating Unit Desc" Then
            OperatingColumn = col
        ElseIf headRange(1, col) = "Customer Name" Then
            customerNameColumn = col
        ElseIf Cells(1, col) = "Trx Currency" Then
            trxColumn = col
        ElseIf headRange(1, col) = "Due Date" Then
            dueDateColumn = col
        ElseIf headRange(1, col) = "Days Late" Then
            dayslateColumn = col
        ElseIf headRange(1, col) = "Total" Then
            totalColumn = col
        ElseIf headRange(1, col) = "Current" Then
            currentColumn = col
        ElseIf headRange(1, col) = "1-30 Days" Then
            day30Column = col
        ElseIf headRange(1, col) = "31-60 Days" Then
            day60Column = col
        ElseIf headRange(1, col) = "61-90 Days" Then
            day90Column = col
        ElseIf headRange(1, col) = "91-180 Days" Then
            day180Column = col
        ElseIf headRange(1, col) = "181-360 Days" Then
            day360Column = col
        ElseIf headRange(1, col) = "361+ Days" Then
            day361Column = col
        ElseIf headRange(1, col) = "Account" Then
            accountColumn = col
        ElseIf headRange(1, col) = "Trx Class" Then
            trxClassColumn = col
        End If
    Next col
    
    
    'MsgBox (dueDateColumn & "" & dayslateColumn & totalColumn & currentColumn & day30Column & day60Column & day90Column & day180Column & day360Column & day361Column)
    
    
     '��Ҫ��ȡ�ı� �ֵ���ʽ�� key������ȡ�ı� value����function currency��������. ���������ӱ��ڴ˴����
    Dim sheetDict
    Set sheetDict = CreateObject("Scripting.Dictionary")
    sheetDict.Add "821", "HKD"
    sheetDict.Add "845", "AUD"
    sheetDict.Add "847", "KRW"
    sheetDict.Add "848", "JPY"
    sheetDict.Add "849", "INR"
    sheetDict.Add "851", "CNY"
    sheetDict.Add "897", "SGD"


    'sheetNames = Array("821", "845", "847", "848", "849", "851", "897")
    sheetNames = sheetDict.Keys()
    
    '�����Ŀ���
    Dim destSheetNames(40)
    destCount = 0
    
    
    
    
    Application.ScreenUpdating = False

    Application.DisplayAlerts = False
    

    ':= ָ���ض��Ĳ���ֵ.����Python�еĹؼ��ֲ�����

   ' Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False

    Application.CutCopyMode = False
    
    
    Set conn = CreateObject("adodb.connection")
    conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
    
    
    '��ȡ��Ҫ�ı�
    For i = 0 To UBound(sheetNames)
        
         '��ȡ3RD
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] not like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i))
        
        destSheetNames(destCount) = sheetNames(i)
        '���ܼ���ͬkey��ֵ
        'sheetDict.Add destSheetNames(destCount), sheetDict.Item(sheetNames(i))
        '���и���
        sheetDict(destSheetNames(destCount)) = sheetDict.Item(sheetNames(i))
        destCount = destCount + 1
        
        
         '��ȡIC
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i) & "IC")
        
        destSheetNames(destCount) = sheetNames(i) & "IC"
        sheetDict(destSheetNames(destCount)) = sheetDict.Item(sheetNames(i))
        destCount = destCount + 1
        
        
    Next i
    
    '�����Ĵ���
    'ѡȡCoountry IN ��һ�ű�
    'ע���ֶ�Ҫ��[]
    Dim specSheet
    Set specSheet = CreateObject("Scripting.Dictionary")
    specSheet.Add "Country IN", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705'"
    specSheet.Add "INR(USD)", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705'"
    specSheet.Add "294IN", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%294%'"
    specSheet.Add "552IN", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%552%'"
    specSheet.Add "596IN", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%596%'"
    specSheet.Add "RELIANCE", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%RELIANCE%'"
    specSheet.Add "IDEA", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%IDEA%'"
    specSheet.Add "CISCO", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%CISCO%'"
    specSheet.Add "TATA", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%TATA%'"
    specSheet.Add "BHARTI", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%BHARTI%' and [Address1] not like '%TELESONIC%'"
    specSheet.Add "TELESONIC", "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%BHARTI%' and [Address1] like '%TELESONIC%'"
    
    
    Dim specRate
    Set specRate = CreateObject("Scripting.Dictionary")
    specRate.Add "Country IN", "USD"
    specRate.Add "INR(USD)", "USD"
    specRate.Add "294IN", "USD"
    specRate.Add "552IN", "EUR"
    specRate.Add "596IN", "EUR"
    specRate.Add "RELIANCE", "USD"
    specRate.Add "IDEA", "USD"
    specRate.Add "CISCO", "USD"
    specRate.Add "TATA", "USD"
    specRate.Add "BHARTI", "USD"
    specRate.Add "TELESONIC", "USD"
    
    

    For Each i In specSheet
        'MsgBox "�ؼ���: " & i & " ��Ӧ�� " & D.Item(i)
        Call CopySheet(conn, specSheet.Item(i), headRange, i)
        destSheetNames(destCount) = i
        destCount = destCount + 1
    Next
    
    For Each i In specRate
        sheetDict(i) = specRate.Item(i)
    Next

        
    conn.Close

    Set conn = Nothing
       
    
    
    '�������Ŀ���
    For i = 0 To destCount - 1
    
        Worksheets(destSheetNames(i)).Activate
        
        'Sheets(destSheetNames(i)).Activate
        
        j = Sheets(destSheetNames(i)).UsedRange.Rows.Count
        
        'MsgBox (j)
        
        'MsgBox (Sheets(destSheetNames(i)).Cells.SpecialCells(xlCellTypeLastCell).Row)
        
        
        '����Due Date �� Days Late
        For r = 2 To j
        
            'DueDate = Range(Cells(r, dueDateColumn))
            DueDate = Cells(r, dueDateColumn)
            lateDays = DateDiff("d", DueDate, mydate)
            'Range(Cells(r, dayslateColumn)) = lateDays
            Cells(r, dayslateColumn) = lateDays
            
            '����Ҳ������Excel�е�������ʽ���д�������ٶȱȽ���
            'If lateDays >= -10 Then
            '    Cells(r, dayslateColumn).Interior.Color = RGB(255, 197, 197) '����ɫ
            '    Cells(r, dayslateColumn).Font.Color = RGB(204, 51, 0)       '������ɫ
            'End If
            
            
            'Call FormatConditions(destSheetNames(i), dayslateColumn)
            
            '���current ~ 361+days
            For DayCol = currentColumn To day361Column
                Cells(r, DayCol) = ""
            Next DayCol
            
            Dim copyColumn
            Select Case lateDays
                Case Is <= 0
                    copyColumn = currentColumn
                Case Is <= 30
                    copyColumn = day30Column
                Case Is <= 60
                    copyColumn = day60Column
                Case Is <= 90
                    copyColumn = day90Column
                Case Is <= 180
                    copyColumn = day180Column
                Case Is <= 360
                    copyColumn = day360Column
                Case Else
                    copyColumn = day361Column
            End Select
            
            'Range(Cells(r, copyColumn)) = Range(r, totalColumn)
            Cells(r, copyColumn) = Cells(r, totalColumn)
            
        Next r
        
        '����ٶȱ�һ������Ԫ�ȽϿ����
        Call FormatConditions(destSheetNames(i), dayslateColumn)
        
        If destSheetNames(i) = "Country IN" Then
            Call SortSheet(destSheetNames(i), OperatingColumn, trxColumn, customerNameColumn, dayslateColumn)
        Else
            Call SortSheet(destSheetNames(i), trxColumn, customerNameColumn, dayslateColumn)
        End If
    
        If specSheet.exists(destSheetNames(i)) = True And destSheetNames(i) Like "*IN*" = False Then
             Call MySubtotal(destSheetNames(i), OperatingColumn, totalColumn, currentColumn, day30Column, day60Column, day90Column, day180Column, day360Column, day361Column)
        Else
            Call MySubtotal(destSheetNames(i), customerNameColumn, totalColumn, currentColumn, day30Column, day60Column, day90Column, day180Column, day360Column, day361Column)
        End If
        
       
        '���ʼ����
        If destSheetNames(i) <> "INR(USD)" Then
            Call CalculateCurrency(destSheetNames(i), trxColumn, accountColumn, totalColumn, day361Column, trxClassColumn, sheetDict)
        Else
            Call HandleINRUSD(destSheetNames(i), trxColumn, totalColumn, day361Column, sheetDict)
        End If
        
        Call FormatSheet(destSheetNames(i))
        
    Next i
    
    
    
    
    Application.DisplayAlerts = True

    Application.ScreenUpdating = True
    
    

End Sub

