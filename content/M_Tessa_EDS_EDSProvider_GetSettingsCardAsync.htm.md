# EDSProvider.GetSettingsCardAsync - метод
Возвращает карточку настроек ЭП для текущих параметров запроса. Секции в
карточке должны соответствовать секциям в типе
[SignatureSettingsType](F_Tessa_Platform_EDS_SignatureHelper_SignatureSettingsType.htm).
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ValueTask<Card> GetSettingsCardAsync(
    	ICAdESServiceSettings signatureSettings,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Protected Overridable Function GetSettingsCardAsync ( 
    	signatureSettings As ICAdESServiceSettings,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of Card)
C++ __Копировать
     protected:
    virtual ValueTask<Card^> GetSettingsCardAsync(
    	ICAdESServiceSettings^ signatureSettings, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSettingsCardAsync : 
            signatureSettings : ICAdESServiceSettings * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
    override GetSettingsCardAsync : 
            signatureSettings : ICAdESServiceSettings * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<Card> 
#### Параметры
signatureSettings ICAdESServiceSettings
    Настройки подписания и проверки подписи.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры запроса к сервису или null, если параметры не указаны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Card](T_Tessa_Cards_Card.htm)>  
Карточка настроек ЭП для текущих параметров запроса.
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
