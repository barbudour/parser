# FmHelper.GetForumSatelliteInfosAsync - метод
Загрузить данные карточке сателлита форумов и упаковать их в List из одного
элемента. В информации содержится идентификатор и тип.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Forums](N_Tessa_Extensions_Default_Shared_Forums.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<List<SatelliteInfo>> GetForumSatelliteInfosAsync(
    	Guid mainCardID,
    	IDbScope dbScope,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Shared Function GetForumSatelliteInfosAsync ( 
    	mainCardID As Guid,
    	dbScope As IDbScope,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of List(Of SatelliteInfo))
C++ __Копировать
     public:
    static Task<List<SatelliteInfo^>^>^ GetForumSatelliteInfosAsync(
    	Guid mainCardID, 
    	IDbScope^ dbScope, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     static member GetForumSatelliteInfosAsync : 
            mainCardID : Guid * 
            dbScope : IDbScope * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<List<SatelliteInfo>> 
#### Параметры
mainCardID [Guid](https://learn.microsoft.com/dotnet/api/system.guid)
dbScope [IDbScope](T_Tessa_Platform_Data_IDbScope.htm)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[SatelliteInfo](T_Tessa_Cards_Extensions_Templates_SatelliteInfo.htm)>>  
##  __См. также
#### Ссылки
[FmHelper - ](T_Tessa_Extensions_Default_Shared_Forums_FmHelper.htm)
[Tessa.Extensions.Default.Shared.Forums - пространство
имён](N_Tessa_Extensions_Default_Shared_Forums.htm)
