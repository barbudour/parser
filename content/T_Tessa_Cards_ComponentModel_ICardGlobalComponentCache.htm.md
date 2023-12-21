# ICardGlobalComponentCache - интерфейс
Глобальный кэш для компонентов API карточек.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardGlobalComponentCache
VB __Копировать
     Public Interface ICardGlobalComponentCache
C++ __Копировать
     public interface class ICardGlobalComponentCache
F# __Копировать
     type ICardGlobalComponentCache = interface end
##  __Свойства
[LoadersByTypeID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_LoadersByTypeID.htm)|
Объекты, загружающие карточку. Доступны по идентификаторам типов карточек.  
---|---  
[NewDefaultResponsesByTypeID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_NewDefaultResponsesByTypeID.htm)|
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Default]. Доступны по идентификаторам типов карточек.  
[NewValidResponsesByTypeID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_NewValidResponsesByTypeID.htm)|
Ответы на запросы, создающие структуру карточки для режима
[Tessa.Cards.CardNewMode.Valid]. Доступны по идентификаторам типов карточек.  
[SectionRowRemoverBySectionID](P_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_SectionRowRemoverBySectionID.htm)|
Объекты, содержащие информацию по удалению строк. Доступны по идентификаторам
секций карточек.  
##  __Методы
[Invalidate](M_Tessa_Cards_ComponentModel_ICardGlobalComponentCache_Invalidate.htm)|
Сбрасывает весь кэш.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
