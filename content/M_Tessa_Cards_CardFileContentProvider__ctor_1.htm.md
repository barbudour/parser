# CardFileContentProvider(Guid, Int64, Func<CancellationToken,
ValueTask<Stream>>) - конструктор
Создаёт экземпляр класса с указанием значений его свойств и методов.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContentProvider(
    	Guid fileID,
    	long size,
    	Func<CancellationToken, ValueTask<Stream>> getContentFuncAsync
    )
VB __Копировать
     Public Sub New ( 
    	fileID As Guid,
    	size As Long,
    	getContentFuncAsync As Func(Of CancellationToken, ValueTask(Of Stream))
    )
C++ __Копировать
     public:
    CardFileContentProvider(
    	Guid fileID, 
    	long long size, 
    	Func<CancellationToken, ValueTask<Stream^>>^ getContentFuncAsync
    )
F# __Копировать
     new : 
            fileID : Guid * 
            size : int64 * 
            getContentFuncAsync : Func<CancellationToken, ValueTask<Stream>> -> CardFileContentProvider
#### Параметры
fileID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор файла.
size [Int64](https://learn.microsoft.com/dotnet/api/system.int64)
    Размер файла в байтах.
getContentFuncAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
     Функция, возвращающая контент файла или null, если в качестве контента требуется вернуть пустой поток размером 0 байт. 
## __См. также
#### Ссылки
[CardFileContentProvider - ](T_Tessa_Cards_CardFileContentProvider.htm)
[CardFileContentProvider -
перегрузка](Overload_Tessa_Cards_CardFileContentProvider__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
