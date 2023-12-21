# CardSection - свойства
##  __Свойства
[Fields](P_Tessa_Cards_CardSection_Fields.htm)|  Значения полей для строковой
секции с поддержкой состояний. При изменении значений любого поля через это
свойство такое поле помечается как изменённое. Если секция является
коллекционной или древовидной, то при этом вызывается исключение
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception).  
---|---  
[Name](P_Tessa_Cards_CardSection_Name.htm)|  Название секции.  
[RawFields](P_Tessa_Cards_CardSection_RawFields.htm)|  Значения полей для
строковой секции или null, если секция является коллекционной или древовидной.  
[Rows](P_Tessa_Cards_CardSection_Rows.htm)|  Строки и их значения для
коллекционной и древовидной секций или null, если секция является строковой.  
[RowSortingType](P_Tessa_Cards_CardSection_RowSortingType.htm)|  Тип
сортировки строк для коллекционной или древовидной секции.  
[StateRows](P_Tessa_Cards_CardSection_StateRows.htm)|  Доступный только для
чтения список значений полей для строк коллекционных и древовидных секций с
поддержкой состояний. При изменении значений любого поля некоторой строки
через это свойство такое поле и строка помечаются как изменённые. Если секция
является строковой, то вызывается исключение
[NotSupportedException](https://learn.microsoft.com/dotnet/api/system.notsupportedexception).  
[TableType](P_Tessa_Cards_CardSection_TableType.htm)|  Тип коллекционной или
древовидной секции. Для строковой секции всегда возвращается значение
Unspecified.  
[Type](P_Tessa_Cards_CardSection_Type.htm)|  Тип секции карточки. Не
содержится в пакете и вычисляется на основании наличия в пакете определённых
полей.  
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
