Attribute VB_Name = "模块11"

Sub CopySheet(ByVal conn, ByVal sql, ByVal headRange, ByVal destSheetName)

    Application.ScreenUpdating = False
     
    Worksheets.Add after:=Sheets(Sheets.Count)
    With ActiveSheet

        .Name = destSheetName
        '复制行头

        For num = 1 To UBound(headRange, 2)

            .Cells(1, num) = headRange(1, num)

        Next num
        
        .Range("A2").CopyFromRecordset conn.Execute(sql)

    End With
    
    
    Worksheets(1).Activate

    '如果是两行的格式复制，在目标表会两行两行进行复制的

    'Sheets(1).Range(Cells(1, 1), Cells(2, Sheets(1).UsedRange.Columns.Count)).Select

    'Sheets(1).Cells.Select
    
    '表头格式复制
    ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select
    
    Selection.Copy

    Worksheets(Sheets.Count).Activate

    'ActiveSheet.Cells.Select
    
    ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select

    ':= 指定特定的参数值.类似Python中的关键字参数。

    Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False
    
    
    
    '内容格式复制
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
    '取消自动换行
     ActiveSheet.Range(Cells(1, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).WrapText = False
    '冻结窗格 固定首行
    'ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select
    'ActiveWindow.FreezePanes = True
    ActiveWindow.SplitRow = 1
    ActiveWindow.FreezePanes = True
    
    
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

    
    'customer name/currency/ days late(降序
    
    'Set k1 = Range("B3") '关键列
    'Set k2 = Range("E3") '关键列
    '使用可变参数处理
    For i = 0 To UBound(cols, 1)
        If cols(i) = day_late_col Then
            '对daylate降序
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
    
    
    '可以在指定的区域按照相应的排序。 注意指定的区域要包含排序的列。
    'Sheets(sheetName).Range(Cells(2, CustCol), Cells(Sheets(sheetName).UsedRange.Rows.Count, CustCol)).Sort key1:=k1, Order1:=1, key2:=k2, Order2:=1
    
    'Sheets(sheetName).Range(Cells(2, 1), Cells(Sheets(sheetName).UsedRange.Rows.Count, Sheets(sheetName).UsedRange.Columns.Count)).Sort key1:=k1, Order1:=1, key2:=k2, Order2:=1, key3:=k3, Order3:=2
    
    Application.ScreenUpdating = True
    
End Sub



'分类汇总（先以某个分类，再根据汇总项汇总）
Sub MySubtotal(sheetName, groupByCol, col1, col2, col3, col4, col5, col6, col7, col8)
    Worksheets(sheetName).Activate
    Sheets(sheetName).Range("A1").CurrentRegion.Subtotal GroupBy:=groupByCol, Function:=xlSum, TotalList:=Array(col1, col2, col3, col4, col5, col6, col7, col8)
End Sub


'条件格式
Sub FormatConditions(sheetName, col)
    
    Worksheets(sheetName).Activate
    
    Sheets(sheetName).Range(Cells(2, col), Cells(Sheets(sheetName).UsedRange.Rows.Count, col)).Select
     
    Selection.FormatConditions.Add Type:=xlCellValue, Operator:=xlGreaterEqual, Formula1:="-10"
    
    Selection.FormatConditions(1).Interior.Color = RGB(255, 197, 197) '背景色
    Selection.FormatConditions(1).Font.Color = RGB(204, 51, 0)
    
    'Selection.FormatConditions(1).Font.ColorIndex = 3

End Sub


Sub preProcess()

    '当多个单元格是合并时，只在第一个单元格位置显示值，其他为空。
    'MsgBox (Cells(1, 1))
    'MsgBox (Cells(1, 2))
    'MsgBox (Cells(2, 1))
    'MsgBox (Cells(2, 2))
    
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
    
    
End Sub


Sub processAging()


    If Cells(1, 1) <> "Operating Unit Desc" Then
         Call preProcess
    End If
    
        
    Application.DisplayAlerts = False

    For i = Sheets.Count To 2 Step -1

        Sheets(i).Delete

    Next i
    Application.DisplayAlerts = True
    

    mydate = Application.InputBox(prompt:="请输入日期：")
    
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
        End If
    Next col
    
    
    'MsgBox (dueDateColumn & "" & dayslateColumn & totalColumn & currentColumn & day30Column & day60Column & day90Column & day180Column & day360Column & day361Column)
    
    
     '需要提取的表
    sheetNames = Array("845", "847", "848", "849", "897", "851")
    
    '保存的目标表
    Dim destSheetNames(20)
    destCount = 0
    
    
    
    
    Application.ScreenUpdating = False

    Application.DisplayAlerts = False
    

    ':= 指定特定的参数值.类似Python中的关键字参数。

   ' Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False

    Application.CutCopyMode = False
    
    
    
    
    Set conn = CreateObject("adodb.connection")
    conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
    
    
    '选取Coountry IN 成一张表
    '注意字段要加[]
    sql = "select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705'"
    Call CopySheet(conn, sql, headRange, "Country IN")
    
    destSheetNames(destCount) = "Country IN"
    destCount = destCount + 1
    
    
    
    '提取需要的表
    For i = 0 To UBound(sheetNames)
        
        '提取IC
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i) & "IC")
        
        destSheetNames(destCount) = sheetNames(i) & "IC"
        destCount = destCount + 1
         
         '提取3RD
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] not like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i) & "-3RD")
        
        destSheetNames(destCount) = sheetNames(i) & "-3RD"
        destCount = destCount + 1
        
    Next i
    
        
    conn.Close

    Set conn = Nothing
       
    
    
    '处理各个目标表
    For i = 0 To destCount - 1
    
    
    
        Call FormatSheet(destSheetNames(i))
        
        
        Worksheets(destSheetNames(i)).Activate
        
        'Sheets(destSheetNames(i)).Activate
        
        j = Sheets(destSheetNames(i)).UsedRange.Rows.Count
        
        'MsgBox (j)
        
        'MsgBox (Sheets(destSheetNames(i)).Cells.SpecialCells(xlCellTypeLastCell).Row)
        
        
        '处理Due Date 和 Days Late
        For r = 2 To j
        
            'DueDate = Range(Cells(r, dueDateColumn))
            DueDate = Cells(r, dueDateColumn)
            lateDays = DateDiff("d", DueDate, mydate)
            'Range(Cells(r, dayslateColumn)) = lateDays
            Cells(r, dayslateColumn) = lateDays
            
            '这里也可以用Excel中的条件格式进行处理。这个速度比较慢
            'If lateDays >= -10 Then
            '    Cells(r, dayslateColumn).Interior.Color = RGB(255, 197, 197) '背景色
            '    Cells(r, dayslateColumn).Font.Color = RGB(204, 51, 0)       '字体颜色
            'End If
            
            
            'Call FormatConditions(destSheetNames(i), dayslateColumn)
            
            '清空current ~ 361+days
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
        
        '这个速度比一个个单元比较快多了
        Call FormatConditions(destSheetNames(i), dayslateColumn)
        
        If destSheetNames(i) = "Country IN" Then
            Call SortSheet(destSheetNames(i), OperatingColumn, customerNameColumn, trxColumn, dayslateColumn)
        Else
            Call SortSheet(destSheetNames(i), customerNameColumn, trxColumn, dayslateColumn)
        End If
        
        Call SortSheet(destSheetNames(i), customerNameColumn, trxColumn, dayslateColumn)
        
        Call MySubtotal(destSheetNames(i), customerNameColumn, totalColumn, currentColumn, day30Column, day60Column, day90Column, day180Column, day360Column, day361Column)
        
    Next i
    
    
    Application.DisplayAlerts = True

    Application.ScreenUpdating = True
    
    

End Sub

