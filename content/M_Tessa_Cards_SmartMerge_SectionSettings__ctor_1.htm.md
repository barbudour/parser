# SectionSettings(String, IReadOnlyList<String>, IReadOnlyList<String>,
IReadOnlyList<String>, IReadOnlyList<String>, Boolean, Nullable<Boolean>) -
конструктор
Инициализирует новый экземпляр класса
[SectionSettings](T_Tessa_Cards_SmartMerge_SectionSettings.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public SectionSettings(
    	string name,
    	IReadOnlyList<string> includedColumns = null,
    	IReadOnlyList<string> excludedColumns = null,
    	IReadOnlyList<string> keyColumns = null,
    	IReadOnlyList<string> ignoredColumns = null,
    	bool ignored = false,
    	bool? ignoreDuplicateRows = null
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	Optional includedColumns As IReadOnlyList(Of String) = Nothing,
    	Optional excludedColumns As IReadOnlyList(Of String) = Nothing,
    	Optional keyColumns As IReadOnlyList(Of String) = Nothing,
    	Optional ignoredColumns As IReadOnlyList(Of String) = Nothing,
    	Optional ignored As Boolean = false,
    	Optional ignoreDuplicateRows As Boolean? = Nothing
    )
C++ __Копировать
     public:
    SectionSettings(
    	String^ name, 
    	IReadOnlyList<String^>^ includedColumns = nullptr, 
    	IReadOnlyList<String^>^ excludedColumns = nullptr, 
    	IReadOnlyList<String^>^ keyColumns = nullptr, 
    	IReadOnlyList<String^>^ ignoredColumns = nullptr, 
    	bool ignored = false, 
    	Nullable<bool> ignoreDuplicateRows = nullptr
    )
F# __Копировать
     new : 
            name : string * 
            ?includedColumns : IReadOnlyList<string> * 
            ?excludedColumns : IReadOnlyList<string> * 
            ?keyColumns : IReadOnlyList<string> * 
            ?ignoredColumns : IReadOnlyList<string> * 
            ?ignored : bool * 
            ?ignoreDuplicateRows : Nullable<bool> 
    (* Defaults:
            let _includedColumns = defaultArg includedColumns null
            let _excludedColumns = defaultArg excludedColumns null
            let _keyColumns = defaultArg keyColumns null
            let _ignoredColumns = defaultArg ignoredColumns null
            let _ignored = defaultArg ignored false
            let _ignoreDuplicateRows = defaultArg ignoreDuplicateRows null
    *)
    -> SectionSettings
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
includedColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
excludedColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
keyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
ignoredColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
ignored [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
ignoreDuplicateRows
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
## __См. также
#### Ссылки
[SectionSettings - ](T_Tessa_Cards_SmartMerge_SectionSettings.htm)
[SectionSettings -
перегрузка](Overload_Tessa_Cards_SmartMerge_SectionSettings__ctor.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
