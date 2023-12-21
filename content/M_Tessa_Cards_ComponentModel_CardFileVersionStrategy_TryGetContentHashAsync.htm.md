# CardFileVersionStrategy.TryGetContentHashAsync - метод
Возвращает хеш контента для версии файла с заданным идентификатором. Хеш может
быть равен null, если версия не найдена или её хеш не был рассчитан.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<byte[]> TryGetContentHashAsync(
    	Guid versionRowID,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function TryGetContentHashAsync ( 
    	versionRowID As Guid,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public:
    virtual Task<array<unsigned char>^>^ TryGetContentHashAsync(
    	Guid versionRowID, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract TryGetContentHashAsync : 
            versionRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
    override TryGetContentHashAsync : 
            versionRowID : Guid * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
#### Параметры
versionRowID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
    Идентификатор версии файла, информацию о которой требуется получить.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>  
Хеш контента для версии файла с заданным идентификатором или null, если версия
не найдена или её хеш не был рассчитан.
#### Реализации
[ICardFileVersionStrategy.TryGetContentHashAsync(Guid,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardFileVersionStrategy_TryGetContentHashAsync.htm)  
##  __См. также
#### Ссылки
[CardFileVersionStrategy -
](T_Tessa_Cards_ComponentModel_CardFileVersionStrategy.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
