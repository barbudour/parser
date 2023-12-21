# CardAutocompleteInfo.TryGet(Dictionary<String, Object>) - метод
Возвращает информацию по выбранной ссылке
[CardAutocompleteInfo](T_Tessa_Cards_CardAutocompleteInfo.htm) или null, если
такая информация не была установлена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static CardAutocompleteInfo TryGet(
    	Dictionary<string, Object> requestInfo
    )
VB __Копировать
     Public Shared Function TryGet ( 
    	requestInfo As Dictionary(Of String, Object)
    ) As CardAutocompleteInfo
C++ __Копировать
     public:
    static CardAutocompleteInfo^ TryGet(
    	Dictionary<String^, Object^>^ requestInfo
    )
F# __Копировать
     static member TryGet : 
            requestInfo : Dictionary<string, Object> -> CardAutocompleteInfo 
#### Параметры
requestInfo
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Дополнительная информация для запроса на открытие карточки.
#### Возвращаемое значение
[CardAutocompleteInfo](T_Tessa_Cards_CardAutocompleteInfo.htm)  
Запрошенная информация или null, если требуемая информация ещё не была
установлена.
##  __См. также
#### Ссылки
[CardAutocompleteInfo - ](T_Tessa_Cards_CardAutocompleteInfo.htm)
[TryGet - перегрузка](Overload_Tessa_Cards_CardAutocompleteInfo_TryGet.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
