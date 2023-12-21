# CardViewControlInfo.TryGet(Dictionary<String, Object>) - метод
Возвращает информацию по выбранной ссылке
[CardAutocompleteInfo](T_Tessa_Cards_CardAutocompleteInfo.htm) или null, если
такая информация не была установлена.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Cards](N_Tessa_Extensions_Default_Shared_Cards.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardViewControlInfo TryGet(
    	Dictionary<string, Object> requestInfo
    )
VB __Копировать
     Public Shared Function TryGet ( 
    	requestInfo As Dictionary(Of String, Object)
    ) As CardViewControlInfo
C++ __Копировать
     public:
    static CardViewControlInfo^ TryGet(
    	Dictionary<String^, Object^>^ requestInfo
    )
F# __Копировать
     static member TryGet : 
            requestInfo : Dictionary<string, Object> -> CardViewControlInfo 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация для запроса на открытие карточки.
#### Возвращаемое значение
[CardViewControlInfo](T_Tessa_Extensions_Default_Shared_Cards_CardViewControlInfo.htm)  
Запрошенная информация или null, если требуемая информация ещё не была
установлена.
##  __См. также
#### Ссылки
[CardViewControlInfo -
](T_Tessa_Extensions_Default_Shared_Cards_CardViewControlInfo.htm)
[TryGet -
перегрузка](Overload_Tessa_Extensions_Default_Shared_Cards_CardViewControlInfo_TryGet.htm)
[Tessa.Extensions.Default.Shared.Cards - пространство
имён](N_Tessa_Extensions_Default_Shared_Cards.htm)
