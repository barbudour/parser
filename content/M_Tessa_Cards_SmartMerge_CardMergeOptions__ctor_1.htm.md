# CardMergeOptions(IEnumerable<SectionSettings>, FileSettings, Boolean,
Boolean) - конструктор
Инициализирует новый экземпляр класса
[CardMergeOptions](T_Tessa_Cards_SmartMerge_CardMergeOptions.htm)
##  __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMergeOptions(
    	IEnumerable<SectionSettings>? sectionSettings = null,
    	FileSettings fileSettings = null,
    	bool ignoreDuplicateRows = true,
    	bool skipIfCardExists = false
    )
VB __Копировать
     Public Sub New ( 
    	Optional sectionSettings As IEnumerable(Of SectionSettings) = Nothing,
    	Optional fileSettings As FileSettings = Nothing,
    	Optional ignoreDuplicateRows As Boolean = true,
    	Optional skipIfCardExists As Boolean = false
    )
C++ __Копировать
     public:
    CardMergeOptions(
    	IEnumerable<SectionSettings^>^ sectionSettings = nullptr, 
    	FileSettings^ fileSettings = nullptr, 
    	bool ignoreDuplicateRows = true, 
    	bool skipIfCardExists = false
    )
F# __Копировать
     new : 
            ?sectionSettings : IEnumerable<SectionSettings> * 
            ?fileSettings : FileSettings * 
            ?ignoreDuplicateRows : bool * 
            ?skipIfCardExists : bool 
    (* Defaults:
            let _sectionSettings = defaultArg sectionSettings null
            let _fileSettings = defaultArg fileSettings null
            let _ignoreDuplicateRows = defaultArg ignoreDuplicateRows true
            let _skipIfCardExists = defaultArg skipIfCardExists false
    *)
    -> CardMergeOptions
#### Параметры
sectionSettings
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[SectionSettings](T_Tessa_Cards_SmartMerge_SectionSettings.htm)>
(Optional)
fileSettings [FileSettings](T_Tessa_Cards_SmartMerge_FileSettings.htm)
(Optional)
ignoreDuplicateRows
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
skipIfCardExists
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) (Optional)
## __См. также
#### Ссылки
[CardMergeOptions - ](T_Tessa_Cards_SmartMerge_CardMergeOptions.htm)
[CardMergeOptions -
перегрузка](Overload_Tessa_Cards_SmartMerge_CardMergeOptions__ctor.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
