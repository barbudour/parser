# ApplicationProcessServiceClient.OnDownloadStreamDisposedActionAsync -
свойство
Делегат, выполняемый при освобождении потока, возвращаемого в методе
[DownloadAsync(ApplicationDownloadRequest, ApplicationDownloadFlags,
CancellationToken)](M_Tessa_Applications_Services_TessaServer_IApplicationService_DownloadAsync.htm),
или null, если делегат отсутствует.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.TessaServer](N_Tessa_Applications_Services_TessaServer.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<ValueTask> OnDownloadStreamDisposedActionAsync { get; set; }
VB __Копировать
     Public Property OnDownloadStreamDisposedActionAsync As Func(Of ValueTask)
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Func<ValueTask>^ OnDownloadStreamDisposedActionAsync {
    	Func<ValueTask>^ get () sealed;
    	void set (Func<ValueTask>^ value) sealed;
    }
F# __Копировать
     abstract OnDownloadStreamDisposedActionAsync : Func<ValueTask> with get, set
    override OnDownloadStreamDisposedActionAsync : Func<ValueTask> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
#### Реализации
[IApplicationServiceHost.OnDownloadStreamDisposedActionAsync](P_Tessa_Applications_Services_TessaServer_IApplicationServiceHost_OnDownloadStreamDisposedActionAsync.htm)  
##  __См. также
#### Ссылки
[ApplicationProcessServiceClient -
](T_Tessa_Applications_Services_TessaServer_ApplicationProcessServiceClient.htm)
[Tessa.Applications.Services.TessaServer - пространство
имён](N_Tessa_Applications_Services_TessaServer.htm)
