# CardComponentHelper.IsAllowedPhysicalColumn - метод
Возвращает признак того, что колонка с заданным именем columnName присутствует
в указанном списке columns и является физической колонкой.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static bool IsAllowedPhysicalColumn(
    	string columnName,
    	CardMetadataColumnCollection columns
    )
VB __Копировать
     Public Shared Function IsAllowedPhysicalColumn ( 
    	columnName As String,
    	columns As CardMetadataColumnCollection
    ) As Boolean
C++ __Копировать
     public:
    static bool IsAllowedPhysicalColumn(
    	String^ columnName, 
    	CardMetadataColumnCollection^ columns
    )
F# __Копировать
     static member IsAllowedPhysicalColumn : 
            columnName : string * 
            columns : CardMetadataColumnCollection -> bool 
#### Параметры
columnName [String](https://learn.microsoft.com/dotnet/api/system.string)
    Проверяемое имя колонки.
columns
[CardMetadataColumnCollection](T_Tessa_Cards_Metadata_CardMetadataColumnCollection.htm)
    Список колонок.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если колонка с заданным именем columnName присутствует в указанном
списке columns и является физической колонкой; false в противном случае.
## __См. также
#### Ссылки
[CardComponentHelper - ](T_Tessa_Cards_ComponentModel_CardComponentHelper.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
