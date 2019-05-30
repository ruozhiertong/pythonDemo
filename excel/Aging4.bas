Attribute VB_Name = "Aging4"

Sub CopySheet(ByVal conn, ByVal sql, ByVal headRange, ByVal destSheetName)

    'Application.ScreenUpdating = False
     
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
    
    
    
    'Application.ScreenUpdating = True
    

End Sub



Sub FormatSheet(sheetName, totalColumn, day361Column)

    Sheets(sheetName).Activate
    '取消自动换行
    ActiveSheet.Range(Cells(1, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).WrapText = False
    '冻结窗格 固定首行
    'ActiveSheet.Range(Cells(1, 1), Cells(1, ActiveSheet.UsedRange.Columns.Count)).Select
    'ActiveWindow.FreezePanes = True
    ActiveWindow.SplitRow = 1
    ActiveWindow.FreezePanes = True
    

    
    '取消填充
    ActiveSheet.Range(Cells(2, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).Interior.ColorIndex = xlColorIndexNone
    
    'https://baijiahao.baidu.com/s?id=1621006684338092173&wfr=spider&for=pc
    
    ActiveSheet.Range(Cells(2, 1), Cells(ActiveSheet.UsedRange.Rows.Count, ActiveSheet.UsedRange.Columns.Count)).Font.Size = 10
    
    
    '区域格式
    'http://www.360doc.com/content/16/0802/12/6076639_580221192.shtml
    'https://zhidao.baidu.com/question/1495713913788426939.html?sort=11&rn=5&pn=0#wgt-answers
    'https://zhidao.baidu.com/question/344215136.html
    'Range(Cells(2, totalColumn), Cells(fcRow, day361Column)).NumberFormat = "Accounting"
    ActiveSheet.Range(Cells(2, totalColumn), Cells(ActiveSheet.UsedRange.Rows.Count, day361Column)).NumberFormat = "#,###0.00"
    
End Sub

Sub SortSheet(sheetName, ParamArray cols())

    'Application.ScreenUpdating = False
 
    Sheets(sheetName).Activate
    
    Dim day_late_col
    
    For col = 1 To Sheets(sheetName).UsedRange.Columns.Count
        If Cells(1, col) = "Days Late" Then
          day_late_col = col
        End If
    Next col

    
    'currency/customer name/ days late(降序
    
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
    
    'Application.ScreenUpdating = True
    
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


Function CountTrxCurrency(sheetName, trxCol)

    Sheets(sheetName).Activate
    
    Set conn = CreateObject("adodb.connection")
    
    Dim rsSQL
    
    conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
    
    '字段中含空格等 用[]
    sql = "select [" & Cells(1, trxCol) & "] from [" & sheetName & "$] group by [" & Cells(1, trxCol) & "]"
    
    Set rsSQL = conn.Execute(sql) ' 返回RecordSet
    
    'MsgBox (rsSQL.BOF)
    'MsgBox (rsSQL.EOF)
    'MsgBox (rsSQL.Fields.Count) '列数， 字段的个数
    'MsgBox (TypeName(rsSQL)) 'RecordSet
    'MsgBox (rsSQL.RecordCount)
    
    
    'Dim arr(0 To 100) '闭区间 [0,100]
    Dim arr()
    ReDim arr(0 To 100)
    Dim i
    i = 0
     
    Do While Not rsSQL.EOF
        If Not IsNull(rsSQL.Fields(0)) Then
            'MsgBox (rsSQL.Fields(0)) ' Fields 是字段中的值
            'MsgBox (rsSQL.Fields(0).Value) '等同上面
            'MsgBox (rsSQL.Fields(0).Name) '字段名
             arr(i) = rsSQL.Fields(0)
             'MsgBox (arr(i))
             i = i + 1
        End If
        rsSQL.MoveNext
    Loop
    
    '重新定义大小时 保留原来的数据
    ReDim Preserve arr(i - 1) ' [0,i-1]
    'ReDim arr(0 To i - 1)
    
  
   ' useless
   ' For i = 1 To rsSQL.Fields.Count
    
   '     MsgBox (rsSQL.Fields(i))
        
  '  Next i
    
    conn.Close

    Set conn = Nothing

    CountTrxCurrency = arr '返回数组
End Function


'获取sheetname中对应的汇率dict。
Function GetRateDict(destSheetName, trxColumn, sheetDict)
    arr = CountTrxCurrency(destSheetName, trxColumn)
    
    
    rowTemp = Sheets(destSheetName).UsedRange.Rows.Count + 1
     
    '汇率Dict
    Dim rateDict
    Set rateDict = CreateObject("Scripting.Dictionary")
    
    '这里cell临时的，只是用于存放公式，计算。获取本表function currency的汇率。
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
    
    '对象(如字典对象)赋值都要Set ，直接=是不行的
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
                '注意字符串内容中有双引号
                condStr = "=SUMIF($" & trxChr & ":$" & trxChr & ",""" & arr(arr_idx) & """," & idx2Chr & ":" & idx2Chr & ")"
                Cells(rowIdx, idx2).Formula = condStr
            Next idx2
           
        Next arr_idx
        
      
      
        '汇率Dict
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
        
        
        '计算payment
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
        
        
        '计算total
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
        
        '计算function currency
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
        
End Sub

Sub HandleINRUSD(destSheetName, trxColumn, totalColumn, day361Column, sheetDict)

     '汇率Dict. 对象(如字典对象)赋值都要Set ，直接=是不行的
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

    '当多个单元格是合并时，只在第一个单元格位置显示值，其他为空。
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
    
    ' 对调 Credit 和 Operation
    
    
   ' 不可行

   ' ActiveSheet.Range("A:A").Select
    
   ' Selection.Copy
    
   ' ActiveSheet.Range("AO:AO").Select
    
   ' Selection.PasteSpecial Paste:=xlPasteFormats, SkipBlanks:=False, Transpose:=False
    
    
    
    
    'ActiveSheet.Range("A:A").Copy
    'ActiveSheet.Range("AO1").PasteSpecial
    '直接赋值更快
    ActiveSheet.Range("AO:AO") = ActiveSheet.Range("A:A").Value
    ActiveSheet.Range("A:A") = ActiveSheet.Range("B:B").Value
    ActiveSheet.Range("B:B") = ActiveSheet.Range("AO:AO").Value
    
    ActiveSheet.Range("AO:AO").Delete
    
End Sub


Sub processAging()

    
    Application.DisplayAlerts = False
    
    Sheets(1).Activate
     
    '注意前两张表是原始固定的表。删除其他无关表
    For i = Sheets.Count To 3 Step -1
        Sheets(i).Delete
    Next i
    
    Application.ScreenUpdating = False
    

    If Cells(1, 1) <> "Operating Unit Desc" Then
         Call preProcess
    End If
    
    
    
    

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
    
    
     '需要提取的表 字典形式。 key代表提取的表， 表名。 value代表function currency货币类型. 如果额外添加表，在此处添加
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
    sheetNames = sheetDict.keys()

       
    ':= 指定特定的参数值.类似Python中的关键字参数。

   ' Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, SkipBlanks:=False, Transpose:=False

    Application.CutCopyMode = False
    
    
    Set conn = CreateObject("adodb.connection")
    conn.Open "provider=microsoft.jet.oledb.4.0;extended properties=excel 8.0;data source=" & ThisWorkbook.FullName
    
    
    '提取需要的表
    For i = 0 To UBound(sheetNames)
        
         '提取3RD
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] not like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i))
        
        '不能加相同key的值
        'sheetDict.Add destSheetNames(destCount), sheetDict.Item(sheetNames(i))
        '进行覆盖
        'sheetDict(sheetNames(i)) = sheetDict.Item(sheetNames(i))
        
        
         '提取IC
        sql = "select * from [" & sourceSheetName & "$] where [Operating Unit Desc] like '%" & sheetNames(i) & "%'" & "and [Account] like '21705'"
        Call CopySheet(conn, sql, headRange, sheetNames(i) & "IC")
        
        sheetDict(sheetNames(i) & "IC") = sheetDict.Item(sheetNames(i))
        
        
    Next i
    
    '特殊表的处理
    '选取Coountry IN 成一张表
    '注意字段要加[]
    'key是表名， value是数组
    Dim specSheet
    Set specSheet = CreateObject("Scripting.Dictionary")
    specSheet.Add "Country IN", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705'", "USD")
    specSheet.Add "INR(USD)", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705'", "USD")
    specSheet.Add "294IN", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%294%'", "USD")
    specSheet.Add "552IN", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%552%'", "EUR")
    specSheet.Add "596IN", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Operating Unit Desc] like  '%596%'", "EUR")
    specSheet.Add "RELIANCE", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%RELIANCE%'", "USD")
    specSheet.Add "IDEA", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%IDEA%'", "USD")
    specSheet.Add "CISCO", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%CISCO%'", "USD")
    specSheet.Add "TATA", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%TATA%'", "USD")
    specSheet.Add "BHARTI", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%BHARTI%' and [Address1] not like '%TELESONIC%'", "USD")
    specSheet.Add "TELESONIC", Array("select * from [" & sourceSheetName & "$] where [Country] = 'IN' and [Account] not like '21705' and [Customer Name] like  '%BHARTI%' and [Address1] like '%TELESONIC%'", "USD")
    

    For Each i In specSheet
        'MsgBox "关键字: " & i & " 对应项 " & D.Item(i)
        Call CopySheet(conn, specSheet.Item(i)(0), headRange, i)
        sheetDict(i) = specSheet.Item(i)(1)
    Next
        
        
    conn.Close

    Set conn = Nothing
       
    
    destSheetNames = sheetDict.keys()
    
    '处理各个目标表
    For i = 0 To UBound(destSheetNames)
    
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
            Call SortSheet(destSheetNames(i), OperatingColumn, trxColumn, customerNameColumn, dayslateColumn)
        Else
            Call SortSheet(destSheetNames(i), trxColumn, customerNameColumn, dayslateColumn)
        End If
    
        If specSheet.exists(destSheetNames(i)) = True And destSheetNames(i) Like "*IN*" = False Then
             Call MySubtotal(destSheetNames(i), OperatingColumn, totalColumn, currentColumn, day30Column, day60Column, day90Column, day180Column, day360Column, day361Column)
        Else
            Call MySubtotal(destSheetNames(i), customerNameColumn, totalColumn, currentColumn, day30Column, day60Column, day90Column, day180Column, day360Column, day361Column)
        End If
        
       
        '汇率计算等
        If destSheetNames(i) <> "INR(USD)" Then
            Call CalculateCurrency(destSheetNames(i), trxColumn, accountColumn, totalColumn, day361Column, trxClassColumn, sheetDict)
        Else
            Call HandleINRUSD(destSheetNames(i), trxColumn, totalColumn, day361Column, sheetDict)
        End If
        
        Call FormatSheet(destSheetNames(i), totalColumn, day361Column)
        
    Next i
    
    
    
    
    Application.DisplayAlerts = True

    Application.ScreenUpdating = True
    
    

End Sub

