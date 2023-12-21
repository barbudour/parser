# EDSProvider.GetSettingsAsync - метод
Возвращает настройки подписания и проверки подписи ICAdESServiceSettings для
текущих параметров запроса.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<ICAdESServiceSettings> GetSettingsAsync(
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetSettingsAsync ( 
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of ICAdESServiceSettings)
C++ __Копировать
     protected:
    virtual ValueTask<ICAdESServiceSettings^> GetSettingsAsync(
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSettingsAsync : 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICAdESServiceSettings> 
    override GetSettingsAsync : 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ICAdESServiceSettings> 
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры запроса к сервису или null, если параметры не указаны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<ICAdESServiceSettings>  
Настройки подписания и проверки подписи для текущих параметров запроса.
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
