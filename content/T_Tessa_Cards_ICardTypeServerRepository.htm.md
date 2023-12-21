# ICardTypeServerRepository - интерфейс
Репозиторий для управления типами карточек на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardTypeServerRepository
VB __Копировать
     Public Interface ICardTypeServerRepository
C++ __Копировать
     public interface class ICardTypeServerRepository
F# __Копировать
     type ICardTypeServerRepository = interface end
##  __Заметки
Предоставляет CRUD-функции для типов карточек.
## __Методы
[CardTypeExistsAsync](M_Tessa_Cards_ICardTypeServerRepository_CardTypeExistsAsync.htm)|
Возвращает признак того, что тип карточки с заданным идентификатором
существует.  
---|---  
[DeleteAsync(Guid,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_DeleteAsync_1.htm)|
Удаляет тип карточки с заданным идентификатором.  
[DeleteAsync(IReadOnlyCollection<Guid>,
CancellationToken)](M_Tessa_Cards_ICardTypeServerRepository_DeleteAsync.htm)|
Удаляет типы карточек с заданными идентификаторами.  
[GetAllCardTypesAsync](M_Tessa_Cards_ICardTypeServerRepository_GetAllCardTypesAsync.htm)|
Возвращает объекты, описывающие типы всех карточек, со всей необходимой
информацией.  
[GetCardTypeAsync](M_Tessa_Cards_ICardTypeServerRepository_GetCardTypeAsync.htm)|
Возвращает объект, описывающий тип карточки, со всей необходимой информацией.  
[InsertAsync](M_Tessa_Cards_ICardTypeServerRepository_InsertAsync.htm)|
Добавляет тип карточки.  
[InsertManyAsync](M_Tessa_Cards_ICardTypeServerRepository_InsertManyAsync.htm)|
Добавляет несколько типов карточек оптимальным способом.  
[UpdateAsync](M_Tessa_Cards_ICardTypeServerRepository_UpdateAsync.htm)|
Обновляет имя и метаданные типа карточки с идентификатором
[Tessa.Cards.CardTypeRepositoryData.ID].  
## __Методы расширения
[DeleteAsync](M_Tessa_Cards_CardExtensions_DeleteAsync_1.htm)|  Удаляет
заданный тип карточки.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
[GetAllCardTypeCollectionAsync](M_Tessa_Cards_CardExtensions_GetAllCardTypeCollectionAsync.htm)|
Возвращает коллекцию, содержащую все типы карточек.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
