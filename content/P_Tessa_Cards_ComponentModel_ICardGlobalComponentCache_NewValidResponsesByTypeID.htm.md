# ICardGlobalComponentCache.NewValidResponsesByTypeID - свойство
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Valid]. Доступны по идентификаторам типов карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ConcurrentDictionary<Guid, CardNewResponse> NewValidResponsesByTypeID { get; }
VB __Копировать
     ReadOnly Property NewValidResponsesByTypeID As ConcurrentDictionary(Of Guid, CardNewResponse)
    	Get
C++ __Копировать
    property ConcurrentDictionary<Guid, CardNewResponse^>^ NewValidResponsesByTypeID {
    	ConcurrentDictionary<Guid, CardNewResponse^>^ get ();
    }
F# __Копировать
     abstract NewValidResponsesByTypeID : ConcurrentDictionary<Guid, CardNewResponse> with get
#### Значение свойства
[ConcurrentDictionary](https://learn.microsoft.com/dotnet/api/system.collections.concurrent.concurrentdictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>
##  __См. также
#### Ссылки
[ICardGlobalComponentCache -
](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
