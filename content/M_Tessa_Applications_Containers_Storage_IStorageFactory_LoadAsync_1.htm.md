# IStorageFactory.LoadAsync(String, CancellationToken) - метод
Осуществляет загрузку хранилища из строки xml
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     ValueTask<IStorage> LoadAsync(
    	[NotNullAttribute] string xml,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Function LoadAsync ( 
    	<NotNullAttribute> xml As String,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IStorage)
C++ __Копировать
     ValueTask<IStorage^> LoadAsync(
    	[NotNullAttribute] String^ xml, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract LoadAsync : 
            [<NotNullAttribute>] xml : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IStorage> 
#### Параметры
xml [String](https://learn.microsoft.com/dotnet/api/system.string)
     Поток из которого будет считано хранилище 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)>  
Считанное хранилище
## __См. также
#### Ссылки
[IStorageFactory -
](T_Tessa_Applications_Containers_Storage_IStorageFactory.htm)
[LoadAsync -
перегрузка](Overload_Tessa_Applications_Containers_Storage_IStorageFactory_LoadAsync.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
