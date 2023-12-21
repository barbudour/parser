# ICardStoreAsyncResponse - интерфейс
Объект, предоставляющий доступ к результату асинхронной операции по сохранению
карточки с файлами.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardStoreAsyncResponse
VB __Копировать
     Public Interface ICardStoreAsyncResponse
C++ __Копировать
     public interface class ICardStoreAsyncResponse
F# __Копировать
     type ICardStoreAsyncResponse = interface end
##  __Свойства
[FileProgress](P_Tessa_Cards_ICardStoreAsyncResponse_FileProgress.htm)|
Прогресс операции, вычисляемый как отношение суммарного количества уже
загруженных байт, относящихся к файлам, к суммарному размеру всех файлов,
которые требуется загрузить. Не учитывает размеры заголовка и запроса на
сохранение карточки.  
---|---  
[Task](P_Tessa_Cards_ICardStoreAsyncResponse_Task.htm)| Асинхронная операция
по сохранению карточки с файлами.  
[TotalFileLength](P_Tessa_Cards_ICardStoreAsyncResponse_TotalFileLength.htm)|
Суммарное количество байт, относящихся к файлам, которое будет загружено на
сервер. Не включает в себя размеры заголовка и запроса на сохранение карточки.  
[UploadedFileLength](P_Tessa_Cards_ICardStoreAsyncResponse_UploadedFileLength.htm)|
Суммарное количество байт, относящихся к файлам, которое было загружено на
сервер. Не включает в себя размеры заголовка и запроса на сохранение карточки.  
## __Методы
[ConfigureAwait](M_Tessa_Cards_ICardStoreAsyncResponse_ConfigureAwait.htm)|
Настраивает ожидание задачи.  
---|---  
[GetAwaiter](M_Tessa_Cards_ICardStoreAsyncResponse_GetAwaiter.htm)|
Возвращает объект, выполняющий ожидание результата задачи
[ICardStoreAsyncResponse.Task].  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
