# CardFileVersionStrategy.SetUploadSuccessfulAsync - метод
Устанавливает, что загрузка контента для версии файла с заданным
идентификатором была успешно завершена.
##  __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task SetUploadSuccessfulAsync(
    	Guid versionRowID,
    	byte[] hash = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function SetUploadSuccessfulAsync ( 
    	versionRowID As Guid,
    	Optional hash As Byte() = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task
C++ __Копировать
     public:
    virtual Task^ SetUploadSuccessfulAsync(
    	Guid versionRowID, 
    	array<unsigned char>^ hash = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract SetUploadSuccessfulAsync : 
            versionRowID : Guid * 
            ?hash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _hash = defaultArg hash null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
    override SetUploadSuccessfulAsync : 
            versionRowID : Guid * 
            ?hash : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _hash = defaultArg hash null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task 
#### Параметры
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла.
hash [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[] (Optional)
     Хеш содержимого версии или null, если хеш не изменяется (он может уже быть установлен при добавлении версии). 
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardFileVersionStrategy.SetUploadSuccessfulAsync(Guid, Byte[],
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_SetUploadSuccessfulAsync.htm)  
##  __См. также
#### Ссылки
[CardFileVersionStrategy -
](T_Tessa_Cards_ComponentModel_CardFileVersionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
