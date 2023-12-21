# ICardCachedMetadata.HasData - свойство
Признак того, что кэш содержит данные. Если значение равно false, то кэш ещё
не заполнен или сброшен, поэтому обращение к другим его свойствам приведёт к
наполнению метаинформации.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     bool HasData { get; }
VB __Копировать
     ReadOnly Property HasData As Boolean
    	Get
C++ __Копировать
    property bool HasData {
    	bool get ();
    }
F# __Копировать
     abstract HasData : bool with get
#### Значение свойства
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
##  __См. также
#### Ссылки
[ICardCachedMetadata - ](T_Tessa_Cards_ICardCachedMetadata.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
