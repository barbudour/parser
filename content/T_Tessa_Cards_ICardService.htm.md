# ICardService - интерфейс
Сервис для управления карточками.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardService
VB __Копировать
     Public Interface ICardService
C++ __Копировать
     public interface class ICardService
F# __Копировать
     type ICardService = interface end
##  __Методы
[DeleteAsync](M_Tessa_Cards_ICardService_DeleteAsync.htm)| Удаляет карточку по
информации, переданной в запросе.  
---|---  
[GetAsync](M_Tessa_Cards_ICardService_GetAsync.htm)| Возвращает данные
карточки по заданному запросу.  
[GetFileContentAsync](M_Tessa_Cards_ICardService_GetFileContentAsync.htm)|
Получает контент версии файла.  
[GetFileVersionsAsync](M_Tessa_Cards_ICardService_GetFileVersionsAsync.htm)|
Возвращает информацию о версиях файла по заданному запросу.  
[NewAsync](M_Tessa_Cards_ICardService_NewAsync.htm)| Возвращает заполненную
структуру карточки по заданному запросу. Физически карточка не создаётся.  
[RequestAsync](M_Tessa_Cards_ICardService_RequestAsync.htm)| Выполняет
универсальный запрос к сервису карточек.  
[StoreAsync(CardStoreRequest,
CancellationToken)](M_Tessa_Cards_ICardService_StoreAsync_1.htm)| Сохраняет
карточку, переданную в запросе.  
[StoreAsync(Stream,
CancellationToken)](M_Tessa_Cards_ICardService_StoreAsync.htm)| Сохраняет
карточку и её файлы, переданные в потоке карточки.  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
