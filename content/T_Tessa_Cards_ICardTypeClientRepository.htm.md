# ICardTypeClientRepository - интерфейс
Репозиторий для управления типами карточек на клиенте.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypeClientRepository
VB __Копировать
     Public Interface ICardTypeClientRepository
C++ __Копировать
     public interface class ICardTypeClientRepository
F# __Копировать
     type ICardTypeClientRepository = interface end
##  __Методы
[DeleteAsync](M_Tessa_Cards_ICardTypeClientRepository_DeleteAsync.htm)|
Удаляет тип карточки с заданным идентификатором.  
---|---  
[GetAllCardTypesAsync](M_Tessa_Cards_ICardTypeClientRepository_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
[GetCachedMetadataAsync](M_Tessa_Cards_ICardTypeClientRepository_GetCachedMetadataAsync.htm)|
Возвращает метаинформацию, описывающую типы всех карточек, со всей необходимой
информацией. Возвращаемая метаинформация и содержащиеся в ней типы карточек
защищены от изменений.  
[GetCardTypeAsync](M_Tessa_Cards_ICardTypeClientRepository_GetCardTypeAsync.htm)|
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.  
[StoreAsync](M_Tessa_Cards_ICardTypeClientRepository_StoreAsync.htm)|
Добавляет или обновляет тип карточки.  
[StoreManyAsync](M_Tessa_Cards_ICardTypeClientRepository_StoreManyAsync.htm)|
Добавляет, обновляет и удаляет типы карточек.  
##  __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync.htm)|  Удаляет заданный
тип карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
