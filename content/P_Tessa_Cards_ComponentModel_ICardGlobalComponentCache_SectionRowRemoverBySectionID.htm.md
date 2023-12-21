# ICardGlobalComponentCache.SectionRowRemoverBySectionID - свойство
Объекты, содержащие информацию по удалению строк. Доступны по идентификаторам
секций карточек.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ConcurrentDictionary<Guid, CardSectionRowRemover> SectionRowRemoverBySectionID { get; }
VB __Копировать
     ReadOnly Property SectionRowRemoverBySectionID As ConcurrentDictionary(Of Guid, CardSectionRowRemover)
    	Get
C++ __Копировать
    property ConcurrentDictionary<Guid, CardSectionRowRemover^>^ SectionRowRemoverBySectionID {
    	ConcurrentDictionary<Guid, CardSectionRowRemover^>^ get ();
    }
F# __Копировать
     abstract SectionRowRemoverBySectionID : ConcurrentDictionary<Guid, CardSectionRowRemover> with get
#### Значение свойства
[ConcurrentDictionary](https://learn.microsoft.com/dotnet/api/system.collections.concurrent.concurrentdictionary-2)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid),
[CardSectionRowRemover](T_Tessa_Cards_ComponentModel_CardSectionRowRemover.htm)>
##  __См. также
#### Ссылки
[ICardGlobalComponentCache -
](T_Tessa_Cards_ComponentModel_ICardGlobalComponentCache.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
