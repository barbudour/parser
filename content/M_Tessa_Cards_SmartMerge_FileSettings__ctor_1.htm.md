# FileSettings(IReadOnlyList<String>, IReadOnlyList<String>,
IReadOnlyList<String>, Boolean) - конструктор
Инициализирует новый экземпляр класса
[FileSettings](T_Tessa_Cards_SmartMerge_FileSettings.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileSettings(
    	IReadOnlyList<string> keyColumns = null,
    	IReadOnlyList<string> includedColumns = null,
    	IReadOnlyList<string> contentColumns = null,
    	bool alwaysUpdateContent = false
    )
VB __Копировать
     Public Sub New ( 
    	Optional keyColumns As IReadOnlyList(Of String) = Nothing,
    	Optional includedColumns As IReadOnlyList(Of String) = Nothing,
    	Optional contentColumns As IReadOnlyList(Of String) = Nothing,
    	Optional alwaysUpdateContent As Boolean = false
    )
C++ __Копировать
     public:
    FileSettings(
    	IReadOnlyList<String^>^ keyColumns = nullptr, 
    	IReadOnlyList<String^>^ includedColumns = nullptr, 
    	IReadOnlyList<String^>^ contentColumns = nullptr, 
    	bool alwaysUpdateContent = false
    )
F# __Копировать
     new : 
            ?keyColumns : IReadOnlyList<string> * 
            ?includedColumns : IReadOnlyList<string> * 
            ?contentColumns : IReadOnlyList<string> * 
            ?alwaysUpdateContent : bool 
    (* Defaults:
            let _keyColumns = defaultArg keyColumns null
            let _includedColumns = defaultArg includedColumns null
            let _contentColumns = defaultArg contentColumns null
            let _alwaysUpdateContent = defaultArg alwaysUpdateContent false
    *)
    -> FileSettings
#### Параметры
keyColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
includedColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
contentColumns
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
(Optional)
alwaysUpdateContent
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
## __См. также
#### Ссылки
[FileSettings - ](T_Tessa_Cards_SmartMerge_FileSettings.htm)
[FileSettings -
перегрузка](Overload_Tessa_Cards_SmartMerge_FileSettings__ctor.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
