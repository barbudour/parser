# IStorage.WriteToAsync - метод
Осуществляет преобразование схемы в строковое представление
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     Task WriteToAsync(
    	[NotNullAttribute] Stream stream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function WriteToAsync ( 
    	<NotNullAttribute> stream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
    Task^ WriteToAsync(
    	[NotNullAttribute] Stream^ stream, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract WriteToAsync : 
            [<NotNullAttribute>] stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
     Поток куда будет записано содержимое хранилища 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IStorage - ](T_Tessa_Applications_Containers_Storage_IStorage.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
