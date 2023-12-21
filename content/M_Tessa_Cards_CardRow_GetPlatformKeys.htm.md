# CardRow.GetPlatformKeys - метод
Возвращает список системных ключей, используемых в объекте
[CardRow](T_Tessa_Cards_CardRow.htm), в зависимости от типа коллекционной
секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static IReadOnlyList<string> GetPlatformKeys(
    	CardTableType tableType
    )
VB __Копировать
     Public Shared Function GetPlatformKeys ( 
    	tableType As CardTableType
    ) As IReadOnlyList(Of String)
C++ __Копировать
     public:
    static IReadOnlyList<String^>^ GetPlatformKeys(
    	CardTableType tableType
    )
F# __Копировать
     static member GetPlatformKeys : 
            tableType : CardTableType -> IReadOnlyList<string> 
#### Параметры
tableType [CardTableType](T_Tessa_Cards_CardTableType.htm)
    Тип коллекционной секции.
#### Возвращаемое значение
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Список системных ключей
##  __См. также
#### Ссылки
[CardRow - ](T_Tessa_Cards_CardRow.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
