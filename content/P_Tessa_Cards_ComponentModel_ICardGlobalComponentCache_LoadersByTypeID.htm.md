# ICardGlobalComponentCache.LoadersByTypeID - свойство
Объекты, загружающие карточку. Доступны по идентификаторам типов карточек.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ConcurrentDictionary<Guid, CardLoader> LoadersByTypeID { get; }
VB __Копировать
     ReadOnly Property LoadersByTypeID As ConcurrentDictionary(Of Guid, CardLoader)
    	Get
C++ __Копировать
    property ConcurrentDictionary<Guid, CardLoader^>^ LoadersByTypeID {
    	ConcurrentDictionary<Guid, CardLoader^>^ get ();
    }
F# __Копировать
     abstract LoadersByTypeID : ConcurrentDictionary<Guid, CardLoader> with get
#### Значение свойства
[ConcurrentDictionary](https://learn.microsoft.com/dotnet/api/system.collections.concurrent.concurrentdictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardLoader](T_Tessa_Cards_ComponentModel_CardLoader.htm)>
##  __См. также
#### Ссылки
[ICardGlobalComponentCache -
](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
