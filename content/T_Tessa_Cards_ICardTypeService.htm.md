# ICardTypeService - интерфейс
Сервис для управления типами карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypeService
VB __Копировать
     Public Interface ICardTypeService
C++ __Копировать
     public interface class ICardTypeService
F# __Копировать
     type ICardTypeService = interface end
##  __Методы
[GetAllCardTypesAsync](M_Tessa_Cards_ICardTypeService_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
---|---  
[GetCachedMetadataAsync](M_Tessa_Cards_ICardTypeService_GetCachedMetadataAsync.htm)|
Возвращает метаинформацию, описывающую типы всех карточек, со всей необходимой
информацией. Возвращаемая метаинформация и содержащиеся в ней типы карточек
защищены от изменений.  
[GetCardTypeAsync](M_Tessa_Cards_ICardTypeService_GetCardTypeAsync.htm)|
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.  
[StoreAsync](M_Tessa_Cards_ICardTypeService_StoreAsync.htm)| Добавляет,
обновляет и удаляет типы карточек.  
##  __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync_2.htm)|  Удаляет
заданный тип карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
