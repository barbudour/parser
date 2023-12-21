# CardStoreAsyncResponse - конструктор
Создаёт экземпляр класса с указанием асинхронной операции по сохранению
карточки с файлами и функции, возвращающей общее количество байт, относящихся
к файлам, которое было загружено на сервер.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardStoreAsyncResponse(
    	Task<CardStoreResponse> task,
    	Func<long> getUploadedFileLength,
    	long totalFileLength
    )
VB __Копировать
     Public Sub New ( 
    	task As Task(Of CardStoreResponse),
    	getUploadedFileLength As Func(Of Long),
    	totalFileLength As Long
    )
C++ __Копировать
     public:
    CardStoreAsyncResponse(
    	Task<CardStoreResponse^>^ task, 
    	Func<long long>^ getUploadedFileLength, 
    	long long totalFileLength
    )
F# __Копировать
     new : 
            task : Task<CardStoreResponse> * 
            getUploadedFileLength : Func<int64> * 
            totalFileLength : int64 -> CardStoreAsyncResponse
#### Параметры
task
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[CardStoreResponse](T_Tessa_Cards_CardStoreResponse.htm)>
    Асинхронная операция по сохранению карточки с файлами.
getUploadedFileLength
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>
     Функция, возвращающая общее количество байт, относящихся к файлам, которое было загружено на сервер. Значение не должно включать в себя размер заголовка и запроса на сохранение карточки. 
totalFileLength [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
     Суммарное количество байт, относящихся к файлам, которое будет загружено на сервер. Не включает в себя размеры заголовка и запроса на сохранение карточки. 
## __См. также
#### Ссылки
[CardStoreAsyncResponse - ](T_Tessa_Cards_CardStoreAsyncResponse.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
