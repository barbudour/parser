# CardGlobalComponentCache.SectionRowRemoverBySectionID - свойство
Объекты, содержащие информацию по удалению строк. Доступны по идентификаторам
секций карточек.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ConcurrentDictionary<Guid, CardSectionRowRemover> SectionRowRemoverBySectionID { get; }
VB __Копировать
     Public ReadOnly Property SectionRowRemoverBySectionID As ConcurrentDictionary(Of Guid, CardSectionRowRemover)
    	Get
C++ __Копировать
     public:
    virtual property ConcurrentDictionary<Guid, CardSectionRowRemover^>^ SectionRowRemoverBySectionID {
    	ConcurrentDictionary<Guid, CardSectionRowRemover^>^ get () sealed;
    }
F# __Копировать
     abstract SectionRowRemoverBySectionID : ConcurrentDictionary<Guid, CardSectionRowRemover> with get
    override SectionRowRemoverBySectionID : ConcurrentDictionary<Guid, CardSectionRowRemover> with get
#### Значение свойства
[ConcurrentDictionary](https://learn.microsoft.com/dotnet/api/system.collections.concurrent.concurrentdictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)>
#### Реализации
[ICardGlobalComponentCache.SectionRowRemoverBySectionID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_SectionRowRemoverBySectionID.htm)  
##  __См. также
#### Ссылки
[CardGlobalComponentCache -
](T_Tessa_Cards_ComponentModel_CardGlobalComponentCache.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
