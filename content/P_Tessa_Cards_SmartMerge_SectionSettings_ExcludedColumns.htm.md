# SectionSettings.ExcludedColumns - свойство
Исключенные колонки. Если заполнены, то значения узлов слияния, относящихся к
данной секции, будут сравниваться исключая эти колонки. Имеют приоритет перед
IncludedColumns. Если ExcludedColumns и IncludedColumns заполнены
одновременно, выдается Warning в ValidationResult.
## __Definition
 **Пространство имён:** [Tessa.Cards.SmartMerge](N_Tessa_Cards_SmartMerge.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public IReadOnlyList<string> ExcludedColumns { get; }
VB __Копировать
     Public ReadOnly Property ExcludedColumns As IReadOnlyList(Of String)
    	Get
C++ __Копировать
     public:
    property IReadOnlyList<String^>^ ExcludedColumns {
    	IReadOnlyList<String^>^ get ();
    }
F# __Копировать
     member ExcludedColumns : IReadOnlyList<string> with get
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>
##  __См. также
#### Ссылки
[SectionSettings - ](T_Tessa_Cards_SmartMerge_SectionSettings.htm)
[Tessa.Cards.SmartMerge - пространство имён](N_Tessa_Cards_SmartMerge.htm)
