# XmlStorageFactory.LoadAsync(Stream, CancellationToken) - метод
Осуществляет загрузку хранилища из потока
[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Containers.Storage](N_Tessa_Applications_Containers_Storage.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ValueTask<IStorage> LoadAsync(
    	Stream stream,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function LoadAsync ( 
    	stream As Stream,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of IStorage)
C++ __Копировать
     public:
    virtual ValueTask<IStorage^> LoadAsync(
    	Stream^ stream, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract LoadAsync : 
            stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IStorage> 
    override LoadAsync : 
            stream : Stream * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<IStorage> 
#### Параметры
stream [Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)
     Поток из которого будет считано хранилище 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[IStorage](T_Tessa_Applications_Containers_Storage_IStorage.htm)>  
Считанное хранилище
#### Реализации
[IStorageFactory.LoadAsync(Stream,
CancellationToken)](M_Tessa_Applications_Containers_Storage_IStorageFactory_LoadAsync.htm)  
##  __См. также
#### Ссылки
[XmlStorageFactory -
](T_Tessa_Applications_Containers_Storage_XmlStorageFactory.htm)
[LoadAsync -
перегрузка](Overload_Tessa_Applications_Containers_Storage_XmlStorageFactory_LoadAsync.htm)
[Tessa.Applications.Containers.Storage - пространство
имён](N_Tessa_Applications_Containers_Storage.htm)
