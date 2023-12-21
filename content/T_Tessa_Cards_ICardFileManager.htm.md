# ICardFileManager - интерфейс
Объект, который управляет объектами контейнеров
[ICardFileContainer](T_Tessa_Cards_ICardFileContainer.htm), объединяющих
карточку с её файлами. Объект доступен на клиенте и на сервере.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardFileManager
VB __Копировать
     Public Interface ICardFileManager
C++ __Копировать
     public interface class ICardFileManager
F# __Копировать
     type ICardFileManager = interface end
##  __Методы
[CreateContainerAsync](M_Tessa_Cards_ICardFileManager_CreateContainerAsync.htm)|
Создаёт контейнер с информацией по заданной карточке и по её файлам.  
---|---  
[PrepareForStoreAsync](M_Tessa_Cards_ICardFileManager_PrepareForStoreAsync.htm)|
Подготавливает карточку из текущего контейнера и контент её файлов к
сохранению. Возвращает объект запрос на сохранение карточки.  
[StoreAsync](M_Tessa_Cards_ICardFileManager_StoreAsync.htm)|  Сохраняет
карточку из текущего контейнера и контент её файлов, при этом позволяет
асинхронно отслеживать её состояние. В процессе сохранения карточка в
контейнере и её файлы не изменяются, поэтому метод безопасно вызывать
повторно.  
## __Методы расширения
[CreateContainerRemoteAsync](M_Tessa_Cards_CardExtensions_CreateContainerRemoteAsync.htm)|
Создаёт контейнер с информацией по заданной карточке и по её файлам. Все файлы
создаются с Remote-содержимым, при загрузке и замене которого не используется
временная папка. Операции с такими файлами будут выполняться быстрее, но при
условии надо быть уверенными, что содержимое файлов, работа с которыми
выполняется, умещается в памяти. Возможные ошибки при загрузке файлов из
карточки игнорируются. В этом случае к созданном контейнере не будет добавлено
файлов, хотя файлы присутствуют в карточке.  
(Определяется [CardExtensions](T_Tessa_Cards_CardExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
