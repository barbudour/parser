# CardGlobalComponentCache.NewDefaultResponsesByTypeID - свойство
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Default]. Доступны по идентификаторам типов карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ConcurrentDictionary<Guid, CardNewResponse> NewDefaultResponsesByTypeID { get; }
VB __Копировать
     Public ReadOnly Property NewDefaultResponsesByTypeID As ConcurrentDictionary(Of Guid, CardNewResponse)
    	Get
C++ __Копировать
     public:
    virtual property ConcurrentDictionary<Guid, CardNewResponse^>^ NewDefaultResponsesByTypeID {
    	ConcurrentDictionary<Guid, CardNewResponse^>^ get () sealed;
    }
F# __Копировать
     abstract NewDefaultResponsesByTypeID : ConcurrentDictionary<Guid, CardNewResponse> with get
    override NewDefaultResponsesByTypeID : ConcurrentDictionary<Guid, CardNewResponse> with get
#### Значение свойства
[ConcurrentDictionary](https://learn.microsoft.com/dotnet/api/system.collections.concurrent.concurrentdictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardNewResponse](T_Tessa_Cards_CardNewResponse.htm)>
#### Реализации
[ICardGlobalComponentCache.NewDefaultResponsesByTypeID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_NewDefaultResponsesByTypeID.htm)  
##  __См. также
#### Ссылки
[CardGlobalComponentCache -
](T_Tessa_Cards_ComponentModel_CardGlobalComponentCache.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
