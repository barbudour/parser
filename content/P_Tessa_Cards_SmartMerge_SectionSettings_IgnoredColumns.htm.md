# SectionSettings.IgnoredColumns - свойство
Игнорируемые колонки. Поведение такое же как и у параметра ExcludedColumns
(дополняют друг друга), но в дополнение к логике параметра ExcludedColumns,
колонки, указанные в этом параметре, будут проигнорированы при апдейте узлов.
## __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<string> IgnoredColumns { get; }
VB __Копировать
     Public ReadOnly Property IgnoredColumns As IReadOnlyList(Of String)
    	Get
C++ __Копировать
     public:
    property IReadOnlyList<String^>^ IgnoredColumns {
    	IReadOnlyList<String^>^ get ();
    }
F# __Копировать
     member IgnoredColumns : IReadOnlyList<string> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[SectionSettings - ](T_Tessa_Cards_SmartMerge_SectionSettings.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
